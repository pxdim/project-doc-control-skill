#!/usr/bin/env python3
"""
專案文檔 Git 同步輔助腳本
用於自動化「進度與需求.md」的 Git 操作
"""

import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime

DOC_FILE = "進度與需求.md"


def run_cmd(cmd, check=True, capture=True):
    """執行 shell 指令並回傳結果"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            check=check,
            capture_output=capture,
            text=True
        )
        return result.returncode == 0, result.stdout.strip(), result.stderr.strip()
    except subprocess.CalledProcessError as e:
        return False, "", str(e)


def is_git_repo():
    """檢查當前目錄是否為 Git repo"""
    returncode, _, _ = run_cmd("git rev-parse --git-dir", check=False, capture=False)
    return returncode == 0


def has_remote():
    """檢查是否有設定 remote"""
    returncode, stdout, _ = run_cmd("git remote get-url origin", check=False)
    return returncode == 0 and stdout


def check_status():
    """檢查 Git 狀態"""
    print("=== Git 狀態檢查 ===")

    if not is_git_repo():
        print("❌ 當前目錄不是 Git repo")
        print("   使用 --init 初始化新 repo")
        return False

    print("✅ 是 Git repo")

    if has_remote():
        _, url, _ = run_cmd("git remote get-url origin")
        print(f"✅ Remote: {url}")
    else:
        print("⚠️  尚未設定 remote")

    # 檢查文檔狀態
    if os.path.exists(DOC_FILE):
        _, status, _ = run_cmd(f"git status {DOC_FILE} --porcelain")
        if status:
            print(f"📝 {DOC_FILE} 有變更待 commit")
        else:
            print(f"✅ {DOC_FILE} 已是最新")
    else:
        print(f"⚠️  {DOC_FILE} 不存在")

    return True


def init_repo():
    """初始化 Git repo"""
    print("=== 初始化 Git repo ===")

    if is_git_repo():
        print("⚠️  已經是 Git repo")
        return

    # 初始化
    run_cmd("git init")
    print("✅ Git repo 已初始化")

    # 檢查文檔是否存在
    if not os.path.exists(DOC_FILE):
        print(f"⚠️  {DOC_FILE} 不存在，無法 commit")
        return

    # 詢問是否要第一次 commit
    response = input(f"是否要將 {DOC_FILE} 加入初始 commit？(y/n): ")
    if response.lower() == 'y':
        run_cmd(f"git add {DOC_FILE}")
        run_cmd(f'git commit -m "docs: 初始化專案文檔 - {datetime.now().strftime("%Y-%m-%d")}"')
        print("✅ 初始 commit 完成")

        # 詢問是否要設定 remote
        setup_remote()


def setup_remote():
    """設定 Git remote"""
    if has_remote():
        print("✅ Remote 已設定")
        return

    print("\n=== 設定 Git Remote ===")
    url = input("請輸入 repo URL (例如: https://github.com/user/repo.git): ").strip()

    if url:
        run_cmd(f"git remote add origin {url}")
        print(f"✅ Remote 已設定: {url}")

        # 詢問 branch 名稱
        branch = input("請輸入 branch 名稱 (預設: main): ").strip() or "main"

        # 詢問是否要立即 push
        response = input(f"是否要立即 push 到 {branch}? (y/n): ")
        if response.lower() == 'y':
            success, _, err = run_cmd(f"git push -u origin {branch}")
            if success:
                print("✅ Push 成功")
            else:
                print(f"❌ Push 失敗: {err}")


def push_changes(commit_message=None):
    """Commit 並 push 變更"""
    if not is_git_repo():
        print("❌ 當前目錄不是 Git repo，請先使用 --init")
        return

    if not os.path.exists(DOC_FILE):
        print(f"❌ {DOC_FILE} 不存在")
        return

    # 檢查是否有變更
    _, status, _ = run_cmd(f"git status {DOC_FILE} --porcelain")
    if not status:
        print(f"✅ {DOC_FILE} 沒有變更，無需 commit")
        return

    print(f"=== Commit & Push {DOC_FILE} ===")

    # 詢問 commit 訊息
    if not commit_message:
        default_msg = f'docs: 更新進度與需求 - {datetime.now().strftime("%Y-%m-%d %H:%M")}'
        commit_message = input(f"請輸入 commit 訊息 (預設: {default_msg}): ").strip()
        if not commit_message:
            commit_message = default_msg

    # Commit
    run_cmd(f"git add {DOC_FILE}")
    success, _, err = run_cmd(f'git commit -m "{commit_message}"')
    if not success:
        print(f"❌ Commit 失敗: {err}")
        return

    print(f"✅ Commit 成功: {commit_message}")

    # Push
    if not has_remote():
        print("⚠️  尚未設定 remote，請先設定 remote")
        setup_remote()
        if not has_remote():
            return

    print("正在 push...")
    success, stdout, err = run_cmd("git push")
    if success:
        print("✅ Push 成功")
    else:
        print(f"❌ Push 失敗: {err}")


def show_help():
    """顯示說明"""
    print("""
專案文檔 Git 同步輔助腳本

用法:
    python git_sync.py --check      檢查 Git 狀態
    python git_sync.py --init       初始化新 Git repo
    python git_sync.py --push [msg] Commit 並 push 變更
    python git_sync.py --remote     設定 Git remote
    python git_sync.py --help       顯示此說明

範例:
    python git_sync.py --check
    python git_sync.py --push "完成使用者登入功能"
""")


def main():
    if len(sys.argv) < 2:
        show_help()
        return

    arg = sys.argv[1]

    if arg == "--check":
        check_status()
    elif arg == "--init":
        init_repo()
    elif arg == "--push":
        commit_msg = sys.argv[2] if len(sys.argv) > 2 else None
        push_changes(commit_msg)
    elif arg == "--remote":
        setup_remote()
    elif arg == "--help" or arg == "-h":
        show_help()
    else:
        print(f"❌ 未知參數: {arg}")
        show_help()


if __name__ == "__main__":
    main()
