#!/usr/bin/env python3
"""
LinkedIn Carousel V10 - BOLD DESIGN
- Background elements at 20-25% opacity (actually visible)
- Hero visual element on each wrapper slide
- Confident, not subtle
- Remove clutter, keep impact
"""

import sys
import base64
sys.path.insert(0, '/home/tech_scaile_it/openfigma')

from openfigma import PNGExporter

WIDTH = 1080
HEIGHT = 1350

def load_template_b64(name):
    with open(f'/home/tech_scaile_it/openfigma/exports/premium/{name}.png', 'rb') as f:
        return base64.b64encode(f.read()).decode()

LOGO_SMALL = '''<svg width="48" height="48" viewBox="0 0 120 120" fill="none"><defs><linearGradient id="logoGradS" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#6366f1"/><stop offset="100%" style="stop-color:#a855f7"/></linearGradient></defs><rect x="4" y="4" width="112" height="112" rx="28" fill="url(#logoGradS)"/><path d="M52 40L32 60L52 80" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M68 40L88 60L68 80" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="60" cy="60" r="6" fill="white"/></svg>'''

NOISE_SVG = "data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E"

# ============================================
# SLIDE 1: HOOK - Giant "?" as hero
# ============================================
SLIDE_1 = f"""<!DOCTYPE html><html><head><style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: #07070b;
  color: #fff;
  width: 1080px; height: 1350px;
  overflow: hidden; position: relative;
}}

/* Blobs */
.blob {{
  position: absolute;
  border-radius: 50%;
  filter: blur(120px);
}}
.blob-1 {{
  width: 800px; height: 800px;
  top: -300px; right: -200px;
  background: linear-gradient(135deg, #6366f1, #a855f7);
  opacity: 0.5;
}}
.blob-2 {{
  width: 500px; height: 500px;
  bottom: -100px; left: -150px;
  background: linear-gradient(135deg, #f97316, #ec4899);
  opacity: 0.3;
}}

/* Noise */
.grain {{
  position: absolute; inset: 0;
  opacity: 0.06;
  background-image: url("{NOISE_SVG}");
  pointer-events: none;
}}

/* HERO: Giant "?" - 25% opacity, actually visible */
.hero-question {{
  position: absolute;
  top: -50px; right: -80px;
  font-size: 800px;
  font-weight: 900;
  color: rgba(255, 255, 255, 0.12);
  line-height: 0.8;
  pointer-events: none;
}}

/* Orange accent bar */
.accent-bar {{
  position: absolute;
  bottom: 0; left: 0; right: 0;
  height: 8px;
  background: linear-gradient(90deg, #f97316, #ec4899, #8b5cf6);
}}

.slide {{
  position: relative; z-index: 1;
  width: 100%; height: 100%;
  padding: 72px;
  display: flex; flex-direction: column;
}}

.slide-num {{
  position: absolute; top: 64px; right: 72px;
  font-size: 14px; font-weight: 700;
  color: rgba(255,255,255,0.25);
  letter-spacing: 0.2em;
}}

.content {{ flex: 1; display: flex; flex-direction: column; justify-content: center; max-width: 800px; }}

.tag {{
  display: inline-flex; align-items: center; gap: 10px;
  background: rgba(249, 115, 22, 0.2);
  border: 2px solid rgba(249, 115, 22, 0.5);
  padding: 12px 20px; border-radius: 8px;
  font-size: 13px; font-weight: 800;
  color: #fb923c;
  margin-bottom: 40px; width: fit-content;
  text-transform: uppercase;
  letter-spacing: 0.15em;
}}

.headline {{
  font-size: 112px;
  font-weight: 900;
  line-height: 0.88;
  letter-spacing: -0.045em;
}}
.line-strike {{
  position: relative;
  display: inline-block;
  color: rgba(255,255,255,0.2);
}}
.line-strike::after {{
  content: '';
  position: absolute;
  left: -10px; right: -10px;
  top: 55%;
  height: 12px;
  background: linear-gradient(90deg, #ef4444, #f97316);
  transform: rotate(-2deg);
  border-radius: 6px;
}}
.line-accent {{
  background: linear-gradient(135deg, #818cf8, #c084fc, #f472b6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}

.subhead {{
  font-size: 28px;
  font-weight: 500;
  color: rgba(255,255,255,0.5);
  line-height: 1.5;
  margin-top: 32px;
}}

.swipe {{
  display: inline-flex; align-items: center; gap: 16px;
  margin-top: 48px;
  padding: 16px 28px;
  background: linear-gradient(135deg, #f97316, #ea580c);
  border-radius: 16px;
  width: fit-content;
  box-shadow: 0 8px 32px rgba(249, 115, 22, 0.4);
}}
.swipe-text {{ font-size: 18px; font-weight: 700; color: #fff; }}

.footer {{ display: flex; align-items: center; gap: 14px; }}
.brand {{ font-size: 18px; font-weight: 600; color: rgba(255,255,255,0.4); }}
</style></head><body>
<div class="blob blob-1"></div>
<div class="blob blob-2"></div>
<div class="grain"></div>
<div class="hero-question">?</div>
<div class="accent-bar"></div>

<div class="slide">
  <div class="slide-num">01 / 08</div>
  <div class="content">
    <div class="tag">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
      Open Source
    </div>
    <h1 class="headline">
      My designer<br>
      <span class="line-strike">quit</span><br>
      <span class="line-accent">so I built this</span>
    </h1>
    <p class="subhead">She got a full-time offer.<br>I needed a solution fast.</p>
    <div class="swipe">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
      <span class="swipe-text">Swipe to see what I made</span>
    </div>
  </div>
  <div class="footer">{LOGO_SMALL}<span class="brand">openfigma</span></div>
</div>
</body></html>"""

# ============================================
# SLIDE 2: PROBLEM - Big numbers on cards
# ============================================
SLIDE_2 = f"""<!DOCTYPE html><html><head><style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: #07070b;
  color: #fff;
  width: 1080px; height: 1350px;
  overflow: hidden; position: relative;
}}

/* Red glow - stronger */
.blob {{
  position: absolute;
  width: 800px; height: 800px;
  top: 50%; left: 50%;
  transform: translate(-50%, -40%);
  background: radial-gradient(circle, rgba(239, 68, 68, 0.4) 0%, transparent 60%);
  filter: blur(80px);
}}

/* Noise */
.grain {{
  position: absolute; inset: 0;
  opacity: 0.06;
  background-image: url("{NOISE_SVG}");
  pointer-events: none;
}}

/* HERO: Giant X - 20% visible */
.hero-x {{
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  font-size: 1000px;
  font-weight: 900;
  color: rgba(239, 68, 68, 0.15);
  line-height: 0.7;
}}

.slide {{ position: relative; z-index: 1; width: 100%; height: 100%; padding: 72px; display: flex; flex-direction: column; }}
.slide-num {{ position: absolute; top: 64px; right: 72px; font-size: 14px; font-weight: 700; color: rgba(255,255,255,0.25); letter-spacing: 0.2em; }}

.header {{ margin-bottom: 32px; }}
.label {{
  font-size: 13px; font-weight: 800;
  color: #ef4444;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  margin-bottom: 16px;
}}
.headline {{ font-size: 68px; font-weight: 900; line-height: 0.95; letter-spacing: -0.04em; }}
.headline span {{ color: #ef4444; }}

/* Cards with BIG numbers */
.cards {{ flex: 1; display: flex; flex-direction: column; gap: 16px; }}

.card {{
  background: rgba(15, 8, 10, 0.85);
  border: 2px solid rgba(239, 68, 68, 0.2);
  border-radius: 20px;
  padding: 24px 28px;
  display: flex; align-items: center; gap: 24px;
  box-shadow: 0 4px 24px rgba(0,0,0,0.3);
}}
.card-1 {{ border-color: rgba(239, 68, 68, 0.5); background: rgba(239, 68, 68, 0.1); }}

/* Hero element: Big number */
.card-num {{
  font-size: 48px;
  font-weight: 900;
  color: rgba(239, 68, 68, 0.6);
  width: 72px;
  flex-shrink: 0;
  text-align: center;
}}
.card-1 .card-num {{ color: #ef4444; }}

.card h3 {{ font-size: 22px; font-weight: 700; margin-bottom: 4px; }}
.card p {{ font-size: 16px; color: rgba(255,255,255,0.5); }}

.footer {{ display: flex; align-items: center; gap: 14px; margin-top: auto; padding-top: 20px; }}
.brand {{ font-size: 18px; font-weight: 600; color: rgba(255,255,255,0.4); }}
</style></head><body>
<div class="blob"></div>
<div class="grain"></div>
<div class="hero-x">×</div>

<div class="slide">
  <div class="slide-num">02 / 08</div>
  <div class="header">
    <div class="label">The Problem</div>
    <h1 class="headline">Design tools<br>are <span>broken</span></h1>
  </div>
  <div class="cards">
    <div class="card card-1">
      <div class="card-num">01</div>
      <div><h3>Steep learning curve</h3><p>Weeks to learn Figma or Canva properly</p></div>
    </div>
    <div class="card">
      <div class="card-num">02</div>
      <div><h3>Expensive templates</h3><p>$20-50 per pack, subscriptions add up</p></div>
    </div>
    <div class="card">
      <div class="card-num">03</div>
      <div><h3>Manual repetition</h3><p>Copy, paste, tweak, export... every time</p></div>
    </div>
    <div class="card">
      <div class="card-num">04</div>
      <div><h3>Designer dependency</h3><p>Need someone for every visual asset</p></div>
    </div>
  </div>
  <div class="footer">{LOGO_SMALL}<span class="brand">openfigma</span></div>
</div>
</body></html>"""

# ============================================
# SLIDE 3: SOLUTION - Giant logo as hero
# ============================================
SLIDE_3 = f"""<!DOCTYPE html><html><head><style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: #07070b;
  color: #fff;
  width: 1080px; height: 1350px;
  overflow: hidden; position: relative;
}}

/* Strong gradient background */
.bg-gradient {{
  position: absolute; inset: 0;
  background: radial-gradient(ellipse 100% 80% at 50% 30%, rgba(99, 102, 241, 0.35) 0%, transparent 50%),
              radial-gradient(ellipse 80% 60% at 50% 70%, rgba(34, 197, 94, 0.2) 0%, transparent 50%);
}}

/* Noise */
.grain {{
  position: absolute; inset: 0;
  opacity: 0.06;
  background-image: url("{NOISE_SVG}");
  pointer-events: none;
}}

/* HERO: Word "openfigma" as giant background text */
.hero-text {{
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%) rotate(-8deg);
  font-size: 180px;
  font-weight: 900;
  color: rgba(99, 102, 241, 0.08);
  letter-spacing: -0.04em;
  white-space: nowrap;
  pointer-events: none;
}}

.slide {{ position: relative; z-index: 1; width: 100%; height: 100%; padding: 72px; display: flex; flex-direction: column; }}
.slide-num {{ position: absolute; top: 64px; right: 72px; font-size: 14px; font-weight: 700; color: rgba(255,255,255,0.25); letter-spacing: 0.2em; }}

.content {{ flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }}

/* Giant logo with dramatic glow */
.logo-hero {{
  margin-bottom: 40px;
  position: relative;
}}
.logo-glow {{
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  width: 400px; height: 400px;
  background: radial-gradient(circle, rgba(99, 102, 241, 0.6) 0%, rgba(168, 85, 247, 0.3) 30%, transparent 70%);
  filter: blur(60px);
}}
.logo-hero svg {{
  position: relative;
  z-index: 1;
  filter: drop-shadow(0 0 30px rgba(99, 102, 241, 0.8));
}}

.headline {{ font-size: 88px; font-weight: 900; line-height: 0.95; letter-spacing: -0.04em; margin-bottom: 20px; }}
.headline span {{
  background: linear-gradient(135deg, #818cf8, #a855f7, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}

.subhead {{ font-size: 26px; font-weight: 500; color: rgba(255,255,255,0.55); line-height: 1.5; margin-bottom: 40px; }}

.features {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 12px; margin-bottom: 36px; }}
.feat {{
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.15);
  padding: 14px 24px; border-radius: 12px;
  font-size: 15px; font-weight: 600;
  color: rgba(255,255,255,0.8);
}}
.feat.primary {{
  background: rgba(34, 197, 94, 0.2);
  border-color: rgba(34, 197, 94, 0.5);
  color: #4ade80;
}}

.pip-box {{
  background: rgba(0,0,0,0.5);
  border: 2px solid rgba(34, 197, 94, 0.4);
  border-radius: 16px;
  padding: 20px 36px;
  display: inline-flex; align-items: center; gap: 14px;
  box-shadow: 0 8px 32px rgba(34, 197, 94, 0.2);
}}
.pip-box .dollar {{ color: #4ade80; font-family: 'SF Mono', Monaco, monospace; font-size: 20px; font-weight: 700; }}
.pip-box code {{ font-family: 'SF Mono', Monaco, monospace; font-size: 20px; font-weight: 600; }}

.footer {{ display: flex; align-items: center; justify-content: center; gap: 14px; }}
.brand {{ font-size: 18px; font-weight: 600; color: rgba(255,255,255,0.4); }}
</style></head><body>
<div class="bg-gradient"></div>
<div class="grain"></div>
<div class="hero-text">openfigma</div>

<div class="slide">
  <div class="slide-num">03 / 08</div>
  <div class="content">
    <div class="logo-hero">
      <div class="logo-glow"></div>
      <svg width="200" height="200" viewBox="0 0 120 120" fill="none"><defs><linearGradient id="logoGradB" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#6366f1"/><stop offset="100%" style="stop-color:#a855f7"/></linearGradient></defs><rect x="4" y="4" width="112" height="112" rx="28" fill="url(#logoGradB)"/><path d="M52 40L32 60L52 80" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M68 40L88 60L68 80" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="60" cy="60" r="6" fill="white"/></svg>
    </div>
    <h1 class="headline">Meet <span>openfigma</span></h1>
    <p class="subhead">Code-first design library.<br>Write Python → Get Figma-quality graphics.</p>
    <div class="features">
      <span class="feat primary">100% Open Source</span>
      <span class="feat">No design skills needed</span>
      <span class="feat">Python + HTML/CSS</span>
      <span class="feat">Instant PNG export</span>
    </div>
    <div class="pip-box">
      <span class="dollar">$</span>
      <code>pip install openfigma</code>
    </div>
  </div>
  <div class="footer">{LOGO_SMALL}<span class="brand">openfigma</span></div>
</div>
</body></html>"""

# ============================================
# SLIDE 7: CODE - Bold "4", clean window
# ============================================
SLIDE_7 = f"""<!DOCTYPE html><html><head><style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: #07070b;
  color: #fff;
  width: 1080px; height: 1350px;
  overflow: hidden; position: relative;
}}

/* Subtle gradient */
.bg-gradient {{
  position: absolute; inset: 0;
  background: radial-gradient(ellipse 80% 60% at 70% 30%, rgba(99, 102, 241, 0.2) 0%, transparent 50%),
              radial-gradient(ellipse 60% 80% at 30% 70%, rgba(34, 197, 94, 0.15) 0%, transparent 50%);
}}

/* Noise */
.grain {{
  position: absolute; inset: 0;
  opacity: 0.06;
  background-image: url("{NOISE_SVG}");
  pointer-events: none;
}}

/* HERO: Giant "4" - 20% visible */
.hero-num {{
  position: absolute;
  top: -120px; left: -100px;
  font-size: 900px;
  font-weight: 900;
  color: rgba(99, 102, 241, 0.12);
  line-height: 0.75;
  pointer-events: none;
}}

.slide {{ position: relative; z-index: 1; width: 100%; height: 100%; padding: 72px; display: flex; flex-direction: column; }}
.slide-num {{ position: absolute; top: 64px; right: 72px; font-size: 14px; font-weight: 700; color: rgba(255,255,255,0.25); letter-spacing: 0.2em; }}

.header {{ margin-bottom: 36px; }}
.label {{ font-size: 13px; font-weight: 800; color: rgba(255,255,255,0.35); letter-spacing: 0.25em; text-transform: uppercase; margin-bottom: 16px; }}
.headline {{ font-size: 80px; font-weight: 900; line-height: 0.95; letter-spacing: -0.04em; }}
.headline span {{
  background: linear-gradient(135deg, #818cf8, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}

.code-window {{
  flex: 1;
  background: rgba(6, 6, 12, 0.95);
  border: 2px solid rgba(99, 102, 241, 0.25);
  border-radius: 24px;
  overflow: hidden;
  display: flex; flex-direction: column;
  box-shadow: 0 4px 16px rgba(0,0,0,0.2), 0 24px 64px rgba(0,0,0,0.4);
}}

.window-header {{
  background: rgba(255,255,255,0.04);
  padding: 18px 24px;
  display: flex; align-items: center; gap: 10px;
  border-bottom: 1px solid rgba(255,255,255,0.08);
}}
.dots {{ display: flex; gap: 8px; }}
.dot {{ width: 14px; height: 14px; border-radius: 50%; }}
.dot.r {{ background: #ef4444; }}
.dot.y {{ background: #eab308; }}
.dot.g {{ background: #22c55e; }}
.code-file {{ font-size: 14px; color: rgba(255,255,255,0.4); margin-left: 12px; font-family: 'SF Mono', Monaco, monospace; }}

.code-body {{
  flex: 1; padding: 48px;
  font-family: 'SF Mono', Monaco, monospace;
  font-size: 26px; line-height: 2.4;
  display: flex; flex-direction: column; justify-content: center;
}}
.line {{ display: flex; }}
.ln {{ color: rgba(255,255,255,0.2); width: 56px; flex-shrink: 0; }}
.kw {{ color: #c084fc; }}
.str {{ color: #4ade80; }}
.fn {{ color: #60a5fa; }}

/* Output badge - more prominent */
.output-box {{
  position: absolute;
  bottom: 180px; right: 72px;
  display: flex; align-items: center; gap: 16px;
  background: rgba(34, 197, 94, 0.15);
  border: 2px solid rgba(34, 197, 94, 0.5);
  padding: 20px 28px;
  border-radius: 16px;
  transform: rotate(2deg);
  box-shadow: 0 8px 32px rgba(34, 197, 94, 0.25);
}}
.output-icon {{
  width: 52px; height: 52px;
  background: rgba(34, 197, 94, 0.25);
  border-radius: 12px;
  display: flex; align-items: center; justify-content: center;
  color: #4ade80;
}}
.output-text h4 {{ font-size: 18px; font-weight: 700; color: #4ade80; margin-bottom: 2px; }}
.output-text p {{ font-size: 14px; color: rgba(255,255,255,0.5); font-family: 'SF Mono', Monaco, monospace; }}

.footer {{ display: flex; align-items: center; gap: 14px; }}
.brand {{ font-size: 18px; font-weight: 600; color: rgba(255,255,255,0.4); }}
</style></head><body>
<div class="bg-gradient"></div>
<div class="grain"></div>
<div class="hero-num">4</div>

<div class="slide">
  <div class="slide-num">07 / 08</div>
  <div class="header">
    <div class="label">How It Works</div>
    <h1 class="headline"><span>4 lines</span> of Python</h1>
  </div>
  <div class="code-window">
    <div class="window-header">
      <div class="dots"><div class="dot r"></div><div class="dot y"></div><div class="dot g"></div></div>
      <span class="code-file">create_post.py</span>
    </div>
    <div class="code-body">
      <div class="line"><span class="ln">1</span><span class="kw">from</span> openfigma <span class="kw">import</span> html_to_png</div>
      <div class="line"><span class="ln">2</span></div>
      <div class="line"><span class="ln">3</span>html = <span class="str">"&lt;your template&gt;"</span></div>
      <div class="line"><span class="ln">4</span><span class="fn">html_to_png</span>(html, <span class="str">"post.png"</span>)</div>
    </div>
  </div>
  <div class="output-box">
    <div class="output-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M5 12l5 5L20 7"/></svg></div>
    <div class="output-text"><h4>Ready to post</h4><p>→ post.png</p></div>
  </div>
  <div class="footer">{LOGO_SMALL}<span class="brand">openfigma</span></div>
</div>
</body></html>"""

# ============================================
# SLIDE 8: CTA - Engagement box as hero, no rings
# ============================================
SLIDE_8 = f"""<!DOCTYPE html><html><head><style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: #07070b;
  color: #fff;
  width: 1080px; height: 1350px;
  overflow: hidden; position: relative;
}}

/* Strong centered glow */
.glow {{
  position: absolute;
  top: 30%; left: 50%;
  transform: translate(-50%, -50%);
  width: 800px; height: 600px;
  background: radial-gradient(ellipse, rgba(99, 102, 241, 0.4) 0%, transparent 60%);
  filter: blur(80px);
}}
.glow-2 {{
  position: absolute;
  bottom: 10%; left: 50%;
  transform: translateX(-50%);
  width: 600px; height: 400px;
  background: radial-gradient(ellipse, rgba(168, 85, 247, 0.3) 0%, transparent 60%);
  filter: blur(80px);
}}

/* Noise */
.grain {{
  position: absolute; inset: 0;
  opacity: 0.06;
  background-image: url("{NOISE_SVG}");
  pointer-events: none;
}}

/* Accent bars top and bottom */
.accent-top {{
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 6px;
  background: linear-gradient(90deg, #6366f1, #a855f7, #ec4899);
}}

.slide {{ position: relative; z-index: 1; width: 100%; height: 100%; padding: 72px; display: flex; flex-direction: column; }}
.slide-num {{ position: absolute; top: 64px; right: 72px; font-size: 14px; font-weight: 700; color: rgba(255,255,255,0.25); letter-spacing: 0.2em; }}

.content {{ flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }}

.logo-wrap {{
  margin-bottom: 32px;
}}
.logo-wrap svg {{ filter: drop-shadow(0 0 40px rgba(99, 102, 241, 0.6)); }}

.headline {{ font-size: 96px; font-weight: 900; line-height: 1.0; letter-spacing: -0.04em; margin-bottom: 12px; }}
.headline span {{
  background: linear-gradient(135deg, #818cf8, #c084fc, #f472b6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}

.tagline {{ font-size: 24px; color: rgba(255,255,255,0.5); margin-bottom: 36px; }}

.github-btn {{
  display: inline-flex; align-items: center; gap: 14px;
  background: #fff;
  color: #0a0a0f;
  padding: 22px 44px;
  border-radius: 16px;
  font-size: 18px;
  font-weight: 700;
  box-shadow: 0 4px 24px rgba(255,255,255,0.2);
}}

/* HERO: Engagement box - prominent */
.engagement {{
  margin-top: 48px;
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(168, 85, 247, 0.15));
  border: 3px solid rgba(139, 92, 246, 0.5);
  border-radius: 24px;
  padding: 36px 48px;
  max-width: 720px;
  box-shadow: 0 8px 40px rgba(99, 102, 241, 0.2);
}}
.engagement-head {{
  display: flex; align-items: center; justify-content: center; gap: 10px;
  font-size: 18px; font-weight: 700; color: #c4b5fd;
  margin-bottom: 12px;
}}
.engagement-text {{ font-size: 32px; font-weight: 700; line-height: 1.35; }}
.engagement-sub {{ font-size: 17px; color: rgba(255,255,255,0.45); margin-top: 14px; font-style: italic; }}

.trust {{ display: flex; justify-content: center; gap: 32px; margin-top: 36px; }}
.trust-item {{ display: flex; align-items: center; gap: 8px; font-size: 15px; color: rgba(255,255,255,0.5); }}
.trust-item svg {{ color: #4ade80; }}

.footer {{ display: flex; align-items: center; justify-content: center; gap: 14px; }}
.brand {{ font-size: 18px; font-weight: 600; color: rgba(255,255,255,0.4); }}
</style></head><body>
<div class="glow"></div>
<div class="glow-2"></div>
<div class="grain"></div>
<div class="accent-top"></div>

<div class="slide">
  <div class="slide-num">08 / 08</div>
  <div class="content">
    <div class="logo-wrap">
      <svg width="100" height="100" viewBox="0 0 120 120" fill="none"><defs><linearGradient id="logoGradH" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#6366f1"/><stop offset="100%" style="stop-color:#a855f7"/></linearGradient></defs><rect x="4" y="4" width="112" height="112" rx="28" fill="url(#logoGradH)"/><path d="M52 40L32 60L52 80" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M68 40L88 60L68 80" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="60" cy="60" r="6" fill="white"/></svg>
    </div>
    <h1 class="headline">Try it.<br><span>It's free.</span></h1>
    <p class="tagline">No signup. No waitlist. No BS.</p>
    <div class="github-btn">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
      github.com/federicodeponte/openfigma
    </div>
    <div class="engagement">
      <div class="engagement-head">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
        Want a custom design?
      </div>
      <div class="engagement-text">Comment your prompt below.<br>I'll generate it within 24h.</div>
      <div class="engagement-sub">"A metric card showing 500% growth"</div>
    </div>
    <div class="trust">
      <div class="trust-item"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M5 12l5 5L20 7"/></svg>MIT License</div>
      <div class="trust-item"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M5 12l5 5L20 7"/></svg>Free forever</div>
      <div class="trust-item"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M5 12l5 5L20 7"/></svg>pip install</div>
    </div>
  </div>
  <div class="footer">{LOGO_SMALL}<span class="brand">openfigma</span></div>
</div>
</body></html>"""

# ============================================
# Template slide generator
# ============================================
def make_template_slide(num, total, img_b64, template_name, description):
    return f"""<!DOCTYPE html><html><head><style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: #07070b;
  color: #fff;
  width: 1080px; height: 1350px;
  overflow: hidden; position: relative;
}}
.bg-gradient {{
  position: absolute; inset: 0;
  background: radial-gradient(ellipse 100% 60% at 50% 0%, rgba(99, 102, 241, 0.25) 0%, transparent 50%);
}}
.grain {{
  position: absolute; inset: 0;
  opacity: 0.05;
  background-image: url("{NOISE_SVG}");
  pointer-events: none;
}}
.slide {{ position: relative; z-index: 1; width: 100%; height: 100%; padding: 72px; display: flex; flex-direction: column; }}
.slide-num {{ position: absolute; top: 64px; right: 72px; font-size: 14px; font-weight: 700; color: rgba(255,255,255,0.25); letter-spacing: 0.2em; }}
.showcase {{ flex: 1; display: flex; flex-direction: column; }}
.label {{ font-size: 13px; font-weight: 800; color: #818cf8; letter-spacing: 0.2em; text-transform: uppercase; margin-bottom: 12px; }}
.headline {{ font-size: 48px; font-weight: 800; line-height: 0.95; letter-spacing: -0.03em; margin-bottom: 20px; }}
.accent {{ background: linear-gradient(135deg, #818cf8, #c084fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
.template-wrap {{ flex: 1; display: flex; flex-direction: column; }}
.template-img {{
  flex: 1;
  border-radius: 20px;
  overflow: hidden;
  border: 2px solid rgba(99, 102, 241, 0.2);
  box-shadow: 0 4px 16px rgba(0,0,0,0.15), 0 24px 64px rgba(0,0,0,0.3);
  display: flex; align-items: center; justify-content: center;
  background: #0a0a10;
}}
.template-img img {{ max-width: 100%; max-height: 100%; object-fit: contain; }}
.template-info {{ margin-top: 16px; font-size: 16px; color: rgba(255,255,255,0.45); }}
.footer {{ display: flex; align-items: center; gap: 14px; }}
.brand {{ font-size: 18px; font-weight: 600; color: rgba(255,255,255,0.4); }}
</style></head><body>
<div class="bg-gradient"></div>
<div class="grain"></div>
<div class="slide">
  <div class="slide-num">{num:02d} / {total:02d}</div>
  <div class="showcase">
    <div class="label">Premium Template</div>
    <h1 class="headline">{template_name}</h1>
    <div class="template-wrap">
      <div class="template-img"><img src="data:image/png;base64,{img_b64}"></div>
      <div class="template-info">{description}</div>
    </div>
  </div>
  <div class="footer">{LOGO_SMALL}<span class="brand">openfigma</span></div>
</div>
</body></html>"""

def main():
    import os

    output_dir = "/home/tech_scaile_it/openfigma/exports/linkedin_v10"
    os.makedirs(output_dir, exist_ok=True)

    print("Loading premium templates...")
    metric_b64 = load_template_b64('metric')
    testimonial_b64 = load_template_b64('testimonial')
    announcement_b64 = load_template_b64('announcement')

    print("Building V10 slides with BOLD design...")

    SLIDE_4 = make_template_slide(4, 8, metric_b64, "Metric <span class='accent'>Hero</span>", "Big numbers that demand attention")
    SLIDE_5 = make_template_slide(5, 8, testimonial_b64, "Social <span class='accent'>Proof</span>", "Customer quotes that convert")
    SLIDE_6 = make_template_slide(6, 8, announcement_b64, "Launch <span class='accent'>Announcement</span>", "News that gets noticed")

    SLIDES = [
        ("01_hook", SLIDE_1),
        ("02_problem", SLIDE_2),
        ("03_solution", SLIDE_3),
        ("04_metric", SLIDE_4),
        ("05_testimonial", SLIDE_5),
        ("06_announcement", SLIDE_6),
        ("07_code", SLIDE_7),
        ("08_cta", SLIDE_8),
    ]

    print(f"Generating {len(SLIDES)} slides...")
    print("-" * 40)

    with PNGExporter() as exporter:
        for name, html in SLIDES:
            output_path = f"{output_dir}/{name}.png"
            exporter.export(html, output_path, width=WIDTH, height=HEIGHT)
            print(f"  ✓ {name}.png")

    print("-" * 40)
    print("Done!")

if __name__ == "__main__":
    main()
