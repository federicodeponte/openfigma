"""
LinkedIn Carousel V11 - The Human Story
Clean, minimal, story-driven design
"""

import os
import sys
sys.path.insert(0, '/home/tech_scaile_it/openfigma')

from openfigma import PNGExporter

OUTPUT_DIR = "/home/tech_scaile_it/openfigma/exports/linkedin_v11"
os.makedirs(OUTPUT_DIR, exist_ok=True)

WIDTH, HEIGHT = 1080, 1350

def base_style():
    return """
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    * { margin: 0; padding: 0; box-sizing: border-box; }
    
    body {
        width: 1080px;
        height: 1350px;
        font-family: 'Inter', -apple-system, sans-serif;
        background: #ffffff;
        color: #0a0a0a;
        display: flex;
        flex-direction: column;
        padding: 80px;
    }
    
    .slide { height: 100%; display: flex; flex-direction: column; }
    
    .swipe {
        position: absolute;
        bottom: 60px;
        right: 80px;
        font-size: 16px;
        color: #666;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    .swipe::after {
        content: "→";
        font-size: 20px;
    }
    
    .page-num {
        position: absolute;
        bottom: 60px;
        left: 80px;
        font-size: 14px;
        color: #999;
        font-weight: 500;
    }
    """

# Slide 1: The Hook
slide1 = f"""
<!DOCTYPE html>
<html>
<head><style>
{base_style()}

.hook-text {{
    font-size: 64px;
    font-weight: 700;
    line-height: 1.2;
    margin-top: auto;
    margin-bottom: auto;
}}

.highlight {{
    background: linear-gradient(120deg, #fef3c7 0%, #fde68a 100%);
    padding: 4px 12px;
    border-radius: 8px;
}}
</style></head>
<body>
<div class="slide">
    <div class="hook-text">
        My designer <span class="highlight">quit</span>.<br><br>
        So I built my own<br>
        design tool.
    </div>
    <div class="swipe">Swipe</div>
    <div class="page-num">1/8</div>
</div>
</body>
</html>
"""

# Slide 2: The Story
slide2 = f"""
<!DOCTYPE html>
<html>
<head><style>
{base_style()}

.story {{
    font-size: 42px;
    font-weight: 500;
    line-height: 1.6;
    margin-top: auto;
    margin-bottom: auto;
    color: #1a1a1a;
}}

.aside {{
    color: #666;
    font-size: 36px;
    font-style: italic;
    margin-top: 40px;
}}
</style></head>
<body>
<div class="slide">
    <div class="story">
        She got a full-time offer.<br><br>
        I was happy for her.<br><br>
        But I still needed:<br>
        • Social media graphics<br>
        • Presentations<br>
        • Marketing assets
        <div class="aside">(and no budget for a new designer)</div>
    </div>
    <div class="swipe">Swipe</div>
    <div class="page-num">2/8</div>
</div>
</body>
</html>
"""

# Slide 3: The Solution
slide3 = f"""
<!DOCTYPE html>
<html>
<head><style>
{base_style()}

.solution {{
    margin-top: auto;
    margin-bottom: auto;
}}

.intro {{
    font-size: 32px;
    color: #666;
    margin-bottom: 30px;
}}

.name {{
    font-size: 72px;
    font-weight: 800;
    color: #0a0a0a;
    margin-bottom: 30px;
}}

.tagline {{
    font-size: 36px;
    font-weight: 500;
    color: #333;
    line-height: 1.5;
}}
</style></head>
<body>
<div class="slide">
    <div class="solution">
        <div class="intro">So I built</div>
        <div class="name">openfigma</div>
        <div class="tagline">
            An open-source Python library<br>
            that turns HTML/CSS into<br>
            Figma-quality graphics.
        </div>
    </div>
    <div class="swipe">Swipe</div>
    <div class="page-num">3/8</div>
</div>
</body>
</html>
"""

# Slide 4: The Code
slide4 = f"""
<!DOCTYPE html>
<html>
<head><style>
{base_style()}

body {{ background: #0a0a0a; }}

.code-section {{
    margin-top: auto;
    margin-bottom: auto;
}}

.label {{
    font-size: 24px;
    color: #666;
    margin-bottom: 40px;
    text-transform: uppercase;
    letter-spacing: 2px;
}}

.code-block {{
    background: #1a1a1a;
    border-radius: 16px;
    padding: 48px;
    font-family: 'SF Mono', 'Fira Code', monospace;
    font-size: 28px;
    line-height: 2;
}}

.keyword {{ color: #c084fc; }}
.string {{ color: #86efac; }}
.comment {{ color: #666; }}
.func {{ color: #60a5fa; }}

.swipe, .page-num {{ color: #666; }}
</style></head>
<body>
<div class="slide">
    <div class="code-section">
        <div class="label">Just 4 lines of code</div>
        <div class="code-block">
            <span class="keyword">from</span> openfigma <span class="keyword">import</span> html_to_png<br><br>
            html = <span class="string">"&lt;your template&gt;"</span><br><br>
            <span class="func">html_to_png</span>(html, <span class="string">"post.png"</span>)
        </div>
    </div>
    <div class="swipe">Swipe</div>
    <div class="page-num">4/8</div>
</div>
</body>
</html>
"""

# Slide 5: Benefits
slide5 = f"""
<!DOCTYPE html>
<html>
<head><style>
{base_style()}

.benefits {{
    margin-top: auto;
    margin-bottom: auto;
}}

.benefit {{
    font-size: 48px;
    font-weight: 600;
    margin-bottom: 50px;
    display: flex;
    align-items: center;
    gap: 24px;
}}

.no {{
    color: #ef4444;
    font-weight: 700;
}}

.benefit-text {{
    color: #333;
}}

.strike {{
    text-decoration: line-through;
    color: #999;
}}
</style></head>
<body>
<div class="slide">
    <div class="benefits">
        <div class="benefit">
            <span class="no">No</span>
            <span class="benefit-text">design skills needed</span>
        </div>
        <div class="benefit">
            <span class="no">No</span>
            <span class="benefit-text">expensive subscriptions</span>
        </div>
        <div class="benefit">
            <span class="no">No</span>
            <span class="benefit-text">learning curve</span>
        </div>
        <div style="margin-top: 60px; font-size: 40px; color: #666;">
            Just Python + HTML/CSS<br>
            → beautiful graphics
        </div>
    </div>
    <div class="swipe">Swipe</div>
    <div class="page-num">5/8</div>
</div>
</body>
</html>
"""

# Slide 6: Features
slide6 = f"""
<!DOCTYPE html>
<html>
<head><style>
{base_style()}

.features {{
    margin-top: auto;
    margin-bottom: auto;
}}

.feature {{
    font-size: 42px;
    font-weight: 500;
    margin-bottom: 40px;
    display: flex;
    align-items: center;
    gap: 20px;
}}

.check {{
    width: 48px;
    height: 48px;
    background: #22c55e;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 28px;
    flex-shrink: 0;
}}
</style></head>
<body>
<div class="slide">
    <div class="features">
        <div class="feature">
            <div class="check">✓</div>
            100% open source (MIT)
        </div>
        <div class="feature">
            <div class="check">✓</div>
            pip install openfigma
        </div>
        <div class="feature">
            <div class="check">✓</div>
            github.com/federicodeponte/openfigma
        </div>
    </div>
    <div class="swipe">Swipe</div>
    <div class="page-num">6/8</div>
</div>
</body>
</html>
"""

# Slide 7: Example output
slide7 = f"""
<!DOCTYPE html>
<html>
<head><style>
{base_style()}

body {{ background: #f8fafc; }}

.example {{
    margin-top: auto;
    margin-bottom: auto;
    text-align: center;
}}

.label {{
    font-size: 20px;
    color: #666;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 40px;
}}

.card {{
    background: white;
    border-radius: 24px;
    padding: 60px;
    box-shadow: 0 25px 50px -12px rgba(0,0,0,0.1);
    display: inline-block;
}}

.metric {{
    font-size: 96px;
    font-weight: 800;
    background: linear-gradient(135deg, #22c55e, #16a34a);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}}

.metric-label {{
    font-size: 32px;
    color: #666;
    margin-top: 16px;
}}

.prompt {{
    margin-top: 50px;
    font-size: 20px;
    color: #999;
    font-style: italic;
}}
</style></head>
<body>
<div class="slide">
    <div class="example">
        <div class="label">Example output</div>
        <div class="card">
            <div class="metric">+500%</div>
            <div class="metric-label">Growth this quarter</div>
        </div>
        <div class="prompt">Prompt: "A metric card showing 500% growth"</div>
    </div>
    <div class="swipe">Swipe</div>
    <div class="page-num">7/8</div>
</div>
</body>
</html>
"""

# Slide 8: CTA
slide8 = f"""
<!DOCTYPE html>
<html>
<head><style>
{base_style()}

.cta {{
    margin-top: auto;
    margin-bottom: auto;
}}

.headline {{
    font-size: 48px;
    font-weight: 700;
    margin-bottom: 50px;
    line-height: 1.3;
}}

.offer {{
    background: #f0fdf4;
    border: 2px solid #22c55e;
    border-radius: 20px;
    padding: 40px;
    margin-bottom: 50px;
}}

.offer-title {{
    font-size: 32px;
    font-weight: 600;
    color: #166534;
    margin-bottom: 20px;
}}

.offer-text {{
    font-size: 26px;
    color: #333;
    line-height: 1.6;
}}

.note {{
    font-size: 24px;
    color: #666;
    font-style: italic;
}}

.page-num {{ left: 80px; }}
</style></head>
<body>
<div class="slide">
    <div class="cta">
        <div class="headline">
            Want me to generate a<br>
            custom design for you?
        </div>
        <div class="offer">
            <div class="offer-title">💬 Comment your prompt below</div>
            <div class="offer-text">
                e.g., "A metric card showing 500% growth"<br><br>
                I'll generate it and send it to you<br>
                within 24 hours.
            </div>
        </div>
        <div class="note">No strings attached. Just showing what it can do.</div>
    </div>
    <div class="page-num">8/8</div>
</div>
</body>
</html>
"""

slides = [
    ("01_hook.png", slide1),
    ("02_story.png", slide2),
    ("03_solution.png", slide3),
    ("04_code.png", slide4),
    ("05_benefits.png", slide5),
    ("06_features.png", slide6),
    ("07_example.png", slide7),
    ("08_cta.png", slide8),
]

with PNGExporter() as exporter:
    for filename, html in slides:
        path = f"{OUTPUT_DIR}/{filename}"
        exporter.export(html, path, width=WIDTH, height=HEIGHT)
        size = os.path.getsize(path) / 1024
        print(f"✓ {filename} ({size:.0f}KB)")

print(f"\nDone! {len(slides)} slides saved to {OUTPUT_DIR}")
