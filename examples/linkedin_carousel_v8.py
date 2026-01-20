#!/usr/bin/env python3
"""
LinkedIn Carousel V8 - V6 richness with targeted fixes
- Keep filter: blur() on blobs (works in Playwright)
- Remove only backdrop-filter (doesn't work headless)
- System fonts (reliable)
- Increased background element opacity (5-8%)
- CSS-based noise grain (more reliable than SVG filter)
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

# Base64 encoded 100x100 noise PNG (generated procedurally, grayscale noise)
NOISE_PNG = "data:image/png;base64,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"

# ============================================
# SLIDE 1: HOOK
# ============================================
SLIDE_1 = f"""<!DOCTYPE html><html><head><style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: #08080c;
  color: #fff;
  width: 1080px;
  height: 1350px;
  overflow: hidden;
  position: relative;
}}

/* Blurred gradient blobs - filter:blur WORKS in Playwright */
.blob {{
  position: absolute;
  border-radius: 50%;
  filter: blur(100px);
}}
.blob-1 {{
  width: 600px; height: 600px;
  top: -150px; right: -100px;
  background: linear-gradient(135deg, #6366f1, #a855f7);
  opacity: 0.4;
}}
.blob-2 {{
  width: 400px; height: 400px;
  bottom: 50px; left: -100px;
  background: linear-gradient(135deg, #f97316, #ec4899);
  opacity: 0.25;
}}

/* Noise overlay */
.noise {{
  position: absolute;
  inset: 0;
  background-image: url("{NOISE_PNG}");
  background-repeat: repeat;
  opacity: 0.08;
  pointer-events: none;
}}

/* VISIBLE background question mark - 6% opacity */
.bg-char {{
  position: absolute;
  top: 20px; right: -20px;
  font-size: 650px;
  font-weight: 900;
  color: rgba(255,255,255,0.06);
  line-height: 0.75;
  pointer-events: none;
}}

/* Decorative elements */
.deco-circle {{
  position: absolute;
  border-radius: 50%;
  border: 2px solid rgba(249, 115, 22, 0.35);
}}
.deco-circle-1 {{ width: 150px; height: 150px; bottom: 280px; right: 120px; }}
.deco-circle-2 {{ width: 80px; height: 80px; bottom: 350px; right: 200px; background: rgba(249, 115, 22, 0.15); }}

.deco-line {{
  position: absolute;
  height: 3px;
  background: linear-gradient(90deg, transparent, rgba(139, 92, 246, 0.5), transparent);
}}
.deco-line-1 {{ width: 200px; top: 250px; right: 200px; transform: rotate(-30deg); }}
.deco-line-2 {{ width: 120px; bottom: 450px; left: 100px; transform: rotate(20deg); }}

.slide {{
  position: relative; z-index: 1;
  width: 100%; height: 100%;
  padding: 64px;
  display: flex; flex-direction: column;
}}

.slide-num {{
  position: absolute; top: 56px; right: 64px;
  font-size: 14px; font-weight: 600;
  color: rgba(255,255,255,0.2);
  letter-spacing: 0.15em;
}}

.content {{ flex: 1; display: flex; flex-direction: column; justify-content: center; }}

.tag {{
  display: inline-flex; align-items: center; gap: 12px;
  background: rgba(249, 115, 22, 0.12);
  border: 1px solid rgba(249, 115, 22, 0.35);
  padding: 14px 24px; border-radius: 100px;
  font-size: 15px; font-weight: 700;
  color: #fb923c;
  margin-bottom: 40px; width: fit-content;
  text-transform: uppercase;
  letter-spacing: 0.1em;
}}

.headline {{
  font-size: 108px;
  font-weight: 800;
  line-height: 0.9;
  letter-spacing: -0.04em;
}}

.line-strike {{
  position: relative;
  display: inline-block;
  color: rgba(255,255,255,0.3);
}}
.line-strike::after {{
  content: '';
  position: absolute;
  left: -8px; right: -8px;
  top: 50%;
  height: 10px;
  background: linear-gradient(90deg, #ef4444, #f97316);
  transform: rotate(-2deg);
  border-radius: 5px;
}}

.line-accent {{
  background: linear-gradient(135deg, #818cf8, #c084fc, #f472b6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}

.subhead {{
  font-size: 30px;
  font-weight: 500;
  color: rgba(255,255,255,0.5);
  line-height: 1.4;
  margin-top: 36px;
  max-width: 600px;
}}

.swipe {{
  display: flex; align-items: center; gap: 20px;
  margin-top: 56px;
  padding: 20px 32px;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 20px;
  width: fit-content;
}}
.swipe-icon {{
  width: 56px; height: 56px;
  background: linear-gradient(135deg, #f97316, #ea580c);
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 8px 24px rgba(249, 115, 22, 0.4);
}}
.swipe-text {{
  font-size: 20px;
  font-weight: 600;
  color: rgba(255,255,255,0.7);
}}

.footer {{ display: flex; align-items: center; gap: 14px; }}
.brand {{ font-size: 18px; font-weight: 600; color: rgba(255,255,255,0.35); }}
</style></head><body>
<div class="blob blob-1"></div>
<div class="blob blob-2"></div>
<div class="noise"></div>
<div class="bg-char">?</div>
<div class="deco-circle deco-circle-1"></div>
<div class="deco-circle deco-circle-2"></div>
<div class="deco-line deco-line-1"></div>
<div class="deco-line deco-line-2"></div>

<div class="slide">
  <div class="slide-num">01 / 08</div>
  <div class="content">
    <div class="tag">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
      Open Source
    </div>
    <h1 class="headline">
      My designer<br>
      <span class="line-strike">quit</span><br>
      <span class="line-accent">so I built this</span>
    </h1>
    <p class="subhead">She got a full-time offer.<br>I needed a solution fast.</p>
    <div class="swipe">
      <div class="swipe-icon">
        <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
      </div>
      <span class="swipe-text">Swipe to see what I made</span>
    </div>
  </div>
  <div class="footer">{LOGO_SMALL}<span class="brand">openfigma</span></div>
</div>
</body></html>"""

# ============================================
# SLIDE 2: PROBLEM - Stacked cards with real rotation
# ============================================
SLIDE_2 = f"""<!DOCTYPE html><html><head><style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: #08080c;
  color: #fff;
  width: 1080px; height: 1350px;
  overflow: hidden; position: relative;
}}

/* Red glow blob */
.blob {{
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -40%);
  width: 700px; height: 700px;
  background: radial-gradient(circle, rgba(239, 68, 68, 0.35) 0%, transparent 60%);
  filter: blur(80px);
}}

/* Noise */
.noise {{
  position: absolute; inset: 0;
  background-image: url("{NOISE_PNG}");
  background-repeat: repeat;
  opacity: 0.07;
  pointer-events: none;
}}

/* BIG X - 8% opacity (visible) */
.bg-x {{
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  font-size: 850px;
  font-weight: 900;
  color: rgba(239, 68, 68, 0.08);
  line-height: 0.7;
}}

/* Diagonal accent stripe */
.stripe {{
  position: absolute;
  top: -200px; left: 0;
  width: 300px; height: 2000px;
  background: linear-gradient(180deg, transparent, rgba(239, 68, 68, 0.06), transparent);
  transform: rotate(30deg);
  transform-origin: top left;
}}

.slide {{ position: relative; z-index: 1; width: 100%; height: 100%; padding: 64px; display: flex; flex-direction: column; }}
.slide-num {{ position: absolute; top: 56px; right: 64px; font-size: 14px; font-weight: 600; color: rgba(255,255,255,0.2); letter-spacing: 0.15em; }}

.header {{ margin-bottom: 20px; }}
.label {{
  font-size: 14px; font-weight: 800;
  color: #ef4444;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  margin-bottom: 16px;
}}
.headline {{ font-size: 76px; font-weight: 800; line-height: 0.95; letter-spacing: -0.04em; }}
.headline span {{ color: #ef4444; }}

/* Card stack with proper rotation */
.cards {{ flex: 1; position: relative; }}

.card {{
  position: absolute;
  left: 0; right: 0;
  background: rgba(15, 10, 12, 0.95);
  border: 2px solid rgba(239, 68, 68, 0.2);
  border-radius: 24px;
  padding: 28px 32px;
  display: flex; align-items: center; gap: 24px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.2), 0 12px 40px rgba(0,0,0,0.3);
}}

/* Rotation: 4-5 degrees (noticeable) */
.card-1 {{ top: 20px; transform: rotate(-4deg); z-index: 4; background: rgba(239, 68, 68, 0.1); border-color: rgba(239, 68, 68, 0.4); }}
.card-2 {{ top: 190px; transform: rotate(2.5deg); z-index: 3; }}
.card-3 {{ top: 360px; transform: rotate(-2deg); z-index: 2; }}
.card-4 {{ top: 530px; transform: rotate(3.5deg); z-index: 1; opacity: 0.9; }}

.card-icon {{
  width: 60px; height: 60px;
  background: rgba(239, 68, 68, 0.15);
  border: 1px solid rgba(239, 68, 68, 0.25);
  border-radius: 14px;
  display: flex; align-items: center; justify-content: center;
  color: #f87171;
  flex-shrink: 0;
}}
.card h3 {{ font-size: 24px; font-weight: 700; margin-bottom: 4px; }}
.card p {{ font-size: 17px; color: rgba(255,255,255,0.5); }}

.footer {{ display: flex; align-items: center; gap: 14px; margin-top: auto; padding-top: 20px; }}
.brand {{ font-size: 18px; font-weight: 600; color: rgba(255,255,255,0.35); }}
</style></head><body>
<div class="blob"></div>
<div class="noise"></div>
<div class="bg-x">×</div>
<div class="stripe"></div>

<div class="slide">
  <div class="slide-num">02 / 08</div>
  <div class="header">
    <div class="label">The Problem</div>
    <h1 class="headline">Design tools<br>are <span>broken</span></h1>
  </div>
  <div class="cards">
    <div class="card card-1">
      <div class="card-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg></div>
      <div><h3>Steep learning curve</h3><p>Weeks to learn Figma or Canva properly</p></div>
    </div>
    <div class="card card-2">
      <div class="card-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div>
      <div><h3>Expensive templates</h3><p>$20-50 per pack, subscriptions add up</p></div>
    </div>
    <div class="card card-3">
      <div class="card-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg></div>
      <div><h3>Manual repetition</h3><p>Copy, paste, tweak, export... every time</p></div>
    </div>
    <div class="card card-4">
      <div class="card-icon"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg></div>
      <div><h3>Designer dependency</h3><p>Need someone for every visual asset</p></div>
    </div>
  </div>
  <div class="footer">{LOGO_SMALL}<span class="brand">openfigma</span></div>
</div>
</body></html>"""

# ============================================
# SLIDE 3: SOLUTION
# ============================================
SLIDE_3 = f"""<!DOCTYPE html><html><head><style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: #08080c;
  color: #fff;
  width: 1080px; height: 1350px;
  overflow: hidden; position: relative;
}}

/* Purple/green blobs */
.blob {{
  position: absolute;
  border-radius: 50%;
  filter: blur(100px);
}}
.blob-1 {{
  width: 600px; height: 500px;
  top: -100px; left: 50%;
  transform: translateX(-50%);
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  opacity: 0.35;
}}
.blob-2 {{
  width: 400px; height: 400px;
  bottom: 150px; right: -50px;
  background: linear-gradient(135deg, #22c55e, #10b981);
  opacity: 0.2;
}}

/* Noise */
.noise {{
  position: absolute; inset: 0;
  background-image: url("{NOISE_PNG}");
  background-repeat: repeat;
  opacity: 0.07;
  pointer-events: none;
}}

/* Concentric circles - visible */
.circle {{
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -45%);
  border-radius: 50%;
  border: 2px solid;
}}
.circle-1 {{ width: 650px; height: 650px; border-color: rgba(99, 102, 241, 0.15); }}
.circle-2 {{ width: 450px; height: 450px; border-color: rgba(168, 85, 247, 0.12); }}
.circle-3 {{ width: 250px; height: 250px; border-color: rgba(34, 197, 94, 0.1); }}

/* Corner accents */
.corner {{
  position: absolute;
  width: 60px; height: 60px;
}}
.corner-tl {{ top: 80px; left: 80px; border-left: 3px solid rgba(99, 102, 241, 0.4); border-top: 3px solid rgba(99, 102, 241, 0.4); }}
.corner-br {{ bottom: 80px; right: 80px; border-right: 3px solid rgba(34, 197, 94, 0.4); border-bottom: 3px solid rgba(34, 197, 94, 0.4); }}

/* Floating dots */
.dot {{ position: absolute; border-radius: 50%; background: linear-gradient(135deg, #6366f1, #a855f7); }}
.dot-1 {{ width: 12px; height: 12px; top: 200px; left: 180px; opacity: 0.6; }}
.dot-2 {{ width: 8px; height: 8px; top: 350px; right: 160px; opacity: 0.5; }}
.dot-3 {{ width: 10px; height: 10px; bottom: 300px; left: 150px; opacity: 0.4; }}

.slide {{ position: relative; z-index: 1; width: 100%; height: 100%; padding: 64px; display: flex; flex-direction: column; }}
.slide-num {{ position: absolute; top: 56px; right: 64px; font-size: 14px; font-weight: 600; color: rgba(255,255,255,0.2); letter-spacing: 0.15em; }}

.content {{ flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }}

.logo-wrap {{
  margin-bottom: 36px;
  padding: 24px;
  background: radial-gradient(circle, rgba(99, 102, 241, 0.2) 0%, transparent 70%);
  border-radius: 50%;
}}
.logo-wrap svg {{ filter: drop-shadow(0 0 40px rgba(99, 102, 241, 0.6)); }}

.headline {{ font-size: 96px; font-weight: 800; line-height: 0.95; letter-spacing: -0.04em; margin-bottom: 20px; }}
.headline span {{
  background: linear-gradient(135deg, #818cf8, #a855f7, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}

.subhead {{ font-size: 28px; font-weight: 500; color: rgba(255,255,255,0.55); line-height: 1.5; margin-bottom: 44px; }}

.features {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 14px; margin-bottom: 40px; }}
.feat {{
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.1);
  padding: 14px 24px; border-radius: 100px;
  font-size: 16px; font-weight: 600;
  color: rgba(255,255,255,0.7);
}}
.feat.green {{
  background: rgba(34, 197, 94, 0.12);
  border-color: rgba(34, 197, 94, 0.35);
  color: #4ade80;
}}

.terminal {{
  background: rgba(0,0,0,0.5);
  border: 2px solid rgba(34, 197, 94, 0.3);
  border-radius: 20px;
  padding: 24px 40px;
  display: inline-flex; align-items: center; gap: 16px;
  box-shadow: 0 8px 32px rgba(34, 197, 94, 0.15);
}}
.terminal .dollar {{ color: #4ade80; font-family: 'SF Mono', Monaco, monospace; font-size: 22px; }}
.terminal code {{ font-family: 'SF Mono', Monaco, monospace; font-size: 24px; font-weight: 500; }}

.footer {{ display: flex; align-items: center; justify-content: center; gap: 14px; }}
.brand {{ font-size: 18px; font-weight: 600; color: rgba(255,255,255,0.35); }}
</style></head><body>
<div class="blob blob-1"></div>
<div class="blob blob-2"></div>
<div class="noise"></div>
<div class="circle circle-1"></div>
<div class="circle circle-2"></div>
<div class="circle circle-3"></div>
<div class="corner corner-tl"></div>
<div class="corner corner-br"></div>
<div class="dot dot-1"></div>
<div class="dot dot-2"></div>
<div class="dot dot-3"></div>

<div class="slide">
  <div class="slide-num">03 / 08</div>
  <div class="content">
    <div class="logo-wrap">
      <svg width="140" height="140" viewBox="0 0 120 120" fill="none"><defs><linearGradient id="logoGradB" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#6366f1"/><stop offset="100%" style="stop-color:#a855f7"/></linearGradient></defs><rect x="4" y="4" width="112" height="112" rx="28" fill="url(#logoGradB)"/><path d="M52 40L32 60L52 80" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M68 40L88 60L68 80" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="60" cy="60" r="6" fill="white"/></svg>
    </div>
    <h1 class="headline">Meet <span>openfigma</span></h1>
    <p class="subhead">Code-first design library.<br>Write Python → Get Figma-quality graphics.</p>
    <div class="features">
      <span class="feat green">100% Open Source</span>
      <span class="feat">No design skills needed</span>
      <span class="feat">Python + HTML/CSS</span>
      <span class="feat">Instant PNG export</span>
    </div>
    <div class="terminal">
      <span class="dollar">$</span>
      <code>pip install openfigma</code>
    </div>
  </div>
  <div class="footer">{LOGO_SMALL}<span class="brand">openfigma</span></div>
</div>
</body></html>"""

# ============================================
# SLIDE 7: CODE
# ============================================
SLIDE_7 = f"""<!DOCTYPE html><html><head><style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: #08080c;
  color: #fff;
  width: 1080px; height: 1350px;
  overflow: hidden; position: relative;
}}

/* Blobs */
.blob {{
  position: absolute;
  border-radius: 50%;
  filter: blur(100px);
}}
.blob-1 {{
  width: 500px; height: 400px;
  top: -50px; right: -100px;
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  opacity: 0.25;
}}
.blob-2 {{
  width: 350px; height: 350px;
  bottom: 100px; left: -80px;
  background: linear-gradient(135deg, #22c55e, #10b981);
  opacity: 0.2;
}}

/* Noise */
.noise {{
  position: absolute; inset: 0;
  background-image: url("{NOISE_PNG}");
  background-repeat: repeat;
  opacity: 0.07;
  pointer-events: none;
}}

/* Giant "4" - visible at 7% */
.bg-num {{
  position: absolute;
  top: -80px; left: -60px;
  font-size: 750px;
  font-weight: 900;
  color: rgba(99, 102, 241, 0.07);
  line-height: 0.75;
}}

/* Code brackets */
.bracket {{
  position: absolute;
  font-family: 'SF Mono', Monaco, monospace;
  font-size: 180px;
  font-weight: 300;
  color: rgba(99, 102, 241, 0.12);
}}
.bracket-l {{ top: 140px; left: 50px; }}
.bracket-r {{ bottom: 140px; right: 50px; }}

.slide {{ position: relative; z-index: 1; width: 100%; height: 100%; padding: 64px; display: flex; flex-direction: column; }}
.slide-num {{ position: absolute; top: 56px; right: 64px; font-size: 14px; font-weight: 600; color: rgba(255,255,255,0.2); letter-spacing: 0.15em; }}

.header {{ margin-bottom: 32px; }}
.label {{ font-size: 14px; font-weight: 700; color: rgba(255,255,255,0.3); letter-spacing: 0.2em; text-transform: uppercase; margin-bottom: 12px; }}
.headline {{ font-size: 84px; font-weight: 800; line-height: 0.95; letter-spacing: -0.04em; }}
.headline span {{
  background: linear-gradient(135deg, #818cf8, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}

.code-window {{
  flex: 1;
  background: rgba(8, 8, 14, 0.95);
  border: 2px solid rgba(99, 102, 241, 0.2);
  border-radius: 24px;
  overflow: hidden;
  display: flex; flex-direction: column;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15), 0 16px 48px rgba(0,0,0,0.25);
}}

.window-bar {{
  background: rgba(255,255,255,0.03);
  padding: 18px 24px;
  display: flex; align-items: center; gap: 10px;
  border-bottom: 1px solid rgba(255,255,255,0.06);
}}
.dot {{ width: 14px; height: 14px; border-radius: 50%; }}
.dot-r {{ background: #ef4444; }}
.dot-y {{ background: #eab308; }}
.dot-g {{ background: #22c55e; }}
.filename {{ font-size: 14px; color: rgba(255,255,255,0.3); margin-left: 12px; font-family: 'SF Mono', Monaco, monospace; }}

.code-body {{
  flex: 1; padding: 48px;
  font-family: 'SF Mono', Monaco, monospace;
  font-size: 28px; line-height: 2.2;
  display: flex; flex-direction: column; justify-content: center;
}}
.line {{ display: flex; }}
.ln {{ color: rgba(255,255,255,0.15); width: 60px; flex-shrink: 0; }}
.kw {{ color: #c084fc; }}
.str {{ color: #4ade80; }}
.fn {{ color: #60a5fa; }}

/* Output badge */
.output {{
  position: absolute;
  bottom: 170px; right: 80px;
  background: rgba(34, 197, 94, 0.12);
  border: 2px solid rgba(34, 197, 94, 0.35);
  padding: 20px 28px;
  border-radius: 16px;
  display: flex; align-items: center; gap: 14px;
  transform: rotate(3deg);
  box-shadow: 0 8px 24px rgba(34, 197, 94, 0.2);
}}
.output-icon {{
  width: 44px; height: 44px;
  background: rgba(34, 197, 94, 0.2);
  border-radius: 10px;
  display: flex; align-items: center; justify-content: center;
  color: #4ade80;
}}
.output h4 {{ font-size: 18px; font-weight: 700; color: #4ade80; }}
.output p {{ font-size: 14px; color: rgba(255,255,255,0.5); font-family: 'SF Mono', Monaco, monospace; }}

.footer {{ display: flex; align-items: center; gap: 14px; }}
.brand {{ font-size: 18px; font-weight: 600; color: rgba(255,255,255,0.35); }}
</style></head><body>
<div class="blob blob-1"></div>
<div class="blob blob-2"></div>
<div class="noise"></div>
<div class="bg-num">4</div>
<div class="bracket bracket-l">{{</div>
<div class="bracket bracket-r">}}</div>

<div class="slide">
  <div class="slide-num">07 / 08</div>
  <div class="header">
    <div class="label">How It Works</div>
    <h1 class="headline"><span>4 lines</span> of Python</h1>
  </div>
  <div class="code-window">
    <div class="window-bar">
      <div class="dot dot-r"></div>
      <div class="dot dot-y"></div>
      <div class="dot dot-g"></div>
      <span class="filename">create_post.py</span>
    </div>
    <div class="code-body">
      <div class="line"><span class="ln">1</span><span class="kw">from</span> openfigma <span class="kw">import</span> html_to_png</div>
      <div class="line"><span class="ln">2</span></div>
      <div class="line"><span class="ln">3</span>html = <span class="str">"&lt;your template&gt;"</span></div>
      <div class="line"><span class="ln">4</span><span class="fn">html_to_png</span>(html, <span class="str">"post.png"</span>)</div>
    </div>
  </div>
  <div class="output">
    <div class="output-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12l5 5L20 7"/></svg></div>
    <div><h4>Ready to post</h4><p>→ post.png</p></div>
  </div>
  <div class="footer">{LOGO_SMALL}<span class="brand">openfigma</span></div>
</div>
</body></html>"""

# ============================================
# SLIDE 8: CTA
# ============================================
SLIDE_8 = f"""<!DOCTYPE html><html><head><style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: #08080c;
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
  width: 700px; height: 500px;
  top: -150px; left: 50%;
  transform: translateX(-50%);
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  opacity: 0.35;
}}
.blob-2 {{
  width: 500px; height: 400px;
  bottom: -100px; left: 50%;
  transform: translateX(-50%);
  background: linear-gradient(135deg, #a855f7, #ec4899);
  opacity: 0.25;
}}

/* Noise */
.noise {{
  position: absolute; inset: 0;
  background-image: url("{NOISE_PNG}");
  background-repeat: repeat;
  opacity: 0.07;
  pointer-events: none;
}}

/* Rings */
.ring {{
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -45%);
  border-radius: 50%;
  border: 2px solid;
}}
.ring-1 {{ width: 900px; height: 900px; border-color: rgba(99, 102, 241, 0.1); }}
.ring-2 {{ width: 650px; height: 650px; border-color: rgba(168, 85, 247, 0.12); }}
.ring-3 {{ width: 400px; height: 400px; border-color: rgba(99, 102, 241, 0.15); }}

/* Sparkles */
.sparkle {{ position: absolute; width: 6px; height: 6px; background: #fff; border-radius: 50%; }}
.sparkle-1 {{ top: 180px; left: 180px; opacity: 0.7; box-shadow: 0 0 15px 4px rgba(99, 102, 241, 0.6); }}
.sparkle-2 {{ top: 280px; right: 200px; opacity: 0.5; box-shadow: 0 0 15px 4px rgba(168, 85, 247, 0.6); }}
.sparkle-3 {{ bottom: 320px; left: 200px; opacity: 0.5; box-shadow: 0 0 15px 4px rgba(99, 102, 241, 0.6); }}
.sparkle-4 {{ bottom: 250px; right: 180px; opacity: 0.6; box-shadow: 0 0 15px 4px rgba(168, 85, 247, 0.6); }}

.slide {{ position: relative; z-index: 1; width: 100%; height: 100%; padding: 64px; display: flex; flex-direction: column; }}
.slide-num {{ position: absolute; top: 56px; right: 64px; font-size: 14px; font-weight: 600; color: rgba(255,255,255,0.2); letter-spacing: 0.15em; }}

.content {{ flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }}

.logo-glow {{
  margin-bottom: 32px;
  padding: 20px;
  background: radial-gradient(circle, rgba(99, 102, 241, 0.25) 0%, transparent 70%);
  border-radius: 50%;
}}
.logo-glow svg {{ filter: drop-shadow(0 0 35px rgba(99, 102, 241, 0.6)); }}

.headline {{ font-size: 88px; font-weight: 800; line-height: 1.0; letter-spacing: -0.04em; margin-bottom: 12px; }}
.headline span {{
  background: linear-gradient(135deg, #818cf8, #c084fc, #f472b6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}

.tagline {{ font-size: 26px; color: rgba(255,255,255,0.5); margin-bottom: 36px; }}

.github-btn {{
  display: inline-flex; align-items: center; gap: 14px;
  background: #fff; color: #0a0a0f;
  padding: 22px 44px; border-radius: 18px;
  font-size: 19px; font-weight: 700;
  box-shadow: 0 4px 20px rgba(255,255,255,0.15);
}}

.engage {{
  margin-top: 44px;
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(168, 85, 247, 0.1));
  border: 2px solid rgba(139, 92, 246, 0.3);
  border-radius: 28px;
  padding: 36px 44px;
  max-width: 720px;
}}
.engage-head {{
  display: flex; align-items: center; justify-content: center; gap: 10px;
  font-size: 17px; font-weight: 700; color: #c4b5fd;
  margin-bottom: 14px;
}}
.engage-text {{ font-size: 28px; font-weight: 700; line-height: 1.4; }}
.engage-example {{ font-size: 17px; color: rgba(255,255,255,0.4); margin-top: 14px; font-style: italic; }}

.trust {{ display: flex; justify-content: center; gap: 28px; margin-top: 36px; }}
.trust-item {{ display: flex; align-items: center; gap: 8px; font-size: 15px; color: rgba(255,255,255,0.5); }}
.trust-item svg {{ color: #4ade80; }}

.footer {{ display: flex; align-items: center; justify-content: center; gap: 14px; }}
.brand {{ font-size: 18px; font-weight: 600; color: rgba(255,255,255,0.35); }}
</style></head><body>
<div class="blob blob-1"></div>
<div class="blob blob-2"></div>
<div class="noise"></div>
<div class="ring ring-1"></div>
<div class="ring ring-2"></div>
<div class="ring ring-3"></div>
<div class="sparkle sparkle-1"></div>
<div class="sparkle sparkle-2"></div>
<div class="sparkle sparkle-3"></div>
<div class="sparkle sparkle-4"></div>

<div class="slide">
  <div class="slide-num">08 / 08</div>
  <div class="content">
    <div class="logo-glow">
      <svg width="110" height="110" viewBox="0 0 120 120" fill="none"><defs><linearGradient id="logoGradH" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#6366f1"/><stop offset="100%" style="stop-color:#a855f7"/></linearGradient></defs><rect x="4" y="4" width="112" height="112" rx="28" fill="url(#logoGradH)"/><path d="M52 40L32 60L52 80" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M68 40L88 60L68 80" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="60" cy="60" r="6" fill="white"/></svg>
    </div>
    <h1 class="headline">Try it.<br><span>It's free.</span></h1>
    <p class="tagline">No signup. No waitlist. No BS.</p>
    <div class="github-btn">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
      github.com/federicodeponte/openfigma
    </div>
    <div class="engage">
      <div class="engage-head">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
        Want a custom design?
      </div>
      <div class="engage-text">Comment your prompt below.<br>I'll generate it within 24h.</div>
      <div class="engage-example">"A metric card showing 500% growth"</div>
    </div>
    <div class="trust">
      <div class="trust-item"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12l5 5L20 7"/></svg>MIT License</div>
      <div class="trust-item"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12l5 5L20 7"/></svg>Free forever</div>
      <div class="trust-item"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12l5 5L20 7"/></svg>pip install</div>
    </div>
  </div>
  <div class="footer">{LOGO_SMALL}<span class="brand">openfigma</span></div>
</div>
</body></html>"""

# ============================================
# Template slide generator
# ============================================
BASE_CSS = """
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: #08080c;
  color: #fff;
  width: 1080px; height: 1350px;
  overflow: hidden; position: relative;
}
"""

def make_template_slide(num, total, img_b64, template_name, description):
    return f"""<!DOCTYPE html><html><head><style>
{BASE_CSS}
.blob {{
  position: absolute;
  border-radius: 50%;
  filter: blur(100px);
}}
.blob-1 {{
  width: 500px; height: 400px;
  top: -100px; left: 50%;
  transform: translateX(-50%);
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  opacity: 0.25;
}}
.noise {{
  position: absolute; inset: 0;
  background-image: url("{NOISE_PNG}");
  background-repeat: repeat;
  opacity: 0.06;
  pointer-events: none;
}}
.slide {{ position: relative; z-index: 1; width: 100%; height: 100%; padding: 64px; display: flex; flex-direction: column; }}
.slide-num {{ position: absolute; top: 56px; right: 64px; font-size: 14px; font-weight: 600; color: rgba(255,255,255,0.2); letter-spacing: 0.15em; }}
.showcase {{ flex: 1; display: flex; flex-direction: column; }}
.label {{ font-size: 14px; font-weight: 700; color: #818cf8; letter-spacing: 0.2em; text-transform: uppercase; margin-bottom: 12px; }}
.headline {{ font-size: 52px; font-weight: 800; line-height: 0.95; letter-spacing: -0.03em; margin-bottom: 20px; }}
.accent {{ background: linear-gradient(135deg, #818cf8, #c084fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
.template-wrap {{ flex: 1; display: flex; flex-direction: column; }}
.template-img {{
  flex: 1;
  border-radius: 20px;
  overflow: hidden;
  border: 2px solid rgba(99, 102, 241, 0.2);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15), 0 16px 48px rgba(0,0,0,0.25);
  display: flex; align-items: center; justify-content: center;
  background: #0a0a10;
}}
.template-img img {{ max-width: 100%; max-height: 100%; object-fit: contain; }}
.template-info {{ margin-top: 16px; font-size: 17px; color: rgba(255,255,255,0.4); }}
.footer {{ display: flex; align-items: center; gap: 14px; }}
.brand {{ font-size: 18px; font-weight: 600; color: rgba(255,255,255,0.35); }}
</style></head><body>
<div class="blob blob-1"></div>
<div class="noise"></div>
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

    output_dir = "/home/tech_scaile_it/openfigma/exports/linkedin_v8"
    os.makedirs(output_dir, exist_ok=True)

    print("Loading premium templates...")
    metric_b64 = load_template_b64('metric')
    testimonial_b64 = load_template_b64('testimonial')
    announcement_b64 = load_template_b64('announcement')

    print("Building slides...")

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
