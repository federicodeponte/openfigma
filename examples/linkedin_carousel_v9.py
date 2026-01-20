#!/usr/bin/env python3
"""
LinkedIn Carousel V9 - V6 with minimal fixes
- Keep SVG feTurbulence noise (it works, creates texture)
- Keep filter: blur() blobs
- System fonts only (the only real fix needed)
- Bump noise opacity to 0.08 (more visible)
- Bump background elements to 6-8%
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

# SVG noise that actually creates texture
NOISE_SVG = "data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E"

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

/* Gradient blobs with blur */
.blob {{
  position: absolute;
  border-radius: 50%;
  filter: blur(120px);
}}
.blob-1 {{
  width: 700px; height: 700px;
  top: -200px; right: -150px;
  background: linear-gradient(135deg, #6366f1, #a855f7);
  opacity: 0.4;
}}
.blob-2 {{
  width: 500px; height: 500px;
  bottom: -100px; left: -200px;
  background: linear-gradient(135deg, #ec4899, #8b5cf6);
  opacity: 0.2;
}}

/* SVG noise - 8% opacity */
.grain {{
  position: absolute;
  inset: 0;
  opacity: 0.08;
  background-image: url("{NOISE_SVG}");
  pointer-events: none;
}}

/* Background question mark - 6% */
.bg-text {{
  position: absolute;
  top: -80px; right: -60px;
  font-size: 600px;
  font-weight: 900;
  color: rgba(255,255,255,0.06);
  line-height: 0.8;
  pointer-events: none;
}}

/* Decorative elements */
.float-shape {{
  position: absolute;
  border-radius: 50%;
  border: 2px solid rgba(255,255,255,0.1);
}}
.float-1 {{ width: 300px; height: 300px; top: 60px; right: 80px; }}
.float-2 {{ width: 180px; height: 180px; bottom: 200px; right: 180px; border-color: rgba(249, 115, 22, 0.25); }}
.float-3 {{ width: 80px; height: 80px; top: 300px; right: 400px; background: rgba(249, 115, 22, 0.15); border: none; }}

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

.content {{ flex: 1; display: flex; flex-direction: column; justify-content: center; padding-right: 100px; }}

.tag {{
  display: inline-flex; align-items: center; gap: 12px;
  background: rgba(249, 115, 22, 0.12);
  border: 1px solid rgba(249, 115, 22, 0.3);
  padding: 14px 24px; border-radius: 100px;
  font-size: 16px; font-weight: 600;
  color: #fb923c;
  margin-bottom: 40px; width: fit-content;
}}

.headline {{
  font-size: 100px;
  font-weight: 900;
  line-height: 0.92;
  letter-spacing: -0.045em;
}}
.line-strike {{
  position: relative;
  display: inline-block;
  color: rgba(255,255,255,0.25);
}}
.line-strike::after {{
  content: '';
  position: absolute;
  left: -5px; right: -5px;
  top: 50%;
  height: 8px;
  background: linear-gradient(90deg, #ef4444, #f97316);
  transform: rotate(-2deg);
  border-radius: 4px;
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
  max-width: 550px;
}}

.swipe {{
  display: flex; align-items: center; gap: 20px;
  margin-top: 56px;
  padding: 24px 36px;
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 20px;
  width: fit-content;
}}
.swipe-icon {{
  width: 56px; height: 56px;
  background: linear-gradient(135deg, #f97316, #ea580c);
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 8px 32px rgba(249, 115, 22, 0.4);
}}
.swipe-text {{ font-size: 20px; font-weight: 600; color: rgba(255,255,255,0.6); }}

.footer {{ display: flex; align-items: center; gap: 14px; }}
.brand {{ font-size: 18px; font-weight: 600; color: rgba(255,255,255,0.35); }}
</style></head><body>
<div class="blob blob-1"></div>
<div class="blob blob-2"></div>
<div class="grain"></div>
<div class="bg-text">?</div>
<div class="float-shape float-1"></div>
<div class="float-shape float-2"></div>
<div class="float-shape float-3"></div>

<div class="slide">
  <div class="slide-num">01 / 08</div>
  <div class="content">
    <div class="tag">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
      Open Source
    </div>
    <h1 class="headline">
      <span>My designer</span><br>
      <span class="line-strike">quit</span><br>
      <span class="line-accent">so I built this</span>
    </h1>
    <p class="subhead">She got a full-time offer.<br>I needed a solution fast.</p>
    <div class="swipe">
      <div class="swipe-icon">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
      </div>
      <span class="swipe-text">Swipe to see what I made</span>
    </div>
  </div>
  <div class="footer">{LOGO_SMALL}<span class="brand">openfigma</span></div>
</div>
</body></html>"""

# ============================================
# SLIDE 2: PROBLEM
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

/* Red glow */
.blob {{
  position: absolute;
  width: 600px; height: 600px;
  top: 50%; left: 50%;
  transform: translate(-50%, -40%);
  background: radial-gradient(circle, rgba(239, 68, 68, 0.35) 0%, transparent 60%);
  filter: blur(60px);
}}

/* Noise */
.grain {{
  position: absolute; inset: 0;
  opacity: 0.08;
  background-image: url("{NOISE_SVG}");
  pointer-events: none;
}}

/* Big X - 8% */
.bg-x {{
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  font-size: 900px;
  font-weight: 900;
  color: rgba(239, 68, 68, 0.08);
  line-height: 0.7;
}}

/* Red stripe */
.stripe {{
  position: absolute;
  top: 0; left: -200px;
  width: 400px; height: 2000px;
  background: linear-gradient(180deg, transparent, rgba(239, 68, 68, 0.06), transparent);
  transform: rotate(25deg);
}}

.slide {{ position: relative; z-index: 1; width: 100%; height: 100%; padding: 64px; display: flex; flex-direction: column; }}
.slide-num {{ position: absolute; top: 56px; right: 64px; font-size: 14px; font-weight: 600; color: rgba(255,255,255,0.2); letter-spacing: 0.15em; }}

.header {{ margin-bottom: 24px; }}
.label {{ font-size: 14px; font-weight: 700; color: #f87171; letter-spacing: 0.2em; text-transform: uppercase; margin-bottom: 16px; }}
.headline {{ font-size: 72px; font-weight: 900; line-height: 0.95; letter-spacing: -0.04em; }}
.headline span {{ color: #ef4444; }}

.cards {{ flex: 1; position: relative; }}

.card {{
  position: absolute;
  left: 0; right: 0;
  background: rgba(15, 8, 10, 0.9);
  border: 2px solid rgba(239, 68, 68, 0.2);
  border-radius: 24px;
  padding: 32px 36px;
  display: flex; align-items: center; gap: 24px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.2), 0 16px 48px rgba(0,0,0,0.3);
}}

.card-1 {{ top: 10px; transform: rotate(-4deg); z-index: 4; background: rgba(239, 68, 68, 0.1); border-color: rgba(239, 68, 68, 0.4); }}
.card-2 {{ top: 180px; transform: rotate(2deg); z-index: 3; }}
.card-3 {{ top: 350px; transform: rotate(-1.5deg); z-index: 2; }}
.card-4 {{ top: 520px; transform: rotate(3deg); z-index: 1; opacity: 0.9; }}

.card-icon {{
  width: 64px; height: 64px;
  background: rgba(239, 68, 68, 0.15);
  border-radius: 16px;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
  color: #f87171;
}}
.card h3 {{ font-size: 24px; font-weight: 700; margin-bottom: 6px; }}
.card p {{ font-size: 17px; color: rgba(255,255,255,0.5); }}

.footer {{ display: flex; align-items: center; gap: 14px; margin-top: auto; }}
.brand {{ font-size: 18px; font-weight: 600; color: rgba(255,255,255,0.35); }}
</style></head><body>
<div class="blob"></div>
<div class="grain"></div>
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
      <div class="card-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg></div>
      <div><h3>Steep learning curve</h3><p>Weeks to learn Figma or Canva properly</p></div>
    </div>
    <div class="card card-2">
      <div class="card-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div>
      <div><h3>Expensive templates</h3><p>$20-50 per pack, subscriptions add up</p></div>
    </div>
    <div class="card card-3">
      <div class="card-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg></div>
      <div><h3>Manual repetition</h3><p>Copy, paste, tweak, export... every time</p></div>
    </div>
    <div class="card card-4">
      <div class="card-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg></div>
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
  width: 800px; height: 600px;
  top: -100px; left: 50%;
  transform: translateX(-50%);
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  opacity: 0.35;
}}
.blob-2 {{
  width: 400px; height: 400px;
  bottom: 100px; right: -50px;
  background: linear-gradient(135deg, #22c55e, #10b981);
  opacity: 0.2;
}}

/* Noise */
.grain {{
  position: absolute; inset: 0;
  opacity: 0.07;
  background-image: url("{NOISE_SVG}");
  pointer-events: none;
}}

/* Circles */
.circle {{
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -45%);
  border-radius: 50%;
  border: 2px solid;
}}
.circle-1 {{ width: 800px; height: 800px; border-color: rgba(99, 102, 241, 0.12); }}
.circle-2 {{ width: 600px; height: 600px; border-color: rgba(168, 85, 247, 0.1); }}
.circle-3 {{ width: 400px; height: 400px; border-color: rgba(34, 197, 94, 0.08); }}

/* Corner accents */
.corner {{
  position: absolute;
  width: 60px; height: 60px;
}}
.corner-tl {{ top: 80px; left: 80px; border-left: 3px solid rgba(99, 102, 241, 0.35); border-top: 3px solid rgba(99, 102, 241, 0.35); }}
.corner-br {{ bottom: 80px; right: 80px; border-right: 3px solid rgba(34, 197, 94, 0.35); border-bottom: 3px solid rgba(34, 197, 94, 0.35); }}

/* Dots */
.dot {{ position: absolute; border-radius: 50%; background: linear-gradient(135deg, #6366f1, #a855f7); }}
.dot-1 {{ width: 12px; height: 12px; top: 180px; left: 200px; opacity: 0.6; }}
.dot-2 {{ width: 8px; height: 8px; top: 400px; right: 150px; opacity: 0.4; }}
.dot-3 {{ width: 16px; height: 16px; bottom: 300px; left: 120px; opacity: 0.3; }}

.slide {{ position: relative; z-index: 1; width: 100%; height: 100%; padding: 64px; display: flex; flex-direction: column; }}
.slide-num {{ position: absolute; top: 56px; right: 64px; font-size: 14px; font-weight: 600; color: rgba(255,255,255,0.2); letter-spacing: 0.15em; }}

.content {{ flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }}

.logo-container {{
  margin-bottom: 40px;
  padding: 20px;
  background: radial-gradient(circle, rgba(99, 102, 241, 0.15) 0%, transparent 70%);
  border-radius: 50%;
}}
.logo-container svg {{ filter: drop-shadow(0 0 60px rgba(99, 102, 241, 0.6)) drop-shadow(0 0 120px rgba(168, 85, 247, 0.4)); }}

.headline {{ font-size: 96px; font-weight: 900; line-height: 0.95; letter-spacing: -0.045em; margin-bottom: 24px; }}
.headline span {{
  background: linear-gradient(135deg, #818cf8, #c084fc, #f472b6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}

.subhead {{ font-size: 28px; font-weight: 500; color: rgba(255,255,255,0.55); line-height: 1.5; margin-bottom: 48px; }}

.features {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 16px; margin-bottom: 48px; }}
.feat {{
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.1);
  padding: 16px 28px; border-radius: 100px;
  font-size: 17px; font-weight: 600;
  color: rgba(255,255,255,0.7);
}}
.feat.primary {{
  background: linear-gradient(135deg, rgba(34, 197, 94, 0.15), rgba(34, 197, 94, 0.08));
  border-color: rgba(34, 197, 94, 0.3);
  color: #4ade80;
}}

.pip-box {{
  background: rgba(0,0,0,0.4);
  border: 2px solid rgba(34, 197, 94, 0.3);
  border-radius: 20px;
  padding: 24px 40px;
  display: inline-flex; align-items: center; gap: 16px;
  box-shadow: 0 8px 32px rgba(34, 197, 94, 0.15);
}}
.pip-box .dollar {{ color: #4ade80; font-family: 'SF Mono', Monaco, monospace; font-size: 22px; }}
.pip-box code {{ font-family: 'SF Mono', Monaco, monospace; font-size: 24px; font-weight: 500; }}

.footer {{ display: flex; align-items: center; justify-content: center; gap: 14px; }}
.brand {{ font-size: 18px; font-weight: 600; color: rgba(255,255,255,0.35); }}
</style></head><body>
<div class="blob blob-1"></div>
<div class="blob blob-2"></div>
<div class="grain"></div>
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
    <div class="logo-container">
      <svg width="160" height="160" viewBox="0 0 120 120" fill="none"><defs><linearGradient id="logoGradB" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#6366f1"/><stop offset="100%" style="stop-color:#a855f7"/></linearGradient></defs><rect x="4" y="4" width="112" height="112" rx="28" fill="url(#logoGradB)"/><path d="M52 40L32 60L52 80" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M68 40L88 60L68 80" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="60" cy="60" r="6" fill="white"/></svg>
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
  width: 400px; height: 400px;
  bottom: 50px; left: -100px;
  background: linear-gradient(135deg, #22c55e, #10b981);
  opacity: 0.2;
}}

/* Noise */
.grain {{
  position: absolute; inset: 0;
  opacity: 0.07;
  background-image: url("{NOISE_SVG}");
  pointer-events: none;
}}

/* Big 4 - 8% */
.bg-num {{
  position: absolute;
  top: -100px; left: -80px;
  font-size: 800px;
  font-weight: 900;
  color: rgba(99, 102, 241, 0.08);
  line-height: 0.75;
}}

/* Brackets - 12% */
.bracket {{
  position: absolute;
  font-family: 'SF Mono', Monaco, monospace;
  font-size: 250px;
  font-weight: 300;
  color: rgba(99, 102, 241, 0.12);
}}
.bracket-open {{ top: 120px; left: 40px; }}
.bracket-close {{ bottom: 120px; right: 40px; }}

.slide {{ position: relative; z-index: 1; width: 100%; height: 100%; padding: 64px; display: flex; flex-direction: column; }}
.slide-num {{ position: absolute; top: 56px; right: 64px; font-size: 14px; font-weight: 600; color: rgba(255,255,255,0.2); letter-spacing: 0.15em; }}

.header {{ margin-bottom: 40px; }}
.label {{ font-size: 14px; font-weight: 700; color: rgba(255,255,255,0.3); letter-spacing: 0.2em; text-transform: uppercase; margin-bottom: 16px; }}
.headline {{ font-size: 88px; font-weight: 900; line-height: 0.95; letter-spacing: -0.04em; }}
.headline span {{
  background: linear-gradient(135deg, #818cf8, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}

.code-window {{
  flex: 1;
  background: rgba(8, 8, 14, 0.95);
  border: 2px solid rgba(99, 102, 241, 0.15);
  border-radius: 28px;
  overflow: hidden;
  display: flex; flex-direction: column;
  box-shadow: 0 4px 16px rgba(0,0,0,0.2), 0 16px 48px rgba(0,0,0,0.3);
}}

.window-header {{
  background: rgba(255,255,255,0.03);
  padding: 20px 28px;
  display: flex; align-items: center; gap: 12px;
  border-bottom: 1px solid rgba(255,255,255,0.06);
}}
.dots {{ display: flex; gap: 8px; }}
.dot {{ width: 14px; height: 14px; border-radius: 50%; }}
.dot.r {{ background: #ef4444; }}
.dot.y {{ background: #eab308; }}
.dot.g {{ background: #22c55e; }}
.code-file {{ font-size: 15px; color: rgba(255,255,255,0.4); margin-left: 12px; font-family: 'SF Mono', Monaco, monospace; }}

.code-body {{
  flex: 1; padding: 48px;
  font-family: 'SF Mono', Monaco, monospace;
  font-size: 28px; line-height: 2.2;
  display: flex; flex-direction: column; justify-content: center;
}}
.line {{ display: flex; }}
.ln {{ color: rgba(255,255,255,0.2); width: 56px; flex-shrink: 0; }}
.kw {{ color: #c084fc; }}
.str {{ color: #4ade80; }}
.fn {{ color: #60a5fa; }}

/* Output badge */
.output-box {{
  position: absolute;
  bottom: 190px; right: 80px;
  display: flex; align-items: center; gap: 20px;
  background: rgba(34, 197, 94, 0.12);
  border: 2px solid rgba(34, 197, 94, 0.3);
  padding: 24px 32px;
  border-radius: 20px;
  transform: rotate(2deg);
  box-shadow: 0 8px 24px rgba(34, 197, 94, 0.2);
}}
.output-icon {{
  width: 56px; height: 56px;
  background: rgba(34, 197, 94, 0.2);
  border-radius: 14px;
  display: flex; align-items: center; justify-content: center;
  color: #4ade80;
}}
.output-text h4 {{ font-size: 20px; font-weight: 700; color: #4ade80; margin-bottom: 4px; }}
.output-text p {{ font-size: 16px; color: rgba(255,255,255,0.5); font-family: 'SF Mono', Monaco, monospace; }}

.footer {{ display: flex; align-items: center; gap: 14px; }}
.brand {{ font-size: 18px; font-weight: 600; color: rgba(255,255,255,0.35); }}
</style></head><body>
<div class="blob blob-1"></div>
<div class="blob blob-2"></div>
<div class="grain"></div>
<div class="bg-num">4</div>
<div class="bracket bracket-open">{{</div>
<div class="bracket bracket-close">}}</div>

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
    <div class="output-icon"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12l5 5L20 7"/></svg></div>
    <div class="output-text"><h4>Ready to post</h4><p>→ post.png (1080×1080)</p></div>
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
  width: 800px; height: 600px;
  top: -200px; left: 50%;
  transform: translateX(-50%);
  background: linear-gradient(135deg, #6366f1, #8b5cf6);
  opacity: 0.35;
}}
.blob-2 {{
  width: 600px; height: 500px;
  bottom: -150px; left: 50%;
  transform: translateX(-50%);
  background: linear-gradient(135deg, #a855f7, #ec4899);
  opacity: 0.25;
}}

/* Noise */
.grain {{
  position: absolute; inset: 0;
  opacity: 0.07;
  background-image: url("{NOISE_SVG}");
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
.ring-1 {{ width: 1200px; height: 1200px; border-color: rgba(99, 102, 241, 0.08); }}
.ring-2 {{ width: 900px; height: 900px; border-color: rgba(168, 85, 247, 0.1); }}
.ring-3 {{ width: 600px; height: 600px; border-color: rgba(99, 102, 241, 0.12); }}
.ring-4 {{ width: 300px; height: 300px; border-color: rgba(168, 85, 247, 0.08); }}

/* Sparkles */
.sparkle {{
  position: absolute;
  width: 6px; height: 6px;
  background: #fff;
  border-radius: 50%;
}}
.sparkle-1 {{ top: 200px; left: 180px; opacity: 0.7; box-shadow: 0 0 15px 4px rgba(99, 102, 241, 0.6); }}
.sparkle-2 {{ top: 350px; right: 200px; opacity: 0.5; box-shadow: 0 0 15px 4px rgba(168, 85, 247, 0.6); }}
.sparkle-3 {{ bottom: 400px; left: 250px; opacity: 0.5; box-shadow: 0 0 15px 4px rgba(99, 102, 241, 0.6); }}
.sparkle-4 {{ bottom: 300px; right: 180px; opacity: 0.4; box-shadow: 0 0 15px 4px rgba(168, 85, 247, 0.6); }}

.slide {{ position: relative; z-index: 1; width: 100%; height: 100%; padding: 64px; display: flex; flex-direction: column; }}
.slide-num {{ position: absolute; top: 56px; right: 64px; font-size: 14px; font-weight: 600; color: rgba(255,255,255,0.2); letter-spacing: 0.15em; }}

.content {{ flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }}

.logo-huge {{
  margin-bottom: 36px;
  padding: 16px;
  background: radial-gradient(circle, rgba(99, 102, 241, 0.2) 0%, transparent 70%);
  border-radius: 50%;
}}
.logo-huge svg {{ filter: drop-shadow(0 0 60px rgba(99, 102, 241, 0.5)) drop-shadow(0 0 120px rgba(168, 85, 247, 0.3)); }}

.headline {{ font-size: 88px; font-weight: 900; line-height: 1.0; letter-spacing: -0.04em; margin-bottom: 16px; }}
.headline span {{
  background: linear-gradient(135deg, #818cf8, #c084fc, #f472b6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}

.cta-sub {{ font-size: 26px; color: rgba(255,255,255,0.5); margin-bottom: 40px; }}

.github-btn {{
  display: inline-flex; align-items: center; gap: 16px;
  background: #fff;
  color: #0a0a0f;
  padding: 26px 52px;
  border-radius: 20px;
  font-size: 20px;
  font-weight: 700;
  box-shadow: 0 4px 20px rgba(255,255,255,0.15);
}}

.engagement {{
  margin-top: 48px;
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(168, 85, 247, 0.1));
  border: 2px solid rgba(139, 92, 246, 0.3);
  border-radius: 28px;
  padding: 40px 52px;
  max-width: 800px;
}}
.engagement-head {{
  display: flex; align-items: center; justify-content: center; gap: 12px;
  font-size: 20px; font-weight: 700; color: #c4b5fd;
  margin-bottom: 16px;
}}
.engagement-text {{ font-size: 30px; font-weight: 700; line-height: 1.35; }}
.engagement-sub {{ font-size: 18px; color: rgba(255,255,255,0.4); margin-top: 16px; font-style: italic; }}

.no-bs {{ display: flex; justify-content: center; gap: 36px; margin-top: 40px; }}
.no-bs-item {{ display: flex; align-items: center; gap: 10px; font-size: 16px; color: rgba(255,255,255,0.5); }}
.no-bs-item svg {{ color: #4ade80; }}

.footer {{ display: flex; align-items: center; justify-content: center; gap: 14px; }}
.brand {{ font-size: 18px; font-weight: 600; color: rgba(255,255,255,0.35); }}
</style></head><body>
<div class="blob blob-1"></div>
<div class="blob blob-2"></div>
<div class="grain"></div>
<div class="ring ring-1"></div>
<div class="ring ring-2"></div>
<div class="ring ring-3"></div>
<div class="ring ring-4"></div>
<div class="sparkle sparkle-1"></div>
<div class="sparkle sparkle-2"></div>
<div class="sparkle sparkle-3"></div>
<div class="sparkle sparkle-4"></div>

<div class="slide">
  <div class="slide-num">08 / 08</div>
  <div class="content">
    <div class="logo-huge">
      <svg width="120" height="120" viewBox="0 0 120 120" fill="none"><defs><linearGradient id="logoGradH" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#6366f1"/><stop offset="100%" style="stop-color:#a855f7"/></linearGradient></defs><rect x="4" y="4" width="112" height="112" rx="28" fill="url(#logoGradH)"/><path d="M52 40L32 60L52 80" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M68 40L88 60L68 80" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="60" cy="60" r="6" fill="white"/></svg>
    </div>
    <h1 class="headline">Try it.<br><span>It's free.</span></h1>
    <p class="cta-sub">No signup. No waitlist. No BS.</p>
    <div class="github-btn">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
      github.com/federicodeponte/openfigma
    </div>
    <div class="engagement">
      <div class="engagement-head">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
        Want a custom design?
      </div>
      <div class="engagement-text">Comment your prompt below.<br>I'll generate it within 24h.</div>
      <div class="engagement-sub">"A metric card showing 500% growth"</div>
    </div>
    <div class="no-bs">
      <div class="no-bs-item"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12l5 5L20 7"/></svg>MIT License</div>
      <div class="no-bs-item"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12l5 5L20 7"/></svg>Free forever</div>
      <div class="no-bs-item"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12l5 5L20 7"/></svg>pip install</div>
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
  top: -100px; left: 50%;
  transform: translateX(-50%);
  width: 800px; height: 500px;
  background: radial-gradient(ellipse, rgba(99, 102, 241, 0.2) 0%, transparent 60%);
  filter: blur(80px);
}}
.grain {{
  position: absolute; inset: 0;
  opacity: 0.06;
  background-image: url("{NOISE_SVG}");
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
  border: 2px solid rgba(99, 102, 241, 0.15);
  box-shadow: 0 4px 16px rgba(0,0,0,0.15), 0 16px 48px rgba(0,0,0,0.25);
  display: flex; align-items: center; justify-content: center;
  background: #0a0a10;
}}
.template-img img {{ max-width: 100%; max-height: 100%; object-fit: contain; }}
.template-info {{ margin-top: 16px; font-size: 17px; color: rgba(255,255,255,0.4); }}
.footer {{ display: flex; align-items: center; gap: 14px; }}
.brand {{ font-size: 18px; font-weight: 600; color: rgba(255,255,255,0.35); }}
</style></head><body>
<div class="blob"></div>
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

    output_dir = "/home/tech_scaile_it/openfigma/exports/linkedin_v9"
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
