#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COS 图片上传脚本 - srt-to-markdown Skill 专用
支持自动生成 YYYY-MM-DD-article-name 格式的路径
"""

import os
import sys
import re
from pathlib import Path
from datetime import datetime

# 添加项目根目录到 Python 路径，以便导入 cos_uploader 模块
current_dir = Path(__file__).parent
skill_dir = current_dir.parent
project_root = skill_dir

for parent in [skill_dir] + list(skill_dir.parents):
    if (parent / 'scripts' / 'cos_uploader').exists():
        project_root = parent
        break

cos_uploader_path = project_root / 'scripts' / 'cos_uploader'
sys.path.insert(0, str(cos_uploader_path))

try:
    from upload_image_to_cos import TencentCOSUploader
except ImportError:
    print(f"❌ 错误: 无法导入 TencentCOSUploader")
    print(f"请确保 {cos_uploader_path} 目录存在")
    sys.exit(1)


def extract_date_and_slug(filename):
    """
    从文件名提取日期和文章 slug

    Args:
        filename: 文件名，如 '2025-01-19-agent-skill.md'

    Returns:
        tuple: (date_str, slug) 或 (None, None)
    """
    # 匹配 YYYY-MM-DD-xxx 格式
    pattern = r'^(\d{4}-\d{2}-\d{2})-(.+?)\.md$'
    match = re.match(pattern, filename)

    if match:
        date_str = match.group(1)
        slug = match.group(2)
        return date_str, slug

    return None, None


def generate_article_path(date_str=None, slug=None, custom_name=None):
    """
    生成文章路径

    Args:
        date_str: 日期字符串 (YYYY-MM-DD)
        slug: 文章 slug
        custom_name: 自定义文章名 (优先级最高)

    Returns:
        str: COS 路径，如 '2025-01-19-agent-skill'
    """
    if custom_name:
        # 使用自定义名称
        today = datetime.now().strftime('%Y-%m-%d')
        # 清理自定义名称：转小写、替换空格和特殊字符
        clean_name = custom_name.lower().strip()
        clean_name = re.sub(r'[^\w\-\u4e00-\u9fff]+', '-', clean_name)
        return f"{today}-{clean_name}"

    if date_str and slug:
        # 从文件名提取
        return f"{date_str}-{slug}"

    # 交互式输入
    today = datetime.now().strftime('%Y-%m-%d')
    print(f"\n📝 需要输入文章信息")
    print(f"今天日期: {today}")

    use_today = input("使用今天的日期吗？(Y/n): ").strip().lower()
    if use_today != 'n':
        date_str = today
    else:
        date_str = input("请输入日期 (YYYY-MM-DD): ").strip()
        while not re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
            print("❌ 日期格式错误，请使用 YYYY-MM-DD 格式")
            date_str = input("请输入日期 (YYYY-MM-DD): ").strip()

    slug = input("请输入文章 slug (英文，用连字符分隔): ").strip()
    while not slug:
        print("❌ slug 不能为空")
        slug = input("请输入文章 slug: ").strip()

    return f"{date_str}-{slug}"


def find_images_directory(current_dir=None):
    """
    查找 images 目录

    Args:
        current_dir: 当前目录

    Returns:
        Path: images 目录路径
    """
    if current_dir is None:
        current_dir = Path.cwd()

    images_dir = current_dir / 'images'
    if images_dir.exists():
        return images_dir

    # 向上查找
    for parent in [current_dir] + list(current_dir.parents):
        if (parent / 'images').exists():
            return parent / 'images'

    return None


def main():
    """主函数"""
    print(f"\n{'='*60}")
    print("🚀 COS 图片上传工具 - srt-to-markdown Skill")
    print(f"{'='*60}")

    # 获取当前目录
    current_dir = Path.cwd()
    print(f"📁 当前目录: {current_dir}")

    # 查找 Markdown 文件
    md_files = list(current_dir.glob('*.md'))
    md_file = None

    if md_files:
        md_file = md_files[0]
        print(f"📄 找到 Markdown 文件: {md_file.name}")

        # 尝试从文件名提取日期和 slug
        date_str, slug = extract_date_and_slug(md_file.name)
        if date_str and slug:
            print(f"✓ 从文件名提取信息:")
            print(f"  - 日期: {date_str}")
            print(f"  - Slug: {slug}")

            use_auto = input("\n使用文件名作为 COS 路径吗？(Y/n): ").strip().lower()
            if use_auto != 'n':
                article_path = generate_article_path(date_str, slug)
            else:
                article_path = generate_article_path()
        else:
            print(f"⚠️  文件名不符合 YYYY-MM-DD-xxx 格式")
            article_path = generate_article_path()
    else:
        print("⚠️  未找到 Markdown 文件")
        article_path = generate_article_path()

    print(f"\n📂 COS 路径: {article_path}")

    # 查找图片目录
    images_dir = find_images_directory(current_dir)
    if not images_dir:
        print(f"\n❌ 错误: 未找到 images 目录")
        print(f"请在当前目录或父目录中创建 images 目录")
        sys.exit(1)

    print(f"📁 图片目录: {images_dir}")

    # 查找图片文件
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg'}
    image_files = [f for f in images_dir.iterdir()
                   if f.is_file() and f.suffix.lower() in image_extensions]

    if not image_files:
        print(f"\n⚠️  images 目录中没有图片文件")
        sys.exit(0)

    print(f"\n📷 找到 {len(image_files)} 个图片文件:")
    for img in sorted(image_files):
        print(f"  - {img.name}")

    confirm = input(f"\n确认上传这 {len(image_files)} 个图片到 COS 吗？(Y/n): ").strip().lower()
    if confirm == 'n':
        print("已取消上传")
        sys.exit(0)

    # 初始化上传器
    try:
        uploader = TencentCOSUploader()
    except ValueError as e:
        print(f"\n❌ 初始化失败: {e}")
        print("\n💡 提示: 请确保已配置 COS 环境变量")
        print(f"配置文件: {project_root / 'scripts' / 'cos_uploader' / '.env.cos'}")
        sys.exit(1)

    # 上传图片
    print(f"\n{'='*60}")
    print("📤 开始上传...")
    print(f"{'='*60}")

    results = []
    for image_file in sorted(image_files):
        print(f"\n上传: {image_file.name}")
        result = uploader.upload_file(
            str(image_file),
            custom_path=article_path,
            enable_cdn=False  # 可以改为 True 来启用 CDN
        )
        results.append((image_file.name, result))

    # 显示结果
    print(f"\n{'='*60}")
    print("📊 上传结果")
    print(f"{'='*60}")

    success_count = 0
    markdown_links = []

    for filename, result in results:
        if result.get('success'):
            success_count += 1
            url = result['url']
            alt_text = Path(filename).stem
            markdown = uploader.generate_markdown_link(url, alt_text)
            markdown_links.append(markdown)

            print(f"\n✓ {filename}")
            print(f"  URL: {url}")
            print(f"  Markdown: {markdown}")
        else:
            print(f"\n✗ {filename}")
            print(f"  错误: {result.get('error')}")

    print(f"\n{'='*60}")
    print(f"✅ 上传完成: {success_count}/{len(image_files)} 成功")
    print(f"{'='*60}")

    if markdown_links:
        print(f"\n📋 所有 Markdown 链接 (可复制使用):")
        print(f"{'-'*60}")
        for link in markdown_links:
            print(link)


if __name__ == '__main__':
    main()
