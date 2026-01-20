#!/usr/bin/env python3
"""
LinkedIn Carousel V5 - Premium wrapper slides to match template quality
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

LOGO_BIG = '''<svg width="140" height="140" viewBox="0 0 120 120" fill="none"><defs><linearGradient id="logoGradB" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#6366f1"/><stop offset="100%" style="stop-color:#a855f7"/></linearGradient></defs><rect x="4" y="4" width="112" height="112" rx="28" fill="url(#logoGradB)"/><path d="M52 40L32 60L52 80" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M68 40L88 60L68 80" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="60" cy="60" r="6" fill="white"/></svg>'''

BASE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Inter', -apple-system, sans-serif; background: #08080c; color: #fff; width: 1080px; height: 1350px; overflow: hidden; }
.slide { width: 100%; height: 100%; padding: 56px; display: flex; flex-direction: column; position: relative; }
.mesh { position: absolute; inset: 0; background: radial-gradient(ellipse 120% 80% at 70% 30%, rgba(99, 102, 241, 0.15) 0%, transparent 50%), radial-gradient(ellipse 80% 120% at 30% 70%, rgba(168, 85, 247, 0.12) 0%, transparent 50%); pointer-events: none; }
.grain { position: absolute; inset: 0; opacity: 0.03; background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E"); pointer-events: none; }
.slide-num { position: absolute; top: 48px; right: 56px; font-size: 14px; font-weight: 600; color: rgba(255,255,255,0.2); letter-spacing: 0.1em; }
.content { position: relative; z-index: 1; flex: 1; display: flex; flex-direction: column; }
.footer { margin-top: auto; display: flex; align-items: center; gap: 14px; padding-top: 40px; }
.brand { font-size: 18px; font-weight: 600; color: rgba(255,255,255,0.4); }
"""

# Slide 1: Hook - DRAMATIC
SLIDE_1 = f"""<!DOCTYPE html><html><head><style>
{BASE_CSS}
.hook {{
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}}
.tag {{
  display: inline-flex;
  align-items: center;
  gap: 12px;
  background: rgba(99, 102, 241, 0.15);
  border: 1px solid rgba(99, 102, 241, 0.3);
  padding: 16px 28px;
  border-radius: 100px;
  font-size: 18px;
  font-weight: 600;
  color: #a5b4fc;
  margin-bottom: 48px;
  width: fit-content;
}}
.headline {{
  font-size: 92px;
  font-weight: 800;
  line-height: 0.95;
  letter-spacing: -0.04em;
}}
.strike {{
  position: relative;
  color: rgba(255,255,255,0.3);
}}
.strike::after {{
  content: '';
  position: absolute;
  left: 0;
  right: 0;
  top: 50%;
  height: 6px;
  background: #ef4444;
  transform: rotate(-2deg);
}}
.accent {{
  background: linear-gradient(135deg, #818cf8, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}
.subhead {{
  font-size: 32px;
  font-weight: 500;
  color: rgba(255,255,255,0.5);
  line-height: 1.4;
  margin-top: 40px;
  max-width: 700px;
}}
.swipe {{
  display: flex;
  align-items: center;
  gap: 16px;
  margin-top: 64px;
  padding: 20px 32px;
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 16px;
  width: fit-content;
}}
.swipe-circle {{
  width: 52px;
  height: 52px;
  background: linear-gradient(135deg, #6366f1, #a855f7);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}}
.swipe-text {{
  font-size: 20px;
  font-weight: 600;
  color: rgba(255,255,255,0.6);
}}
</style></head><body>
<div class="slide">
  <div class="mesh"></div><div class="grain"></div>
  <div class="slide-num">01 / 08</div>
  <div class="content">
    <div class="hook">
      <div class="tag">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
        Open Source
      </div>
      <h1 class="headline">
        My designer<br>
        <span class="strike">quit</span><br>
        <span class="accent">so I built this</span>
      </h1>
      <p class="subhead">She got a full-time offer.<br>I needed a solution fast.</p>
      <div class="swipe">
        <div class="swipe-circle">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </div>
        <span class="swipe-text">Swipe to see what I made</span>
      </div>
    </div>
  </div>
  <div class="footer">{LOGO_SMALL}<span class="brand">openfigma</span></div>
</div>
</body></html>"""

# Slide 2: Problem - BOLD CARDS
SLIDE_2 = f"""<!DOCTYPE html><html><head><style>
{BASE_CSS}
.problem-slide {{
  flex: 1;
  display: flex;
  flex-direction: column;
}}
.section-label {{
  font-size: 15px;
  font-weight: 700;
  color: #f87171;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  margin-bottom: 16px;
}}
.headline {{
  font-size: 76px;
  font-weight: 800;
  line-height: 0.95;
  letter-spacing: -0.04em;
  margin-bottom: 48px;
}}
.accent {{
  background: linear-gradient(135deg, #f87171, #ef4444);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}
.problems {{
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 20px;
}}
.card {{
  background: rgba(239, 68, 68, 0.06);
  border: 1px solid rgba(239, 68, 68, 0.15);
  border-radius: 24px;
  padding: 32px;
  display: flex;
  align-items: center;
  gap: 28px;
}}
.card-icon {{
  width: 64px;
  height: 64px;
  background: rgba(239, 68, 68, 0.15);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  color: #f87171;
}}
.card h3 {{
  font-size: 26px;
  font-weight: 700;
  margin-bottom: 8px;
}}
.card p {{
  font-size: 18px;
  color: rgba(255,255,255,0.5);
  line-height: 1.4;
}}
</style></head><body>
<div class="slide">
  <div class="mesh"></div><div class="grain"></div>
  <div class="slide-num">02 / 08</div>
  <div class="content">
    <div class="problem-slide">
      <div class="section-label">The Problem</div>
      <h1 class="headline">Design tools<br>are <span class="accent">broken</span></h1>
      <div class="problems">
        <div class="card">
          <div class="card-icon"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg></div>
          <div><h3>Steep learning curve</h3><p>Weeks to learn Figma or Canva properly</p></div>
        </div>
        <div class="card">
          <div class="card-icon"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg></div>
          <div><h3>Expensive templates</h3><p>$20-50 per pack, subscriptions add up</p></div>
        </div>
        <div class="card">
          <div class="card-icon"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg></div>
          <div><h3>Manual repetition</h3><p>Copy, paste, tweak, export... every time</p></div>
        </div>
        <div class="card">
          <div class="card-icon"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg></div>
          <div><h3>Designer dependency</h3><p>Need someone for every visual asset</p></div>
        </div>
      </div>
    </div>
  </div>
  <div class="footer">{LOGO_SMALL}<span class="brand">openfigma</span></div>
</div>
</body></html>"""

# Slide 3: Solution - HERO INTRO
SLIDE_3 = f"""<!DOCTYPE html><html><head><style>
{BASE_CSS}
.solution {{
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}}
.logo-container {{
  margin-bottom: 48px;
  filter: drop-shadow(0 0 80px rgba(99, 102, 241, 0.5)) drop-shadow(0 0 160px rgba(168, 85, 247, 0.3));
}}
.headline {{
  font-size: 84px;
  font-weight: 800;
  line-height: 0.95;
  letter-spacing: -0.04em;
}}
.accent {{
  background: linear-gradient(135deg, #818cf8, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}
.subhead {{
  font-size: 30px;
  font-weight: 500;
  color: rgba(255,255,255,0.55);
  line-height: 1.5;
  margin-top: 28px;
  max-width: 750px;
}}
.features {{
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  margin-top: 48px;
}}
.feat {{
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.1);
  padding: 18px 28px;
  border-radius: 100px;
  font-size: 18px;
  font-weight: 600;
  color: rgba(255,255,255,0.7);
}}
.feat.primary {{
  background: linear-gradient(135deg, rgba(34, 197, 94, 0.2), rgba(34, 197, 94, 0.1));
  border-color: rgba(34, 197, 94, 0.3);
  color: #4ade80;
}}
.pip-box {{
  margin-top: 48px;
  background: #0c0c14;
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 16px;
  padding: 24px 32px;
  display: inline-flex;
  align-items: center;
  gap: 16px;
  width: fit-content;
}}
.pip-box .dollar {{
  color: #4ade80;
  font-family: 'SF Mono', monospace;
  font-size: 20px;
}}
.pip-box code {{
  font-family: 'SF Mono', monospace;
  font-size: 22px;
  font-weight: 500;
}}
</style></head><body>
<div class="slide">
  <div class="mesh"></div><div class="grain"></div>
  <div class="slide-num">03 / 08</div>
  <div class="content">
    <div class="solution">
      <div class="logo-container">{LOGO_BIG}</div>
      <h1 class="headline">Meet<br><span class="accent">openfigma</span></h1>
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
  </div>
  <div class="footer">{LOGO_SMALL}<span class="brand">openfigma</span></div>
</div>
</body></html>"""

# Slide 7: Code - DOMINANT CODE BLOCK
SLIDE_7 = f"""<!DOCTYPE html><html><head><style>
{BASE_CSS}
.code-slide {{
  flex: 1;
  display: flex;
  flex-direction: column;
}}
.section-label {{
  font-size: 15px;
  font-weight: 700;
  color: rgba(255,255,255,0.3);
  letter-spacing: 0.2em;
  text-transform: uppercase;
  margin-bottom: 16px;
}}
.headline {{
  font-size: 76px;
  font-weight: 800;
  line-height: 0.95;
  letter-spacing: -0.04em;
  margin-bottom: 40px;
}}
.accent {{
  background: linear-gradient(135deg, #818cf8, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}
.code-block {{
  flex: 1;
  background: #0a0a10;
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 24px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}}
.code-header {{
  background: rgba(255,255,255,0.03);
  padding: 20px 28px;
  display: flex;
  align-items: center;
  gap: 12px;
  border-bottom: 1px solid rgba(255,255,255,0.06);
}}
.dots {{ display: flex; gap: 8px; }}
.dot {{ width: 14px; height: 14px; border-radius: 50%; }}
.dot.r {{ background: #ef4444; }}
.dot.y {{ background: #eab308; }}
.dot.g {{ background: #22c55e; }}
.code-file {{ font-size: 15px; color: rgba(255,255,255,0.4); margin-left: 12px; font-family: 'SF Mono', monospace; }}
.code-body {{
  flex: 1;
  padding: 40px;
  font-family: 'SF Mono', 'Fira Code', monospace;
  font-size: 24px;
  line-height: 2;
  display: flex;
  flex-direction: column;
  justify-content: center;
}}
.line {{ display: flex; }}
.ln {{ color: rgba(255,255,255,0.2); width: 48px; flex-shrink: 0; }}
.kw {{ color: #c084fc; }}
.str {{ color: #4ade80; }}
.fn {{ color: #60a5fa; }}
.output-box {{
  display: flex;
  align-items: center;
  gap: 24px;
  background: rgba(34, 197, 94, 0.1);
  border: 1px solid rgba(34, 197, 94, 0.25);
  padding: 28px 36px;
  border-radius: 20px;
  margin-top: 32px;
}}
.output-icon {{
  width: 64px;
  height: 64px;
  background: rgba(34, 197, 94, 0.2);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #4ade80;
}}
.output-text h4 {{
  font-size: 24px;
  font-weight: 700;
  margin-bottom: 4px;
}}
.output-text p {{
  font-size: 18px;
  color: rgba(255,255,255,0.5);
  font-family: 'SF Mono', monospace;
}}
</style></head><body>
<div class="slide">
  <div class="mesh"></div><div class="grain"></div>
  <div class="slide-num">07 / 08</div>
  <div class="content">
    <div class="code-slide">
      <div class="section-label">How It Works</div>
      <h1 class="headline"><span class="accent">4 lines</span><br>of Python</h1>
      <div class="code-block">
        <div class="code-header">
          <div class="dots"><div class="dot r"></div><div class="dot y"></div><div class="dot g"></div></div>
          <span class="code-file">create_post.py</span>
        </div>
        <div class="code-body">
          <div class="line"><span class="ln">1</span><span><span class="kw">from</span> openfigma <span class="kw">import</span> html_to_png</span></div>
          <div class="line"><span class="ln">2</span><span></span></div>
          <div class="line"><span class="ln">3</span><span>html = <span class="str">"&lt;your template&gt;"</span></span></div>
          <div class="line"><span class="ln">4</span><span><span class="fn">html_to_png</span>(html, <span class="str">"post.png"</span>)</span></div>
        </div>
      </div>
      <div class="output-box">
        <div class="output-icon"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12l5 5L20 7"/></svg></div>
        <div class="output-text"><h4>Ready for LinkedIn</h4><p>→ post.png (1080×1080)</p></div>
      </div>
    </div>
  </div>
  <div class="footer">{LOGO_SMALL}<span class="brand">openfigma</span></div>
</div>
</body></html>"""

# Slide 8: CTA - CLEAR AND BOLD
SLIDE_8 = f"""<!DOCTYPE html><html><head><style>
{BASE_CSS}
.cta {{
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}}
.logo-huge {{
  margin-bottom: 40px;
  filter: drop-shadow(0 0 80px rgba(99, 102, 241, 0.5)) drop-shadow(0 0 160px rgba(168, 85, 247, 0.3));
}}
.headline {{
  font-size: 84px;
  font-weight: 800;
  line-height: 1.0;
  letter-spacing: -0.04em;
  margin-bottom: 20px;
}}
.accent {{
  background: linear-gradient(135deg, #818cf8, #c084fc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}}
.cta-sub {{
  font-size: 28px;
  color: rgba(255,255,255,0.5);
  margin-bottom: 48px;
}}
.github-btn {{
  display: inline-flex;
  align-items: center;
  gap: 16px;
  background: #fff;
  color: #0a0a0f;
  padding: 28px 56px;
  border-radius: 20px;
  font-size: 22px;
  font-weight: 700;
}}
.engagement {{
  margin-top: 56px;
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.12), rgba(168, 85, 247, 0.12));
  border: 2px solid rgba(139, 92, 246, 0.3);
  border-radius: 28px;
  padding: 40px 56px;
  max-width: 900px;
}}
.engagement-head {{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 14px;
  font-size: 22px;
  font-weight: 700;
  color: #c4b5fd;
  margin-bottom: 20px;
}}
.engagement-text {{
  font-size: 32px;
  font-weight: 600;
  line-height: 1.35;
}}
.engagement-sub {{
  font-size: 20px;
  color: rgba(255,255,255,0.45);
  margin-top: 20px;
}}
.no-bs {{
  display: flex;
  justify-content: center;
  gap: 40px;
  margin-top: 48px;
}}
.no-bs-item {{
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 18px;
  color: rgba(255,255,255,0.5);
}}
.no-bs-item svg {{ color: #4ade80; }}
</style></head><body>
<div class="slide">
  <div class="mesh"></div><div class="grain"></div>
  <div class="slide-num">08 / 08</div>
  <div class="content">
    <div class="cta">
      <div class="logo-huge"><svg width="120" height="120" viewBox="0 0 120 120" fill="none"><defs><linearGradient id="logoGradH" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#6366f1"/><stop offset="100%" style="stop-color:#a855f7"/></linearGradient></defs><rect x="4" y="4" width="112" height="112" rx="28" fill="url(#logoGradH)"/><path d="M52 40L32 60L52 80" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/><path d="M68 40L88 60L68 80" stroke="white" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="60" cy="60" r="6" fill="white"/></svg></div>
      <h1 class="headline">Try it.<br><span class="accent">It's free.</span></h1>
      <p class="cta-sub">No signup. No waitlist. No BS.</p>
      <div class="github-btn">
        <svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
        github.com/federicodeponte/openfigma
      </div>
      <div class="engagement">
        <div class="engagement-head">
          <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
          Want a custom design?
        </div>
        <div class="engagement-text">Comment your prompt below.<br>I'll generate it and send within 24h.</div>
        <div class="engagement-sub">Example: "A metric card showing 500% growth"</div>
      </div>
      <div class="no-bs">
        <div class="no-bs-item"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12l5 5L20 7"/></svg>MIT License</div>
        <div class="no-bs-item"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12l5 5L20 7"/></svg>Free forever</div>
        <div class="no-bs-item"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12l5 5L20 7"/></svg>pip install</div>
      </div>
    </div>
  </div>
  <div class="footer">{LOGO_SMALL}<span class="brand">openfigma</span></div>
</div>
</body></html>"""

def make_template_slide(num, total, img_b64, template_name, description):
    return f"""<!DOCTYPE html><html><head><style>
{BASE_CSS}
.showcase {{ flex: 1; display: flex; flex-direction: column; }}
.section-label {{ font-size: 15px; font-weight: 700; color: #818cf8; letter-spacing: 0.2em; text-transform: uppercase; margin-bottom: 12px; }}
.headline {{ font-size: 56px; font-weight: 800; line-height: 0.95; letter-spacing: -0.03em; margin-bottom: 24px; }}
.accent {{ background: linear-gradient(135deg, #818cf8, #c084fc); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
.template-container {{ flex: 1; display: flex; flex-direction: column; }}
.template-img {{ flex: 1; border-radius: 24px; overflow: hidden; box-shadow: 0 40px 80px rgba(0,0,0,0.5), 0 0 0 1px rgba(255,255,255,0.08); display: flex; align-items: center; justify-content: center; background: #0c0c14; }}
.template-img img {{ max-width: 100%; max-height: 100%; object-fit: contain; }}
.template-info {{ margin-top: 24px; font-size: 18px; color: rgba(255,255,255,0.45); }}
</style></head><body>
<div class="slide">
  <div class="mesh"></div><div class="grain"></div>
  <div class="slide-num">{num:02d} / {total:02d}</div>
  <div class="content">
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

    output_dir = "/home/tech_scaile_it/openfigma/exports/linkedin_v5"
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
