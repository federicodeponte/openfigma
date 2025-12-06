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

from .advanced import AdvancedComponentRenderer, HeroIcons


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
    font_family: str = "'Inter', -apple-system, sans-serif"
    font_headline: str = "800"
    font_subheadline: str = "600"
    font_body: str = "500"
    
    # Spacing
    padding_large: str = "60px"  # Reduced from 80px
    padding_medium: str = "40px"  # Reduced from 60px
    padding_small: str = "24px"  # Reduced from 40px
    gap_large: str = "40px"  # Reduced from 50px
    gap_medium: str = "24px"  # Reduced from 30px
    gap_small: str = "16px"  # Reduced from 20px
    
    # Border radius
    radius_large: str = "28px"
    radius_medium: str = "20px"
    radius_small: str = "16px"
    radius_pill: str = "100px"
    
    # Shadows
    shadow_small: str = "0 1px 4px rgba(0,0,0,0.04)"
    shadow_medium: str = "0 4px 12px rgba(99, 102, 241, 0.3)"
    
    # Grid pattern
    grid_enabled: bool = False  # Disabled by default
    grid_color: str = "rgba(0,0,0,0.025)"
    grid_size: str = "20px"


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
    {text}
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
        
        # Format text with bold/muted parts
        formatted_text = text
        if bold_parts or muted_parts:
            words = text.split(" ")
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
            formatted_text = f'<span class="bold">{text}</span>'
        
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
        
        # Format quote with emphasis
        formatted_quote = quote
        if emphasis:
            for emp in emphasis:
                formatted_quote = formatted_quote.replace(emp, f"<strong>{emp}</strong>")
        
        avatar_html = ""
        if avatar:
            avatar_html = f'<div class="author-avatar"><img src="{avatar}" alt="{author or ""}"></div>'
        elif author:
            initials = "".join([n[0].upper() for n in author.split()[:2]]) if author else "?"
            avatar_html = f'<div class="author-avatar"><div class="avatar-placeholder">{initials}</div></div>'
        
        author_html = ""
        if author:
            author_html = f"""<div class="quote-author">
      {avatar_html}
      <div class="author-info">
        <div class="author-name">{author}</div>
        {f'<div class="author-role">{role}</div>' if role else ''}
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
        
        change_html = f'<div class="metric-change">{change}</div>' if change else ""
        
        return f"""<div class="metric-card">
    <div class="metric-value">{value}</div>
    <div class="metric-label">{label}</div>
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
        
        desc_html = f'<p class="cta-description">{description}</p>' if description else ""
        button_href = button_url or "#"
        
        return f"""<div class="cta-card">
    <h1 class="cta-headline">{headline}</h1>
    {desc_html}
    <a href="{button_href}" class="cta-button">{button_text}</a>
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
        
        items_html = "".join([
            f'<div class="infographic-item"><div class="item-number">{i+1}</div><div class="item-text">{item}</div></div>'
            for i, item in enumerate(items)
        ])
        
        return f"""<div class="infographic-card">
    <h1 class="infographic-title">{title}</h1>
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
        
        return f"""<div class="logos-card">
    <div class="logo">
      <svg class="logo-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
        <path d="M4 6h16M4 12h16M4 18h10"/>
      </svg>
      {client_name.upper()}
    </div>
    <div class="logo-divider"></div>
    <div class="logo">
      <div class="scaile-icon"></div>
      {provider_name.upper()}
    </div>
  </div>"""


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
    }}"""
        
        return f"""
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{
      font-family: {t.font_family};
      background: {t.background};
      width: {dimensions[0]}px;
      height: {dimensions[1]}px;
      display: flex;
      flex-direction: column;
      padding: {t.padding_medium} {t.padding_large};
      position: relative;
      justify-content: center;  /* Center content vertically */
      gap: {t.gap_medium};
    }}
    {grid_css}
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: {t.surface};
      border: 1px solid {t.border};
      border-radius: {t.radius_pill};
      padding: 12px 24px;
      font-size: 16px;
      font-weight: {t.font_subheadline};
      color: {t.text_primary};
      box-shadow: {t.shadow_small};
      width: fit-content;
      margin-bottom: {t.gap_medium};
    }}
    .badge svg {{ width: 20px; height: 20px; }}
    .headline {{
      font-weight: {t.font_headline};
      line-height: 1.15;
      letter-spacing: -0.03em;
      margin-bottom: auto;
    }}
    .headline .bold {{ color: {t.text_primary}; }}
    .headline .muted {{ color: {t.text_muted}; }}
    .quote-card {{
      background: {t.surface};
      border-radius: {t.radius_large};
      padding: {t.padding_medium};
      box-shadow: {t.shadow_small};
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }}
    .quote-text {{
      font-size: 32px;
      line-height: 1.45;
      color: {t.text_secondary};
      margin-bottom: {t.gap_large};
    }}
    .quote-text strong {{
      color: {t.text_primary};
      font-weight: 700;
    }}
    .quote-author {{
      display: flex;
      align-items: center;
      gap: {t.gap_medium};
    }}
    .author-avatar {{
      width: 80px;
      height: 80px;
      border-radius: 50%;
      background: {t.border_light};
      overflow: hidden;
      flex-shrink: 0;
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
      font-size: 32px;
      font-weight: 700;
      background: {t.gradient_primary};
      color: white;
    }}
    .author-name {{
      font-size: 26px;
      font-weight: 700;
      color: {t.text_primary};
    }}
    .author-role {{
      font-size: 22px;
      color: {t.text_secondary};
      margin-top: 4px;
    }}
    .metric-card {{
      background: {t.surface};
      border-radius: {t.radius_large};
      padding: {t.padding_medium};
      box-shadow: {t.shadow_small};
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
      text-align: center;
    }}
    .metric-value {{
      font-size: 120px;
      font-weight: {t.font_headline};
      background: {t.gradient_text};
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      margin-bottom: {t.gap_small};
    }}
    .metric-label {{
      font-size: 28px;
      font-weight: {t.font_subheadline};
      color: {t.text_primary};
      margin-bottom: {t.gap_small};
    }}
    .metric-change {{
      font-size: 20px;
      font-weight: {t.font_body};
      color: #22c55e;
    }}
    .cta-card {{
      background: {t.surface};
      border-radius: {t.radius_large};
      padding: {t.padding_medium};
      box-shadow: {t.shadow_small};
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
    }}
    .cta-headline {{
      font-size: 56px;
      font-weight: {t.font_headline};
      color: {t.text_primary};
      margin-bottom: {t.gap_medium};
      line-height: 1.15;
      letter-spacing: -0.03em;
    }}
    .cta-description {{
      font-size: 28px;
      color: {t.text_secondary};
      margin-bottom: {t.gap_large};
      line-height: 1.5;
      max-width: 700px;
    }}
    .cta-button {{
      display: inline-block;
      background: {t.gradient_primary};
      color: white;
      padding: 24px 56px;
      border-radius: {t.radius_medium};
      font-size: 24px;
      font-weight: 700;
      text-decoration: none;
      box-shadow: {t.shadow_medium};
    }}
    .infographic-card {{
      background: {t.surface};
      border-radius: {t.radius_large};
      padding: {t.padding_medium};
      box-shadow: {t.shadow_small};
      flex: 1;
      display: flex;
      flex-direction: column;
    }}
    .infographic-title {{
      font-size: 48px;
      font-weight: {t.font_headline};
      color: {t.text_primary};
      margin-bottom: {t.gap_large};
      text-align: center;
      letter-spacing: -0.02em;
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
      padding: 28px;
      background: {t.border_light};
      border-radius: {t.radius_medium};
      border: 1px solid {t.border};
    }}
    .item-number {{
      width: 56px;
      height: 56px;
      border-radius: 50%;
      background: {t.gradient_primary};
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      font-weight: 700;
      color: white;
      flex-shrink: 0;
      box-shadow: {t.shadow_medium};
    }}
    .item-text {{
      font-size: 26px;
      font-weight: {t.font_subheadline};
      color: {t.text_primary};
      line-height: 1.4;
    }}
    .logos-card {{
      background: {t.border_light};
      border-radius: {t.radius_large};
      padding: {t.padding_small} {t.padding_medium};
      display: flex;
      align-items: center;
      justify-content: center;
      gap: {t.padding_small};
      margin-top: {t.gap_medium};
    }}
    .logo {{
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 28px;
      font-weight: {t.font_headline};
      color: {t.text_primary};
      letter-spacing: -0.02em;
    }}
    .logo-icon {{ width: 32px; height: 32px; }}
    .logo-divider {{ width: 1px; height: 36px; background: #d0d0d0; }}
    .scaile-icon {{
      width: 30px;
      height: 30px;
      background: {t.gradient_primary};
      border-radius: 8px;
    }}
    
    /* Advanced Components */
    .hero-icon {{ flex-shrink: 0; }}
    
    /* Process Flow */
    .process-flow {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: {t.gap_medium};
      flex: 1;
    }}
    .process-flow.vertical {{
      flex-direction: column;
      gap: 0;
    }}
    .flow-step {{
      background: {t.surface};
      border-radius: {t.radius_medium};
      padding: {t.padding_medium};
      border: 2px solid {t.border};
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 20px;
      min-width: 220px;
      text-align: center;
      box-shadow: {t.shadow_small};
    }}
    .flow-step.vertical {{
      flex-direction: row;
      min-width: 600px;
      text-align: left;
    }}
    .step-number {{
      width: 64px;
      height: 64px;
      border-radius: 50%;
      background: {t.gradient_primary};
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 32px;
      font-weight: 800;
      color: white;
      box-shadow: {t.shadow_medium};
      flex-shrink: 0;
    }}
    .step-text {{
      font-size: 22px;
      font-weight: 600;
      color: {t.text_primary};
      line-height: 1.4;
    }}
    .flow-arrow {{
      color: {t.accent};
      flex-shrink: 0;
    }}
    .flow-connector {{
      width: 3px;
      height: 40px;
      background: {t.gradient_primary};
      margin: 0 auto;
    }}
    
    /* Bar Chart */
    .bar-chart {{
      display: flex;
      align-items: flex-end;
      justify-content: space-around;
      gap: {t.gap_large};
      background: {t.surface};
      border-radius: {t.radius_large};
      padding: {t.padding_large};
      height: 400px;
      border: 2px solid {t.border};
      box-shadow: {t.shadow_small};
    }}
    .bar-item {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 20px;
      flex: 1;
    }}
    .bar-container {{
      width: 100%;
      height: 300px;
      background: {t.border_light};
      border-radius: {t.radius_medium};
      position: relative;
      display: flex;
      align-items: flex-end;
      overflow: hidden;
    }}
    .bar-fill {{
      width: 100%;
      background: {t.gradient_primary};
      border-radius: {t.radius_medium} {t.radius_medium} 0 0;
      display: flex;
      align-items: flex-start;
      justify-content: center;
      padding-top: 16px;
      transition: height 0.3s ease;
      box-shadow: {t.shadow_medium};
    }}
    .bar-value {{
      font-size: 24px;
      font-weight: 800;
      color: white;
    }}
    .bar-label {{
      font-size: 20px;
      font-weight: 600;
      color: {t.text_primary};
      text-align: center;
    }}
    
    /* Timeline */
    .timeline {{
      display: flex;
      flex-direction: column;
      gap: 0;
      position: relative;
      padding-left: 60px;
    }}
    .timeline::before {{
      content: '';
      position: absolute;
      left: 20px;
      top: 40px;
      bottom: 40px;
      width: 4px;
      background: {t.gradient_primary};
    }}
    .timeline-event {{
      display: flex;
      gap: 40px;
      padding: 30px 0;
      position: relative;
    }}
    .timeline-marker {{
      position: absolute;
      left: -54px;
      width: 64px;
      height: 64px;
      border-radius: 50%;
      background: {t.surface};
      border: 4px solid {t.accent};
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: {t.shadow_medium};
      z-index: 1;
    }}
    .timeline-content {{
      background: {t.surface};
      border-radius: {t.radius_medium};
      padding: {t.padding_medium};
      border: 2px solid {t.border};
      flex: 1;
      box-shadow: {t.shadow_small};
    }}
    .timeline-date {{
      font-size: 18px;
      font-weight: 600;
      color: {t.accent};
      margin-bottom: 12px;
    }}
    .timeline-title {{
      font-size: 26px;
      font-weight: 700;
      color: {t.text_primary};
      margin-bottom: 8px;
    }}
    .timeline-desc {{
      font-size: 20px;
      color: {t.text_secondary};
      line-height: 1.5;
    }}
    
    /* Comparison */
    .comparison {{
      display: flex;
      align-items: stretch;
      gap: {t.gap_large};
    }}
    .comparison-side {{
      flex: 1;
      background: {t.surface};
      border-radius: {t.radius_large};
      padding: {t.padding_large};
      border: 2px solid {t.border};
      display: flex;
      flex-direction: column;
      gap: {t.gap_medium};
      box-shadow: {t.shadow_small};
    }}
    .comparison-side.right {{
      border-color: {t.accent};
      border-width: 3px;
    }}
    .comparison-label {{
      font-size: 22px;
      font-weight: 600;
      color: {t.text_secondary};
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .comparison-content {{
      font-size: 32px;
      font-weight: 700;
      color: {t.text_primary};
      line-height: 1.3;
    }}
    .comparison-stats {{
      font-size: 48px;
      font-weight: 800;
      color: {t.text_muted};
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
      width: 80px;
      height: 80px;
      border-radius: 50%;
      background: {t.gradient_primary};
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 28px;
      font-weight: 800;
      color: white;
      box-shadow: {t.shadow_medium};
    }}
    
    /* Feature Grid */
    .feature-grid {{
      display: grid;
      gap: {t.gap_large};
    }}
    .feature-grid.cols-2 {{ grid-template-columns: repeat(2, 1fr); }}
    .feature-grid.cols-3 {{ grid-template-columns: repeat(3, 1fr); }}
    .feature-grid.cols-4 {{ grid-template-columns: repeat(4, 1fr); }}
    .feature-item {{
      background: {t.surface};
      border-radius: {t.radius_medium};
      padding: {t.padding_medium};
      border: 2px solid {t.border};
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 20px;
      text-align: center;
      box-shadow: {t.shadow_small};
    }}
    .feature-icon {{
      width: 80px;
      height: 80px;
      border-radius: {t.radius_medium};
      background: {t.border_light};
      display: flex;
      align-items: center;
      justify-content: center;
      color: {t.accent};
    }}
    .feature-title {{
      font-size: 24px;
      font-weight: 700;
      color: {t.text_primary};
    }}
    .feature-desc {{
      font-size: 18px;
      color: {t.text_secondary};
      line-height: 1.5;
    }}
    
    /* Stats Dashboard */
    .stats-dashboard {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: {t.gap_large};
    }}
    .stat-card {{
      background: {t.surface};
      border-radius: {t.radius_large};
      padding: {t.padding_medium};
      border: 2px solid {t.border};
      display: flex;
      flex-direction: column;
      gap: 20px;
      box-shadow: {t.shadow_small};
    }}
    .stat-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .stat-icon {{
      width: 56px;
      height: 56px;
      border-radius: {t.radius_medium};
      background: {t.border_light};
      display: flex;
      align-items: center;
      justify-content: center;
      color: {t.accent};
    }}
    .stat-change {{
      font-size: 18px;
      font-weight: 600;
      padding: 8px 16px;
      border-radius: {t.radius_pill};
    }}
    .stat-change.trend-up {{
      background: #dcfce7;
      color: #16a34a;
    }}
    .stat-change.trend-down {{
      background: #fee2e2;
      color: #dc2626;
    }}
    .stat-change.trend-neutral {{
      background: {t.border_light};
      color: {t.text_secondary};
    }}
    .stat-value {{
      font-size: 56px;
      font-weight: 800;
      background: {t.gradient_text};
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }}
    .stat-label {{
      font-size: 20px;
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
  """

