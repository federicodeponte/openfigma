"""
Graphics Component System
Reusable, composable components for building graphics from JSON config.

Components:
- Badge: Top badge/label
- Headline: Large headline text
- QuoteCard: Testimonial/quote card
- MetricCard: Statistics/metric display
- CTACard: Call-to-action card
- InfographicCard: Process/steps display
- LogoCard: Branding footer
- ProcessFlow: Connected steps with arrows
- BarChart: Data visualization
- Timeline: Event timeline
- Comparison: Side-by-side comparison
- FeatureGrid: Icon + text grid
- StatsDashboard: Multi-metric display
- ProgressBar: Progress indicator

Themes:
- Colors, fonts, spacing configurable per business/client
"""

from typing import Dict, Any, Optional, List
from dataclasses import dataclass, field
from html import escape as html_escape

from .advanced import AdvancedComponentRenderer, HeroIcons


def escape_html(text: str) -> str:
    """Escape HTML special characters to prevent XSS."""
    if text is None:
        return ""
    return html_escape(str(text), quote=True)


@dataclass
class Theme:
    """Theme configuration for graphics."""
    # Colors
    background: str = "#f8f8f8"
    surface: str = "#ffffff"
    text_primary: str = "#1a1a1a"
    text_secondary: str = "#6b7280"
    text_muted: str = "#b0b0b0"
    accent: str = "#6366f1"
    accent_secondary: str = "#8b5cf6"
    border: str = "#e8e8e8"
    border_light: str = "#f0f0f0"

    # Gradients
    gradient_primary: str = "linear-gradient(135deg, #6366f1, #8b5cf6)"
    gradient_text: str = "linear-gradient(135deg, #6366f1, #8b5cf6)"

    # Fonts
    font_family: str = "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    font_headline: str = "800"
    font_subheadline: str = "600"
    font_body: str = "500"

    # Spacing
    padding_large: str = "72px"
    padding_medium: str = "48px"
    padding_small: str = "28px"
    gap_large: str = "48px"
    gap_medium: str = "28px"
    gap_small: str = "18px"

    # Border radius
    radius_large: str = "32px"
    radius_medium: str = "24px"
    radius_small: str = "16px"
    radius_pill: str = "100px"

    # Shadows - multi-layered for depth
    shadow_small: str = "0 1px 2px rgba(0,0,0,0.04), 0 4px 8px rgba(0,0,0,0.04)"
    shadow_medium: str = "0 4px 6px rgba(0,0,0,0.05), 0 12px 24px rgba(99, 102, 241, 0.15)"
    shadow_large: str = "0 8px 16px rgba(0,0,0,0.08), 0 24px 48px rgba(0,0,0,0.12)"

    # Grid pattern
    grid_enabled: bool = False  # Disabled by default
    grid_color: str = "rgba(0,0,0,0.025)"
    grid_size: str = "20px"
    grid_style: str = "lines"  # "lines" or "dots"
    grid_dot_size: str = "2px"

    # Background
    background_svg: Optional[str] = None  # SVG content for background silhouettes
    background_svg_color: str = "rgba(255,255,255,0.05)"
    background_svg_position: str = "right bottom"

    # Glassmorphism
    glass_blur: str = "20px"
    glass_opacity: str = "0.85"

    # Typography refinements
    letter_spacing_tight: str = "-0.04em"
    letter_spacing_normal: str = "-0.01em"
    line_height_tight: str = "1.1"
    line_height_normal: str = "1.5"


def dark_theme() -> Theme:
    """Create a dark theme preset."""
    return Theme(
        background="#0a0a0b",
        surface="rgba(255, 255, 255, 0.03)",
        text_primary="#f5f5f5",
        text_secondary="rgba(255, 255, 255, 0.6)",
        text_muted="rgba(255, 255, 255, 0.4)",
        accent="#22d3ee",  # Cyan
        accent_secondary="#06b6d4",
        border="rgba(255, 255, 255, 0.06)",
        border_light="rgba(255, 255, 255, 0.03)",
        gradient_primary="linear-gradient(135deg, #22d3ee, #06b6d4)",
        gradient_text="linear-gradient(135deg, #22d3ee, #06b6d4)",
        shadow_small="0 1px 4px rgba(0,0,0,0.3)",
        shadow_medium="0 4px 20px rgba(34, 211, 238, 0.2)",
        grid_color="rgba(34, 211, 238, 0.3)",
        grid_style="dots",
        grid_dot_size="2px",
    )


def linkedin_theme(accent: str = "#0077b5") -> Theme:
    """
    Create a clean, professional LinkedIn theme.

    Args:
        accent: Accent color (default LinkedIn blue)
               Options: "#0077b5" (blue), "#10b981" (green),
                       "#8b5cf6" (purple), "#f59e0b" (orange)
    """
    return Theme(
        background="#ffffff",
        surface="#f8fafc",
        text_primary="#0f172a",
        text_secondary="#475569",
        text_muted="#94a3b8",
        accent=accent,
        accent_secondary=accent,
        border="#e2e8f0",
        border_light="#f1f5f9",
        gradient_primary=f"linear-gradient(135deg, {accent}, {accent})",
        gradient_text=f"linear-gradient(135deg, {accent}, {accent})",
        shadow_small="0 1px 3px rgba(0,0,0,0.08)",
        shadow_medium=f"0 4px 12px rgba(0,0,0,0.1)",
        grid_enabled=False,
    )


class ComponentRenderer:
    """Renders individual components."""
    
    @staticmethod
    def render_badge(text: str, theme: Theme, icon: Optional[str] = None) -> str:
        """Render badge component."""
        icon_svg = ""
        if icon == "case-study":
            icon_svg = """<svg viewBox="0 0 24 24" fill="currentColor">
      <rect x="3" y="3" width="7" height="7" rx="1"/>
      <rect x="14" y="3" width="7" height="7" rx="1"/>
      <rect x="3" y="14" width="7" height="7" rx="1"/>
      <rect x="14" y="14" width="7" height="7" rx="1"/>
    </svg>"""
        elif icon == "process":
            icon_svg = """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
      <path d="M4 6h16M4 12h16M4 18h10"/>
    </svg>"""
        
        return f"""<div class="badge">
    {icon_svg if icon_svg else ''}
    {escape_html(text)}
  </div>"""
    
    @staticmethod
    def render_headline(
        text: str,
        theme: Theme,
        size: str = "large",
        align: str = "center",
        bold_parts: Optional[List[str]] = None,
        muted_parts: Optional[List[str]] = None,
    ) -> str:
        """Render headline component."""
        import re
        
        # Escape HTML in text first for security
        safe_text = escape_html(text)

        # Format text with bold/muted parts
        formatted_text = safe_text
        if bold_parts or muted_parts:
            words = safe_text.split(" ")
            formatted_words = []
            for word in words:
                word_clean = re.sub(r'[^\w]', '', word.lower())
                if bold_parts and any(word_clean in re.sub(r'[^\w]', '', p.lower()) for p in bold_parts):
                    formatted_words.append(f'<span class="bold">{word}</span>')
                elif muted_parts and any(word_clean in re.sub(r'[^\w]', '', p.lower()) for p in muted_parts):
                    formatted_words.append(f'<span class="muted">{word}</span>')
                else:
                    formatted_words.append(f'<span class="bold">{word}</span>')
            formatted_text = " ".join(formatted_words)
        else:
            formatted_text = f'<span class="bold">{safe_text}</span>'
        
        size_class = {
            "small": "48px",
            "medium": "56px",
            "large": "64px",
            "xlarge": "72px",
        }.get(size, "56px")
        
        return f"""<h1 class="headline" style="font-size: {size_class}; text-align: {align};">
    {formatted_text}
  </h1>"""
    
    @staticmethod
    def render_quote_card(
        quote: str,
        author: Optional[str] = None,
        role: Optional[str] = None,
        avatar: Optional[str] = None,
        theme: Theme = None,
        emphasis: Optional[List[str]] = None,
    ) -> str:
        """Render quote card component."""
        if theme is None:
            theme = Theme()
        
        # Escape HTML and format quote with emphasis
        safe_quote = escape_html(quote)
        formatted_quote = safe_quote
        if emphasis:
            for emp in emphasis:
                safe_emp = escape_html(emp)
                formatted_quote = formatted_quote.replace(safe_emp, f"<strong>{safe_emp}</strong>")
        
        safe_author = escape_html(author) if author else ""
        safe_role = escape_html(role) if role else ""

        avatar_html = ""
        if avatar:
            safe_avatar = escape_html(avatar)
            avatar_html = f'<div class="author-avatar"><img src="{safe_avatar}" alt="{safe_author}"></div>'
        elif author:
            initials = "".join([n[0].upper() for n in safe_author.split()[:2]]) if safe_author else "?"
            avatar_html = f'<div class="author-avatar"><div class="avatar-placeholder">{initials}</div></div>'

        author_html = ""
        if author:
            author_html = f"""<div class="quote-author">
      {avatar_html}
      <div class="author-info">
        <div class="author-name">{safe_author}</div>
        {f'<div class="author-role">{safe_role}</div>' if role else ''}
      </div>
    </div>"""
        
        return f"""<div class="quote-card">
    <p class="quote-text">"{formatted_quote}"</p>
    {author_html}
  </div>"""
    
    @staticmethod
    def render_metric_card(
        value: str,
        label: str,
        change: Optional[str] = None,
        change_type: str = "positive",
        theme: Theme = None,
    ) -> str:
        """Render metric card component."""
        if theme is None:
            theme = Theme()

        safe_value = escape_html(value)
        safe_label = escape_html(label)
        safe_change = escape_html(change) if change else ""
        change_html = f'<div class="metric-change">{safe_change}</div>' if change else ""

        return f"""<div class="metric-card">
    <div class="metric-value">{safe_value}</div>
    <div class="metric-label">{safe_label}</div>
    {change_html}
  </div>"""
    
    @staticmethod
    def render_cta_card(
        headline: str,
        description: Optional[str] = None,
        button_text: str = "Get Started",
        button_url: Optional[str] = None,
        theme: Theme = None,
    ) -> str:
        """Render CTA card component."""
        if theme is None:
            theme = Theme()

        safe_headline = escape_html(headline)
        safe_desc = escape_html(description) if description else ""
        safe_button_text = escape_html(button_text)
        safe_button_url = escape_html(button_url) if button_url else "#"

        desc_html = f'<p class="cta-description">{safe_desc}</p>' if description else ""

        return f"""<div class="cta-card">
    <h1 class="cta-headline">{safe_headline}</h1>
    {desc_html}
    <a href="{safe_button_url}" class="cta-button">{safe_button_text}</a>
  </div>"""
    
    @staticmethod
    def render_infographic_card(
        title: str,
        items: List[str],
        theme: Theme = None,
    ) -> str:
        """Render infographic card component."""
        if theme is None:
            theme = Theme()

        safe_title = escape_html(title)
        items_html = "".join([
            f'<div class="infographic-item"><div class="item-number">{i+1}</div><div class="item-text">{escape_html(item)}</div></div>'
            for i, item in enumerate(items)
        ])

        return f"""<div class="infographic-card">
    <h1 class="infographic-title">{safe_title}</h1>
    <div class="infographic-items">
      {items_html}
    </div>
  </div>"""
    
    @staticmethod
    def render_logo_card(
        client_name: str,
        provider_name: str = "SCAILE",
        theme: Theme = None,
    ) -> str:
        """Render logo card component."""
        if theme is None:
            theme = Theme()

        safe_client = escape_html(client_name).upper()
        safe_provider = escape_html(provider_name).upper()

        return f"""<div class="logos-card">
    <div class="logo">
      <svg class="logo-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
        <path d="M4 6h16M4 12h16M4 18h10"/>
      </svg>
      {safe_client}
    </div>
    <div class="logo-divider"></div>
    <div class="logo">
      <div class="scaile-icon"></div>
      {safe_provider}
    </div>
  </div>"""

    @staticmethod
    def render_event_poster(
        lines: List[Dict[str, Any]],
        theme: Theme = None,
        align: str = "left",
    ) -> str:
        """
        Render event poster with stacked metric lines.

        Each line can have:
        - number: The metric number (e.g., "3", "40", "100k")
        - text: The text label (e.g., "months", "founders", "EUR")
        - size: Font size (default "120px")
        """
        if theme is None:
            theme = Theme()

        lines_html = []
        for line in lines:
            safe_number = escape_html(line.get("number", ""))
            safe_text = escape_html(line.get("text", ""))
            size = escape_html(line.get("size", "120px"))

            lines_html.append(f'''<div class="poster-line" style="font-size: {size};">
        <span class="poster-number">{safe_number}</span>
        <span class="poster-text">{safe_text}</span>
      </div>''')

        safe_align = escape_html(align)
        return f'''<div class="event-poster" style="text-align: {safe_align};">
    {"".join(lines_html)}
  </div>'''

    @staticmethod
    def render_subtitle(
        text: str,
        theme: Theme = None,
        highlight: Optional[str] = None,
        align: str = "left",
    ) -> str:
        """
        Render subtitle/tagline text.

        - text: The subtitle text
        - highlight: Text to highlight (e.g., brand name)
        - align: Text alignment
        """
        if theme is None:
            theme = Theme()

        safe_text = escape_html(text)
        safe_align = escape_html(align)
        formatted_text = safe_text
        if highlight and highlight in text:
            safe_highlight = escape_html(highlight)
            formatted_text = safe_text.replace(safe_highlight, f'<span class="subtitle-highlight">{safe_highlight}</span>')

        return f'''<div class="subtitle" style="text-align: {safe_align};">
    {formatted_text}
  </div>'''

    @staticmethod
    def render_positioned_logo(
        text: str,
        theme: Theme = None,
        position: str = "bottom-right",
        icon_svg: Optional[str] = None,
    ) -> str:
        """
        Render a logo positioned in a corner.

        - text: Logo text (e.g., "pioneers")
        - position: "top-left", "top-right", "bottom-left", "bottom-right"
        - icon_svg: Optional SVG icon to show before text (trusted SVG only)
        """
        if theme is None:
            theme = Theme()

        safe_text = escape_html(text)
        # Validate position to prevent CSS injection
        valid_positions = ["top-left", "top-right", "bottom-left", "bottom-right"]
        safe_position = position if position in valid_positions else "bottom-right"

        # Note: icon_svg is trusted SVG content from the developer
        icon_html = ""
        if icon_svg:
            icon_html = f'<span class="positioned-logo-icon">{icon_svg}</span>'

        return f'''<div class="positioned-logo {safe_position}">
    {icon_html}
    <span class="positioned-logo-text">{safe_text}</span>
  </div>'''

    @staticmethod
    def render_background_svg(svg_content: str, theme: Theme = None) -> str:
        """Render background SVG silhouette."""
        if theme is None:
            theme = Theme()
        return f'''<div class="background-svg">{svg_content}</div>'''


class GraphicsBuilder:
    """Builds graphics from JSON config."""
    
    def __init__(self, theme: Optional[Theme] = None):
        self.theme = theme or Theme()
        self.renderer = ComponentRenderer()
    
    def build_from_config(self, config: Dict[str, Any], dimensions: tuple = (1920, 1080)) -> str:
        """
        Build HTML graphic from JSON config.
        
        Config structure:
        {
          "theme": {...},  # Optional theme overrides
          "components": [
            {"type": "badge", "content": {...}},
            {"type": "headline", "content": {...}},
            ...
          ]
        }
        """
        # Apply theme overrides if provided
        if "theme" in config:
            theme_dict = config["theme"]
            for key, value in theme_dict.items():
                if hasattr(self.theme, key):
                    setattr(self.theme, key, value)
        
        # Build components
        components_html = []
        for component in config.get("components", []):
            comp_type = component.get("type")
            comp_content = component.get("content", {})
            
            if comp_type == "badge":
                components_html.append(
                    self.renderer.render_badge(
                        comp_content.get("text", ""),
                        self.theme,
                        comp_content.get("icon"),
                    )
                )
            elif comp_type == "headline":
                components_html.append(
                    self.renderer.render_headline(
                        comp_content.get("text", ""),
                        self.theme,
                        comp_content.get("size", "large"),
                        comp_content.get("align", "center"),
                        comp_content.get("bold_parts"),
                        comp_content.get("muted_parts"),
                    )
                )
            elif comp_type == "quote_card":
                components_html.append(
                    self.renderer.render_quote_card(
                        comp_content.get("quote", ""),
                        comp_content.get("author"),
                        comp_content.get("role"),
                        comp_content.get("avatar"),
                        self.theme,
                        comp_content.get("emphasis"),
                    )
                )
            elif comp_type == "metric_card":
                components_html.append(
                    self.renderer.render_metric_card(
                        comp_content.get("value", ""),
                        comp_content.get("label", ""),
                        comp_content.get("change"),
                        comp_content.get("change_type", "positive"),
                        self.theme,
                    )
                )
            elif comp_type == "cta_card":
                components_html.append(
                    self.renderer.render_cta_card(
                        comp_content.get("headline", ""),
                        comp_content.get("description"),
                        comp_content.get("button_text", "Get Started"),
                        comp_content.get("button_url"),
                        self.theme,
                    )
                )
            elif comp_type == "infographic_card":
                components_html.append(
                    self.renderer.render_infographic_card(
                        comp_content.get("title", ""),
                        comp_content.get("items", []),
                        self.theme,
                    )
                )
            elif comp_type == "logo_card":
                components_html.append(
                    self.renderer.render_logo_card(
                        comp_content.get("client_name", ""),
                        comp_content.get("provider_name", "SCAILE"),
                        self.theme,
                    )
                )
            elif comp_type == "process_flow":
                components_html.append(
                    AdvancedComponentRenderer.render_process_flow(
                        comp_content.get("steps", []),
                        self.theme,
                        comp_content.get("orientation", "horizontal"),
                        comp_content.get("show_arrows", True),
                    )
                )
            elif comp_type == "bar_chart":
                components_html.append(
                    AdvancedComponentRenderer.render_bar_chart(
                        comp_content.get("data", []),
                        self.theme,
                        comp_content.get("max_value"),
                    )
                )
            elif comp_type == "timeline":
                components_html.append(
                    AdvancedComponentRenderer.render_timeline(
                        comp_content.get("events", []),
                        self.theme,
                        comp_content.get("orientation", "vertical"),
                    )
                )
            elif comp_type == "comparison":
                components_html.append(
                    AdvancedComponentRenderer.render_comparison(
                        comp_content.get("left", {}),
                        comp_content.get("right", {}),
                        self.theme,
                    )
                )
            elif comp_type == "feature_grid":
                components_html.append(
                    AdvancedComponentRenderer.render_feature_grid(
                        comp_content.get("features", []),
                        self.theme,
                        comp_content.get("columns", 3),
                    )
                )
            elif comp_type == "stats_dashboard":
                components_html.append(
                    AdvancedComponentRenderer.render_stats_dashboard(
                        comp_content.get("stats", []),
                        self.theme,
                    )
                )
            elif comp_type == "progress_bar":
                components_html.append(
                    AdvancedComponentRenderer.render_progress_bar(
                        comp_content.get("label", ""),
                        comp_content.get("value", 0),
                        comp_content.get("max_value", 100),
                        self.theme,
                        comp_content.get("show_percentage", True),
                    )
                )
            elif comp_type == "event_poster":
                components_html.append(
                    self.renderer.render_event_poster(
                        comp_content.get("lines", []),
                        self.theme,
                        comp_content.get("align", "left"),
                    )
                )
            elif comp_type == "subtitle":
                components_html.append(
                    self.renderer.render_subtitle(
                        comp_content.get("text", ""),
                        self.theme,
                        comp_content.get("highlight"),
                        comp_content.get("align", "left"),
                    )
                )
            elif comp_type == "positioned_logo":
                components_html.append(
                    self.renderer.render_positioned_logo(
                        comp_content.get("text", ""),
                        self.theme,
                        comp_content.get("position", "bottom-right"),
                        comp_content.get("icon_svg"),
                    )
                )
            elif comp_type == "background_svg":
                components_html.append(
                    self.renderer.render_background_svg(
                        comp_content.get("svg", ""),
                        self.theme,
                    )
                )

        # Generate full HTML
        return self._generate_html(components_html, dimensions)
    
    def _generate_html(self, components: List[str], dimensions: tuple) -> str:
        """Generate full HTML document with components."""
        components_html = "\n  ".join(components)
        
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Graphic</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    {self._generate_css(dimensions)}
  </style>
</head>
<body>
  {components_html}
</body>
</html>"""
    
    def _generate_css(self, dimensions: tuple) -> str:
        """Generate CSS from theme."""
        t = self.theme

        grid_css = ""
        if t.grid_enabled:
            if t.grid_style == "dots":
                grid_css = f"""
    body::before {{
      content: '';
      position: absolute;
      inset: 0;
      background-image: radial-gradient(circle, {t.grid_color} {t.grid_dot_size}, transparent {t.grid_dot_size});
      background-size: {t.grid_size} {t.grid_size};
      pointer-events: none;
      z-index: 0;
    }}"""
            else:
                grid_css = f"""
    body::before {{
      content: '';
      position: absolute;
      inset: 0;
      background-image:
        linear-gradient({t.grid_color} 1px, transparent 1px),
        linear-gradient(90deg, {t.grid_color} 1px, transparent 1px);
      background-size: {t.grid_size} {t.grid_size};
      pointer-events: none;
      z-index: 0;
    }}"""

        background_svg_css = ""
        if t.background_svg:
            background_svg_css = f"""
    .background-svg {{
      position: absolute;
      inset: 0;
      pointer-events: none;
      z-index: 1;
      display: flex;
      align-items: flex-end;
      justify-content: flex-end;
    }}
    .background-svg svg {{
      width: auto;
      height: 80%;
      opacity: 0.15;
      fill: {t.background_svg_color};
    }}"""

        return f"""
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}

    /* Anti-aliasing for crisp text */
    html {{
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-rendering: optimizeLegibility;
    }}

    body {{
      font-family: {t.font_family};
      background: {t.background};
      width: {dimensions[0]}px;
      height: {dimensions[1]}px;
      display: flex;
      flex-direction: column;
      padding: {t.padding_large};
      position: relative;
      justify-content: center;
      gap: {t.gap_large};
      overflow: hidden;
    }}
    {grid_css}
    {background_svg_css}
    body > * {{
      position: relative;
      z-index: 2;
    }}

    /* Badge - refined pill style */
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: {t.surface};
      backdrop-filter: blur({t.glass_blur});
      -webkit-backdrop-filter: blur({t.glass_blur});
      border: 1.5px solid {t.border};
      border-radius: {t.radius_pill};
      padding: 14px 28px;
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: {t.accent};
      box-shadow: {t.shadow_small};
      width: fit-content;
      margin-bottom: {t.gap_small};
    }}
    .badge svg {{ width: 18px; height: 18px; }}

    /* Headline - bold, impactful typography */
    .headline {{
      font-weight: {t.font_headline};
      line-height: {t.line_height_tight};
      letter-spacing: {t.letter_spacing_tight};
    }}
    .headline .bold {{
      color: {t.text_primary};
      display: inline;
    }}
    .headline .muted {{
      color: {t.text_muted};
      display: inline;
    }}

    /* Quote Card - elegant, spacious */
    .quote-card {{
      background: {t.surface};
      backdrop-filter: blur({t.glass_blur});
      -webkit-backdrop-filter: blur({t.glass_blur});
      border-radius: {t.radius_large};
      padding: {t.padding_large};
      border: 1px solid {t.border};
      box-shadow: {t.shadow_medium};
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }}
    .quote-text {{
      font-size: 38px;
      font-weight: 500;
      line-height: 1.5;
      color: {t.text_secondary};
      margin-bottom: {t.gap_large};
      letter-spacing: {t.letter_spacing_normal};
    }}
    .quote-text strong {{
      color: {t.text_primary};
      font-weight: 700;
    }}
    .quote-author {{
      display: flex;
      align-items: center;
      gap: 20px;
      padding-top: {t.gap_medium};
      border-top: 1px solid {t.border};
    }}
    .author-avatar {{
      width: 64px;
      height: 64px;
      border-radius: 50%;
      background: {t.border_light};
      overflow: hidden;
      flex-shrink: 0;
      border: 2px solid {t.border};
    }}
    .author-avatar img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
    }}
    .avatar-placeholder {{
      width: 100%;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      font-weight: 700;
      background: {t.gradient_primary};
      color: white;
    }}
    .author-name {{
      font-size: 20px;
      font-weight: 700;
      color: {t.text_primary};
      letter-spacing: {t.letter_spacing_normal};
    }}
    .author-role {{
      font-size: 16px;
      color: {t.text_secondary};
      margin-top: 4px;
      font-weight: 500;
    }}

    /* Metric Card - bold, centered */
    .metric-card {{
      background: {t.surface};
      backdrop-filter: blur({t.glass_blur});
      -webkit-backdrop-filter: blur({t.glass_blur});
      border-radius: {t.radius_large};
      padding: {t.padding_large};
      border: 1px solid {t.border};
      box-shadow: {t.shadow_medium};
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
      text-align: center;
    }}
    .metric-value {{
      font-size: 140px;
      font-weight: {t.font_headline};
      background: {t.gradient_text};
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      letter-spacing: -0.05em;
      line-height: 1;
      margin-bottom: {t.gap_medium};
    }}
    .metric-label {{
      font-size: 24px;
      font-weight: 600;
      color: {t.text_primary};
      letter-spacing: 0.02em;
      margin-bottom: {t.gap_small};
    }}
    .metric-change {{
      font-size: 18px;
      font-weight: 600;
      color: {t.accent};
      padding: 10px 20px;
      background: {t.border_light};
      border-radius: {t.radius_pill};
      display: inline-block;
    }}

    /* CTA Card - compelling, action-oriented */
    .cta-card {{
      background: {t.surface};
      backdrop-filter: blur({t.glass_blur});
      -webkit-backdrop-filter: blur({t.glass_blur});
      border-radius: {t.radius_large};
      padding: {t.padding_large};
      border: 1px solid {t.border};
      box-shadow: {t.shadow_medium};
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
    }}
    .cta-headline {{
      font-size: 64px;
      font-weight: {t.font_headline};
      color: {t.text_primary};
      margin-bottom: {t.gap_medium};
      line-height: {t.line_height_tight};
      letter-spacing: {t.letter_spacing_tight};
    }}
    .cta-description {{
      font-size: 24px;
      color: {t.text_secondary};
      margin-bottom: {t.gap_large};
      line-height: {t.line_height_normal};
      max-width: 600px;
      font-weight: 500;
    }}
    .cta-button {{
      display: inline-block;
      background: {t.gradient_primary};
      color: white;
      padding: 20px 48px;
      border-radius: {t.radius_pill};
      font-size: 18px;
      font-weight: 700;
      text-decoration: none;
      letter-spacing: 0.02em;
      box-shadow: {t.shadow_medium}, 0 0 0 0 {t.accent};
      transition: all 0.2s ease;
    }}

    /* Infographic Card - structured, readable */
    .infographic-card {{
      background: {t.surface};
      backdrop-filter: blur({t.glass_blur});
      -webkit-backdrop-filter: blur({t.glass_blur});
      border-radius: {t.radius_large};
      padding: {t.padding_large};
      border: 1px solid {t.border};
      box-shadow: {t.shadow_medium};
      flex: 1;
      display: flex;
      flex-direction: column;
    }}
    .infographic-title {{
      font-size: 42px;
      font-weight: {t.font_headline};
      color: {t.text_primary};
      margin-bottom: {t.gap_large};
      text-align: center;
      letter-spacing: {t.letter_spacing_tight};
      line-height: {t.line_height_tight};
    }}
    .infographic-items {{
      display: flex;
      flex-direction: column;
      gap: {t.gap_small};
      flex: 1;
      justify-content: center;
    }}
    .infographic-item {{
      display: flex;
      align-items: center;
      gap: 24px;
      padding: 24px 28px;
      background: {t.border_light};
      border-radius: {t.radius_medium};
      border: 1px solid {t.border};
      transition: all 0.2s ease;
    }}
    .item-number {{
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background: {t.gradient_primary};
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      font-weight: 700;
      color: white;
      flex-shrink: 0;
      box-shadow: {t.shadow_small};
    }}
    .item-text {{
      font-size: 20px;
      font-weight: 600;
      color: {t.text_primary};
      line-height: 1.4;
      letter-spacing: {t.letter_spacing_normal};
    }}

    /* Logos Card */
    .logos-card {{
      background: {t.border_light};
      border-radius: {t.radius_large};
      padding: 20px {t.padding_medium};
      display: flex;
      align-items: center;
      justify-content: center;
      gap: {t.padding_small};
      margin-top: {t.gap_medium};
      border: 1px solid {t.border};
    }}
    .logo {{
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 22px;
      font-weight: {t.font_headline};
      color: {t.text_primary};
      letter-spacing: 0.02em;
    }}
    .logo-icon {{ width: 28px; height: 28px; }}
    .logo-divider {{
      width: 1px;
      height: 32px;
      background: {t.border};
    }}
    .scaile-icon {{
      width: 28px;
      height: 28px;
      background: {t.gradient_primary};
      border-radius: 8px;
    }}
    
    /* Advanced Components */
    .hero-icon {{ flex-shrink: 0; }}

    /* Process Flow - clean, connected steps */
    .process-flow {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 16px;
      flex: 1;
    }}
    .process-flow.vertical {{
      flex-direction: column;
      gap: 0;
    }}
    .flow-step {{
      background: {t.surface};
      backdrop-filter: blur({t.glass_blur});
      -webkit-backdrop-filter: blur({t.glass_blur});
      border-radius: {t.radius_large};
      padding: {t.padding_medium};
      border: 1px solid {t.border};
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 16px;
      min-width: 200px;
      text-align: center;
      box-shadow: {t.shadow_medium};
    }}
    .flow-step.vertical {{
      flex-direction: row;
      min-width: 500px;
      text-align: left;
    }}
    .step-number {{
      width: 56px;
      height: 56px;
      border-radius: 50%;
      background: {t.gradient_primary};
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      font-weight: 800;
      color: white;
      box-shadow: 0 4px 12px rgba(0,0,0,0.15);
      flex-shrink: 0;
    }}
    .step-text {{
      font-size: 18px;
      font-weight: 600;
      color: {t.text_primary};
      line-height: 1.4;
      letter-spacing: {t.letter_spacing_normal};
    }}
    .flow-arrow {{
      color: {t.accent};
      flex-shrink: 0;
      opacity: 0.6;
    }}
    .flow-connector {{
      width: 2px;
      height: 32px;
      background: {t.gradient_primary};
      margin: 0 auto;
      opacity: 0.5;
    }}

    /* Bar Chart - refined data visualization */
    .bar-chart {{
      display: flex;
      align-items: flex-end;
      justify-content: space-around;
      gap: {t.gap_medium};
      background: {t.surface};
      backdrop-filter: blur({t.glass_blur});
      -webkit-backdrop-filter: blur({t.glass_blur});
      border-radius: {t.radius_large};
      padding: {t.padding_large};
      height: 420px;
      border: 1px solid {t.border};
      box-shadow: {t.shadow_medium};
    }}
    .bar-item {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 16px;
      flex: 1;
      max-width: 120px;
    }}
    .bar-container {{
      width: 100%;
      height: 320px;
      background: {t.border_light};
      border-radius: {t.radius_small};
      position: relative;
      display: flex;
      align-items: flex-end;
      overflow: hidden;
    }}
    .bar-fill {{
      width: 100%;
      background: {t.gradient_primary};
      border-radius: {t.radius_small} {t.radius_small} 0 0;
      display: flex;
      align-items: flex-start;
      justify-content: center;
      padding-top: 12px;
      box-shadow: 0 -4px 20px rgba(0,0,0,0.1);
    }}
    .bar-value {{
      font-size: 18px;
      font-weight: 800;
      color: white;
      text-shadow: 0 1px 2px rgba(0,0,0,0.2);
    }}
    .bar-label {{
      font-size: 16px;
      font-weight: 600;
      color: {t.text_primary};
      text-align: center;
      letter-spacing: 0.02em;
    }}

    /* Timeline - elegant vertical progression */
    .timeline {{
      display: flex;
      flex-direction: column;
      gap: 0;
      position: relative;
      padding-left: 80px;
    }}
    .timeline::before {{
      content: '';
      position: absolute;
      left: 28px;
      top: 32px;
      bottom: 32px;
      width: 3px;
      background: {t.gradient_primary};
      border-radius: 2px;
      opacity: 0.4;
    }}
    .timeline-event {{
      display: flex;
      gap: 32px;
      padding: 24px 0;
      position: relative;
    }}
    .timeline-marker {{
      position: absolute;
      left: -68px;
      top: 24px;
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background: {t.surface};
      border: 3px solid {t.accent};
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: {t.shadow_small};
      z-index: 1;
    }}
    .timeline-content {{
      background: {t.surface};
      backdrop-filter: blur({t.glass_blur});
      -webkit-backdrop-filter: blur({t.glass_blur});
      border-radius: {t.radius_medium};
      padding: {t.padding_medium};
      border: 1px solid {t.border};
      flex: 1;
      box-shadow: {t.shadow_small};
    }}
    .timeline-date {{
      font-size: 14px;
      font-weight: 700;
      color: {t.accent};
      margin-bottom: 8px;
      letter-spacing: 0.05em;
      text-transform: uppercase;
    }}
    .timeline-title {{
      font-size: 22px;
      font-weight: 700;
      color: {t.text_primary};
      margin-bottom: 8px;
      letter-spacing: {t.letter_spacing_normal};
    }}
    .timeline-desc {{
      font-size: 16px;
      color: {t.text_secondary};
      line-height: {t.line_height_normal};
    }}

    /* Comparison - clear side-by-side */
    .comparison {{
      display: flex;
      align-items: stretch;
      gap: {t.gap_medium};
    }}
    .comparison-side {{
      flex: 1;
      background: {t.surface};
      backdrop-filter: blur({t.glass_blur});
      -webkit-backdrop-filter: blur({t.glass_blur});
      border-radius: {t.radius_large};
      padding: {t.padding_large};
      border: 1px solid {t.border};
      display: flex;
      flex-direction: column;
      gap: {t.gap_medium};
      box-shadow: {t.shadow_small};
    }}
    .comparison-side.right {{
      border-color: {t.accent};
      border-width: 2px;
      box-shadow: {t.shadow_medium};
    }}
    .comparison-label {{
      font-size: 14px;
      font-weight: 700;
      color: {t.text_secondary};
      text-transform: uppercase;
      letter-spacing: 0.1em;
    }}
    .comparison-content {{
      font-size: 26px;
      font-weight: 600;
      color: {t.text_primary};
      line-height: 1.4;
      letter-spacing: {t.letter_spacing_normal};
    }}
    .comparison-stats {{
      font-size: 56px;
      font-weight: 800;
      color: {t.text_muted};
      letter-spacing: -0.03em;
    }}
    .comparison-stats.highlight {{
      background: {t.gradient_text};
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }}
    .comparison-divider {{
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
    }}
    .vs-badge {{
      width: 64px;
      height: 64px;
      border-radius: 50%;
      background: {t.gradient_primary};
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      font-weight: 800;
      color: white;
      box-shadow: {t.shadow_medium};
    }}

    /* Feature Grid - balanced icon cards */
    .feature-grid {{
      display: grid;
      gap: {t.gap_medium};
    }}
    .feature-grid.cols-2 {{ grid-template-columns: repeat(2, 1fr); }}
    .feature-grid.cols-3 {{ grid-template-columns: repeat(3, 1fr); }}
    .feature-grid.cols-4 {{ grid-template-columns: repeat(4, 1fr); }}
    .feature-item {{
      background: {t.surface};
      backdrop-filter: blur({t.glass_blur});
      -webkit-backdrop-filter: blur({t.glass_blur});
      border-radius: {t.radius_medium};
      padding: {t.padding_medium};
      border: 1px solid {t.border};
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 16px;
      text-align: center;
      box-shadow: {t.shadow_small};
    }}
    .feature-icon {{
      width: 64px;
      height: 64px;
      border-radius: {t.radius_medium};
      background: {t.border_light};
      display: flex;
      align-items: center;
      justify-content: center;
      color: {t.accent};
    }}
    .feature-title {{
      font-size: 20px;
      font-weight: 700;
      color: {t.text_primary};
      letter-spacing: {t.letter_spacing_normal};
    }}
    .feature-desc {{
      font-size: 15px;
      color: {t.text_secondary};
      line-height: {t.line_height_normal};
    }}

    /* Stats Dashboard - compact, informative */
    .stats-dashboard {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: {t.gap_medium};
    }}
    .stat-card {{
      background: {t.surface};
      backdrop-filter: blur({t.glass_blur});
      -webkit-backdrop-filter: blur({t.glass_blur});
      border-radius: {t.radius_large};
      padding: {t.padding_medium};
      border: 1px solid {t.border};
      display: flex;
      flex-direction: column;
      gap: 16px;
      box-shadow: {t.shadow_medium};
    }}
    .stat-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .stat-icon {{
      width: 48px;
      height: 48px;
      border-radius: {t.radius_small};
      background: {t.border_light};
      display: flex;
      align-items: center;
      justify-content: center;
      color: {t.accent};
    }}
    .stat-change {{
      font-size: 14px;
      font-weight: 700;
      padding: 6px 14px;
      border-radius: {t.radius_pill};
    }}
    .stat-change.trend-up {{
      background: rgba(34, 197, 94, 0.15);
      color: #16a34a;
    }}
    .stat-change.trend-down {{
      background: rgba(239, 68, 68, 0.15);
      color: #dc2626;
    }}
    .stat-change.trend-neutral {{
      background: {t.border_light};
      color: {t.text_secondary};
    }}
    .stat-value {{
      font-size: 48px;
      font-weight: 800;
      background: {t.gradient_text};
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      letter-spacing: -0.03em;
      line-height: 1;
    }}
    .stat-label {{
      font-size: 16px;
      font-weight: 600;
      color: {t.text_secondary};
    }}
    
    /* Progress Bar */
    .progress-bar-container {{
      display: flex;
      flex-direction: column;
      gap: 12px;
      padding: {t.padding_small} 0;
    }}
    .progress-label {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 20px;
      font-weight: 600;
      color: {t.text_primary};
    }}
    .progress-percentage {{
      font-size: 18px;
      font-weight: 700;
      color: {t.accent};
    }}
    .progress-track {{
      width: 100%;
      height: 16px;
      background: {t.border_light};
      border-radius: {t.radius_pill};
      overflow: hidden;
    }}
    .progress-fill {{
      height: 100%;
      background: {t.gradient_primary};
      border-radius: {t.radius_pill};
      transition: width 0.3s ease;
      box-shadow: {t.shadow_medium};
    }}

    /* Event Poster */
    .event-poster {{
      display: flex;
      flex-direction: column;
      gap: 0;
    }}
    .poster-line {{
      display: flex;
      align-items: baseline;
      gap: 24px;
      font-weight: {t.font_headline};
      line-height: 1.0;
      letter-spacing: -0.04em;
    }}
    .poster-number {{
      color: {t.text_primary};
      font-style: italic;
    }}
    .poster-text {{
      color: {t.text_primary};
      font-style: normal;
    }}

    /* Subtitle */
    .subtitle {{
      font-size: 24px;
      font-weight: {t.font_body};
      color: {t.text_secondary};
      letter-spacing: 0.02em;
      margin-top: {t.gap_large};
    }}
    .subtitle-highlight {{
      color: {t.text_primary};
      font-weight: {t.font_subheadline};
      background: {t.surface};
      padding: 4px 12px;
      border-radius: 4px;
    }}

    /* Positioned Logo */
    .positioned-logo {{
      position: absolute;
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 20px;
      font-weight: {t.font_subheadline};
      color: {t.text_secondary};
      z-index: 10;
    }}
    .positioned-logo.bottom-right {{
      bottom: {t.padding_medium};
      right: {t.padding_large};
    }}
    .positioned-logo.bottom-left {{
      bottom: {t.padding_medium};
      left: {t.padding_large};
    }}
    .positioned-logo.top-right {{
      top: {t.padding_medium};
      right: {t.padding_large};
    }}
    .positioned-logo.top-left {{
      top: {t.padding_medium};
      left: {t.padding_large};
    }}
    .positioned-logo-icon {{
      display: flex;
      align-items: center;
    }}
    .positioned-logo-icon svg {{
      width: 24px;
      height: 24px;
    }}
    .positioned-logo-text {{
      letter-spacing: 0.05em;
    }}

    /* Background SVG */
    .background-svg {{
      position: absolute;
      inset: 0;
      pointer-events: none;
      z-index: 1;
      display: flex;
      align-items: flex-end;
      justify-content: flex-end;
      overflow: hidden;
    }}
    .background-svg svg {{
      width: auto;
      height: 90%;
      max-width: 60%;
      fill: {t.text_primary};
      opacity: 0.08;
    }}
  """

