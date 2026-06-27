DEFAULT_API_KEY = "sk-damqzjFWpWBzG8L03Nn0066jDHrfdM7cMbH7pyWwRKrFZlNh"

import os
import sys
import json
import time
import requests
import re
from pathlib import Path
from datetime import datetime


API_URL = "https://apihub.agnes-ai.com/v1/images/generations"
DEFAULT_SIZE = "1024x1024"
OUTPUT_DIR_NAME = "agnes_images"


def get_api_key():
    key = os.environ.get("AGNES_API_KEY", DEFAULT_API_KEY)
    if not key:
        print("错误：未设置 AGNES_API_KEY 环境变量")
        print("请运行: =\"your-api-key-here\"")
    return key
    return key


def translate_prompt_to_english(keyword, style_hint=None):
    """将中文关键词扩展为英文生图提示词"""
    base_prompts = {
        "猫咪": "A cute fluffy cat, soft fur, big expressive eyes, cozy indoor scene, warm natural lighting, ultra detailed, high quality",
        "狗狗": "A adorable puppy, golden retriever, sunny park, soft bokeh background, ultra detailed, high quality",
        "风景": "Breathtaking mountain landscape at sunset, golden hour lighting, dramatic clouds, ultra detailed, high quality",
        "城市": "Futuristic cyberpunk cityscape at night, neon lights, rain-soaked streets, flying cars, cinematic composition, ultra detailed, high quality",
        "人物": "Portrait of a beautiful person, studio lighting, shallow depth of field, ultra detailed, high quality",
        "动物": "Wild tiger in dense jungle, dramatic sunlight filtering through trees, ultra detailed, high quality",
        "花卉": "Beautiful rose garden in spring morning dew, soft pastel colors, macro photography, ultra detailed, high quality",
        "美食": "Exquisite gourmet dish plating, restaurant lighting, steam rising, food photography, ultra detailed, high quality",
        "科技": "Futuristic technology concept, holographic interfaces, blue and purple neon glow, ultra detailed, high quality",
        "动漫": "Anime style character, vibrant colors, dynamic pose, detailed background, cel shading, high quality",
        "水彩": "Watercolor painting of a serene lake at dawn, soft pastel colors, artistic brush strokes, high quality",
        "抽象": "Abstract geometric art, vibrant colors, dynamic composition, modern art style, ultra detailed, high quality",
        "建筑": "Grand cathedral interior, stained glass windows, dramatic light beams, architectural photography, ultra detailed, high quality",
        "星空": "Stunning night sky with milky way, star trails, mountain silhouette, long exposure photography, ultra detailed, high quality",
        "海洋": "Crystal clear tropical ocean, coral reef, sunlight rays underwater, marine life, ultra detailed, high quality",
        "森林": "Enchanted forest with mist and sunbeams, magical atmosphere, ferns and moss, ultra detailed, high quality",
        "太空": "Astronaut floating in deep space, nebula background, Earth visible in distance, cinematic, ultra detailed, high quality",
        "赛博朋克": "Cyberpunk street scene, neon signs in Japanese, rain, reflections, futuristic gadgets, ultra detailed, high quality",
        "中国风": "Traditional Chinese ink wash painting style, misty mountains, bamboo forest, cranes, poetic atmosphere, high quality",
        "机械": "Futuristic robotic mech, detailed mechanical parts, metallic textures, dramatic lighting, ultra detailed, high quality",
    }

    for cn_keyword, base_prompt in base_prompts.items():
        if cn_keyword in keyword:
            prompt = base_prompt
            break
    else:
        prompt = f"{keyword}, ultra detailed, high quality, professional composition"

    if style_hint:
        prompt += f", {style_hint} style"

    return prompt


def generate_image(api_key, prompt, size=DEFAULT_SIZE, max_retries=3):
    """调用 API 生成一张图片，返回图片 URL"""
    payload = {
        "model": "agnes-image-2.0-flash",
        "prompt": prompt,
        "size": size,
        "extra_body": {
            "response_format": "url"
        }
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    for attempt in range(max_retries):
        try:
            resp = requests.post(API_URL, json=payload, headers=headers, timeout=180)
            resp.raise_for_status()
            data = resp.json()
            url = data["data"][0]["url"]
            return url
        except Exception as e:
            if attempt < max_retries - 1:
                wait_time = 5 * (attempt + 1)
                print(f"  请求失败，{wait_time}秒后重试 ({attempt + 1}/{max_retries}): {e}")
                time.sleep(wait_time)
            else:
                print(f"  请求最终失败: {e}")
                return None


def download_image(url, save_path):
    """从 URL 下载图片到本地"""
    try:
        resp = requests.get(url, timeout=60)
        resp.raise_for_status()
        with open(save_path, "wb") as f:
            f.write(resp.content)
        return True
    except Exception as e:
        print(f"  下载失败 {url}: {e}")
        return False


def sanitize_filename(name):
    """清理文件名中的非法字符"""
    name = re.sub(r'[<>:"/\\|?*]', '_', name)
    name = re.sub(r'\s+', '_', name).strip('_')
    return name[:50] or "image"


def build_html_gallery(images, output_path):
    """生成 HTML 展示页面"""
    rows = []
    for img in images:
        rows.append(f'''
        <div class="card">
            <img src="{img["filename"]}" alt="{img["prompt"]}" onclick="showModal(this)">
            <div class="caption">{img["prompt"]}</div>
        </div>''')

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agnes AI 图片集 - {datetime.now().strftime("%Y-%m-%d %H:%M")}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: #0f0f0f;
            color: #e0e0e0;
            padding: 2rem;
        }}
        h1 {{
            text-align: center;
            margin-bottom: 0.5rem;
            font-size: 2rem;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .subtitle {{
            text-align: center;
            color: #888;
            margin-bottom: 2rem;
            font-size: 0.9rem;
        }}
        .gallery {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
            max-width: 1400px;
            margin: 0 auto;
        }}
        .card {{
            background: #1a1a1a;
            border-radius: 12px;
            overflow: hidden;
            transition: transform 0.2s;
            cursor: pointer;
        }}
        .card:hover {{ transform: translateY(-4px); }}
        .card img {{
            width: 100%;
            aspect-ratio: 1;
            object-fit: cover;
            display: block;
        }}
        .caption {{
            padding: 0.75rem 1rem;
            font-size: 0.85rem;
            color: #bbb;
            line-height: 1.4;
        }}
        .modal-overlay {{
            display: none;
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(0,0,0,0.9);
            z-index: 1000;
            justify-content: center;
            align-items: center;
            cursor: pointer;
        }}
        .modal-overlay.active {{ display: flex; }}
        .modal-overlay img {{
            max-width: 90vw;
            max-height: 90vh;
            border-radius: 8px;
        }}
    </style>
</head>
<body>
    <h1>Agnes AI 批量生图</h1>
    <p class="subtitle">共 {len(images)} 张 · {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    <div class="gallery">
        {"".join(rows)}
    </div>
    <div class="modal-overlay" onclick="this.classList.remove('active')">
        <img src="" alt="preview">
    </div>
    <script>
        function showModal(img) {{
            const overlay = document.querySelector('.modal-overlay');
            overlay.querySelector('img').src = img.src;
            overlay.classList.add('active');
        }}
    </script>
</body>
</html>'''

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)


def main():
    keywords_str = sys.argv[1] if len(sys.argv) > 1 else ""
    size = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_SIZE
    count_per_keyword = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    style_hint = sys.argv[4] if len(sys.argv) > 4 else None

    if not keywords_str.strip():
        print("用法: python agnes_generator.py <关键词1,关键词2,...> [尺寸] [每词生成数] [风格]")
        print('示例: python agnes_generator.py "猫咪,风景,城市" 1024x1024 2')
        sys.exit(1)

    api_key = get_api_key()
    keywords = [k.strip() for k in keywords_str.split(",") if k.strip()]

    # 创建输出目录
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path(OUTPUT_DIR_NAME) / timestamp
    output_dir.mkdir(parents=True, exist_ok=True)

    images = []
    failed = []

    for kw_idx, keyword in enumerate(keywords, 1):
        print(f"\n[{kw_idx}/{len(keywords)}] 处理关键词: {keyword}")

        for img_idx in range(1, count_per_keyword + 1):
            prompt = translate_prompt_to_english(keyword, style_hint)
            print(f"  提示词: {prompt[:80]}...")

            url = generate_image(api_key, prompt, size)
            if not url:
                failed.append({"keyword": keyword, "index": img_idx})
                continue

            # 下载图片
            safe_kw = sanitize_filename(keyword)
            filename = f"{safe_kw}_{img_idx:03d}.jpg"
            save_path = output_dir / filename

            if download_image(url, save_path):
                images.append({
                    "keyword": keyword,
                    "prompt": prompt,
                    "url": url,
                    "filename": save_path.name,
                })
                print(f"  [OK] Saved: {filename}")
            else:
                failed.append({"keyword": keyword, "index": img_idx})

            # 避免请求过快
            time.sleep(1)

    # 生成 HTML
    html_path = output_dir / "agnes_gallery.html"
    build_html_gallery(images, html_path)

    # 汇总
    print(f"\n{'='*50}")
    print(f"完成！")
    print(f"  成功: {len(images)} 张")
    print(f"  失败: {len(failed)} 个")
    print(f"  保存目录: {output_dir.absolute()}")
    print(f"  HTML 页面: {html_path.absolute()}")
    if failed:
        print(f"\n失败的请求:")
        for f in failed:
            print(f"  - {f['keyword']} #{f['index']}")


if __name__ == "__main__":
    main()

