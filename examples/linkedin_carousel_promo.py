#!/usr/bin/env python3
"""
LinkedIn Carousel: OpenFigma Promo
7 slides showcasing the library
"""

import sys
sys.path.insert(0, '/home/tech_scaile_it/openfigma')

from openfigma import PNGExporter

# Carousel dimensions (LinkedIn optimal)
WIDTH = 1080
HEIGHT = 1350

# Shared styles
BASE_STYLES = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  background: #0a0a0f;
  color: #fff;
  width: 1080px;
  height: 1350px;
  overflow: hidden;
}

.slide {
  width: 100%;
  height: 100%;
  padding: 64px;
  display: flex;
  flex-direction: column;
  position: relative;
}

.mesh {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse 100% 80% at 80% 20%, rgba(99, 102, 241, 0.15) 0%, transparent 50%),
    radial-gradient(ellipse 80% 100% at 20% 80%, rgba(168, 85, 247, 0.12) 0%, transparent 50%),
    radial-gradient(ellipse 60% 60% at 50% 50%, rgba(236, 72, 153, 0.08) 0%, transparent 50%);
  pointer-events: none;
}

.grain {
  position: absolute;
  inset: 0;
  opacity: 0.03;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  pointer-events: none;
}

.slide-number {
  position: absolute;
  top: 48px;
  right: 48px;
  font-size: 14px;
  font-weight: 600;
  color: rgba(255,255,255,0.3);
  letter-spacing: 0.1em;
}

.content {
  position: relative;
  z-index: 1;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.headline {
  font-size: 72px;
  font-weight: 800;
  line-height: 1.05;
  letter-spacing: -0.03em;
  margin-bottom: 32px;
}

.headline-xl {
  font-size: 84px;
}

.subhead {
  font-size: 28px;
  font-weight: 500;
  color: rgba(255,255,255,0.6);
  line-height: 1.5;
  max-width: 800px;
}

.accent {
  background: linear-gradient(135deg, #6366f1, #a855f7);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.accent-underline {
  position: relative;
  display: inline-block;
}

.accent-underline::after {
  content: '';
  position: absolute;
  bottom: 4px;
  left: 0;
  right: 0;
  height: 8px;
  background: linear-gradient(135deg, #6366f1, #a855f7);
  opacity: 0.4;
  border-radius: 4px;
}

.footer {
  margin-top: auto;
  padding-top: 48px;
  display: flex;
  align-items: center;
  gap: 16px;
}

.logo {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #6366f1, #a855f7);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 24px;
}

.brand {
  font-size: 20px;
  font-weight: 600;
  color: rgba(255,255,255,0.5);
}
"""

# Slide 1: Hook
SLIDE_1_HOOK = f"""
<!DOCTYPE html>
<html>
<head>
<style>
{BASE_STYLES}

.hook-container {{
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}}

.strikethrough {{
  text-decoration: line-through;
  text-decoration-color: rgba(239, 68, 68, 0.8);
  text-decoration-thickness: 4px;
  color: rgba(255,255,255,0.4);
}}

.tag {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(99, 102, 241, 0.15);
  border: 1px solid rgba(99, 102, 241, 0.3);
  padding: 12px 20px;
  border-radius: 100px;
  font-size: 16px;
  font-weight: 600;
  color: #a5b4fc;
  margin-bottom: 40px;
  width: fit-content;
}}

.arrow {{
  font-size: 24px;
  position: absolute;
  bottom: 120px;
  right: 64px;
  color: rgba(255,255,255,0.3);
}}
</style>
</head>
<body>
<div class="slide">
  <div class="mesh"></div>
  <div class="grain"></div>
  <div class="slide-number">01 / 07</div>

  <div class="content">
    <div class="hook-container">
      <div class="tag">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
        </svg>
        Open Source Design
      </div>

      <h1 class="headline headline-xl">
        My designer<br>
        <span class="strikethrough">quit</span><br>
        <span class="accent">so I built this</span>
      </h1>

      <p class="subhead">
        She got a full-time job. I needed a solution...
      </p>
    </div>

    <div class="arrow">swipe →</div>
  </div>

  <div class="footer">
    <div class="logo">O</div>
    <span class="brand">openfigma</span>
  </div>
</div>
</body>
</html>
"""

# Slide 2: Problem
SLIDE_2_PROBLEM = f"""
<!DOCTYPE html>
<html>
<head>
<style>
{BASE_STYLES}

.problems {{
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 32px;
}}

.problem-card {{
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 20px;
  padding: 32px;
  display: flex;
  align-items: flex-start;
  gap: 24px;
}}

.problem-icon {{
  width: 56px;
  height: 56px;
  background: rgba(239, 68, 68, 0.15);
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}}

.problem-icon svg {{
  color: #f87171;
}}

.problem-content h3 {{
  font-size: 24px;
  font-weight: 700;
  margin-bottom: 8px;
}}

.problem-content p {{
  font-size: 18px;
  color: rgba(255,255,255,0.5);
  line-height: 1.5;
}}

.section-label {{
  font-size: 14px;
  font-weight: 600;
  color: rgba(255,255,255,0.3);
  letter-spacing: 0.15em;
  text-transform: uppercase;
  margin-bottom: 24px;
}}
</style>
</head>
<body>
<div class="slide">
  <div class="mesh"></div>
  <div class="grain"></div>
  <div class="slide-number">02 / 07</div>

  <div class="content">
    <div class="section-label">The Problem</div>
    <h1 class="headline">Design tools<br>are <span class="accent">broken</span></h1>

    <div class="problems">
      <div class="problem-card">
        <div class="problem-icon">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"/>
            <path d="M12 6v6l4 2"/>
          </svg>
        </div>
        <div class="problem-content">
          <h3>Steep learning curve</h3>
          <p>Weeks to learn Figma, Canva, or design tools properly</p>
        </div>
      </div>

      <div class="problem-card">
        <div class="problem-icon">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>
          </svg>
        </div>
        <div class="problem-content">
          <h3>Expensive templates</h3>
          <p>$20-50 per template pack, subscriptions add up</p>
        </div>
      </div>

      <div class="problem-card">
        <div class="problem-icon">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <rect x="3" y="3" width="18" height="18" rx="2"/>
            <path d="M3 9h18M9 21V9"/>
          </svg>
        </div>
        <div class="problem-content">
          <h3>Manual repetition</h3>
          <p>Copy-paste, tweak, export... for every single post</p>
        </div>
      </div>
    </div>
  </div>

  <div class="footer">
    <div class="logo">O</div>
    <span class="brand">openfigma</span>
  </div>
</div>
</body>
</html>
"""

# Slide 3: Solution
SLIDE_3_SOLUTION = f"""
<!DOCTYPE html>
<html>
<head>
<style>
{BASE_STYLES}

.solution-container {{
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}}

.big-logo {{
  width: 120px;
  height: 120px;
  background: linear-gradient(135deg, #6366f1, #a855f7);
  border-radius: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 900;
  font-size: 64px;
  margin-bottom: 40px;
  box-shadow:
    0 0 60px rgba(99, 102, 241, 0.4),
    0 0 120px rgba(168, 85, 247, 0.2);
}}

.features {{
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 40px;
}}

.feature-tag {{
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.1);
  padding: 12px 20px;
  border-radius: 100px;
  font-size: 16px;
  font-weight: 500;
  color: rgba(255,255,255,0.7);
}}

.feature-tag.highlight {{
  background: rgba(34, 197, 94, 0.15);
  border-color: rgba(34, 197, 94, 0.3);
  color: #4ade80;
}}

.github-star {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.15);
  padding: 16px 24px;
  border-radius: 12px;
  font-size: 18px;
  font-weight: 600;
  margin-top: 40px;
  width: fit-content;
}}

.github-star svg {{
  color: #fbbf24;
}}
</style>
</head>
<body>
<div class="slide">
  <div class="mesh"></div>
  <div class="grain"></div>
  <div class="slide-number">03 / 07</div>

  <div class="content">
    <div class="solution-container">
      <div class="big-logo">O</div>

      <h1 class="headline">Meet<br><span class="accent">openfigma</span></h1>

      <p class="subhead">
        Code-first design library.<br>
        Write Python, get Figma-quality graphics.
      </p>

      <div class="features">
        <span class="feature-tag highlight">100% Open Source</span>
        <span class="feature-tag">No design skills needed</span>
        <span class="feature-tag">Python + HTML/CSS</span>
        <span class="feature-tag">Instant PNG export</span>
        <span class="feature-tag">Premium templates</span>
      </div>

      <div class="github-star">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
          <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
        </svg>
        github.com/federicodeponte/openfigma
      </div>
    </div>
  </div>

  <div class="footer">
    <div class="logo">O</div>
    <span class="brand">openfigma</span>
  </div>
</div>
</body>
</html>
"""

# Slide 4: Showcase Template 1 (Statement)
SLIDE_4_SHOWCASE_1 = f"""
<!DOCTYPE html>
<html>
<head>
<style>
{BASE_STYLES}

.showcase {{
  flex: 1;
  display: flex;
  flex-direction: column;
}}

.template-frame {{
  flex: 1;
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 24px;
  overflow: hidden;
  position: relative;
  margin: 32px 0;
  display: flex;
  align-items: center;
  justify-content: center;
}}

.template-preview {{
  width: 90%;
  aspect-ratio: 1;
  background: #0c0c14;
  border-radius: 16px;
  position: relative;
  overflow: hidden;
  box-shadow:
    0 25px 50px rgba(0,0,0,0.5),
    0 0 0 1px rgba(255,255,255,0.05);
}}

/* Mini version of statement template */
.mini-mesh {{
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse 120% 80% at 70% 60%, rgba(139, 92, 246, 0.15) 0%, transparent 50%),
    radial-gradient(ellipse 80% 100% at 10% 80%, rgba(236, 72, 153, 0.10) 0%, transparent 50%);
}}

.mini-content {{
  position: relative;
  z-index: 1;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 48px;
}}

.mini-label {{
  font-size: 12px;
  font-weight: 600;
  color: rgba(255,255,255,0.4);
  letter-spacing: 0.15em;
  text-transform: uppercase;
  margin-bottom: 24px;
}}

.mini-quote {{
  font-size: 32px;
  font-weight: 700;
  line-height: 1.2;
  letter-spacing: -0.02em;
}}

.mini-author {{
  margin-top: auto;
  font-size: 14px;
  color: rgba(255,255,255,0.5);
}}

.template-label {{
  text-align: center;
  font-size: 18px;
  font-weight: 600;
  color: rgba(255,255,255,0.5);
}}

.section-label {{
  font-size: 14px;
  font-weight: 600;
  color: #a5b4fc;
  letter-spacing: 0.15em;
  text-transform: uppercase;
}}
</style>
</head>
<body>
<div class="slide">
  <div class="mesh"></div>
  <div class="grain"></div>
  <div class="slide-number">04 / 07</div>

  <div class="content">
    <div class="showcase">
      <div class="section-label">Template #1</div>
      <h1 class="headline" style="font-size: 56px;">Bold<br><span class="accent">Statement</span></h1>

      <div class="template-frame">
        <div class="template-preview">
          <div class="mini-mesh"></div>
          <div class="mini-content">
            <div class="mini-label">Insight</div>
            <p class="mini-quote">
              The best code is no code at all. Every line you write is a line you have to maintain.
            </p>
            <div class="mini-author">— Jeff Atwood</div>
          </div>
        </div>
      </div>

      <p class="template-label">Gradient mesh • Corner brackets • Grain texture</p>
    </div>
  </div>

  <div class="footer">
    <div class="logo">O</div>
    <span class="brand">openfigma</span>
  </div>
</div>
</body>
</html>
"""

# Slide 5: Showcase Template 2 (Metric)
SLIDE_5_SHOWCASE_2 = f"""
<!DOCTYPE html>
<html>
<head>
<style>
{BASE_STYLES}

.showcase {{
  flex: 1;
  display: flex;
  flex-direction: column;
}}

.template-frame {{
  flex: 1;
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 24px;
  overflow: hidden;
  position: relative;
  margin: 32px 0;
  display: flex;
  align-items: center;
  justify-content: center;
}}

.template-preview {{
  width: 90%;
  aspect-ratio: 1;
  background: #0c0c14;
  border-radius: 16px;
  position: relative;
  overflow: hidden;
  box-shadow:
    0 25px 50px rgba(0,0,0,0.5),
    0 0 0 1px rgba(255,255,255,0.05);
}}

.mini-mesh {{
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse 100% 100% at 80% 80%, rgba(34, 197, 94, 0.12) 0%, transparent 50%),
    radial-gradient(ellipse 80% 80% at 20% 20%, rgba(99, 102, 241, 0.10) 0%, transparent 50%);
}}

.mini-content {{
  position: relative;
  z-index: 1;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 48px;
}}

.mini-label {{
  font-size: 12px;
  font-weight: 600;
  color: rgba(255,255,255,0.4);
  letter-spacing: 0.15em;
  text-transform: uppercase;
  margin-bottom: 16px;
}}

.mini-metric {{
  font-size: 96px;
  font-weight: 800;
  line-height: 1;
  letter-spacing: -0.04em;
  background: linear-gradient(135deg, #4ade80, #22c55e);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}

.mini-change {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(34, 197, 94, 0.15);
  padding: 8px 14px;
  border-radius: 100px;
  font-size: 14px;
  font-weight: 600;
  color: #4ade80;
  margin-top: 16px;
  width: fit-content;
}}

.mini-chart {{
  margin-top: auto;
  height: 60px;
  display: flex;
  align-items: flex-end;
  gap: 8px;
}}

.chart-bar {{
  flex: 1;
  background: rgba(34, 197, 94, 0.3);
  border-radius: 4px 4px 0 0;
}}

.template-label {{
  text-align: center;
  font-size: 18px;
  font-weight: 600;
  color: rgba(255,255,255,0.5);
}}

.section-label {{
  font-size: 14px;
  font-weight: 600;
  color: #4ade80;
  letter-spacing: 0.15em;
  text-transform: uppercase;
}}
</style>
</head>
<body>
<div class="slide">
  <div class="mesh"></div>
  <div class="grain"></div>
  <div class="slide-number">05 / 07</div>

  <div class="content">
    <div class="showcase">
      <div class="section-label">Template #2</div>
      <h1 class="headline" style="font-size: 56px;">Metric<br><span class="accent">Hero</span></h1>

      <div class="template-frame">
        <div class="template-preview">
          <div class="mini-mesh"></div>
          <div class="mini-content">
            <div class="mini-label">Monthly Active Users</div>
            <div class="mini-metric">2.4M</div>
            <div class="mini-change">
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3">
                <path d="M12 19V5M5 12l7-7 7 7"/>
              </svg>
              +127% vs last year
            </div>
            <div class="mini-chart">
              <div class="chart-bar" style="height: 30%"></div>
              <div class="chart-bar" style="height: 45%"></div>
              <div class="chart-bar" style="height: 35%"></div>
              <div class="chart-bar" style="height: 60%"></div>
              <div class="chart-bar" style="height: 55%"></div>
              <div class="chart-bar" style="height: 75%"></div>
              <div class="chart-bar" style="height: 85%"></div>
              <div class="chart-bar" style="height: 100%"></div>
            </div>
          </div>
        </div>
      </div>

      <p class="template-label">Live indicator • Trend chart • Change pills</p>
    </div>
  </div>

  <div class="footer">
    <div class="logo">O</div>
    <span class="brand">openfigma</span>
  </div>
</div>
</body>
</html>
"""

# Slide 6: How it works (Code)
SLIDE_6_CODE = f"""
<!DOCTYPE html>
<html>
<head>
<style>
{BASE_STYLES}

.code-container {{
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}}

.code-block {{
  background: #0d0d12;
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 20px;
  overflow: hidden;
  margin: 32px 0;
}}

.code-header {{
  background: rgba(255,255,255,0.03);
  padding: 16px 24px;
  display: flex;
  align-items: center;
  gap: 12px;
  border-bottom: 1px solid rgba(255,255,255,0.06);
}}

.code-dots {{
  display: flex;
  gap: 8px;
}}

.code-dot {{
  width: 12px;
  height: 12px;
  border-radius: 50%;
}}

.code-dot.red {{ background: #ef4444; }}
.code-dot.yellow {{ background: #eab308; }}
.code-dot.green {{ background: #22c55e; }}

.code-title {{
  font-size: 14px;
  color: rgba(255,255,255,0.4);
  margin-left: 12px;
}}

.code-content {{
  padding: 32px;
  font-family: 'SF Mono', 'Fira Code', monospace;
  font-size: 18px;
  line-height: 1.7;
}}

.code-line {{
  display: flex;
}}

.line-number {{
  color: rgba(255,255,255,0.2);
  width: 40px;
  flex-shrink: 0;
  user-select: none;
}}

.keyword {{ color: #c084fc; }}
.string {{ color: #4ade80; }}
.function {{ color: #60a5fa; }}
.comment {{ color: rgba(255,255,255,0.3); font-style: italic; }}
.variable {{ color: #f472b6; }}

.output-label {{
  font-size: 14px;
  font-weight: 600;
  color: rgba(255,255,255,0.4);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-top: 24px;
  margin-bottom: 16px;
}}

.output-result {{
  display: flex;
  align-items: center;
  gap: 16px;
  background: rgba(34, 197, 94, 0.1);
  border: 1px solid rgba(34, 197, 94, 0.2);
  padding: 20px 24px;
  border-radius: 12px;
}}

.output-icon {{
  width: 48px;
  height: 48px;
  background: rgba(34, 197, 94, 0.2);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #4ade80;
}}

.output-text {{
  font-size: 18px;
  font-weight: 600;
}}

.output-file {{
  font-size: 14px;
  color: rgba(255,255,255,0.5);
  margin-top: 4px;
  font-family: 'SF Mono', monospace;
}}
</style>
</head>
<body>
<div class="slide">
  <div class="mesh"></div>
  <div class="grain"></div>
  <div class="slide-number">06 / 07</div>

  <div class="content">
    <div class="code-container">
      <div class="section-label" style="font-size: 14px; font-weight: 600; color: rgba(255,255,255,0.3); letter-spacing: 0.15em; text-transform: uppercase;">How It Works</div>
      <h1 class="headline" style="font-size: 56px;"><span class="accent">3 lines</span><br>of Python</h1>

      <div class="code-block">
        <div class="code-header">
          <div class="code-dots">
            <div class="code-dot red"></div>
            <div class="code-dot yellow"></div>
            <div class="code-dot green"></div>
          </div>
          <span class="code-title">create_post.py</span>
        </div>
        <div class="code-content">
          <div class="code-line">
            <span class="line-number">1</span>
            <span><span class="keyword">from</span> openfigma <span class="keyword">import</span> export_png</span>
          </div>
          <div class="code-line">
            <span class="line-number">2</span>
            <span></span>
          </div>
          <div class="code-line">
            <span class="line-number">3</span>
            <span>html = <span class="string">"&lt;your template&gt;"</span></span>
          </div>
          <div class="code-line">
            <span class="line-number">4</span>
            <span><span class="function">export_png</span>(html, <span class="string">"post.png"</span>)</span>
          </div>
        </div>
      </div>

      <div class="output-label">Output</div>
      <div class="output-result">
        <div class="output-icon">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M5 12l5 5L20 7"/>
          </svg>
        </div>
        <div>
          <div class="output-text">1080x1080 PNG exported</div>
          <div class="output-file">→ post.png (ready for LinkedIn)</div>
        </div>
      </div>
    </div>
  </div>

  <div class="footer">
    <div class="logo">O</div>
    <span class="brand">openfigma</span>
  </div>
</div>
</body>
</html>
"""

# Slide 7: CTA
SLIDE_7_CTA = f"""
<!DOCTYPE html>
<html>
<head>
<style>
{BASE_STYLES}

.cta-container {{
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}}

.big-logo {{
  width: 140px;
  height: 140px;
  background: linear-gradient(135deg, #6366f1, #a855f7);
  border-radius: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 900;
  font-size: 72px;
  margin-bottom: 48px;
  box-shadow:
    0 0 80px rgba(99, 102, 241, 0.5),
    0 0 160px rgba(168, 85, 247, 0.3);
}}

.cta-headline {{
  font-size: 64px;
  font-weight: 800;
  line-height: 1.1;
  letter-spacing: -0.03em;
  margin-bottom: 24px;
}}

.cta-sub {{
  font-size: 24px;
  color: rgba(255,255,255,0.5);
  margin-bottom: 48px;
}}

.github-button {{
  display: inline-flex;
  align-items: center;
  gap: 16px;
  background: #fff;
  color: #0a0a0f;
  padding: 24px 48px;
  border-radius: 16px;
  font-size: 22px;
  font-weight: 700;
  margin-bottom: 24px;
}}

.github-button svg {{
  width: 28px;
  height: 28px;
}}

.no-bs {{
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 16px;
  margin-top: 32px;
}}

.no-bs-tag {{
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 16px;
  color: rgba(255,255,255,0.4);
}}

.no-bs-tag svg {{
  color: #4ade80;
}}
</style>
</head>
<body>
<div class="slide">
  <div class="mesh"></div>
  <div class="grain"></div>
  <div class="slide-number">07 / 07</div>

  <div class="content">
    <div class="cta-container">
      <div class="big-logo">O</div>

      <h1 class="cta-headline">
        Star it.<br>
        <span class="accent">Use it.</span>
      </h1>

      <p class="cta-sub">No signup. No waitlist. No BS.</p>

      <div class="github-button">
        <svg viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
        </svg>
        github.com/federicodeponte/openfigma
      </div>

      <div class="no-bs">
        <div class="no-bs-tag">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <path d="M5 12l5 5L20 7"/>
          </svg>
          MIT License
        </div>
        <div class="no-bs-tag">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <path d="M5 12l5 5L20 7"/>
          </svg>
          Free forever
        </div>
        <div class="no-bs-tag">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <path d="M5 12l5 5L20 7"/>
          </svg>
          pip install openfigma
        </div>
      </div>
    </div>
  </div>

  <div class="footer">
    <div class="logo">O</div>
    <span class="brand">openfigma</span>
  </div>
</div>
</body>
</html>
"""

SLIDES = [
    ("01_hook", SLIDE_1_HOOK),
    ("02_problem", SLIDE_2_PROBLEM),
    ("03_solution", SLIDE_3_SOLUTION),
    ("04_showcase_statement", SLIDE_4_SHOWCASE_1),
    ("05_showcase_metric", SLIDE_5_SHOWCASE_2),
    ("06_code", SLIDE_6_CODE),
    ("07_cta", SLIDE_7_CTA),
]

def main():
    import os

    output_dir = "/home/tech_scaile_it/openfigma/exports/linkedin_promo"
    os.makedirs(output_dir, exist_ok=True)

    print("Generating LinkedIn carousel slides...")
    print(f"Output: {output_dir}")
    print("-" * 40)

    with PNGExporter() as exporter:
        for name, html in SLIDES:
            output_path = f"{output_dir}/{name}.png"
            exporter.export(html, output_path, width=WIDTH, height=HEIGHT)
            print(f"  {name}.png")

    print("-" * 40)
    print(f"Done! {len(SLIDES)} slides generated.")

if __name__ == "__main__":
    main()
