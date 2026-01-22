#!/usr/bin/env python3
"""
Generate an animated HTML page from simplified content.
"""

import sys
import json
from datetime import datetime


def escape_html(text):
    """Escape HTML special characters."""
    if not text:
        return ""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def generate_html_content(content_data):
    """Generate the complete HTML content."""

    title = escape_html(content_data.get("title", "Simplified Explanation"))
    url = escape_html(content_data.get("url", ""))

    # Build key concepts cards HTML
    concepts_html = ""
    for i, concept in enumerate(content_data.get("key_concepts", [])):
        delay = i * 0.2
        concepts_html += f"""
        <div class="concept-card" style="animation-delay: {delay}s">
            <h3 class="concept-term">{escape_html(concept.get('term', ''))}</h3>
            <p class="concept-explanation">{escape_html(concept.get('explanation', ''))}</p>
            <div class="concept-analogy">
                <span class="analogy-icon">💡</span>
                <p><strong>Think of it like:</strong> {escape_html(concept.get('real_world_analogy', concept.get('analogy', '')))}</p>
            </div>
        </div>
        """

    # Build step-by-step HTML
    steps_html = ""
    for step in content_data.get("step_by_step", []):
        steps_html += f"""
        <div class="step-card scroll-reveal">
            <div class="step-number">{escape_html(str(step.get('step', '')))}</div>
            <div class="step-content">
                <p>{escape_html(step.get('description', ''))}</p>
            </div>
        </div>
        """

    # Build summary cards HTML
    summary_html = ""
    for card in content_data.get("summary_cards", []):
        key_points_html = ""
        for point in card.get("key_points", []):
            key_points_html += f"<li>{escape_html(point)}</li>"

        summary_html += f"""
        <div class="summary-card scroll-reveal">
            <h3 class="summary-title">{escape_html(card.get('title', 'Summary'))}</h3>
            <p class="summary-intro">{escape_html(card.get('summary', ''))}</p>
            <ul class="key-points">
                {key_points_html}
            </ul>
        </div>
        """

    # Build simplified sections HTML
    sections_html = ""
    simplified_sections = content_data.get("simplified_version", {}).get("sections", [])
    for i, section in enumerate(simplified_sections):
        if section.get("heading"):
            sections_html += f"""
            <section class="content-section scroll-reveal">
                <h2 class="section-heading">{escape_html(section.get('heading', ''))}</h2>
                <div class="section-content">
                    <p>{escape_html(section.get('simplified_content', ''))}</p>
                </div>
            </section>
            """

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Simplified</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        :root {{
            --primary-color: #4a90a4;
            --secondary-color: #6ab0c4;
            --accent-color: #f0a050;
            --bg-color: #f8f9fa;
            --card-bg: #ffffff;
            --text-color: #2c3e50;
            --text-light: #6c757d;
            --shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            --shadow-hover: 0 8px 15px rgba(0, 0, 0, 0.15);
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: var(--bg-color);
            color: var(--text-color);
            line-height: 1.8;
            overflow-x: hidden;
        }}

        /* Hero Section */
        .hero {{
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
            color: white;
            padding: 80px 20px;
            text-align: center;
            position: relative;
            overflow: hidden;
        }}

        .hero::before {{
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 60%);
            animation: heroPulse 8s ease-in-out infinite;
        }}

        @keyframes heroPulse {{
            0%, 100% {{ transform: scale(1); opacity: 0.5; }}
            50% {{ transform: scale(1.1); opacity: 0.8; }}
        }}

        .hero-content {{
            position: relative;
            z-index: 1;
            max-width: 800px;
            margin: 0 auto;
        }}

        .hero h1 {{
            font-size: 2.5rem;
            margin-bottom: 20px;
            opacity: 0;
            animation: fadeInUp 0.8s ease forwards 0.2s;
        }}

        .hero .subtitle {{
            font-size: 1.2rem;
            opacity: 0.8;
            margin-bottom: 30px;
            opacity: 0;
            animation: fadeInUp 0.8s ease forwards 0.4s;
        }}

        .source-link {{
            display: inline-block;
            padding: 10px 25px;
            background: rgba(255,255,255,0.2);
            border-radius: 25px;
            text-decoration: none;
            color: white;
            font-size: 0.9rem;
            transition: all 0.3s ease;
            opacity: 0;
            animation: fadeInUp 0.8s ease forwards 0.6s;
        }}

        .source-link:hover {{
            background: rgba(255,255,255,0.3);
            transform: translateY(-2px);
        }}

        /* Main Content */
        .container {{
            max-width: 900px;
            margin: 0 auto;
            padding: 60px 20px;
        }}

        /* Section Titles */
        .section-title {{
            font-size: 1.8rem;
            color: var(--primary-color);
            margin-bottom: 30px;
            text-align: center;
            position: relative;
        }}

        .section-title::after {{
            content: '';
            display: block;
            width: 60px;
            height: 3px;
            background: var(--accent-color);
            margin: 15px auto 0;
            border-radius: 2px;
        }}

        /* Concept Cards */
        .concepts-section {{
            margin-bottom: 80px;
        }}

        .concepts-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 25px;
            margin-top: 30px;
        }}

        .concept-card {{
            background: var(--card-bg);
            border-radius: 16px;
            padding: 30px;
            box-shadow: var(--shadow);
            transition: all 0.4s ease;
            opacity: 0;
            animation: fadeInUp 0.6s ease forwards;
        }}

        .concept-card:hover {{
            transform: translateY(-8px);
            box-shadow: var(--shadow-hover);
        }}

        .concept-term {{
            font-size: 1.3rem;
            color: var(--primary-color);
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .concept-term::before {{
            content: '🔑';
            font-size: 1.2rem;
        }}

        .concept-explanation {{
            color: var(--text-color);
            margin-bottom: 20px;
            line-height: 1.7;
        }}

        .concept-analogy {{
            background: linear-gradient(135deg, #fff3cd 0%, #ffeeba 100%);
            border-radius: 12px;
            padding: 20px;
            border-left: 4px solid var(--accent-color);
        }}

        .analogy-icon {{
            font-size: 1.5rem;
            margin-bottom: 10px;
            display: block;
        }}

        .concept-analogy p {{
            margin: 0;
            font-size: 0.95rem;
            color: #856404;
        }}

        /* Step by Step */
        .steps-section {{
            margin-bottom: 80px;
        }}

        .steps-container {{
            display: flex;
            flex-direction: column;
            gap: 20px;
            margin-top: 30px;
        }}

        .step-card {{
            display: flex;
            align-items: flex-start;
            gap: 25px;
            background: var(--card-bg);
            padding: 30px;
            border-radius: 16px;
            box-shadow: var(--shadow);
            opacity: 0;
        }}

        .step-number {{
            flex-shrink: 0;
            width: 50px;
            height: 50px;
            background: linear-gradient(135deg, var(--accent-color) 0%, #e09030 100%);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.4rem;
            font-weight: bold;
        }}

        .step-content p {{
            margin: 0;
            font-size: 1.1rem;
            line-height: 1.7;
        }}

        /* Summary Cards */
        .summary-section {{
            margin-bottom: 80px;
        }}

        .summary-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            margin-top: 30px;
        }}

        .summary-card {{
            background: var(--card-bg);
            border-radius: 16px;
            padding: 30px;
            box-shadow: var(--shadow);
            opacity: 0;
        }}

        .summary-title {{
            font-size: 1.2rem;
            color: var(--primary-color);
            margin-bottom: 15px;
            padding-bottom: 15px;
            border-bottom: 2px solid #eee;
        }}

        .summary-intro {{
            color: var(--text-light);
            margin-bottom: 20px;
            font-size: 0.95rem;
        }}

        .key-points {{
            list-style: none;
            padding: 0;
        }}

        .key-points li {{
            padding: 10px 0;
            padding-left: 25px;
            position: relative;
            border-bottom: 1px solid #f0f0f0;
        }}

        .key-points li:last-child {{
            border-bottom: none;
        }}

        .key-points li::before {{
            content: '✓';
            position: absolute;
            left: 0;
            color: var(--accent-color);
            font-weight: bold;
        }}

        /* Content Sections */
        .content-section {{
            margin-bottom: 60px;
            opacity: 0;
        }}

        .section-heading {{
            font-size: 1.5rem;
            color: var(--primary-color);
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #e0e0e0;
        }}

        .section-content {{
            background: var(--card-bg);
            padding: 30px;
            border-radius: 12px;
            box-shadow: var(--shadow);
        }}

        .section-content p {{
            margin-bottom: 15px;
        }}

        .section-content p:last-child {{
            margin-bottom: 0;
        }}

        /* Footer */
        footer {{
            background: var(--text-color);
            color: white;
            text-align: center;
            padding: 40px 20px;
            margin-top: 60px;
        }}

        footer p {{
            opacity: 0.7;
            font-size: 0.9rem;
        }}

        /* Scroll Progress Bar */
        .scroll-progress {{
            position: fixed;
            top: 0;
            left: 0;
            height: 3px;
            background: var(--accent-color);
            z-index: 1000;
            transition: width 0.1s ease;
        }}

        /* Animations */
        @keyframes fadeInUp {{
            from {{
                opacity: 0;
                transform: translateY(30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}

        @keyframes slideInLeft {{
            from {{
                opacity: 0;
                transform: translateX(-50px);
            }}
            to {{
                opacity: 1;
                transform: translateX(0);
            }}
        }}

        /* Scroll Reveal Classes */
        .scroll-reveal {{
            opacity: 0;
            transform: translateY(40px);
            transition: all 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        }}

        .scroll-reveal.visible {{
            opacity: 1;
            transform: translateY(0);
        }}

        /* Responsive */
        @media (max-width: 768px) {{
            .hero h1 {{
                font-size: 1.8rem;
            }}

            .step-card {{
                flex-direction: column;
                gap: 15px;
            }}

            .step-number {{
                width: 40px;
                height: 40px;
                font-size: 1.1rem;
            }}
        }}

        /* Reading Time */
        .reading-time {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            margin-top: 15px;
            font-size: 0.9rem;
            opacity: 0.9;
        }}
    </style>
</head>
<body>
    <div class="scroll-progress" id="scrollProgress"></div>

    <header class="hero">
        <div class="hero-content">
            <h1>{title}</h1>
            <p class="subtitle">A simplified, beginner-friendly explanation</p>
            <a href="{url}" class="source-link" target="_blank">📄 View Original Article</a>
            <div class="reading-time">
                <span>⏱️</span>
                <span id="readingTime">3 min read</span>
            </div>
        </div>
    </header>

    <main class="container">
        <!-- Key Concepts -->
        <section class="concepts-section">
            <h2 class="section-title">🎯 Key Concepts</h2>
            <div class="concepts-grid">
                {concepts_html}
            </div>
        </section>

        <!-- Step by Step Guide -->
        {steps_html if steps_html else ''}

        <!-- Summary Cards -->
        <section class="summary-section">
            <h2 class="section-title">📋 Summary</h2>
            <div class="summary-grid">
                {summary_html}
            </div>
        </section>

        <!-- Simplified Content -->
        {sections_html}
    </main>

    <footer>
        <p>Generated with ❤️ using Link Explainer Skill</p>
        <p>Created on {datetime.now().strftime('%Y-%m-%d')}</p>
    </footer>

    <script>
        // Scroll Progress Bar
        window.addEventListener('scroll', () => {{
            const scrollProgress = document.getElementById('scrollProgress');
            const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
            const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrollPercentage = (scrollTop / scrollHeight) * 100;
            scrollProgress.style.width = scrollPercentage + '%';
        }});

        // Scroll Reveal Animation
        const observerOptions = {{
            root: null,
            rootMargin: '0px',
            threshold: 0.1
        }};

        const observer = new IntersectionObserver((entries) => {{
            entries.forEach(entry => {{
                if (entry.isIntersecting) {{
                    entry.target.classList.add('visible');
                }}
            }});
        }}, observerOptions);

        document.querySelectorAll('.scroll-reveal').forEach(el => {{
            observer.observe(el);
        }});

        // Smooth scroll for internal links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({{
                    behavior: 'smooth'
                }});
            }});
        }});

        // Calculate reading time
        function calculateReadingTime() {{
            const text = document.body.innerText;
            const words = text.split(/\s+/).length;
            const minutes = Math.ceil(words / 200);
            document.getElementById('readingTime').textContent = minutes + ' min read';
        }}

        calculateReadingTime();
    </script>
</body>
</html>
"""

    return html


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_html.py <simplified_content.json>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading input file: {e}", file=sys.stderr)
        sys.exit(1)

    html_content = generate_html_content(content_data)

    output_file = "explanation.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Successfully generated: {output_file}", file=sys.stderr)


if __name__ == "__main__":
    main()
