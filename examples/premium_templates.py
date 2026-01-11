"""
Premium V6 - 10/10 Polish
Fixes from V5 audit:
- No dead space
- Stronger visual anchors
- Tighter typography
- Richer gradients
- Micro-details that elevate
"""

import sys
import os
sys.path.insert(0, '/home/tech_scaile_it/openfigma')

from openfigma import PNGExporter

TEMPLATES = {}

# -----------------------------------------------------------------------------
# 1. STATEMENT - Rich atmosphere, perfect balance
# -----------------------------------------------------------------------------
TEMPLATES["statement"] = {
    "html": """<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;450;500;600;700;800&display=swap" rel="stylesheet">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: 'Inter', -apple-system, sans-serif;
  width: 1080px;
  height: 1080px;
  background: #08080a;
  position: relative;
  overflow: hidden;
}

/* Rich layered gradient mesh */
.mesh {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse 120% 80% at 70% 60%, rgba(139, 92, 246, 0.12) 0%, transparent 50%),
    radial-gradient(ellipse 80% 100% at 10% 80%, rgba(236, 72, 153, 0.08) 0%, transparent 50%),
    radial-gradient(ellipse 60% 60% at 90% 20%, rgba(59, 130, 246, 0.06) 0%, transparent 50%);
}

/* Subtle grain */
.grain {
  position: absolute;
  inset: 0;
  opacity: 0.025;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}

/* Decorative line */
.deco-line {
  position: absolute;
  top: 64px;
  left: 64px;
  right: 64px;
  height: 1px;
  background: linear-gradient(90deg, rgba(139, 92, 246, 0.3) 0%, rgba(255,255,255,0.05) 50%, transparent 100%);
}

.content {
  position: relative;
  z-index: 2;
  height: 100%;
  padding: 64px;
  display: flex;
  flex-direction: column;
}

.top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 24px;
}

.label {
  font-size: 11px;
  font-weight: 600;
  color: rgba(255,255,255,0.35);
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.label-accent {
  color: #a78bfa;
}

.main {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 40px 0;
}

.headline {
  font-size: 82px;
  font-weight: 700;
  color: #fafafa;
  line-height: 1.02;
  letter-spacing: -0.035em;
  margin-bottom: 28px;
}

.headline .muted {
  color: rgba(255,255,255,0.35);
}

.headline .accent {
  background: linear-gradient(135deg, #a78bfa 0%, #c084fc 50%, #e879f9 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.subline {
  font-size: 18px;
  font-weight: 450;
  color: rgba(255,255,255,0.45);
  max-width: 440px;
  line-height: 1.65;
  letter-spacing: -0.01em;
}

.bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 32px;
  border-top: 1px solid rgba(255,255,255,0.06);
}

.author {
  display: flex;
  align-items: center;
  gap: 14px;
}

.avatar {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  background: linear-gradient(135deg, #8b5cf6, #a78bfa);
  box-shadow: 0 4px 12px rgba(139, 92, 246, 0.3);
}

.author-name {
  font-size: 14px;
  font-weight: 600;
  color: rgba(255,255,255,0.9);
  margin-bottom: 2px;
}
.author-role {
  font-size: 13px;
  font-weight: 450;
  color: rgba(255,255,255,0.4);
}

.cta {
  display: flex;
  align-items: center;
  gap: 10px;
  background: linear-gradient(135deg, rgba(139, 92, 246, 0.2) 0%, rgba(168, 85, 247, 0.1) 100%);
  border: 1px solid rgba(139, 92, 246, 0.25);
  color: #c4b5fd;
  font-size: 14px;
  font-weight: 600;
  padding: 14px 24px;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(139, 92, 246, 0.15);
}
.cta svg {
  width: 16px;
  height: 16px;
  stroke: currentColor;
  fill: none;
  stroke-width: 2;
}

/* Corner accents */
.corner-tl, .corner-br {
  position: absolute;
  width: 80px;
  height: 80px;
  border: 1px solid rgba(255,255,255,0.04);
}
.corner-tl {
  top: 48px;
  left: 48px;
  border-right: none;
  border-bottom: none;
}
.corner-br {
  bottom: 48px;
  right: 48px;
  border-left: none;
  border-top: none;
}
</style>
</head>
<body>
  <div class="mesh"></div>
  <div class="grain"></div>
  <div class="deco-line"></div>
  <div class="corner-tl"></div>
  <div class="corner-br"></div>

  <div class="content">
    <div class="top">
      <div class="label"><span class="label-accent">●</span>&nbsp;&nbsp;Insight</div>
      <div class="label">01 / 12</div>
    </div>

    <div class="main">
      <h1 class="headline">
        <span class="muted">Stop building</span><br>
        <span class="accent">features.</span>
      </h1>
      <p class="subline">
        Start solving problems. The best products aren't feature-rich—they're focused on what matters.
      </p>
    </div>

    <div class="bottom">
      <div class="author">
        <div class="avatar"></div>
        <div>
          <div class="author-name">Alex Chen</div>
          <div class="author-role">Product Lead at Scale</div>
        </div>
      </div>
      <div class="cta">
        Continue reading
        <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
      </div>
    </div>
  </div>
</body>
</html>""",
    "dimensions": (1080, 1080)
}

# -----------------------------------------------------------------------------
# 2. METRIC - Data visualization excellence
# -----------------------------------------------------------------------------
TEMPLATES["metric"] = {
    "html": """<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;450;500;600;700;800&display=swap" rel="stylesheet">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: 'Inter', -apple-system, sans-serif;
  width: 1080px;
  height: 1080px;
  background: #050506;
  position: relative;
  overflow: hidden;
}

/* Rich green-tinted atmosphere */
.mesh {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse 100% 80% at 0% 40%, rgba(34, 197, 94, 0.1) 0%, transparent 50%),
    radial-gradient(ellipse 80% 100% at 100% 100%, rgba(16, 185, 129, 0.06) 0%, transparent 50%);
}

/* Grid pattern */
.grid {
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px);
  background-size: 40px 40px;
  mask-image: radial-gradient(ellipse 80% 80% at 50% 50%, black, transparent);
}

.content {
  position: relative;
  z-index: 2;
  height: 100%;
  padding: 56px;
  display: flex;
  flex-direction: column;
}

.top {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.status {
  display: flex;
  align-items: center;
  gap: 10px;
}

.status-dot {
  width: 8px;
  height: 8px;
  background: #22c55e;
  border-radius: 50%;
  box-shadow: 0 0 12px rgba(34, 197, 94, 0.8), 0 0 24px rgba(34, 197, 94, 0.4);
}

.status-text {
  font-size: 12px;
  font-weight: 600;
  color: #4ade80;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.timestamp {
  font-size: 12px;
  font-weight: 500;
  color: rgba(255,255,255,0.3);
}

.main {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.metric-row {
  display: flex;
  align-items: baseline;
  gap: 8px;
  margin-bottom: 12px;
}

.metric-value {
  font-size: 200px;
  font-weight: 700;
  color: #fafafa;
  line-height: 0.85;
  letter-spacing: -0.04em;
}

.metric-unit {
  font-size: 64px;
  font-weight: 600;
  color: #22c55e;
}

.metric-label {
  font-size: 24px;
  font-weight: 500;
  color: rgba(255,255,255,0.5);
  margin-bottom: 20px;
  letter-spacing: -0.01em;
}

.metric-context {
  font-size: 16px;
  font-weight: 450;
  color: rgba(255,255,255,0.35);
  max-width: 380px;
  line-height: 1.6;
}

/* Chart area */
.chart-area {
  position: absolute;
  right: 56px;
  top: 50%;
  transform: translateY(-50%);
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 16px;
}

.chart {
  display: flex;
  align-items: flex-end;
  gap: 8px;
  height: 120px;
}

.bar {
  width: 16px;
  background: rgba(34, 197, 94, 0.15);
  border-radius: 4px;
  transition: all 0.3s;
}

.bar.highlight {
  background: linear-gradient(180deg, #22c55e 0%, rgba(34, 197, 94, 0.3) 100%);
  box-shadow: 0 4px 16px rgba(34, 197, 94, 0.3);
}

.chart-label {
  font-size: 11px;
  font-weight: 600;
  color: rgba(255,255,255,0.3);
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

.bottom {
  display: flex;
  gap: 56px;
  padding-top: 32px;
  border-top: 1px solid rgba(255,255,255,0.06);
}

.stat {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.stat-value {
  font-size: 32px;
  font-weight: 700;
  color: rgba(255,255,255,0.9);
  letter-spacing: -0.02em;
}

.stat-label {
  font-size: 12px;
  font-weight: 500;
  color: rgba(255,255,255,0.35);
  letter-spacing: 0.02em;
}

.stat-change {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 13px;
  font-weight: 600;
  color: #4ade80;
  background: rgba(34, 197, 94, 0.1);
  padding: 4px 10px;
  border-radius: 6px;
  margin-top: 6px;
}
</style>
</head>
<body>
  <div class="mesh"></div>
  <div class="grid"></div>

  <div class="content">
    <div class="top">
      <div class="status">
        <div class="status-dot"></div>
        <div class="status-text">Live</div>
      </div>
      <div class="timestamp">Updated 2 min ago</div>
    </div>

    <div class="main">
      <div class="metric-row">
        <div class="metric-value">93</div>
        <div class="metric-unit">%</div>
      </div>
      <div class="metric-label">Customer satisfaction</div>
      <p class="metric-context">Highest score in company history. Up 26 points from last quarter.</p>
    </div>

    <div class="chart-area">
      <div class="chart">
        <div class="bar" style="height: 30%"></div>
        <div class="bar" style="height: 40%"></div>
        <div class="bar" style="height: 35%"></div>
        <div class="bar" style="height: 50%"></div>
        <div class="bar" style="height: 55%"></div>
        <div class="bar" style="height: 67%"></div>
        <div class="bar highlight" style="height: 93%"></div>
      </div>
      <div class="chart-label">Q1–Q4 Trend</div>
    </div>

    <div class="bottom">
      <div class="stat">
        <div class="stat-value">2.4M</div>
        <div class="stat-label">Responses</div>
      </div>
      <div class="stat">
        <div class="stat-value">4.8</div>
        <div class="stat-label">Avg Rating</div>
        <div class="stat-change">↑ 0.6</div>
      </div>
      <div class="stat">
        <div class="stat-value">98%</div>
        <div class="stat-label">Would recommend</div>
      </div>
    </div>
  </div>
</body>
</html>""",
    "dimensions": (1080, 1080)
}

# -----------------------------------------------------------------------------
# 3. COMPARISON - Editorial split
# -----------------------------------------------------------------------------
TEMPLATES["comparison"] = {
    "html": """<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;450;500;600;700;800&display=swap" rel="stylesheet">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: 'Inter', -apple-system, sans-serif;
  width: 1080px;
  height: 1350px;
  background: #08080a;
  position: relative;
  overflow: hidden;
}

.header {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  padding: 48px 56px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 10;
}

.header-label {
  font-size: 11px;
  font-weight: 600;
  color: rgba(255,255,255,0.4);
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.panels {
  display: flex;
  height: 100%;
}

.panel {
  flex: 1;
  padding: 140px 48px 48px;
  display: flex;
  flex-direction: column;
  position: relative;
}

.panel-before {
  background: linear-gradient(180deg, #0c0c0e 0%, #08080a 100%);
}

.panel-after {
  background: linear-gradient(135deg, rgba(34, 197, 94, 0.08) 0%, rgba(16, 185, 129, 0.03) 100%);
  border-left: 1px solid rgba(34, 197, 94, 0.15);
}

/* Subtle pattern on before panel */
.panel-before::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: radial-gradient(circle at 1px 1px, rgba(255,255,255,0.03) 1px, transparent 0);
  background-size: 32px 32px;
}

.panel-tag {
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  margin-bottom: 48px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.panel-before .panel-tag {
  color: rgba(255,255,255,0.3);
}

.panel-after .panel-tag {
  color: #4ade80;
}

.panel-tag::before {
  content: '';
  width: 24px;
  height: 1px;
}

.panel-before .panel-tag::before {
  background: rgba(255,255,255,0.15);
}

.panel-after .panel-tag::before {
  background: #22c55e;
}

.panel-main {
  flex: 1;
  position: relative;
  z-index: 2;
}

.panel-number {
  font-size: 140px;
  font-weight: 800;
  line-height: 1;
  letter-spacing: -0.04em;
  margin-bottom: 4px;
}

.panel-before .panel-number {
  color: rgba(255,255,255,0.5);
}

.panel-after .panel-number {
  color: #fafafa;
}

.panel-unit {
  font-size: 20px;
  font-weight: 600;
  color: rgba(255,255,255,0.4);
  margin-bottom: 40px;
}

.panel-title {
  font-size: 22px;
  font-weight: 700;
  color: rgba(255,255,255,0.9);
  margin-bottom: 12px;
  letter-spacing: -0.02em;
}

.panel-desc {
  font-size: 15px;
  font-weight: 450;
  color: rgba(255,255,255,0.4);
  line-height: 1.6;
  margin-bottom: 32px;
}

.panel-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.panel-item {
  display: flex;
  align-items: center;
  gap: 14px;
  font-size: 14px;
  font-weight: 500;
}

.panel-before .panel-item {
  color: rgba(255,255,255,0.35);
}

.panel-after .panel-item {
  color: rgba(255,255,255,0.7);
}

.panel-item-icon {
  width: 20px;
  height: 20px;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.panel-before .panel-item-icon {
  background: rgba(239, 68, 68, 0.1);
}

.panel-before .panel-item-icon svg {
  width: 12px;
  height: 12px;
  stroke: #f87171;
  fill: none;
  stroke-width: 2.5;
}

.panel-after .panel-item-icon {
  background: rgba(34, 197, 94, 0.15);
}

.panel-after .panel-item-icon svg {
  width: 12px;
  height: 12px;
  stroke: #4ade80;
  fill: none;
  stroke-width: 2.5;
}

.panel-footer {
  padding-top: 32px;
  border-top: 1px solid rgba(255,255,255,0.06);
  font-size: 12px;
  font-weight: 600;
  color: rgba(255,255,255,0.3);
  letter-spacing: 0.05em;
  text-transform: uppercase;
}

/* Center badge */
.badge {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
  color: #052e16;
  font-size: 15px;
  font-weight: 800;
  padding: 18px 32px;
  border-radius: 100px;
  box-shadow:
    0 8px 32px rgba(34, 197, 94, 0.4),
    0 0 0 1px rgba(255,255,255,0.1) inset;
  z-index: 20;
  letter-spacing: -0.01em;
}
</style>
</head>
<body>
  <div class="header">
    <div class="header-label">Comparison</div>
    <div class="header-label">Time to Ship</div>
  </div>

  <div class="panels">
    <div class="panel panel-before">
      <div class="panel-tag">Without</div>
      <div class="panel-main">
        <div class="panel-number">6</div>
        <div class="panel-unit">months average</div>
        <div class="panel-title">Drowning in process</div>
        <p class="panel-desc">Manual coordination, endless meetings, context switching between tools.</p>
        <div class="panel-list">
          <div class="panel-item">
            <div class="panel-item-icon"><svg viewBox="0 0 24 24"><path d="M18 6L6 18M6 6l12 12"/></svg></div>
            Slow feedback loops
          </div>
          <div class="panel-item">
            <div class="panel-item-icon"><svg viewBox="0 0 24 24"><path d="M18 6L6 18M6 6l12 12"/></svg></div>
            High coordination cost
          </div>
          <div class="panel-item">
            <div class="panel-item-icon"><svg viewBox="0 0 24 24"><path d="M18 6L6 18M6 6l12 12"/></svg></div>
            Team burnout
          </div>
        </div>
      </div>
      <div class="panel-footer">Industry Average</div>
    </div>

    <div class="panel panel-after">
      <div class="panel-tag">With Platform</div>
      <div class="panel-main">
        <div class="panel-number">6</div>
        <div class="panel-unit">weeks average</div>
        <div class="panel-title">Focused on shipping</div>
        <p class="panel-desc">Automated workflows, async collaboration, instant deployments.</p>
        <div class="panel-list">
          <div class="panel-item">
            <div class="panel-item-icon"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>
            Real-time feedback
          </div>
          <div class="panel-item">
            <div class="panel-item-icon"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>
            Zero coordination tax
          </div>
          <div class="panel-item">
            <div class="panel-item-icon"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>
            Teams love it
          </div>
        </div>
      </div>
      <div class="panel-footer">Our Customers</div>
    </div>
  </div>

  <div class="badge">4× Faster</div>
</body>
</html>""",
    "dimensions": (1080, 1350)
}

# -----------------------------------------------------------------------------
# 4. FEATURES - No dead space, full utilization
# -----------------------------------------------------------------------------
TEMPLATES["features"] = {
    "html": """<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;450;500;600;700;800&display=swap" rel="stylesheet">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: 'Inter', -apple-system, sans-serif;
  width: 1080px;
  height: 1350px;
  background: #07070a;
  position: relative;
  overflow: hidden;
}

.mesh {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse 100% 60% at 50% 0%, rgba(99, 102, 241, 0.1) 0%, transparent 50%),
    radial-gradient(ellipse 80% 80% at 100% 100%, rgba(139, 92, 246, 0.06) 0%, transparent 50%);
}

.content {
  position: relative;
  z-index: 2;
  height: 100%;
  padding: 56px;
  display: flex;
  flex-direction: column;
}

.header {
  text-align: center;
  margin-bottom: 40px;
}

.header-tag {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  font-weight: 700;
  color: #818cf8;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin-bottom: 20px;
}

.header-tag::before, .header-tag::after {
  content: '';
  width: 20px;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(129, 140, 248, 0.5));
}

.header-tag::after {
  background: linear-gradient(90deg, rgba(129, 140, 248, 0.5), transparent);
}

.header-title {
  font-size: 44px;
  font-weight: 700;
  color: #fafafa;
  letter-spacing: -0.03em;
  margin-bottom: 12px;
  line-height: 1.1;
}

.header-sub {
  font-size: 17px;
  font-weight: 450;
  color: rgba(255,255,255,0.45);
}

.cards {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.card {
  flex: 1;
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(255,255,255,0.05);
  border-radius: 20px;
  padding: 28px 32px;
  display: flex;
  align-items: center;
  gap: 24px;
  transition: all 0.2s;
}

.card:hover {
  border-color: rgba(129, 140, 248, 0.2);
  background: rgba(129, 140, 248, 0.03);
}

.card-icon {
  width: 56px;
  height: 56px;
  background: linear-gradient(135deg, rgba(99, 102, 241, 0.15) 0%, rgba(139, 92, 246, 0.08) 100%);
  border: 1px solid rgba(99, 102, 241, 0.1);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.card-icon svg {
  width: 26px;
  height: 26px;
  stroke: #a5b4fc;
  fill: none;
  stroke-width: 1.5;
}

.card-body {
  flex: 1;
  min-width: 0;
}

.card-step {
  font-size: 11px;
  font-weight: 700;
  color: rgba(255,255,255,0.25);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 6px;
}

.card-title {
  font-size: 20px;
  font-weight: 600;
  color: rgba(255,255,255,0.9);
  margin-bottom: 6px;
  letter-spacing: -0.01em;
}

.card-desc {
  font-size: 14px;
  font-weight: 450;
  color: rgba(255,255,255,0.4);
  line-height: 1.5;
}

.card-stat {
  text-align: right;
  flex-shrink: 0;
  padding-left: 24px;
  border-left: 1px solid rgba(255,255,255,0.06);
}

.card-stat-value {
  font-size: 28px;
  font-weight: 700;
  color: #818cf8;
  margin-bottom: 2px;
  letter-spacing: -0.02em;
}

.card-stat-label {
  font-size: 11px;
  font-weight: 500;
  color: rgba(255,255,255,0.3);
  letter-spacing: 0.02em;
}

.footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 32px;
  margin-top: 16px;
  border-top: 1px solid rgba(255,255,255,0.06);
}

.footer-stats {
  display: flex;
  gap: 40px;
}

.footer-stat {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.footer-stat-value {
  font-size: 24px;
  font-weight: 700;
  color: rgba(255,255,255,0.9);
}

.footer-stat-label {
  font-size: 12px;
  font-weight: 500;
  color: rgba(255,255,255,0.35);
}

.cta {
  display: flex;
  align-items: center;
  gap: 10px;
  background: #6366f1;
  color: #fff;
  font-size: 15px;
  font-weight: 600;
  padding: 16px 32px;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(99, 102, 241, 0.35);
}

.cta svg {
  width: 18px;
  height: 18px;
  stroke: currentColor;
  fill: none;
  stroke-width: 2;
}
</style>
</head>
<body>
  <div class="mesh"></div>

  <div class="content">
    <div class="header">
      <div class="header-tag">Platform</div>
      <h1 class="header-title">Everything you need<br>to ship faster</h1>
      <p class="header-sub">Three layers of intelligence, one platform.</p>
    </div>

    <div class="cards">
      <div class="card">
        <div class="card-icon">
          <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
        </div>
        <div class="card-body">
          <div class="card-step">Step 01</div>
          <div class="card-title">Connect your data sources</div>
          <div class="card-desc">One-click integrations with 200+ tools. Real-time sync, zero configuration required.</div>
        </div>
        <div class="card-stat">
          <div class="card-stat-value">200+</div>
          <div class="card-stat-label">Integrations</div>
        </div>
      </div>

      <div class="card">
        <div class="card-icon">
          <svg viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
        </div>
        <div class="card-body">
          <div class="card-step">Step 02</div>
          <div class="card-title">AI-powered analysis</div>
          <div class="card-desc">ML models automatically surface patterns, anomalies, and opportunities in your data.</div>
        </div>
        <div class="card-stat">
          <div class="card-stat-value">&lt;1s</div>
          <div class="card-stat-label">Analysis</div>
        </div>
      </div>

      <div class="card">
        <div class="card-icon">
          <svg viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
        </div>
        <div class="card-body">
          <div class="card-step">Step 03</div>
          <div class="card-title">Deploy with confidence</div>
          <div class="card-desc">Ship to production in seconds. Automatic rollbacks, zero-downtime deployments.</div>
        </div>
        <div class="card-stat">
          <div class="card-stat-value">50+</div>
          <div class="card-stat-label">Regions</div>
        </div>
      </div>
    </div>

    <div class="footer">
      <div class="footer-stats">
        <div class="footer-stat">
          <div class="footer-stat-value">10,000+</div>
          <div class="footer-stat-label">Teams using</div>
        </div>
        <div class="footer-stat">
          <div class="footer-stat-value">99.99%</div>
          <div class="footer-stat-label">Uptime SLA</div>
        </div>
      </div>
      <div class="cta">
        Start building
        <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
      </div>
    </div>
  </div>
</body>
</html>""",
    "dimensions": (1080, 1350)
}

# -----------------------------------------------------------------------------
# 5. TESTIMONIAL - Refined elegance
# -----------------------------------------------------------------------------
TEMPLATES["testimonial"] = {
    "html": """<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;450;500;600;700&family=Newsreader:ital,wght@0,400;0,500;1,400;1,500&display=swap" rel="stylesheet">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: 'Inter', -apple-system, sans-serif;
  width: 1080px;
  height: 1080px;
  background: #0a0a0c;
  position: relative;
  overflow: hidden;
}

/* Warm gradient mesh */
.mesh {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse 100% 80% at 20% 30%, rgba(251, 191, 36, 0.08) 0%, transparent 50%),
    radial-gradient(ellipse 60% 80% at 80% 80%, rgba(245, 158, 11, 0.04) 0%, transparent 50%);
}

/* Large quote mark */
.quote-deco {
  position: absolute;
  top: 80px;
  left: 56px;
  font-family: 'Newsreader', Georgia, serif;
  font-size: 280px;
  font-weight: 400;
  color: rgba(251, 191, 36, 0.1);
  line-height: 1;
  pointer-events: none;
}

/* Accent line */
.accent-line {
  position: absolute;
  left: 56px;
  top: 240px;
  bottom: 240px;
  width: 2px;
  background: linear-gradient(180deg, #fbbf24 0%, rgba(251, 191, 36, 0.1) 100%);
  border-radius: 1px;
}

.content {
  position: relative;
  z-index: 2;
  height: 100%;
  padding: 56px;
  display: flex;
  flex-direction: column;
}

.top {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.label {
  font-size: 11px;
  font-weight: 600;
  color: #fbbf24;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.company-badge {
  font-size: 12px;
  font-weight: 600;
  color: rgba(255,255,255,0.3);
  letter-spacing: 0.05em;
}

.quote-section {
  flex: 1;
  display: flex;
  align-items: center;
  padding: 60px 0 60px 40px;
}

.quote {
  font-family: 'Newsreader', Georgia, serif;
  font-size: 38px;
  font-weight: 400;
  font-style: italic;
  color: rgba(255,255,255,0.9);
  line-height: 1.45;
  letter-spacing: -0.01em;
  max-width: 820px;
}

.quote .highlight {
  color: #fcd34d;
  font-style: normal;
  font-weight: 500;
}

.bottom {
  display: flex;
  align-items: center;
  gap: 20px;
  padding-top: 32px;
  border-top: 1px solid rgba(255,255,255,0.06);
}

.avatar {
  width: 56px;
  height: 56px;
  border-radius: 14px;
  background: linear-gradient(135deg, #fbbf24, #f59e0b);
  box-shadow: 0 4px 16px rgba(251, 191, 36, 0.3);
}

.author-info {
  flex: 1;
}

.author-name {
  font-size: 17px;
  font-weight: 600;
  color: rgba(255,255,255,0.9);
  margin-bottom: 4px;
}

.author-role {
  font-size: 14px;
  font-weight: 450;
  color: rgba(255,255,255,0.4);
}

.company-logo {
  font-size: 22px;
  font-weight: 700;
  color: rgba(255,255,255,0.12);
  letter-spacing: -0.02em;
}

/* 5-star rating */
.rating {
  position: absolute;
  bottom: 56px;
  right: 56px;
  display: flex;
  gap: 4px;
}

.star {
  width: 20px;
  height: 20px;
  fill: #fbbf24;
}
</style>
</head>
<body>
  <div class="mesh"></div>
  <div class="quote-deco">"</div>
  <div class="accent-line"></div>

  <div class="content">
    <div class="top">
      <div class="label">Customer Story</div>
      <div class="company-badge">ACME INC</div>
    </div>

    <div class="quote-section">
      <p class="quote">
        This platform <span class="highlight">fundamentally changed</span> how our team ships product. We went from quarterly releases to weekly—and our engineers are happier than ever.
      </p>
    </div>

    <div class="bottom">
      <div class="avatar"></div>
      <div class="author-info">
        <div class="author-name">Sarah Mitchell</div>
        <div class="author-role">VP of Engineering, Acme Inc</div>
      </div>
      <div class="company-logo">ACME</div>
    </div>
  </div>

  <div class="rating">
    <svg class="star" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
    <svg class="star" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
    <svg class="star" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
    <svg class="star" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
    <svg class="star" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  </div>
</body>
</html>""",
    "dimensions": (1080, 1080)
}

# -----------------------------------------------------------------------------
# 6. ANNOUNCEMENT - Sophisticated celebration
# -----------------------------------------------------------------------------
TEMPLATES["announcement"] = {
    "html": """<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;450;500;600;700;800&display=swap" rel="stylesheet">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: 'Inter', -apple-system, sans-serif;
  width: 1080px;
  height: 1080px;
  background: linear-gradient(150deg, #0c1445 0%, #080d2e 40%, #060818 100%);
  position: relative;
  overflow: hidden;
}

/* Radial glows */
.glow-1 {
  position: absolute;
  width: 800px;
  height: 800px;
  background: radial-gradient(circle, rgba(99, 102, 241, 0.15) 0%, transparent 60%);
  top: -300px;
  right: -200px;
}

.glow-2 {
  position: absolute;
  width: 500px;
  height: 500px;
  background: radial-gradient(circle, rgba(34, 197, 94, 0.1) 0%, transparent 60%);
  bottom: -150px;
  left: -100px;
}

/* Subtle grid */
.grid {
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px);
  background-size: 48px 48px;
}

/* Floating orbs */
.orb {
  position: absolute;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.02) 100%);
  border: 1px solid rgba(255,255,255,0.05);
}

.orb-1 { width: 120px; height: 120px; top: 15%; left: 10%; }
.orb-2 { width: 80px; height: 80px; bottom: 25%; right: 15%; }
.orb-3 { width: 40px; height: 40px; top: 30%; right: 25%; }

.content {
  position: relative;
  z-index: 2;
  height: 100%;
  padding: 56px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.badge {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: rgba(34, 197, 94, 0.1);
  border: 1px solid rgba(34, 197, 94, 0.2);
  padding: 12px 24px;
  border-radius: 100px;
  font-size: 12px;
  font-weight: 700;
  color: #4ade80;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 40px;
}

.badge-dot {
  width: 8px;
  height: 8px;
  background: #22c55e;
  border-radius: 50%;
  box-shadow: 0 0 12px rgba(34, 197, 94, 0.8);
}

.headline {
  font-size: 110px;
  font-weight: 800;
  color: #fafafa;
  line-height: 1;
  letter-spacing: -0.04em;
  margin-bottom: 24px;
}

.headline .accent {
  background: linear-gradient(135deg, #22c55e 0%, #4ade80 50%, #86efac 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.subline {
  font-size: 20px;
  font-weight: 450;
  color: rgba(255,255,255,0.55);
  max-width: 500px;
  line-height: 1.6;
  margin-bottom: 48px;
}

.cta {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  background: #fafafa;
  color: #0c1445;
  font-size: 16px;
  font-weight: 700;
  padding: 20px 40px;
  border-radius: 14px;
  box-shadow:
    0 8px 32px rgba(0, 0, 0, 0.3),
    0 0 0 1px rgba(255,255,255,0.1) inset;
}

.cta svg {
  width: 20px;
  height: 20px;
  stroke: currentColor;
  fill: none;
  stroke-width: 2;
}

.footer {
  position: absolute;
  bottom: 56px;
  left: 56px;
  right: 56px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 15px;
  font-weight: 700;
  color: rgba(255,255,255,0.7);
  letter-spacing: -0.01em;
}

.date {
  font-size: 13px;
  font-weight: 500;
  color: rgba(255,255,255,0.35);
}

/* Corner accents */
.corner {
  position: absolute;
  width: 100px;
  height: 100px;
}

.corner-tl {
  top: 40px;
  left: 40px;
  border-top: 1px solid rgba(255,255,255,0.08);
  border-left: 1px solid rgba(255,255,255,0.08);
}

.corner-br {
  bottom: 40px;
  right: 40px;
  border-bottom: 1px solid rgba(255,255,255,0.08);
  border-right: 1px solid rgba(255,255,255,0.08);
}
</style>
</head>
<body>
  <div class="glow-1"></div>
  <div class="glow-2"></div>
  <div class="grid"></div>
  <div class="orb orb-1"></div>
  <div class="orb orb-2"></div>
  <div class="orb orb-3"></div>
  <div class="corner corner-tl"></div>
  <div class="corner corner-br"></div>

  <div class="content">
    <div class="badge">
      <span class="badge-dot"></span>
      Announcement
    </div>
    <h1 class="headline">Series <span class="accent">B</span></h1>
    <p class="subline">$75 million to build the next generation of collaborative intelligence for teams everywhere.</p>
    <a class="cta">
      Read the news
      <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
    </a>
  </div>

  <div class="footer">
    <div class="logo">COMPANY</div>
    <div class="date">January 2025</div>
  </div>
</body>
</html>""",
    "dimensions": (1080, 1080)
}

# -----------------------------------------------------------------------------
# 7. LIST - Clean, scannable, polished
# -----------------------------------------------------------------------------
TEMPLATES["list"] = {
    "html": """<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;450;500;600;700;800&display=swap" rel="stylesheet">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: 'Inter', -apple-system, sans-serif;
  width: 1080px;
  height: 1350px;
  background: #fafafa;
  position: relative;
}

/* Subtle accent bar */
.accent-bar {
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  width: 4px;
  background: linear-gradient(180deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%);
}

/* Background shape */
.bg-shape {
  position: absolute;
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(99, 102, 241, 0.04) 0%, transparent 60%);
  top: -200px;
  right: -200px;
}

.content {
  position: relative;
  z-index: 2;
  height: 100%;
  padding: 56px 56px 56px 64px;
  display: flex;
  flex-direction: column;
}

.header {
  margin-bottom: 40px;
}

.header-tag {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  font-weight: 700;
  color: #6366f1;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin-bottom: 20px;
}

.header-tag::before {
  content: '';
  width: 16px;
  height: 2px;
  background: #6366f1;
  border-radius: 1px;
}

.header-title {
  font-size: 42px;
  font-weight: 700;
  color: #18181b;
  line-height: 1.15;
  letter-spacing: -0.03em;
}

.list {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.item {
  flex: 1;
  display: flex;
  gap: 24px;
  padding: 24px 0;
  border-bottom: 1px solid rgba(0,0,0,0.06);
  align-items: flex-start;
}

.item:last-child {
  border-bottom: none;
}

.item-number {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 15px;
  font-weight: 700;
  color: #fff;
  flex-shrink: 0;
  box-shadow: 0 4px 12px rgba(99, 102, 241, 0.25);
}

.item-content {
  flex: 1;
  padding-top: 6px;
}

.item-title {
  font-size: 19px;
  font-weight: 600;
  color: #18181b;
  margin-bottom: 6px;
  letter-spacing: -0.01em;
}

.item-desc {
  font-size: 15px;
  font-weight: 450;
  color: #71717a;
  line-height: 1.5;
}

.footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 28px;
  border-top: 2px solid #18181b;
}

.author {
  display: flex;
  align-items: center;
  gap: 14px;
}

.avatar {
  width: 48px;
  height: 48px;
  border-radius: 14px;
  background: linear-gradient(135deg, #18181b, #3f3f46);
}

.author-name {
  font-size: 15px;
  font-weight: 600;
  color: #18181b;
}

.author-handle {
  font-size: 14px;
  font-weight: 450;
  color: #a1a1aa;
}

.action {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  font-weight: 600;
  color: #6366f1;
  background: rgba(99, 102, 241, 0.08);
  padding: 12px 24px;
  border-radius: 10px;
}

.action svg {
  width: 18px;
  height: 18px;
  stroke: currentColor;
  fill: none;
  stroke-width: 2;
}
</style>
</head>
<body>
  <div class="accent-bar"></div>
  <div class="bg-shape"></div>

  <div class="content">
    <div class="header">
      <div class="header-tag">Playbook</div>
      <h1 class="header-title">5 lessons from scaling<br>to 10M users</h1>
    </div>

    <div class="list">
      <div class="item">
        <div class="item-number">1</div>
        <div class="item-content">
          <div class="item-title">Focus beats features</div>
          <div class="item-desc">The products that win do fewer things exceptionally well.</div>
        </div>
      </div>

      <div class="item">
        <div class="item-number">2</div>
        <div class="item-content">
          <div class="item-title">Ship weekly, not quarterly</div>
          <div class="item-desc">Small, frequent releases compound faster than big launches.</div>
        </div>
      </div>

      <div class="item">
        <div class="item-number">3</div>
        <div class="item-content">
          <div class="item-title">Talk to users every day</div>
          <div class="item-desc">Data shows what's happening. Conversations show why.</div>
        </div>
      </div>

      <div class="item">
        <div class="item-number">4</div>
        <div class="item-content">
          <div class="item-title">Hire for slope, not intercept</div>
          <div class="item-desc">Growth potential matters more than current skill level.</div>
        </div>
      </div>

      <div class="item">
        <div class="item-number">5</div>
        <div class="item-content">
          <div class="item-title">Protect maker time ruthlessly</div>
          <div class="item-desc">Deep work is the only way to build something exceptional.</div>
        </div>
      </div>
    </div>

    <div class="footer">
      <div class="author">
        <div class="avatar"></div>
        <div>
          <div class="author-name">Jordan Chen</div>
          <div class="author-handle">@jordanbuilds</div>
        </div>
      </div>
      <div class="action">
        <svg viewBox="0 0 24 24"><path d="M19 21l-7-5-7 5V5a2 2 0 012-2h10a2 2 0 012 2z"/></svg>
        Save post
      </div>
    </div>
  </div>
</body>
</html>""",
    "dimensions": (1080, 1350)
}

# -----------------------------------------------------------------------------
# 8. PRODUCT - Feature launch, premium feel
# -----------------------------------------------------------------------------
TEMPLATES["product"] = {
    "html": """<!DOCTYPE html>
<html>
<head>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;450;500;600;700;800&display=swap" rel="stylesheet">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: 'Inter', -apple-system, sans-serif;
  width: 1080px;
  height: 1080px;
  background: #fafafa;
  position: relative;
  overflow: hidden;
}

/* Gradient shape */
.bg-gradient {
  position: absolute;
  width: 900px;
  height: 900px;
  background: radial-gradient(circle, rgba(99, 102, 241, 0.06) 0%, transparent 60%);
  top: -400px;
  right: -400px;
}

/* Grid pattern */
.grid {
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(0,0,0,0.02) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,0,0,0.02) 1px, transparent 1px);
  background-size: 40px 40px;
  mask-image: linear-gradient(180deg, black 0%, transparent 60%);
}

.content {
  position: relative;
  z-index: 2;
  height: 100%;
  padding: 56px;
  display: flex;
  flex-direction: column;
}

.top {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 15px;
  font-weight: 700;
  color: #18181b;
}

.badge {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 11px;
  font-weight: 700;
  color: #6366f1;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  background: rgba(99, 102, 241, 0.08);
  padding: 10px 18px;
  border-radius: 8px;
}

.badge::before {
  content: '';
  width: 6px;
  height: 6px;
  background: #6366f1;
  border-radius: 50%;
}

.main {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.icon-row {
  margin-bottom: 32px;
}

.icon-box {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #18181b 0%, #27272a 100%);
  border-radius: 22px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow:
    0 8px 32px rgba(0, 0, 0, 0.15),
    0 0 0 1px rgba(255,255,255,0.1) inset;
}

.icon-box svg {
  width: 36px;
  height: 36px;
  stroke: #fafafa;
  fill: none;
  stroke-width: 1.5;
}

.title {
  font-size: 56px;
  font-weight: 700;
  color: #18181b;
  line-height: 1.08;
  letter-spacing: -0.03em;
  margin-bottom: 20px;
  max-width: 600px;
}

.description {
  font-size: 19px;
  font-weight: 450;
  color: #71717a;
  line-height: 1.6;
  max-width: 480px;
  margin-bottom: 36px;
}

.cta {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  background: linear-gradient(135deg, #18181b 0%, #27272a 100%);
  color: #fafafa;
  font-size: 16px;
  font-weight: 600;
  padding: 18px 36px;
  border-radius: 14px;
  width: fit-content;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
}

.cta svg {
  width: 20px;
  height: 20px;
  stroke: currentColor;
  fill: none;
  stroke-width: 2;
}

.bottom {
  display: flex;
  gap: 56px;
  padding-top: 32px;
  border-top: 1px solid rgba(0,0,0,0.08);
}

.stat {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.stat-value {
  font-size: 36px;
  font-weight: 700;
  color: #18181b;
  letter-spacing: -0.02em;
}

.stat-label {
  font-size: 13px;
  font-weight: 500;
  color: #a1a1aa;
}

/* Feature tags */
.feature-tags {
  position: absolute;
  right: 56px;
  top: 50%;
  transform: translateY(-50%);
  display: flex;
  flex-direction: column;
  gap: 12px;
  align-items: flex-end;
}

.feature-tag {
  display: flex;
  align-items: center;
  gap: 10px;
  background: #fff;
  border: 1px solid rgba(0,0,0,0.08);
  padding: 14px 20px;
  border-radius: 12px;
  font-size: 14px;
  font-weight: 500;
  color: #3f3f46;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}

.feature-tag svg {
  width: 18px;
  height: 18px;
  stroke: #6366f1;
  fill: none;
  stroke-width: 2;
}
</style>
</head>
<body>
  <div class="bg-gradient"></div>
  <div class="grid"></div>

  <div class="content">
    <div class="top">
      <div class="logo">COMPANY</div>
      <div class="badge">New Feature</div>
    </div>

    <div class="main">
      <div class="icon-row">
        <div class="icon-box">
          <svg viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
        </div>
      </div>
      <h1 class="title">Deploy to any cloud in seconds</h1>
      <p class="description">One-click deployment to AWS, GCP, or Azure. Zero configuration. Automatic scaling and instant rollbacks.</p>
      <a class="cta">
        Try it free
        <svg viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
      </a>
    </div>

    <div class="bottom">
      <div class="stat">
        <div class="stat-value">3 sec</div>
        <div class="stat-label">Average deploy</div>
      </div>
      <div class="stat">
        <div class="stat-value">99.99%</div>
        <div class="stat-label">Uptime SLA</div>
      </div>
      <div class="stat">
        <div class="stat-value">50+</div>
        <div class="stat-label">Global regions</div>
      </div>
    </div>
  </div>

  <div class="feature-tags">
    <div class="feature-tag">
      <svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>
      Zero config
    </div>
    <div class="feature-tag">
      <svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>
      Auto-scaling
    </div>
    <div class="feature-tag">
      <svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>
      Instant rollback
    </div>
  </div>
</body>
</html>""",
    "dimensions": (1080, 1080)
}


def generate():
    output_dir = "/home/tech_scaile_it/openfigma/exports/premium_v6"
    os.makedirs(output_dir, exist_ok=True)

    with PNGExporter() as exporter:
        for name, template in TEMPLATES.items():
            output_path = os.path.join(output_dir, f"{name}.png")
            exporter.export(template["html"], output_path,
                          width=template["dimensions"][0],
                          height=template["dimensions"][1])
            print(f"✓ {name}")

    print(f"\n✅ V6 Complete: {output_dir}")


if __name__ == "__main__":
    generate()
