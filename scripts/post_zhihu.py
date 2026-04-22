#!/usr/bin/env python3
"""
自动发知乎「想法」脚本
从 zhihu_posts.txt 轮流取文案，通过 Chrome Cookie + HTTP API 发布
"""
import os, sys, json, logging, hashlib, re, shutil, sqlite3, tempfile, subprocess, requests
from pathlib import Path
from datetime import datetime

# ── 路径 ──────────────────────────────────────────────────────
REPO_DIR   = Path(__file__).parent.parent
POSTS_FILE = Path(__file__).parent / "zhihu_posts.txt"
STATE_FILE = Path(__file__).parent / ".zhihu_state"
LOGS_DIR   = REPO_DIR / "logs"

# ── 日志 ──────────────────────────────────────────────────────
LOGS_DIR.mkdir(exist_ok=True)
log_file = LOGS_DIR / f"zhihu_{datetime.now().strftime('%Y-%m-%d')}.log"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler(), logging.FileHandler(log_file, encoding="utf-8")],
)
log = logging.getLogger(__name__)

# ── cryptography (xcookie-venv) ───────────────────────────────
sys.path.insert(0, '/Users/a10093140/.openclaw/workspace/venvs/xcookie-venv/lib/python3.14/site-packages')
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

CHROME_COOKIE_DB = os.path.expanduser(
    "~/Library/Application Support/Google/Chrome/Default/Cookies"
)


# ── Cookie 解密 ───────────────────────────────────────────────
def _chrome_key() -> bytes:
    pw = subprocess.run(
        ["security", "find-generic-password", "-w", "-s", "Chrome Safe Storage", "-a", "Chrome"],
        capture_output=True, text=True
    ).stdout.strip()
    return hashlib.pbkdf2_hmac("sha1", pw.encode(), b"saltysalt", 1003, dklen=16)


def _decrypt(enc: bytes, key: bytes) -> str:
    enc = bytes(enc)
    if enc[:3] == b'v10':
        enc = enc[3:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(b' ' * 16), backend=default_backend())
    dec = cipher.decryptor()
    plain = dec.update(enc) + dec.finalize()
    pad = plain[-1]
    raw = plain[:-pad].decode('latin-1')
    # 前16字节是CBC噪声，以反引号结尾——截取反引号之后的内容
    if '`' in raw:
        return raw.split('`', 1)[1].strip()
    # 备用：取最长可打印段
    parts = re.findall(r'[\x21-\x7e]{4,}', raw)
    return max(parts, key=len) if parts else ""


def get_zhihu_cookies() -> dict:
    key = _chrome_key()
    tmp = tempfile.mktemp(suffix=".db")
    shutil.copy2(CHROME_COOKIE_DB, tmp)
    try:
        conn = sqlite3.connect(tmp)
        cur  = conn.cursor()
        cur.execute(
            "SELECT name, value, encrypted_value FROM cookies "
            "WHERE host_key LIKE '%zhihu%' AND name IN ('z_c0','_xsrf','d_c0','SESSIONID')"
        )
        rows = cur.fetchall()
        conn.close()
    finally:
        os.unlink(tmp)

    jar = {}
    for name, value, enc_value in rows:
        jar[name] = value if value else _decrypt(enc_value, key)

    log.info(f"获取到 Cookie 键: {list(jar.keys())}")
    return jar


# ── 文案管理 ──────────────────────────────────────────────────
def load_posts() -> list[str]:
    text = POSTS_FILE.read_text(encoding="utf-8")
    return [p.strip() for p in text.split("\n---\n") if p.strip()]


def get_next_index(total: int) -> int:
    if STATE_FILE.exists():
        try:
            return int(STATE_FILE.read_text().strip()) % total
        except:
            pass
    return 0


def save_index(idx: int):
    STATE_FILE.write_text(str(idx + 1))


# ── 发布知乎想法 ──────────────────────────────────────────────
def post_zhihu_pin(content: str, jar: dict) -> dict:
    xsrf = jar.get("_xsrf", "")
    if not xsrf:
        raise RuntimeError("未找到 _xsrf cookie，请确保已登录知乎")

    url = "https://www.zhihu.com/api/v4/pins"
    headers = {
        "x-xsrftoken": xsrf,
        "Content-Type": "application/json",
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Referer": "https://www.zhihu.com/",
        "Origin":  "https://www.zhihu.com",
    }
    # 构造 Cookie 字符串
    cookie_str = "; ".join(f"{k}={v}" for k, v in jar.items() if v)
    headers["Cookie"] = cookie_str

    payload = {
        "content": [{"type": "text", "content": content}],
        "reshipment_settings": "anyone",
        "comment_permission": "all"
    }

    resp = requests.post(url, headers=headers, json=payload, timeout=15)
    log.info(f"HTTP {resp.status_code}")
    try:
        return resp.json()
    except:
        return {"raw": resp.text[:500]}


# ── 主流程 ────────────────────────────────────────────────────
def main():
    posts = load_posts()
    if not posts:
        log.error("zhihu_posts.txt 为空")
        sys.exit(1)

    total = len(posts)
    idx   = get_next_index(total)
    content = posts[idx]

    log.info(f"📝 发布第 {idx+1}/{total} 条知乎想法")
    log.info(f"预览: {content[:60]}...")

    try:
        jar  = get_zhihu_cookies()
        resp = post_zhihu_pin(content, jar)
    except Exception as e:
        log.error(f"❌ 调用失败: {e}")
        sys.exit(1)

    log.info(f"响应: {json.dumps(resp, ensure_ascii=False)[:300]}")

    # 判断成功
    pin_id = None
    if isinstance(resp, dict):
        pin_id = resp.get("id") or (resp.get("data") or {}).get("id")
    if pin_id:
        log.info(f"✅ 发布成功！想法 ID: {pin_id}")
        log.info(f"   链接: https://www.zhihu.com/pin/{pin_id}")
        save_index(idx)
    else:
        err = resp.get("error") or resp.get("raw") or resp
        log.error(f"❌ 发布失败: {err}")
        sys.exit(1)


if __name__ == "__main__":
    main()
