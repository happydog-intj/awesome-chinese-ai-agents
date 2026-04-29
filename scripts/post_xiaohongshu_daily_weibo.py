#!/usr/bin/env python3
"""
AI 小红书日报 → 微博发布脚本
每天从 ai-xiaohongshu-daily 仓库获取最新日报 issue，
附封面图（cover1.png）发一条微博。
"""
import os, sys, json, logging, subprocess, re, base64, tempfile, urllib.request
from pathlib import Path
from datetime import datetime, timezone, timedelta

REPO_DIR = Path(__file__).parent.parent
LOGS_DIR = REPO_DIR / "logs"
LOGS_DIR.mkdir(exist_ok=True)

XHS_REPO = "happydog-intj/ai-xiaohongshu-daily"
STATE_FILE = Path(__file__).parent / ".xiaohongshu_weibo_state"

log_file = LOGS_DIR / f"xiaohongshu_weibo_{datetime.now().strftime('%Y-%m-%d')}.log"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler(), logging.FileHandler(log_file, encoding="utf-8")],
)
log = logging.getLogger(__name__)


def get_latest_daily_issue() -> dict:
    """用 gh CLI 获取最新的 📱 AI 小红书日报 issue"""
    result = subprocess.run(
        [
            "gh", "issue", "list",
            "--repo", XHS_REPO,
            "--search", "📱 AI 小红书日报 in:title",
            "--limit", "5",
            "--json", "number,title,url,createdAt",
        ],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"gh 命令失败: {result.stderr[:200]}")
    issues = json.loads(result.stdout)
    # 只取标题含 "小红书日报" 的
    daily = [i for i in issues if "小红书日报" in i["title"]]
    if not daily:
        raise RuntimeError("未找到小红书日报 issue")
    return daily[0]


def extract_date_from_title(title: str) -> str:
    """从标题 '📱 AI 小红书日报 · 2026-04-29' 提取日期"""
    m = re.search(r"(\d{4}-\d{2}-\d{2})", title)
    if not m:
        raise RuntimeError(f"无法从标题提取日期: {title}")
    return m.group(1)


def get_cover_image_url(date: str) -> str:
    return (
        f"https://raw.githubusercontent.com/{XHS_REPO}/master/assets/{date}/cover1.png"
    )


def already_posted(issue_number: int) -> bool:
    if STATE_FILE.exists():
        try:
            return int(STATE_FILE.read_text().strip()) == issue_number
        except:
            pass
    return False


def save_posted(issue_number: int):
    STATE_FILE.write_text(str(issue_number))


def download_image(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read()


def upload_image_via_chrome(image_bytes: bytes) -> str:
    """通过 Chrome AppleScript 上传图片到微博，返回 pic_id"""
    b64 = base64.b64encode(image_bytes).decode()

    js_code = f"""(function() {{
    var b64 = "{b64}";
    var byteChars = atob(b64);
    var byteNums = new Array(byteChars.length);
    for (var i = 0; i < byteChars.length; i++) {{
        byteNums[i] = byteChars.charCodeAt(i);
    }}
    var byteArr = new Uint8Array(byteNums);
    var blob = new Blob([byteArr], {{type: 'image/png'}});

    var xsrfMatch = document.cookie.match(/XSRF-TOKEN=([^;]+)/);
    if (!xsrfMatch) return JSON.stringify({{error: 'NO_XSRF'}});
    var xsrf = xsrfMatch[1];

    var formData = new FormData();
    formData.append('b64_data', b64);
    formData.append('type', 'json');

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/aj/mblog/pic/upload', false);
    xhr.setRequestHeader('X-Xsrf-Token', xsrf);
    xhr.withCredentials = true;
    xhr.send(formData);
    return xhr.responseText.substring(0, 1000);
}})()"""

    js_escaped = js_code.replace('\\', '\\\\').replace('"', '\\"')

    apple_script = f'''
tell application "Google Chrome"
    set wbTab to missing value
    repeat with w in windows
        repeat with t in tabs of w
            set u to URL of t
            if u contains "weibo.com" and u does not contain "passport" and u does not contain "login" then
                set wbTab to t
                exit repeat
            end if
        end repeat
        if wbTab is not missing value then exit repeat
    end repeat
    if wbTab is missing value then
        set wbTab to make new tab at end of tabs of window 1
        set URL of wbTab to "https://weibo.com/"
        delay 4
    end if
    set result to execute wbTab javascript "{js_escaped}"
    return result
end tell
'''
    result = subprocess.run(["osascript", "-e", apple_script], capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"AppleScript 图片上传失败: {result.stderr[:200]}")

    resp_text = result.stdout.strip()
    log.info(f"上传响应: {resp_text[:200]}")
    try:
        data = json.loads(resp_text)
        # 尝试各种字段路径
        pic_id = (
            data.get("pic_id")
            or data.get("data", {}).get("pic_id")
            or data.get("data", {}).get("pics", [{}])[0].get("pic_id")
            if isinstance(data.get("data"), dict) else None
        )
        if not pic_id and isinstance(data.get("data"), list) and data["data"]:
            pic_id = data["data"][0].get("pic_id")
        return pic_id or ""
    except:
        return ""


def post_weibo_with_pic(content: str, pic_id: str) -> dict:
    """通过 Chrome AppleScript 发微博（含图片）"""
    js_content = json.dumps(content)

    pic_param = f"&pic_id={pic_id}" if pic_id else ""
    js_code = f"""(function() {{
    var content = {js_content};
    var picId = "{pic_id}";
    var xsrfMatch = document.cookie.match(/XSRF-TOKEN=([^;]+)/);
    if (!xsrfMatch) return JSON.stringify({{error: 'NO_XSRF', cookies: document.cookie.substring(0,100)}});
    var xsrf = xsrfMatch[1];
    var body = 'content=' + encodeURIComponent(content) + '&visible=0';
    if (picId) body += '&pic_id=' + encodeURIComponent(picId);
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/ajax/statuses/update', false);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.setRequestHeader('X-Xsrf-Token', xsrf);
    xhr.setRequestHeader('Accept', 'application/json');
    xhr.withCredentials = true;
    xhr.send(body);
    return xhr.responseText.substring(0, 500);
}})()"""

    js_escaped = js_code.replace('\\', '\\\\').replace('"', '\\"')

    apple_script = f'''
tell application "Google Chrome"
    set wbTab to missing value
    repeat with w in windows
        repeat with t in tabs of w
            set u to URL of t
            if u contains "weibo.com" and u does not contain "passport" and u does not contain "login" then
                set wbTab to t
                exit repeat
            end if
        end repeat
        if wbTab is not missing value then exit repeat
    end repeat
    if wbTab is missing value then
        set wbTab to make new tab at end of tabs of window 1
        set URL of wbTab to "https://weibo.com/"
        delay 4
    end if
    set result to execute wbTab javascript "{js_escaped}"
    return result
end tell
'''
    result = subprocess.run(["osascript", "-e", apple_script], capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"AppleScript 发布失败: {result.stderr[:200]}")

    resp_text = result.stdout.strip()
    try:
        return json.loads(resp_text)
    except:
        return {"raw": resp_text}


def build_weibo_text(title: str, issue_url: str, date: str) -> str:
    # 从 "📱 AI 小红书日报 · 2026-04-29" 提取简洁日期
    friendly_date = date  # e.g. 2026-04-29
    return (
        f"🤖 {title}\n\n"
        f"今日 AI 动态已整理为小红书风格日报，涵盖最热技术帖、实测技巧与行业快讯，"
        f"可直接搬运发布。\n\n"
        f"📎 查看完整内容：{issue_url}\n\n"
        f"#AI日报# #小红书运营# #AI工具# #大模型# #LLM#"
    )


def main():
    log.info("🔍 获取最新小红书日报 issue...")
    issue = get_latest_daily_issue()
    log.info(f"找到: #{issue['number']} {issue['title']}")

    if already_posted(issue["number"]):
        log.info(f"✅ issue #{issue['number']} 已发布过，跳过")
        return

    date = extract_date_from_title(issue["title"])
    cover_url = get_cover_image_url(date)
    content = build_weibo_text(issue["title"], issue["url"], date)

    log.info(f"📥 下载封面图: {cover_url}")
    try:
        image_bytes = download_image(cover_url)
        log.info(f"图片大小: {len(image_bytes)} bytes")
    except Exception as e:
        log.warning(f"⚠️ 封面图下载失败: {e}，将纯文字发布")
        image_bytes = None

    pic_id = ""
    if image_bytes:
        log.info("📤 上传图片到微博...")
        try:
            pic_id = upload_image_via_chrome(image_bytes)
            if pic_id:
                log.info(f"✅ 图片上传成功，pic_id: {pic_id}")
            else:
                log.warning("⚠️ 图片上传未返回 pic_id，将纯文字发布")
        except Exception as e:
            log.warning(f"⚠️ 图片上传异常: {e}，将纯文字发布")

    log.info(f"📝 发布微博...\n{content[:100]}...")
    resp = post_weibo_with_pic(content, pic_id)
    log.info(f"响应: {json.dumps(resp, ensure_ascii=False)[:300]}")

    # 判断成功
    mid = None
    if isinstance(resp, dict):
        mid = resp.get("data", {}).get("idstr")
        if not mid and "raw" in resp:
            try:
                inner = json.loads(resp["raw"])
                mid = inner.get("data", {}).get("idstr")
            except:
                m = re.search(r'"idstr"\s*:\s*"(\d+)"', resp.get("raw", ""))
                if m:
                    mid = m.group(1)

    if mid:
        log.info(f"✅ 发布成功！微博 ID: {mid} | https://weibo.com/{mid}")
        save_posted(issue["number"])
    else:
        err = resp.get("error") or resp.get("raw") or str(resp)
        log.error(f"❌ 发布失败: {err}")
        sys.exit(1)


if __name__ == "__main__":
    main()
