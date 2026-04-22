#!/usr/bin/env python3
"""
三平台统一发布入口
顺序执行：微博 → 知乎 → 小红书
- 每个平台独立状态文件、独立日志
- 单个平台失败不阻断后续平台
- 最终汇总报告
"""
import os, sys, logging, subprocess
from pathlib import Path
from datetime import datetime

# ── 路径 ──────────────────────────────────────────────────────
REPO_DIR = Path(__file__).parent.parent
LOGS_DIR = REPO_DIR / "logs"
SCRIPTS  = Path(__file__).parent

PLATFORMS = [
    ("微博",   SCRIPTS / "post_weibo.py"),
    ("知乎",   SCRIPTS / "post_zhihu.py"),
    ("小红书", SCRIPTS / "post_xhs.py"),
]

# ── 日志 ──────────────────────────────────────────────────────
LOGS_DIR.mkdir(exist_ok=True)
log_file = LOGS_DIR / f"post_all_{datetime.now().strftime('%Y-%m-%d')}.log"
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler(), logging.FileHandler(log_file, encoding="utf-8")],
)
log = logging.getLogger(__name__)


def run_platform(name: str, script: Path) -> bool:
    """运行单个平台脚本，返回是否成功"""
    log.info(f"{'='*50}")
    log.info(f"▶  开始发布：{name}")
    log.info(f"{'='*50}")

    result = subprocess.run(
        [sys.executable, str(script)],
        capture_output=False,   # 让子进程直接输出到 stdout/stderr
        text=True,
    )
    success = (result.returncode == 0)
    if success:
        log.info(f"✅ {name} 发布完成")
    else:
        log.error(f"❌ {name} 发布失败（exit code {result.returncode}）")
    return success


def main():
    log.info(f"🚀 三平台统一发布开始 [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")

    results = {}
    for name, script in PLATFORMS:
        if not script.exists():
            log.warning(f"⚠️  {name} 脚本不存在: {script}，跳过")
            results[name] = None
            continue
        try:
            results[name] = run_platform(name, script)
        except Exception as e:
            log.error(f"❌ {name} 运行异常: {e}")
            results[name] = False

    # ── 汇总报告 ──────────────────────────────────────────────
    log.info("")
    log.info("=" * 50)
    log.info("📊 发布汇总")
    log.info("=" * 50)
    ok_count   = 0
    fail_count = 0
    skip_count = 0
    for name, status in results.items():
        if status is True:
            log.info(f"  ✅ {name}")
            ok_count += 1
        elif status is False:
            log.info(f"  ❌ {name}")
            fail_count += 1
        else:
            log.info(f"  ⏭️  {name}（跳过）")
            skip_count += 1

    log.info(f"\n成功 {ok_count} / 失败 {fail_count} / 跳过 {skip_count}")
    log.info("=" * 50)

    # 只要有失败就以非零退出
    sys.exit(1 if fail_count > 0 else 0)


if __name__ == "__main__":
    main()
