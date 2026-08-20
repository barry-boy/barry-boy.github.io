#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
字幕转 Markdown - 完整处理流程
整合截图、替换链接、上传 COS 的完整流程
"""

import os
import sys
import subprocess
from pathlib import Path


def run_command(cmd, description):
    """运行命令并显示进度"""
    print(f"\n{'='*60}")
    print(f"📋 {description}")
    print(f"{'='*60}")
    print(f"命令: {cmd}")
    print()

    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=False,
        text=True
    )

    if result.returncode != 0:
        print(f"❌ {description} 失败")
        return False

    print(f"✅ {description} 完成")
    return True


def main():
    """主函数"""
    # 获取项目根目录（向上查找直到找到 scripts 目录）
    current_dir = Path.cwd()

    # 查找项目根目录（包含 scripts/cos_uploader 的目录）
    project_root = current_dir
    for parent in [current_dir] + list(current_dir.parents):
        if (parent / 'scripts' / 'cos_uploader').exists():
            project_root = parent
            break

    print(f"📁 项目根目录: {project_root}")
    print(f"📁 当前工作目录: {current_dir}")

    # 检查必要的文件和目录
    md_files = list(current_dir.glob('*.md'))
    if not md_files:
        print("❌ 错误: 当前目录下没有找到 Markdown 文件")
        sys.exit(1)

    md_file = md_files[0]
    print(f"📄 Markdown 文件: {md_file.name}")

    images_dir = current_dir / 'images'
    if not images_dir.exists():
        print("❌ 错误: images 目录不存在，请先运行截图脚本")
        sys.exit(1)

    # 获取脚本路径
    skill_dir = Path(__file__).parent.parent
    screenshot_script = skill_dir / 'scripts' / 'screenshot.py'
    replace_script = project_root / 'scripts' / 'replace_screenshots.py'
    upload_script = skill_dir / 'scripts' / 'cos_uploader.py'

    # 显示菜单
    print(f"\n{'='*60}")
    print("字幕转 Markdown - 完整处理流程")
    print(f"{'='*60}")
    print("\n请选择要执行的操作:")
    print("1. 仅截图 (已有 Markdown 文件)")
    print("2. 仅替换链接 (已有截图)")
    print("3. 仅上传 COS (已有本地链接)")
    print("4. 截图 + 替换链接")
    print("5. 替换链接 + 上传 COS")
    print("6. 完整流程 (截图 + 替换 + 上传)")
    print("0. 退出")

    choice = input("\n请输入选项 (0-6): ").strip()

    # 步骤1: 截图
    if choice in ['1', '4', '6']:
        video_path = input("\n请输入视频文件路径 (直接回车使用默认: /Users/beiyiwangdejiyi/Downloads/videoplayback.mp4): ").strip()
        if not video_path:
            video_path = "/Users/beiyiwangdejiyi/Downloads/videoplayback.mp4"

        cmd = f"python3 {screenshot_script} {video_path}"
        if not run_command(cmd, "步骤1: 视频截图"):
            sys.exit(1)

    # 步骤2: 替换链接
    if choice in ['2', '4', '5', '6']:
        cmd = f"python3 {replace_script}"
        if not run_command(cmd, "步骤2: 替换截图占位符"):
            sys.exit(1)

    # 步骤3: 上传 COS
    if choice in ['3', '5', '6']:
        # 使用新的上传脚本，会自动从文件名提取路径
        cmd = f"python3 {upload_script}"

        if not run_command(cmd, "步骤3: 上传到腾讯云 COS (自动生成 YYYY-MM-DD-article-name 路径)"):
            sys.exit(1)

    print(f"\n{'='*60}")
    print("🎉 所有操作完成！")
    print(f"{'='*60}")
    print(f"\n📄 最终文件: {md_file}")
    print(f"📁 截图目录: {images_dir}")


if __name__ == '__main__':
    main()
