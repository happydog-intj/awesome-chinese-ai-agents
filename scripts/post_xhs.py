#!/usr/bin/env python3
"""
自动发小红书笔记脚本
从 xhs_posts.txt 轮流取文案（第一行为标题），通过 Chrome AppleScript JS 调用发布接口。
小红书 API 有强签名，必须在 xiaohongshu.com 域名下执行才有效。
"""
import os, sys, json, logging, subprocess, re
from pathlib import Path
from datetime import datetime

# ── 路径 ──────────────────────────────────────────────────────
REPO_DIR   = Path(__file__).parent.parent
POSTS_FILE = Path(__file__).parent / "xhs_posts.txt"
STATE_FILE = Path(__file__).parent / ".xhs_state"
LOGS_DIR   = REPO_DIR / "logs"

# ── 日志 ──────────────────────────────────────────────────────
LOGS_DIR.mkdir(exist_ok=True)
log_file = LOGS_DIR / f"xhs_{datetime.now().strftime('%Y-%m-%d')}.log"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler(), logging.FileHandler(log_file, encoding="utf-8")],
)
log = logging.getLogger(__name__)


# ── 文案管理 ──────────────────────────────────────────────────
def load_posts() -> list[tuple[str, str]]:
    """返回 [(title, content), ...]，每条第一行为标题，其余为正文"""
    text = POSTS_FILE.read_text(encoding="utf-8")
    posts = []
    for block in text.split("\n---\n"):
        block = block.strip()
        if not block:
            continue
        lines = block.split("\n", 1)
        title   = lines[0].strip()
        content = lines[1].strip() if len(lines) > 1 else ""
        posts.append((title, content))
    return posts


def get_next_index(total: int) -> int:
    if STATE_FILE.exists():
        try:
            return int(STATE_FILE.read_text().strip()) % total
        except:
            pass
    return 0


def save_index(idx: int):
    STATE_FILE.write_text(str(idx + 1))


# ── Chrome AppleScript 发布 ────────────────────────────────────
def post_via_chrome(title: str, content: str) -> dict:
    """在 xiaohongshu.com tab 下执行 JS 调用发布接口"""
    js_title   = json.dumps(title)
    js_content = json.dumps(content)

    js_code = f"""(async function() {{
    var title   = {js_title};
    var content = {js_content};
    var resp = await fetch('https://edith.xiaohongshu.com/api/sns/web/v1/note/post', {{
        method: 'POST',
        credentials: 'include',
        headers: {{'Content-Type': 'application/json'}},
        body: JSON.stringify({{
            "note_id": "",
            "type": "normal",
            "title": title,
            "desc": content,
            "privacy_info": {{"op_type": 1, "type": 0}},
            "post_to_topic": true,
            "topics": [],
            "at_user_list": [],
            "image_info_list": [],
            "video_info": {{}}
        }})
    }});
    var data = await resp.json();
    return JSON.stringify(data);
}})()"""

    # 转义供 AppleScript 使用
    js_escaped = js_code.replace('\\', '\\\\').replace('"', '\\"')

    apple_script = f'''
tell application "Google Chrome"
    set xhsTab to missing value

    -- 1. 查找已有 xiaohongshu.com tab
    repeat with w in windows
        repeat with t in tabs of w
            set u to URL of t
            if u contains "xiaohongshu.com" then
                set xhsTab to t
                set index of w to 1
                set active tab index of w to tab_index_of(w, t)
                exit repeat
            end if
        end repeat
        if xhsTab is not missing value then exit repeat
    end repeat

    -- 2. 没有则新建 tab
    if xhsTab is missing value then
        set xhsTab to make new tab at end of tabs of window 1
        set URL of xhsTab to "https://www.xiaohongshu.com/"
        delay 5
    end if

    set result to execute xhsTab javascript "{js_escaped}"
    return result
end tell

on tab_index_of(w, t)
    set i to 1
    repeat with tab in tabs of w
        if tab is t then return i
        set i to i + 1
    end repeat
    return 1
end tab_index_of
'''

    result = subprocess.run(
        ["osascript", "-e", apple_script],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"AppleScript 失败: {result.stderr[:300]}")

    resp_text = result.stdout.strip()
    try:
        return json.loads(resp_text)
    except:
        return {"raw": resp_text}


# ── 主流程 ────────────────────────────────────────────────────
def main():
    posts = load_posts()
    if not posts:
        log.error("xhs_posts.txt 为空")
        sys.exit(1)

    total = len(posts)
    idx   = get_next_index(total)
    title, content = posts[idx]

    log.info(f"📝 发布第 {idx+1}/{total} 条小红书笔记")
    log.info(f"标题: {title}")
    log.info(f"预览: {content[:60]}...")

    try:
        resp = post_via_chrome(title, content)
    except Exception as e:
        log.error(f"❌ 调用失败: {e}")
        sys.exit(1)

    log.info(f"响应: {json.dumps(resp, ensure_ascii=False)[:300]}")

    # 判断成功
    note_id = None
    if isinstance(resp, dict):
        note_id = (
            resp.get("data", {}).get("note_id")
            or resp.get("data", {}).get("id")
        )
        if not note_id and "raw" in resp:
            try:
                inner   = json.loads(resp["raw"])
                note_id = inner.get("data", {}).get("note_id") or inner.get("data", {}).get("id")
            except:
                m = re.search(r'"note_id"\s*:\s*"([^"]+)"', resp.get("raw", ""))
                if m:
                    note_id = m.group(1)

    if note_id:
        log.info(f"✅ 发布成功！笔记 ID: {note_id}")
        save_index(idx)
    else:
        # 兼容：部分响应 code=0 即成功但不返回 note_id
        code = None
        if isinstance(resp, dict):
            code = resp.get("code") or resp.get("success")
        if code == 0 or code is True:
            log.info("✅ 发布成功（code=0）")
            save_index(idx)
        else:
            err = resp.get("message") or resp.get("raw") or resp
            log.error(f"❌ 发布失败: {err}")
            sys.exit(1)


if __name__ == "__main__":
    main()
