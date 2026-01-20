#!/usr/bin/env python3
"""
LinkedIn Carousel V6 - PREMIUM QUALITY
Full Figma-level treatment: decorative shapes, depth, visual drama
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

# Slide 1: Hook - MASSIVE VISUAL DRAMA
SLIDE_1 = f"""<!DOCTYPE html><html><head><style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: 'Inter', sans-serif; background: #08080c; color: #fff; width: 1080px; height: 1350px; overflow: hidden; position: relative; }}

/* Background layers */
.bg-gradient {{ position: absolute; inset: 0; background: radial-gradient(ellipse 140% 100% at 80% 20%, rgba(99, 102, 241, 0.25) 0%, transparent 50%), radial-gradient(ellipse 100% 140% at 20% 80%, rgba(168, 85, 247, 0.2) 0%, transparent 50%); }}
.grain {{ position: absolute; inset: 0; opacity: 0.06; background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E"); }}

/* Decorative oversized background text */
.bg-text {{ position: absolute; top: -80px; right: -60px; font-size: 500px; font-weight: 900; color: rgba(255,255,255,0.02); line-height: 0.8; pointer-events: none; }}

/* Decorative blob */
.blob {{ position: absolute; width: 600px; height: 600px; border-radius: 50%; filter: blur(120px); pointer-events: none; }}
.blob-1 {{ top: -200px; right: -150px; background: linear-gradient(135deg, #6366f1, #a855f7); opacity: 0.3; }}
.blob-2 {{ bottom: -100px; left: -200px; background: linear-gradient(135deg, #ec4899, #8b5cf6); opacity: 0.15; }}

/* Floating decorative shapes */
.float-shape {{ position: absolute; border-radius: 50%; border: 2px solid rgba(255,255,255,0.1); }}
.float-1 {{ width: 300px; height: 300px; top: 60px; right: 80px; }}
.float-2 {{ width: 180px; height: 180px; bottom: 200px; right: 180px; border-color: rgba(139, 92, 246, 0.2); }}
.float-3 {{ width: 80px; height: 80px; top: 300px; right: 400px; background: rgba(99, 102, 241, 0.1); }}

/* Content */
.slide {{ position: relative; z-index: 1; width: 100%; height: 100%; padding: 64px; display: flex; flex-direction: column; }}
.slide-num {{ position: absolute; top: 56px; right: 64px; font-size: 14px; font-weight: 600; color: rgba(255,255,255,0.15); letter-spacing: 0.15em; }}

.content {{ flex: 1; display: flex; flex-direction: column; justify-content: center; padding-right: 100px; }}

.tag {{ display: inline-flex; align-items: center; gap: 12px; background: rgba(99, 102, 241, 0.12); border: 1px solid rgba(99, 102, 241, 0.25); padding: 14px 24px; border-radius: 100px; font-size: 16px; font-weight: 600; color: #a5b4fc; margin-bottom: 40px; width: fit-content; backdrop-filter: blur(10px); }}

.headline {{ font-size: 100px; font-weight: 900; line-height: 0.92; letter-spacing: -0.045em; }}
.line-1 {{ color: #fff; }}
.line-2 {{ position: relative; display: inline-block; color: rgba(255,255,255,0.25); }}
.line-2::after {{ content: ''; position: absolute; left: -5px; right: -5px; top: 50%; height: 8px; background: linear-gradient(90deg, #ef4444, #f97316); transform: rotate(-1.5deg); border-radius: 4px; }}
.line-3 {{ background: linear-gradient(135deg, #818cf8, #c084fc, #f472b6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}

.subhead {{ font-size: 28px; font-weight: 500; color: rgba(255,255,255,0.5); line-height: 1.5; margin-top: 32px; max-width: 550px; }}

/* Swipe CTA */
.swipe {{ display: flex; align-items: center; gap: 20px; margin-top: 56px; padding: 24px 36px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 20px; width: fit-content; backdrop-filter: blur(10px); }}
.swipe-icon {{ width: 56px; height: 56px; background: linear-gradient(135deg, #6366f1, #a855f7); border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 8px 32px rgba(99, 102, 241, 0.4); }}
.swipe-text {{ font-size: 20px; font-weight: 600; color: rgba(255,255,255,0.6); }}

.footer {{ display: flex; align-items: center; gap: 14px; padding-top: 40px; }}
.brand {{ font-size: 18px; font-weight: 600; color: rgba(255,255,255,0.35); }}
</style></head><body>
<div class="bg-gradient"></div>
<div class="grain"></div>
<div class="bg-text">?</div>
<div class="blob blob-1"></div>
<div class="blob blob-2"></div>
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
      <span class="line-1">My designer</span><br>
      <span class="line-2">quit</span><br>
      <span class="line-3">so I built this</span>
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

# Slide 2: Problem - STACKED OVERLAPPING CARDS
SLIDE_2 = f"""<!DOCTYPE html><html><head><style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: 'Inter', sans-serif; background: #08080c; color: #fff; width: 1080px; height: 1350px; overflow: hidden; position: relative; }}

.bg-gradient {{ position: absolute; inset: 0; background: radial-gradient(ellipse 120% 80% at 30% 70%, rgba(239, 68, 68, 0.15) 0%, transparent 50%), radial-gradient(ellipse 80% 120% at 80% 30%, rgba(251, 146, 60, 0.1) 0%, transparent 50%); }}
.grain {{ position: absolute; inset: 0; opacity: 0.06; background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E"); }}

/* Massive X in background */
.bg-x {{ position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); font-size: 800px; font-weight: 900; color: rgba(239, 68, 68, 0.03); pointer-events: none; }}

/* Red glow blob */
.blob {{ position: absolute; width: 500px; height: 500px; border-radius: 50%; background: radial-gradient(circle, rgba(239, 68, 68, 0.3), transparent 70%); filter: blur(80px); top: 50%; left: 50%; transform: translate(-50%, -50%); }}

.slide {{ position: relative; z-index: 1; width: 100%; height: 100%; padding: 64px; display: flex; flex-direction: column; }}
.slide-num {{ position: absolute; top: 56px; right: 64px; font-size: 14px; font-weight: 600; color: rgba(255,255,255,0.15); letter-spacing: 0.15em; }}

.header {{ margin-bottom: 32px; }}
.label {{ font-size: 14px; font-weight: 700; color: #f87171; letter-spacing: 0.2em; text-transform: uppercase; margin-bottom: 16px; }}
.headline {{ font-size: 72px; font-weight: 900; line-height: 0.95; letter-spacing: -0.04em; }}
.headline span {{ background: linear-gradient(135deg, #f87171, #fb923c); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}

/* Stacked cards container */
.cards-stack {{ flex: 1; position: relative; display: flex; align-items: center; justify-content: center; }}

/* Cards with overlap and rotation */
.card {{ position: absolute; width: 880px; background: rgba(0,0,0,0.6); border: 1px solid rgba(239, 68, 68, 0.2); border-radius: 28px; padding: 36px 40px; display: flex; align-items: center; gap: 28px; backdrop-filter: blur(20px); box-shadow: 0 4px 16px rgba(0,0,0,0.2), 0 16px 48px rgba(0,0,0,0.3); }}

.card-1 {{ transform: rotate(-2deg) translateY(-180px); z-index: 4; background: rgba(239, 68, 68, 0.08); border-color: rgba(239, 68, 68, 0.25); }}
.card-2 {{ transform: rotate(1deg) translateY(-60px); z-index: 3; }}
.card-3 {{ transform: rotate(-1deg) translateY(60px); z-index: 2; }}
.card-4 {{ transform: rotate(2deg) translateY(180px); z-index: 1; opacity: 0.8; }}

.card-icon {{ width: 64px; height: 64px; background: rgba(239, 68, 68, 0.15); border-radius: 16px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; color: #f87171; }}
.card h3 {{ font-size: 24px; font-weight: 700; margin-bottom: 6px; }}
.card p {{ font-size: 17px; color: rgba(255,255,255,0.5); }}

.footer {{ display: flex; align-items: center; gap: 14px; padding-top: 40px; }}
.brand {{ font-size: 18px; font-weight: 600; color: rgba(255,255,255,0.35); }}
</style></head><body>
<div class="bg-gradient"></div>
<div class="grain"></div>
<div class="bg-x">×</div>
<div class="blob"></div>

<div class="slide">
  <div class="slide-num">02 / 08</div>
  <div class="header">
    <div class="label">The Problem</div>
    <h1 class="headline">Design tools are <span>broken</span></h1>
  </div>
  <div class="cards-stack">
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

# Slide 3: Solution - DRAMATIC HERO
SLIDE_3 = f"""<!DOCTYPE html><html><head><style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: 'Inter', sans-serif; background: #08080c; color: #fff; width: 1080px; height: 1350px; overflow: hidden; position: relative; }}

.bg-gradient {{ position: absolute; inset: 0; background: radial-gradient(ellipse 100% 80% at 50% 30%, rgba(99, 102, 241, 0.2) 0%, transparent 50%), radial-gradient(ellipse 80% 100% at 30% 70%, rgba(168, 85, 247, 0.15) 0%, transparent 50%), radial-gradient(ellipse 60% 60% at 70% 60%, rgba(34, 197, 94, 0.1) 0%, transparent 50%); }}
.grain {{ position: absolute; inset: 0; opacity: 0.05; background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E"); }}

/* Large decorative circles */
.circle {{ position: absolute; border-radius: 50%; border: 1px solid; }}
.circle-1 {{ width: 800px; height: 800px; top: 50%; left: 50%; transform: translate(-50%, -50%); border-color: rgba(99, 102, 241, 0.15); }}
.circle-2 {{ width: 600px; height: 600px; top: 50%; left: 50%; transform: translate(-50%, -50%); border-color: rgba(168, 85, 247, 0.1); }}
.circle-3 {{ width: 400px; height: 400px; top: 50%; left: 50%; transform: translate(-50%, -50%); border-color: rgba(99, 102, 241, 0.08); }}

/* Glowing orb behind logo */
.glow-orb {{ position: absolute; width: 300px; height: 300px; top: 200px; left: 50%; transform: translateX(-50%); background: radial-gradient(circle, rgba(99, 102, 241, 0.4) 0%, rgba(168, 85, 247, 0.2) 40%, transparent 70%); filter: blur(60px); }}

/* Floating accent dots */
.dot {{ position: absolute; border-radius: 50%; background: linear-gradient(135deg, #6366f1, #a855f7); }}
.dot-1 {{ width: 12px; height: 12px; top: 180px; left: 200px; opacity: 0.6; }}
.dot-2 {{ width: 8px; height: 8px; top: 400px; right: 150px; opacity: 0.4; }}
.dot-3 {{ width: 16px; height: 16px; bottom: 300px; left: 120px; opacity: 0.3; }}
.dot-4 {{ width: 10px; height: 10px; bottom: 400px; right: 200px; opacity: 0.5; }}

.slide {{ position: relative; z-index: 1; width: 100%; height: 100%; padding: 64px; display: flex; flex-direction: column; }}
.slide-num {{ position: absolute; top: 56px; right: 64px; font-size: 14px; font-weight: 600; color: rgba(255,255,255,0.15); letter-spacing: 0.15em; }}

.content {{ flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }}

.logo-container {{ margin-bottom: 40px; }}
.logo-container svg {{ filter: drop-shadow(0 0 60px rgba(99, 102, 241, 0.6)) drop-shadow(0 0 120px rgba(168, 85, 247, 0.4)); }}

.headline {{ font-size: 96px; font-weight: 900; line-height: 0.95; letter-spacing: -0.045em; margin-bottom: 24px; }}
.headline span {{ background: linear-gradient(135deg, #818cf8, #c084fc, #f472b6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}

.subhead {{ font-size: 28px; font-weight: 500; color: rgba(255,255,255,0.55); line-height: 1.5; margin-bottom: 48px; }}

/* Feature pills floating */
.features {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 16px; margin-bottom: 48px; }}
.feat {{ background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.1); padding: 16px 28px; border-radius: 100px; font-size: 17px; font-weight: 600; color: rgba(255,255,255,0.7); backdrop-filter: blur(10px); }}
.feat.primary {{ background: linear-gradient(135deg, rgba(34, 197, 94, 0.15), rgba(34, 197, 94, 0.08)); border-color: rgba(34, 197, 94, 0.3); color: #4ade80; }}

/* Terminal box */
.terminal {{ background: rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.1); border-radius: 20px; padding: 24px 36px; display: inline-flex; align-items: center; gap: 16px; backdrop-filter: blur(20px); box-shadow: 0 8px 32px rgba(0,0,0,0.3); }}
.terminal .dollar {{ color: #4ade80; font-family: 'SF Mono', monospace; font-size: 20px; }}
.terminal code {{ font-family: 'SF Mono', monospace; font-size: 22px; font-weight: 500; }}

.footer {{ display: flex; align-items: center; justify-content: center; gap: 14px; padding-top: 40px; }}
.brand {{ font-size: 18px; font-weight: 600; color: rgba(255,255,255,0.35); }}
</style></head><body>
<div class="bg-gradient"></div>
<div class="grain"></div>
<div class="circle circle-1"></div>
<div class="circle circle-2"></div>
<div class="circle circle-3"></div>
<div class="glow-orb"></div>
<div class="dot dot-1"></div>
<div class="dot dot-2"></div>
<div class="dot dot-3"></div>
<div class="dot dot-4"></div>

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
    <div class="terminal">
      <span class="dollar">$</span>
      <code>pip install openfigma</code>
    </div>
  </div>
  <div class="footer">{LOGO_SMALL}<span class="brand">openfigma</span></div>
</div>
</body></html>"""

# Slide 7: Code - EDITORIAL STYLE
SLIDE_7 = f"""<!DOCTYPE html><html><head><style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: 'Inter', sans-serif; background: #08080c; color: #fff; width: 1080px; height: 1350px; overflow: hidden; position: relative; }}

.bg-gradient {{ position: absolute; inset: 0; background: radial-gradient(ellipse 100% 80% at 70% 40%, rgba(99, 102, 241, 0.12) 0%, transparent 50%), radial-gradient(ellipse 80% 100% at 30% 60%, rgba(34, 197, 94, 0.1) 0%, transparent 50%); }}
.grain {{ position: absolute; inset: 0; opacity: 0.05; background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E"); }}

/* Giant "4" in background */
.bg-num {{ position: absolute; top: -100px; left: -80px; font-size: 700px; font-weight: 900; background: linear-gradient(180deg, rgba(99, 102, 241, 0.06) 0%, rgba(99, 102, 241, 0) 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; pointer-events: none; line-height: 0.8; }}

/* Decorative code brackets */
.deco-bracket {{ position: absolute; font-family: 'SF Mono', monospace; font-size: 300px; font-weight: 300; color: rgba(99, 102, 241, 0.05); }}
.bracket-open {{ top: 100px; left: 40px; }}
.bracket-close {{ bottom: 100px; right: 40px; }}

.slide {{ position: relative; z-index: 1; width: 100%; height: 100%; padding: 64px; display: flex; flex-direction: column; }}
.slide-num {{ position: absolute; top: 56px; right: 64px; font-size: 14px; font-weight: 600; color: rgba(255,255,255,0.15); letter-spacing: 0.15em; }}

.header {{ margin-bottom: 40px; }}
.label {{ font-size: 14px; font-weight: 700; color: rgba(255,255,255,0.3); letter-spacing: 0.2em; text-transform: uppercase; margin-bottom: 16px; }}
.headline {{ font-size: 88px; font-weight: 900; line-height: 0.95; letter-spacing: -0.04em; }}
.headline span {{ background: linear-gradient(135deg, #818cf8, #c084fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}

/* Code window with depth */
.code-window {{ flex: 1; background: rgba(0,0,0,0.6); border: 1px solid rgba(255,255,255,0.08); border-radius: 28px; overflow: hidden; display: flex; flex-direction: column; backdrop-filter: blur(20px); box-shadow: 0 4px 8px rgba(0,0,0,0.1), 0 8px 16px rgba(0,0,0,0.1), 0 16px 32px rgba(0,0,0,0.15), 0 32px 64px rgba(0,0,0,0.2); }}

.window-header {{ background: rgba(255,255,255,0.03); padding: 20px 28px; display: flex; align-items: center; gap: 12px; border-bottom: 1px solid rgba(255,255,255,0.06); }}
.dots {{ display: flex; gap: 8px; }}
.dot {{ width: 14px; height: 14px; border-radius: 50%; }}
.dot.r {{ background: #ef4444; }}
.dot.y {{ background: #eab308; }}
.dot.g {{ background: #22c55e; }}
.filename {{ font-size: 14px; color: rgba(255,255,255,0.35); margin-left: 12px; font-family: 'SF Mono', monospace; }}

.code-body {{ flex: 1; padding: 48px; font-family: 'SF Mono', 'Fira Code', monospace; font-size: 26px; line-height: 2.2; display: flex; flex-direction: column; justify-content: center; }}
.line {{ display: flex; }}
.ln {{ color: rgba(255,255,255,0.15); width: 56px; flex-shrink: 0; user-select: none; }}
.kw {{ color: #c084fc; }}
.str {{ color: #4ade80; }}
.fn {{ color: #60a5fa; }}
.cm {{ color: rgba(255,255,255,0.3); font-style: italic; }}

/* Output badge floating */
.output-badge {{ position: absolute; bottom: 200px; right: 80px; background: linear-gradient(135deg, rgba(34, 197, 94, 0.2), rgba(34, 197, 94, 0.1)); border: 1px solid rgba(34, 197, 94, 0.3); padding: 24px 32px; border-radius: 20px; display: flex; align-items: center; gap: 16px; backdrop-filter: blur(20px); box-shadow: 0 8px 32px rgba(34, 197, 94, 0.2); transform: rotate(2deg); }}
.output-badge .icon {{ width: 48px; height: 48px; background: rgba(34, 197, 94, 0.2); border-radius: 12px; display: flex; align-items: center; justify-content: center; color: #4ade80; }}
.output-badge .text h4 {{ font-size: 18px; font-weight: 700; color: #4ade80; }}
.output-badge .text p {{ font-size: 14px; color: rgba(255,255,255,0.5); font-family: 'SF Mono', monospace; }}

.footer {{ display: flex; align-items: center; gap: 14px; padding-top: 40px; }}
.brand {{ font-size: 18px; font-weight: 600; color: rgba(255,255,255,0.35); }}
</style></head><body>
<div class="bg-gradient"></div>
<div class="grain"></div>
<div class="bg-num">4</div>
<div class="deco-bracket bracket-open">{{</div>
<div class="deco-bracket bracket-close">}}</div>

<div class="slide">
  <div class="slide-num">07 / 08</div>
  <div class="header">
    <div class="label">How It Works</div>
    <h1 class="headline"><span>4 lines</span> of Python</h1>
  </div>
  <div class="code-window">
    <div class="window-header">
      <div class="dots"><div class="dot r"></div><div class="dot y"></div><div class="dot g"></div></div>
      <span class="filename">create_post.py</span>
    </div>
    <div class="code-body">
      <div class="line"><span class="ln">1</span><span class="kw">from</span> openfigma <span class="kw">import</span> html_to_png</div>
      <div class="line"><span class="ln">2</span></div>
      <div class="line"><span class="ln">3</span>html = <span class="str">"&lt;your template html&gt;"</span></div>
      <div class="line"><span class="ln">4</span><span class="fn">html_to_png</span>(html, <span class="str">"post.png"</span>)</div>
    </div>
  </div>
  <div class="output-badge">
    <div class="icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12l5 5L20 7"/></svg></div>
    <div class="text"><h4>Ready to post</h4><p>→ post.png</p></div>
  </div>
  <div class="footer">{LOGO_SMALL}<span class="brand">openfigma</span></div>
</div>
</body></html>"""

# Slide 8: CTA - PREMIUM CLOSER
SLIDE_8 = f"""<!DOCTYPE html><html><head><style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
body {{ font-family: 'Inter', sans-serif; background: #08080c; color: #fff; width: 1080px; height: 1350px; overflow: hidden; position: relative; }}

.bg-gradient {{ position: absolute; inset: 0; background: radial-gradient(ellipse 120% 100% at 50% 20%, rgba(99, 102, 241, 0.2) 0%, transparent 50%), radial-gradient(ellipse 100% 120% at 50% 80%, rgba(168, 85, 247, 0.15) 0%, transparent 50%); }}
.grain {{ position: absolute; inset: 0; opacity: 0.05; background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E"); }}

/* Concentric circles */
.ring {{ position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); border-radius: 50%; border: 1px solid; }}
.ring-1 {{ width: 1200px; height: 1200px; border-color: rgba(99, 102, 241, 0.08); }}
.ring-2 {{ width: 900px; height: 900px; border-color: rgba(168, 85, 247, 0.1); }}
.ring-3 {{ width: 600px; height: 600px; border-color: rgba(99, 102, 241, 0.12); }}
.ring-4 {{ width: 300px; height: 300px; border-color: rgba(168, 85, 247, 0.08); }}

/* Glow center */
.center-glow {{ position: absolute; top: 50%; left: 50%; transform: translate(-50%, -60%); width: 400px; height: 400px; background: radial-gradient(circle, rgba(99, 102, 241, 0.3) 0%, transparent 70%); filter: blur(80px); }}

/* Floating sparkles */
.sparkle {{ position: absolute; width: 4px; height: 4px; background: #fff; border-radius: 50%; }}
.sparkle-1 {{ top: 200px; left: 180px; opacity: 0.6; box-shadow: 0 0 10px 2px rgba(99, 102, 241, 0.5); }}
.sparkle-2 {{ top: 350px; right: 200px; opacity: 0.4; box-shadow: 0 0 10px 2px rgba(168, 85, 247, 0.5); }}
.sparkle-3 {{ bottom: 400px; left: 250px; opacity: 0.5; box-shadow: 0 0 10px 2px rgba(99, 102, 241, 0.5); }}
.sparkle-4 {{ bottom: 300px; right: 180px; opacity: 0.3; box-shadow: 0 0 10px 2px rgba(168, 85, 247, 0.5); }}

.slide {{ position: relative; z-index: 1; width: 100%; height: 100%; padding: 64px; display: flex; flex-direction: column; }}
.slide-num {{ position: absolute; top: 56px; right: 64px; font-size: 14px; font-weight: 600; color: rgba(255,255,255,0.15); letter-spacing: 0.15em; }}

.content {{ flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; }}

.logo-glow {{ margin-bottom: 36px; }}
.logo-glow svg {{ filter: drop-shadow(0 0 40px rgba(99, 102, 241, 0.5)) drop-shadow(0 0 80px rgba(168, 85, 247, 0.3)); }}

.headline {{ font-size: 88px; font-weight: 900; line-height: 1.0; letter-spacing: -0.04em; margin-bottom: 16px; }}
.headline span {{ background: linear-gradient(135deg, #818cf8, #c084fc, #f472b6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}

.tagline {{ font-size: 26px; color: rgba(255,255,255,0.5); margin-bottom: 40px; }}

/* GitHub button with glow */
.github-btn {{ display: inline-flex; align-items: center; gap: 16px; background: #fff; color: #0a0a0f; padding: 24px 48px; border-radius: 20px; font-size: 20px; font-weight: 700; box-shadow: 0 4px 16px rgba(255,255,255,0.1), 0 8px 32px rgba(255,255,255,0.05); }}

/* Engagement card with premium feel */
.engage-card {{ margin-top: 48px; background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(168, 85, 247, 0.1)); border: 2px solid rgba(139, 92, 246, 0.25); border-radius: 32px; padding: 40px 48px; max-width: 800px; backdrop-filter: blur(20px); box-shadow: 0 8px 32px rgba(99, 102, 241, 0.1); }}
.engage-header {{ display: flex; align-items: center; justify-content: center; gap: 12px; font-size: 18px; font-weight: 700; color: #c4b5fd; margin-bottom: 16px; }}
.engage-text {{ font-size: 30px; font-weight: 700; line-height: 1.4; }}
.engage-example {{ font-size: 18px; color: rgba(255,255,255,0.4); margin-top: 16px; font-style: italic; }}

/* Trust badges */
.trust {{ display: flex; justify-content: center; gap: 32px; margin-top: 40px; }}
.trust-item {{ display: flex; align-items: center; gap: 8px; font-size: 16px; color: rgba(255,255,255,0.45); }}
.trust-item svg {{ color: #4ade80; }}

.footer {{ display: flex; align-items: center; justify-content: center; gap: 14px; padding-top: 40px; }}
.brand {{ font-size: 18px; font-weight: 600; color: rgba(255,255,255,0.35); }}
</style></head><body>
<div class="bg-gradient"></div>
<div class="grain"></div>
<div class="ring ring-1"></div>
<div class="ring ring-2"></div>
<div class="ring ring-3"></div>
<div class="ring ring-4"></div>
<div class="center-glow"></div>
<div class="sparkle sparkle-1"></div>
<div class="sparkle sparkle-2"></div>
<div class="sparkle sparkle-3"></div>
<div class="sparkle sparkle-4"></div>

<div class="slide">
  <div class="slide-num">08 / 08</div>
  <div class="content">
    <div class="logo-glow">
      <svg width="120" height="120" viewBox="0 0 120 120" fill="none"><defs><linearGradient id="logoGradH" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#6366f1"/><stop offset="100%" style="stop-color:#a855f7"/></linearGradient></defs><rect x="4" y="4" width="112" height="112" rx="28" fill="url(#logoGradH)"/><path d="M52 40L32 60L52 80" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M68 40L88 60L68 80" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="60" cy="60" r="6" fill="white"/></svg>
    </div>
    <h1 class="headline">Try it.<br><span>It's free.</span></h1>
    <p class="tagline">No signup. No waitlist. No BS.</p>
    <div class="github-btn">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
      github.com/federicodeponte/openfigma
    </div>
    <div class="engage-card">
      <div class="engage-header">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
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

BASE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Inter', sans-serif; background: #08080c; color: #fff; width: 1080px; height: 1350px; overflow: hidden; position: relative; }
.bg-gradient { position: absolute; inset: 0; background: radial-gradient(ellipse 120% 80% at 70% 30%, rgba(99, 102, 241, 0.15) 0%, transparent 50%), radial-gradient(ellipse 80% 120% at 30% 70%, rgba(168, 85, 247, 0.12) 0%, transparent 50%); }
.grain { position: absolute; inset: 0; opacity: 0.05; background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E"); }
.slide { position: relative; z-index: 1; width: 100%; height: 100%; padding: 64px; display: flex; flex-direction: column; }
.slide-num { position: absolute; top: 56px; right: 64px; font-size: 14px; font-weight: 600; color: rgba(255,255,255,0.15); letter-spacing: 0.15em; }
.footer { display: flex; align-items: center; gap: 14px; padding-top: 40px; }
.brand { font-size: 18px; font-weight: 600; color: rgba(255,255,255,0.35); }
"""

def make_template_slide(num, total, img_b64, template_name, description):
    return f"""<!DOCTYPE html><html><head><style>
{BASE_CSS}
.showcase {{ flex: 1; display: flex; flex-direction: column; }}
.section-label {{ font-size: 14px; font-weight: 700; color: #818cf8; letter-spacing: 0.2em; text-transform: uppercase; margin-bottom: 12px; }}
.headline {{ font-size: 52px; font-weight: 800; line-height: 0.95; letter-spacing: -0.03em; margin-bottom: 20px; }}
.accent {{ background: linear-gradient(135deg, #818cf8, #c084fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
.template-container {{ flex: 1; display: flex; flex-direction: column; }}
.template-img {{ flex: 1; border-radius: 24px; overflow: hidden; box-shadow: 0 4px 8px rgba(0,0,0,0.1), 0 8px 16px rgba(0,0,0,0.1), 0 16px 32px rgba(0,0,0,0.15), 0 32px 64px rgba(0,0,0,0.2), 0 0 0 1px rgba(255,255,255,0.06); display: flex; align-items: center; justify-content: center; background: #0c0c14; }}
.template-img img {{ max-width: 100%; max-height: 100%; object-fit: contain; }}
.template-info {{ margin-top: 20px; font-size: 17px; color: rgba(255,255,255,0.4); }}
</style></head><body>
<div class="bg-gradient"></div>
<div class="grain"></div>
<div class="slide">
  <div class="slide-num">{num:02d} / {total:02d}</div>
  <div class="content" style="flex:1;display:flex;flex-direction:column;">
    <div class="showcase">
      <div class="section-label">Premium Template</div>
      <h1 class="headline">{template_name}</h1>
      <div class="template-container">
        <div class="template-img"><img src="data:image/png;base64,{img_b64}"></div>
        <div class="template-info">{description}</div>
      </div>
    </div>
  </div>
  <div class="footer">{LOGO_SMALL}<span class="brand">openfigma</span></div>
</div>
</body></html>"""

def main():
    import os

    output_dir = "/home/tech_scaile_it/openfigma/exports/linkedin_v6"
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
