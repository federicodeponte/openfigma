# CLAUDE.md - AI Context File

> **Purpose:** This file provides context for AI models (Claude, GPT, etc.) working on this repository.

---

## 🎯 Project Overview

**OpenFigma** - Open-source Figma-style design system for AI/ML pipeline diagrams with Cursor/YC-level aesthetics.

### What This Is
- Self-contained HTML/CSS design templates
- No build tools or frameworks required
- Dark mode, glassmorphism, gradient accents
- Ready-to-use AI pipeline flow diagrams

### What This Is NOT
- Not a React/Vue/Svelte component library
- Not a npm package
- Not a Figma plugin

---

## 📁 Repository Structure

```
openfigma/
├── CLAUDE.md             # This file (AI context)
├── README.md             # User documentation
├── .gitignore
├── diagrams/             # HTML source files (editable)
│   ├── diagram-1-cursor-style.html   # Context Analysis (Brain)
│   ├── diagram-2-cursor-style.html   # Query Distribution (OpenRouter)
│   ├── diagram-3-cursor-style.html   # Data Aggregation (Database)
│   └── diagram-4-cursor-style.html   # Content Generation (Article)
├── exports/              # PNG exports (regenerate after edits)
│   ├── cursor-style-1-brain.png
│   ├── cursor-style-2-openrouter.png
│   ├── cursor-style-3-database.png
│   └── cursor-style-4-article.png
└── assets/               # Additional resources (logos, fonts, etc.)
```

---

## 🎨 Design System

### Color Palette
```css
/* Background */
--bg-primary: #0a0a0b;
--bg-card: rgba(255, 255, 255, 0.03);
--bg-card-hover: rgba(255, 255, 255, 0.05);

/* Borders */
--border-default: rgba(255, 255, 255, 0.06);
--border-hover: rgba(255, 255, 255, 0.1);

/* Text */
--text-primary: #f5f5f5;
--text-muted: rgba(255, 255, 255, 0.4);
--text-subtle: rgba(255, 255, 255, 0.5);

/* Accent Gradients (by step) */
--gradient-purple: linear-gradient(135deg, #6366f1, #8b5cf6);  /* Step 1-2 */
--gradient-green: linear-gradient(135deg, #22c55e, #16a34a);   /* Step 3 */
--gradient-orange: linear-gradient(135deg, #f97316, #ea580c);  /* Step 4 */

/* Status */
--success: #22c55e;
--success-bg: rgba(34, 197, 94, 0.15);
--success-border: rgba(34, 197, 94, 0.3);
```

### Typography
- **Primary font**: Inter (400, 500, 600, 700)
- **Monospace**: SF Mono, Monaco (for model versions)
- **Sizes**: 12px (subtitle), 13px (label), 14px (body), 15px (title), 16px (heading)

### Effects
- **Glassmorphism**: `backdrop-filter: blur(20px)`
- **Glow**: `box-shadow: 0 0 40px rgba(color, 0.3), 0 0 80px rgba(color, 0.15)`
- **Animation**: `pulse` keyframes for connection lines (3s ease-in-out infinite)

---

## 🤖 AI Models (December 2025)

When updating model names, use these latest versions:

| Platform | Model Name | Logo Source |
|----------|------------|-------------|
| Perplexity | `sonar-pro` | Clearbit |
| Google Gemini | `gemini-3.0-pro` | Google Static |
| Claude | `claude-opus-4.5` | Clearbit (Anthropic) |
| Mistral | `mixtral-8x22b` | Inline SVG (pixel grid) |
| ChatGPT | `gpt-5` | Wikipedia Commons |

### Logo URLs
```html
<!-- Perplexity -->
<img src="https://logo.clearbit.com/perplexity.ai">

<!-- Google Gemini -->
<img src="https://www.gstatic.com/lamda/images/gemini_sparkle_v002_d4735304ff6292a690345.svg">

<!-- Claude/Anthropic -->
<img src="https://logo.clearbit.com/anthropic.com">

<!-- ChatGPT -->
<img src="https://upload.wikimedia.org/wikipedia/commons/0/04/ChatGPT_logo.svg">

<!-- Mistral (inline SVG - black/yellow pixel grid) -->
<svg width="24" height="24" viewBox="0 0 24 24" fill="none">
  <rect x="1" y="1" width="5" height="5" fill="#000"/>
  <rect x="9.5" y="1" width="5" height="5" fill="#F7D046"/>
  <rect x="18" y="1" width="5" height="5" fill="#000"/>
  <rect x="1" y="9.5" width="5" height="5" fill="#F7D046"/>
  <rect x="9.5" y="9.5" width="5" height="5" fill="#000"/>
  <rect x="18" y="9.5" width="5" height="5" fill="#F7D046"/>
  <rect x="1" y="18" width="5" height="5" fill="#000"/>
  <rect x="9.5" y="18" width="5" height="5" fill="#F7D046"/>
  <rect x="18" y="18" width="5" height="5" fill="#000"/>
</svg>
```

---

## 📝 Editing Guidelines

### To Edit Content
1. Open the HTML file in `diagrams/`
2. Find the text you want to change
3. Edit directly (all styles are inline)
4. Open in browser to preview
5. Re-export PNG if needed

### To Add a New Diagram
1. Copy an existing diagram HTML as template
2. Update the step number, label, and colors
3. Modify inputs, center node, and outputs
4. Adjust SVG connection paths as needed

### To Export PNGs
1. Open HTML in browser
2. Use browser screenshot (Cmd+Shift+4 on Mac)
3. Or use Playwright/Puppeteer script
4. Save to `exports/` folder

### Connection Line SVG Pattern
```html
<svg class="connections" viewBox="0 0 1100 400">
  <defs>
    <linearGradient id="lineGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#6366f1;stop-opacity:0.3" />
      <stop offset="50%" style="stop-color:#8b5cf6;stop-opacity:0.6" />
      <stop offset="100%" style="stop-color:#6366f1;stop-opacity:0.3" />
    </linearGradient>
  </defs>
  <path class="connection-line" d="M startX startY Q controlX controlY endX endY" />
</svg>
```

---

## 🚨 Common Mistakes to Avoid

1. ❌ Don't forget to update the gradient colors when changing step themes
2. ❌ Don't use external CSS files - keep everything inline for portability
3. ❌ Don't forget to update model names when AI platforms release new versions
4. ❌ Don't use broken logo URLs - Mistral requires inline SVG
5. ❌ Don't forget to regenerate PNGs after making changes

---

## 🔧 Quick Commands

```bash
# Serve locally
cd openfigma
python3 -m http.server 8080
# Open http://localhost:8080/diagrams/diagram-1-cursor-style.html

# View all diagrams
open diagrams/*.html
```

---

**Last Updated:** December 2025

