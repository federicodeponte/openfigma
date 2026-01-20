#!/usr/bin/env python3
"""
LinkedIn Carousel: OpenFigma Promo V2
Improved with real logo, better showcases, engagement CTA
"""

import sys
import base64
sys.path.insert(0, '/home/tech_scaile_it/openfigma')

from openfigma import PNGExporter

WIDTH = 1080
HEIGHT = 1350

# OpenFigma Logo SVG - Code brackets morphing into design shape
LOGO_SVG = '''<svg width="120" height="120" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="logoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#6366f1"/>
      <stop offset="100%" style="stop-color:#a855f7"/>
    </linearGradient>
  </defs>
  <!-- Rounded square background -->
  <rect x="4" y="4" width="112" height="112" rx="28" fill="url(#logoGrad)"/>
  <!-- Code bracket left < -->
  <path d="M52 40L32 60L52 80" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
  <!-- Code bracket right > morphing into design corner -->
  <path d="M68 40L88 60L68 80" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
  <!-- Center dot - the "figma" design element -->
  <circle cx="60" cy="60" r="6" fill="white"/>
</svg>'''

LOGO_SMALL_SVG = '''<svg width="48" height="48" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="logoGradS" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#6366f1"/>
      <stop offset="100%" style="stop-color:#a855f7"/>
    </linearGradient>
  </defs>
  <rect x="4" y="4" width="112" height="112" rx="28" fill="url(#logoGradS)"/>
  <path d="M52 40L32 60L52 80" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
  <path d="M68 40L88 60L68 80" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
  <circle cx="60" cy="60" r="6" fill="white"/>
</svg>'''

BASE_STYLES = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  font-family: 'Inter', -apple-system, sans-serif;
  background: #08080c;
  color: #fff;
  width: 1080px;
  height: 1350px;
  overflow: hidden;
}

.slide {
  width: 100%;
  height: 100%;
  padding: 56px;
  display: flex;
  flex-direction: column;
  position: relative;
}

.mesh {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse 100% 80% at 80% 20%, rgba(99, 102, 241, 0.12) 0%, transparent 50%),
    radial-gradient(ellipse 80% 100% at 20% 80%, rgba(168, 85, 247, 0.10) 0%, transparent 50%);
  pointer-events: none;
}

.grain {
  position: absolute;
  inset: 0;
  opacity: 0.025;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  pointer-events: none;
}

.slide-num {
  position: absolute;
  top: 48px;
  right: 56px;
  font-size: 14px;
  font-weight: 600;
  color: rgba(255,255,255,0.25);
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
  line-height: 1.0;
  letter-spacing: -0.035em;
}

.headline-lg { font-size: 80px; }

.accent {
  background: linear-gradient(135deg, #818cf8, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.subhead {
  font-size: 26px;
  font-weight: 500;
  color: rgba(255,255,255,0.55);
  line-height: 1.5;
  margin-top: 20px;
}

.footer {
  margin-top: auto;
  display: flex;
  align-items: center;
  gap: 14px;
  padding-top: 40px;
}

.brand {
  font-size: 18px;
  font-weight: 600;
  color: rgba(255,255,255,0.4);
}

.swipe {
  position: absolute;
  bottom: 56px;
  right: 56px;
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 15px;
  font-weight: 600;
  color: rgba(255,255,255,0.3);
}

.swipe svg {
  animation: bounce 1.5s ease-in-out infinite;
}

@keyframes bounce {
  0%, 100% { transform: translateX(0); }
  50% { transform: translateX(6px); }
}
"""

# Slide 1: Hook - Designer quit story
SLIDE_1 = f"""
<!DOCTYPE html>
<html>
<head>
<style>
{BASE_STYLES}

.hook {{
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}}

.tag {{
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: rgba(99, 102, 241, 0.12);
  border: 1px solid rgba(99, 102, 241, 0.25);
  padding: 14px 22px;
  border-radius: 100px;
  font-size: 15px;
  font-weight: 600;
  color: #a5b4fc;
  margin-bottom: 36px;
  width: fit-content;
}}

.strike {{
  text-decoration: line-through;
  text-decoration-color: #ef4444;
  text-decoration-thickness: 4px;
  color: rgba(255,255,255,0.35);
}}

.arrow-hint {{
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 48px;
  font-size: 16px;
  font-weight: 600;
  color: rgba(255,255,255,0.4);
}}

.arrow-hint .circle {{
  width: 44px;
  height: 44px;
  border: 2px solid rgba(255,255,255,0.15);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}}
</style>
</head>
<body>
<div class="slide">
  <div class="mesh"></div>
  <div class="grain"></div>
  <div class="slide-num">01 / 07</div>

  <div class="content">
    <div class="hook">
      <div class="tag">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
        </svg>
        Open Source
      </div>

      <h1 class="headline headline-lg">
        My designer<br>
        <span class="strike">quit</span><br>
        <span class="accent">so I built this</span>
      </h1>

      <p class="subhead">
        She got a full-time offer.<br>
        I needed a solution fast...
      </p>

      <div class="arrow-hint">
        <div class="circle">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M5 12h14M12 5l7 7-7 7"/>
          </svg>
        </div>
        Swipe to see what I made
      </div>
    </div>
  </div>

  <div class="footer">
    {LOGO_SMALL_SVG}
    <span class="brand">openfigma</span>
  </div>
</div>
</body>
</html>
"""

# Slide 2: Problem
SLIDE_2 = f"""
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
  gap: 24px;
}}

.section-label {{
  font-size: 13px;
  font-weight: 700;
  color: rgba(255,255,255,0.3);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  margin-bottom: 12px;
}}

.card {{
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 20px;
  padding: 28px 32px;
  display: flex;
  align-items: center;
  gap: 24px;
}}

.card-icon {{
  width: 52px;
  height: 52px;
  background: rgba(239, 68, 68, 0.12);
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  color: #f87171;
}}

.card h3 {{
  font-size: 22px;
  font-weight: 700;
  margin-bottom: 6px;
}}

.card p {{
  font-size: 16px;
  color: rgba(255,255,255,0.45);
  line-height: 1.4;
}}
</style>
</head>
<body>
<div class="slide">
  <div class="mesh"></div>
  <div class="grain"></div>
  <div class="slide-num">02 / 07</div>

  <div class="content">
    <div class="section-label">The Problem</div>
    <h1 class="headline">Design tools<br>are <span class="accent">broken</span></h1>

    <div class="problems">
      <div class="card">
        <div class="card-icon">
          <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>
          </svg>
        </div>
        <div>
          <h3>Steep learning curve</h3>
          <p>Weeks to learn Figma or Canva properly</p>
        </div>
      </div>

      <div class="card">
        <div class="card-icon">
          <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>
          </svg>
        </div>
        <div>
          <h3>Expensive templates</h3>
          <p>$20-50 per pack, subscriptions add up fast</p>
        </div>
      </div>

      <div class="card">
        <div class="card-icon">
          <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/>
          </svg>
        </div>
        <div>
          <h3>Manual repetition</h3>
          <p>Copy, paste, tweak, export... every single time</p>
        </div>
      </div>

      <div class="card">
        <div class="card-icon">
          <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>
          </svg>
        </div>
        <div>
          <h3>Designer dependency</h3>
          <p>Need someone else for every visual asset</p>
        </div>
      </div>
    </div>
  </div>

  <div class="footer">
    {LOGO_SMALL_SVG}
    <span class="brand">openfigma</span>
  </div>
</div>
</body>
</html>
"""

# Slide 3: Solution intro
SLIDE_3 = f"""
<!DOCTYPE html>
<html>
<head>
<style>
{BASE_STYLES}

.solution {{
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}}

.logo-big {{
  margin-bottom: 40px;
}}

.features {{
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 40px;
}}

.feat {{
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
  padding: 14px 22px;
  border-radius: 100px;
  font-size: 16px;
  font-weight: 500;
  color: rgba(255,255,255,0.65);
}}

.feat.green {{
  background: rgba(34, 197, 94, 0.12);
  border-color: rgba(34, 197, 94, 0.25);
  color: #4ade80;
}}

.pip-cmd {{
  display: inline-flex;
  align-items: center;
  gap: 12px;
  background: rgba(0,0,0,0.4);
  border: 1px solid rgba(255,255,255,0.1);
  padding: 18px 28px;
  border-radius: 12px;
  font-family: 'SF Mono', 'Fira Code', monospace;
  font-size: 18px;
  margin-top: 36px;
  width: fit-content;
}}

.pip-cmd .dollar {{
  color: rgba(255,255,255,0.3);
}}
</style>
</head>
<body>
<div class="slide">
  <div class="mesh"></div>
  <div class="grain"></div>
  <div class="slide-num">03 / 07</div>

  <div class="content">
    <div class="solution">
      <div class="logo-big">
        {LOGO_SVG}
      </div>

      <h1 class="headline">Meet<br><span class="accent">openfigma</span></h1>

      <p class="subhead">
        Code-first design library.<br>
        Write Python → Get Figma-quality graphics.
      </p>

      <div class="features">
        <span class="feat green">100% Open Source</span>
        <span class="feat">No design skills needed</span>
        <span class="feat">Python + HTML/CSS</span>
        <span class="feat">Instant PNG export</span>
      </div>

      <div class="pip-cmd">
        <span class="dollar">$</span> pip install openfigma
      </div>
    </div>
  </div>

  <div class="footer">
    {LOGO_SMALL_SVG}
    <span class="brand">openfigma</span>
  </div>
</div>
</body>
</html>
"""

# Slide 4: Showcase - actual templates grid
SLIDE_4 = f"""
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

.section-label {{
  font-size: 13px;
  font-weight: 700;
  color: #818cf8;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  margin-bottom: 12px;
}}

.grid {{
  flex: 1;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-top: 32px;
}}

.template {{
  border-radius: 16px;
  overflow: hidden;
  position: relative;
  background: #0c0c14;
  border: 1px solid rgba(255,255,255,0.08);
}}

.template-inner {{
  width: 100%;
  height: 100%;
  padding: 24px;
  display: flex;
  flex-direction: column;
}}

/* Statement template mini */
.t1 {{
  background:
    radial-gradient(ellipse 120% 80% at 70% 60%, rgba(139, 92, 246, 0.15) 0%, transparent 50%),
    radial-gradient(ellipse 80% 100% at 10% 80%, rgba(236, 72, 153, 0.10) 0%, transparent 50%),
    #0c0c14;
}}

.t1 .label {{ font-size: 10px; color: rgba(255,255,255,0.4); letter-spacing: 0.15em; text-transform: uppercase; margin-bottom: 12px; }}
.t1 .quote {{ font-size: 18px; font-weight: 600; line-height: 1.3; flex: 1; }}
.t1 .author {{ font-size: 11px; color: rgba(255,255,255,0.4); margin-top: auto; }}

/* Metric template mini */
.t2 {{
  background:
    radial-gradient(ellipse 100% 100% at 80% 80%, rgba(34, 197, 94, 0.12) 0%, transparent 50%),
    #0c0c14;
}}

.t2 .label {{ font-size: 10px; color: rgba(255,255,255,0.4); letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 8px; }}
.t2 .metric {{ font-size: 48px; font-weight: 800; background: linear-gradient(135deg, #4ade80, #22c55e); -webkit-background-clip: text; -webkit-text-fill-color: transparent; line-height: 1; }}
.t2 .change {{ display: inline-flex; align-items: center; gap: 4px; font-size: 12px; color: #4ade80; margin-top: 8px; }}
.t2 .bars {{ display: flex; align-items: flex-end; gap: 4px; height: 40px; margin-top: auto; }}
.t2 .bar {{ flex: 1; background: rgba(34, 197, 94, 0.3); border-radius: 2px 2px 0 0; }}

/* Testimonial template mini */
.t3 {{
  background:
    radial-gradient(ellipse 80% 80% at 20% 80%, rgba(251, 191, 36, 0.08) 0%, transparent 50%),
    #0c0c14;
}}

.t3 .stars {{ color: #fbbf24; font-size: 14px; letter-spacing: 2px; margin-bottom: 12px; }}
.t3 .quote {{ font-size: 16px; font-weight: 500; line-height: 1.4; font-style: italic; flex: 1; }}
.t3 .author-row {{ display: flex; align-items: center; gap: 10px; margin-top: auto; }}
.t3 .avatar {{ width: 32px; height: 32px; background: linear-gradient(135deg, #6366f1, #a855f7); border-radius: 50%; }}
.t3 .author-info {{ font-size: 11px; }}
.t3 .author-name {{ font-weight: 600; }}
.t3 .author-title {{ color: rgba(255,255,255,0.4); }}

/* Announcement template mini */
.t4 {{
  background:
    radial-gradient(ellipse 100% 100% at 50% 0%, rgba(99, 102, 241, 0.2) 0%, transparent 50%),
    #0c0c14;
}}

.t4 .badge {{ display: inline-block; background: rgba(99, 102, 241, 0.2); border: 1px solid rgba(99, 102, 241, 0.3); padding: 6px 12px; border-radius: 100px; font-size: 10px; font-weight: 600; color: #a5b4fc; margin-bottom: 12px; }}
.t4 .title {{ font-size: 22px; font-weight: 700; line-height: 1.2; }}
.t4 .btn {{ margin-top: auto; background: linear-gradient(135deg, #6366f1, #a855f7); padding: 10px 20px; border-radius: 8px; font-size: 12px; font-weight: 600; text-align: center; }}

.template-name {{
  position: absolute;
  bottom: 12px;
  left: 12px;
  font-size: 11px;
  font-weight: 600;
  color: rgba(255,255,255,0.3);
  text-transform: uppercase;
  letter-spacing: 0.1em;
}}
</style>
</head>
<body>
<div class="slide">
  <div class="mesh"></div>
  <div class="grain"></div>
  <div class="slide-num">04 / 07</div>

  <div class="content">
    <div class="showcase">
      <div class="section-label">What You Can Create</div>
      <h1 class="headline" style="font-size: 56px;">8 Premium<br><span class="accent">Templates</span></h1>

      <div class="grid">
        <div class="template">
          <div class="template-inner t1">
            <div class="label">Insight</div>
            <div class="quote">"The best code is no code at all."</div>
            <div class="author">— Jeff Atwood</div>
          </div>
          <div class="template-name">Statement</div>
        </div>

        <div class="template">
          <div class="template-inner t2">
            <div class="label">Monthly Users</div>
            <div class="metric">2.4M</div>
            <div class="change">↑ +127%</div>
            <div class="bars">
              <div class="bar" style="height: 30%"></div>
              <div class="bar" style="height: 50%"></div>
              <div class="bar" style="height: 40%"></div>
              <div class="bar" style="height: 70%"></div>
              <div class="bar" style="height: 60%"></div>
              <div class="bar" style="height: 90%"></div>
              <div class="bar" style="height: 100%"></div>
            </div>
          </div>
          <div class="template-name">Metric</div>
        </div>

        <div class="template">
          <div class="template-inner t3">
            <div class="stars">★★★★★</div>
            <div class="quote">"This changed how our team creates content."</div>
            <div class="author-row">
              <div class="avatar"></div>
              <div class="author-info">
                <div class="author-name">Sarah Chen</div>
                <div class="author-title">Head of Marketing</div>
              </div>
            </div>
          </div>
          <div class="template-name">Testimonial</div>
        </div>

        <div class="template">
          <div class="template-inner t4">
            <div class="badge">NEW RELEASE</div>
            <div class="title">We just launched v2.0</div>
            <div class="btn">Learn More →</div>
          </div>
          <div class="template-name">Announcement</div>
        </div>
      </div>
    </div>
  </div>

  <div class="footer">
    {LOGO_SMALL_SVG}
    <span class="brand">openfigma</span>
  </div>
</div>
</body>
</html>
"""

# Slide 5: More templates
SLIDE_5 = f"""
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

.section-label {{
  font-size: 13px;
  font-weight: 700;
  color: #818cf8;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  margin-bottom: 12px;
}}

.grid {{
  flex: 1;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-top: 32px;
}}

.template {{
  border-radius: 16px;
  overflow: hidden;
  position: relative;
  background: #0c0c14;
  border: 1px solid rgba(255,255,255,0.08);
}}

.template-inner {{
  width: 100%;
  height: 100%;
  padding: 24px;
  display: flex;
  flex-direction: column;
}}

/* Comparison */
.t5 {{
  background: #0c0c14;
}}

.t5 .split {{
  display: flex;
  gap: 12px;
  flex: 1;
}}

.t5 .side {{
  flex: 1;
  border-radius: 12px;
  padding: 16px;
  display: flex;
  flex-direction: column;
}}

.t5 .before {{
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.2);
}}

.t5 .after {{
  background: rgba(34, 197, 94, 0.1);
  border: 1px solid rgba(34, 197, 94, 0.2);
}}

.t5 .side-label {{
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 8px;
}}

.t5 .before .side-label {{ color: #f87171; }}
.t5 .after .side-label {{ color: #4ade80; }}

.t5 .side-value {{
  font-size: 28px;
  font-weight: 800;
  margin-top: auto;
}}

/* Features list */
.t6 {{
  background:
    radial-gradient(ellipse 80% 80% at 80% 20%, rgba(99, 102, 241, 0.1) 0%, transparent 50%),
    #0c0c14;
}}

.t6 .feature-item {{
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 0;
  border-bottom: 1px solid rgba(255,255,255,0.06);
}}

.t6 .feature-item:last-child {{
  border-bottom: none;
}}

.t6 .check {{
  width: 24px;
  height: 24px;
  background: rgba(34, 197, 94, 0.15);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #4ade80;
  flex-shrink: 0;
}}

.t6 .feature-text {{
  font-size: 14px;
  font-weight: 500;
}}

/* List/numbered */
.t7 {{
  background:
    radial-gradient(ellipse 100% 100% at 0% 100%, rgba(168, 85, 247, 0.1) 0%, transparent 50%),
    #0c0c14;
}}

.t7 .list-item {{
  display: flex;
  align-items: flex-start;
  gap: 14px;
  margin-bottom: 16px;
}}

.t7 .num {{
  width: 28px;
  height: 28px;
  background: linear-gradient(135deg, #6366f1, #a855f7);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  font-weight: 700;
  flex-shrink: 0;
}}

.t7 .list-text {{
  font-size: 14px;
  font-weight: 500;
  line-height: 1.4;
}}

/* Product */
.t8 {{
  background:
    radial-gradient(ellipse 100% 100% at 100% 0%, rgba(59, 130, 246, 0.12) 0%, transparent 50%),
    #0c0c14;
}}

.t8 .product-icon {{
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #3b82f6, #6366f1);
  border-radius: 14px;
  margin-bottom: 16px;
}}

.t8 .product-name {{
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 8px;
}}

.t8 .product-desc {{
  font-size: 13px;
  color: rgba(255,255,255,0.5);
  line-height: 1.4;
  flex: 1;
}}

.t8 .product-tags {{
  display: flex;
  gap: 8px;
  margin-top: auto;
}}

.t8 .tag {{
  background: rgba(255,255,255,0.06);
  padding: 6px 12px;
  border-radius: 100px;
  font-size: 11px;
  font-weight: 500;
  color: rgba(255,255,255,0.6);
}}

.template-name {{
  position: absolute;
  bottom: 12px;
  left: 12px;
  font-size: 11px;
  font-weight: 600;
  color: rgba(255,255,255,0.3);
  text-transform: uppercase;
  letter-spacing: 0.1em;
}}
</style>
</head>
<body>
<div class="slide">
  <div class="mesh"></div>
  <div class="grain"></div>
  <div class="slide-num">05 / 07</div>

  <div class="content">
    <div class="showcase">
      <div class="section-label">And More...</div>
      <h1 class="headline" style="font-size: 56px;">Every format<br><span class="accent">you need</span></h1>

      <div class="grid">
        <div class="template">
          <div class="template-inner t5">
            <div class="split">
              <div class="side before">
                <div class="side-label">Before</div>
                <div class="side-value">2hrs</div>
              </div>
              <div class="side after">
                <div class="side-label">After</div>
                <div class="side-value">5min</div>
              </div>
            </div>
          </div>
          <div class="template-name">Comparison</div>
        </div>

        <div class="template">
          <div class="template-inner t6">
            <div class="feature-item">
              <div class="check">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M5 12l5 5L20 7"/></svg>
              </div>
              <span class="feature-text">Dark mode support</span>
            </div>
            <div class="feature-item">
              <div class="check">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M5 12l5 5L20 7"/></svg>
              </div>
              <span class="feature-text">Responsive layouts</span>
            </div>
            <div class="feature-item">
              <div class="check">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M5 12l5 5L20 7"/></svg>
              </div>
              <span class="feature-text">Custom branding</span>
            </div>
            <div class="feature-item">
              <div class="check">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M5 12l5 5L20 7"/></svg>
              </div>
              <span class="feature-text">Export to PNG</span>
            </div>
          </div>
          <div class="template-name">Features</div>
        </div>

        <div class="template">
          <div class="template-inner t7">
            <div class="list-item">
              <div class="num">1</div>
              <span class="list-text">Install with pip</span>
            </div>
            <div class="list-item">
              <div class="num">2</div>
              <span class="list-text">Choose a template</span>
            </div>
            <div class="list-item">
              <div class="num">3</div>
              <span class="list-text">Customize content</span>
            </div>
            <div class="list-item">
              <div class="num">4</div>
              <span class="list-text">Export PNG</span>
            </div>
          </div>
          <div class="template-name">List</div>
        </div>

        <div class="template">
          <div class="template-inner t8">
            <div class="product-icon"></div>
            <div class="product-name">openfigma</div>
            <div class="product-desc">Code-first design library for developers</div>
            <div class="product-tags">
              <span class="tag">Python</span>
              <span class="tag">Open Source</span>
            </div>
          </div>
          <div class="template-name">Product</div>
        </div>
      </div>
    </div>
  </div>

  <div class="footer">
    {LOGO_SMALL_SVG}
    <span class="brand">openfigma</span>
  </div>
</div>
</body>
</html>
"""

# Slide 6: Code example
SLIDE_6 = f"""
<!DOCTYPE html>
<html>
<head>
<style>
{BASE_STYLES}

.code-slide {{
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}}

.section-label {{
  font-size: 13px;
  font-weight: 700;
  color: rgba(255,255,255,0.3);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  margin-bottom: 12px;
}}

.code-block {{
  background: #0d0d14;
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

.dots {{ display: flex; gap: 8px; }}
.dot {{ width: 12px; height: 12px; border-radius: 50%; }}
.dot.r {{ background: #ef4444; }}
.dot.y {{ background: #eab308; }}
.dot.g {{ background: #22c55e; }}

.code-file {{
  font-size: 13px;
  color: rgba(255,255,255,0.4);
  margin-left: 12px;
}}

.code-body {{
  padding: 28px 32px;
  font-family: 'SF Mono', 'Fira Code', monospace;
  font-size: 17px;
  line-height: 1.8;
}}

.line {{
  display: flex;
}}

.ln {{
  color: rgba(255,255,255,0.2);
  width: 36px;
  flex-shrink: 0;
  user-select: none;
}}

.kw {{ color: #c084fc; }}
.str {{ color: #4ade80; }}
.fn {{ color: #60a5fa; }}
.cmt {{ color: rgba(255,255,255,0.3); font-style: italic; }}

.output-box {{
  display: flex;
  align-items: center;
  gap: 20px;
  background: rgba(34, 197, 94, 0.08);
  border: 1px solid rgba(34, 197, 94, 0.2);
  padding: 24px 28px;
  border-radius: 16px;
}}

.output-icon {{
  width: 56px;
  height: 56px;
  background: rgba(34, 197, 94, 0.15);
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #4ade80;
}}

.output-text h4 {{
  font-size: 20px;
  font-weight: 700;
  margin-bottom: 4px;
}}

.output-text p {{
  font-size: 15px;
  color: rgba(255,255,255,0.5);
  font-family: 'SF Mono', monospace;
}}
</style>
</head>
<body>
<div class="slide">
  <div class="mesh"></div>
  <div class="grain"></div>
  <div class="slide-num">06 / 07</div>

  <div class="content">
    <div class="code-slide">
      <div class="section-label">How It Works</div>
      <h1 class="headline"><span class="accent">4 lines</span><br>of Python</h1>

      <div class="code-block">
        <div class="code-header">
          <div class="dots">
            <div class="dot r"></div>
            <div class="dot y"></div>
            <div class="dot g"></div>
          </div>
          <span class="code-file">create_post.py</span>
        </div>
        <div class="code-body">
          <div class="line"><span class="ln">1</span><span><span class="kw">from</span> openfigma <span class="kw">import</span> html_to_png</span></div>
          <div class="line"><span class="ln">2</span><span></span></div>
          <div class="line"><span class="ln">3</span><span>html = <span class="str">"&lt;your template html&gt;"</span></span></div>
          <div class="line"><span class="ln">4</span><span><span class="fn">html_to_png</span>(html, <span class="str">"post.png"</span>)</span></div>
        </div>
      </div>

      <div class="output-box">
        <div class="output-icon">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
            <path d="M5 12l5 5L20 7"/>
          </svg>
        </div>
        <div class="output-text">
          <h4>Ready for LinkedIn</h4>
          <p>→ post.png (1080×1080)</p>
        </div>
      </div>
    </div>
  </div>

  <div class="footer">
    {LOGO_SMALL_SVG}
    <span class="brand">openfigma</span>
  </div>
</div>
</body>
</html>
"""

# Slide 7: CTA with engagement hook
SLIDE_7 = f"""
<!DOCTYPE html>
<html>
<head>
<style>
{BASE_STYLES}

.cta {{
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}}

.logo-huge {{
  margin-bottom: 48px;
  filter: drop-shadow(0 0 60px rgba(99, 102, 241, 0.4)) drop-shadow(0 0 120px rgba(168, 85, 247, 0.2));
}}

.cta-head {{
  font-size: 64px;
  font-weight: 800;
  line-height: 1.05;
  letter-spacing: -0.03em;
  margin-bottom: 16px;
}}

.cta-sub {{
  font-size: 22px;
  color: rgba(255,255,255,0.5);
  margin-bottom: 40px;
}}

.github-btn {{
  display: inline-flex;
  align-items: center;
  gap: 14px;
  background: #fff;
  color: #0a0a0f;
  padding: 22px 44px;
  border-radius: 14px;
  font-size: 20px;
  font-weight: 700;
}}

.engagement {{
  margin-top: 56px;
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(168, 85, 247, 0.15));
  border: 1px solid rgba(139, 92, 246, 0.3);
  border-radius: 20px;
  padding: 32px 40px;
  max-width: 800px;
}}

.engagement-head {{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  font-size: 18px;
  font-weight: 700;
  color: #c4b5fd;
  margin-bottom: 12px;
}}

.engagement-head svg {{
  color: #a78bfa;
}}

.engagement-text {{
  font-size: 24px;
  font-weight: 600;
  line-height: 1.4;
}}

.engagement-sub {{
  font-size: 16px;
  color: rgba(255,255,255,0.5);
  margin-top: 12px;
}}

.no-bs {{
  display: flex;
  justify-content: center;
  gap: 24px;
  margin-top: 40px;
}}

.no-bs-item {{
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 15px;
  color: rgba(255,255,255,0.4);
}}

.no-bs-item svg {{
  color: #4ade80;
}}
</style>
</head>
<body>
<div class="slide">
  <div class="mesh"></div>
  <div class="grain"></div>
  <div class="slide-num">07 / 07</div>

  <div class="content">
    <div class="cta">
      <div class="logo-huge">
        <svg width="100" height="100" viewBox="0 0 120 120" fill="none" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="logoGradH" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" style="stop-color:#6366f1"/>
              <stop offset="100%" style="stop-color:#a855f7"/>
            </linearGradient>
          </defs>
          <rect x="4" y="4" width="112" height="112" rx="28" fill="url(#logoGradH)"/>
          <path d="M52 40L32 60L52 80" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
          <path d="M68 40L88 60L68 80" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
          <circle cx="60" cy="60" r="6" fill="white"/>
        </svg>
      </div>

      <h1 class="cta-head">
        Try it.<br>
        <span class="accent">It's free.</span>
      </h1>

      <p class="cta-sub">No signup. No waitlist. No BS.</p>

      <div class="github-btn">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
          <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
        </svg>
        github.com/federicodeponte/openfigma
      </div>

      <div class="engagement">
        <div class="engagement-head">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
          </svg>
          Want a custom design?
        </div>
        <div class="engagement-text">
          Comment your prompt below.<br>
          I'll generate it and send it within 24h.
        </div>
        <div class="engagement-sub">
          Example: "A metric card showing 500% growth in dark theme"
        </div>
      </div>

      <div class="no-bs">
        <div class="no-bs-item">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12l5 5L20 7"/></svg>
          MIT License
        </div>
        <div class="no-bs-item">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12l5 5L20 7"/></svg>
          Free forever
        </div>
        <div class="no-bs-item">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12l5 5L20 7"/></svg>
          pip install
        </div>
      </div>
    </div>
  </div>

  <div class="footer">
    {LOGO_SMALL_SVG}
    <span class="brand">openfigma</span>
  </div>
</div>
</body>
</html>
"""

SLIDES = [
    ("01_hook", SLIDE_1),
    ("02_problem", SLIDE_2),
    ("03_solution", SLIDE_3),
    ("04_templates_1", SLIDE_4),
    ("05_templates_2", SLIDE_5),
    ("06_code", SLIDE_6),
    ("07_cta", SLIDE_7),
]

def main():
    import os

    output_dir = "/home/tech_scaile_it/openfigma/exports/linkedin_v2"
    os.makedirs(output_dir, exist_ok=True)

    print("Generating LinkedIn carousel V2...")
    print(f"Output: {output_dir}")
    print("-" * 40)

    with PNGExporter() as exporter:
        for name, html in SLIDES:
            output_path = f"{output_dir}/{name}.png"
            exporter.export(html, output_path, width=WIDTH, height=HEIGHT)
            print(f"  ✓ {name}.png")

    print("-" * 40)
    print(f"Done! {len(SLIDES)} slides generated.")

if __name__ == "__main__":
    main()
