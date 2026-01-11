"""
Advanced Graphics Components - Visual Elements Library
Reusable components for creating rich, engaging graphics with charts, flows, icons.

Components:
- ProcessFlow: Connected steps with arrows
- DataChart: Bar charts, line charts, progress bars
- Timeline: Horizontal/vertical timelines
- Comparison: Side-by-side layouts
- FeatureGrid: Icon + text grid layouts
- StatsDashboard: Multi-metric displays
- IconCard: Cards with Hero Icons
"""

from typing import Dict, Any, List, Optional, Literal
from html import escape as html_escape


def escape_html(text: str) -> str:
    """Escape HTML special characters to prevent XSS."""
    if text is None:
        return ""
    return html_escape(str(text), quote=True)


class HeroIcons:
    """Hero Icons SVG paths (outline style)."""
    
    @staticmethod
    def get_icon(name: str) -> str:
        """Get Hero Icon SVG path."""
        icons = {
            "chart-bar": '<path stroke-linecap="round" stroke-linejoin="round" d="M3 13.125C3 12.504 3.504 12 4.125 12h2.25c.621 0 1.125.504 1.125 1.125v6.75C7.5 20.496 6.996 21 6.375 21h-2.25A1.125 1.125 0 013 19.875v-6.75zM9.75 8.625c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125v11.25c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V8.625zM16.5 4.125c0-.621.504-1.125 1.125-1.125h2.25C20.496 3 21 3.504 21 4.125v15.75c0 .621-.504 1.125-1.125 1.125h-2.25a1.125 1.125 0 01-1.125-1.125V4.125z"/>',
            "arrow-trending-up": '<path stroke-linecap="round" stroke-linejoin="round" d="M2.25 18L9 11.25l4.306 4.307a11.95 11.95 0 015.814-5.519l2.74-1.22m0 0l-5.94-2.28m5.94 2.28l-2.28 5.941"/>',
            "check-circle": '<path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>',
            "lightning-bolt": '<path stroke-linecap="round" stroke-linejoin="round" d="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z"/>',
            "clock": '<path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z"/>',
            "users": '<path stroke-linecap="round" stroke-linejoin="round" d="M15 19.128a9.38 9.38 0 002.625.372 9.337 9.337 0 004.121-.952 4.125 4.125 0 00-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 018.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0111.964-3.07M12 6.375a3.375 3.375 0 11-6.75 0 3.375 3.375 0 016.75 0zm8.25 2.25a2.625 2.625 0 11-5.25 0 2.625 2.625 0 015.25 0z"/>',
            "rocket-launch": '<path stroke-linecap="round" stroke-linejoin="round" d="M15.59 14.37a6 6 0 01-5.84 7.38v-4.8m5.84-2.58a14.98 14.98 0 006.16-12.12A14.98 14.98 0 009.631 8.41m5.96 5.96a14.926 14.926 0 01-5.841 2.58m-.119-8.54a6 6 0 00-7.381 5.84h4.8m2.581-5.84a14.927 14.927 0 00-2.58 5.84m2.699 2.7c-.103.021-.207.041-.311.06a15.09 15.09 0 01-2.448-2.448 14.9 14.9 0 01.06-.312m-2.24 2.39a4.493 4.493 0 00-1.757 4.306 4.493 4.493 0 004.306-1.758M16.5 9a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z"/>',
            "sparkles": '<path stroke-linecap="round" stroke-linejoin="round" d="M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09zM18.259 8.715L18 9.75l-.259-1.035a3.375 3.375 0 00-2.455-2.456L14.25 6l1.036-.259a3.375 3.375 0 002.455-2.456L18 2.25l.259 1.035a3.375 3.375 0 002.456 2.456L21.75 6l-1.035.259a3.375 3.375 0 00-2.456 2.456zM16.894 20.567L16.5 21.75l-.394-1.183a2.25 2.25 0 00-1.423-1.423L13.5 18.75l1.183-.394a2.25 2.25 0 001.423-1.423l.394-1.183.394 1.183a2.25 2.25 0 001.423 1.423l1.183.394-1.183.394a2.25 2.25 0 00-1.423 1.423z"/>',
            "cog": '<path stroke-linecap="round" stroke-linejoin="round" d="M10.343 3.94c.09-.542.56-.94 1.11-.94h1.093c.55 0 1.02.398 1.11.94l.149.894c.07.424.384.764.78.93.398.164.855.142 1.205-.108l.737-.527a1.125 1.125 0 011.45.12l.773.774c.39.389.44 1.002.12 1.45l-.527.737c-.25.35-.272.806-.107 1.204.165.397.505.71.93.78l.893.15c.543.09.94.56.94 1.109v1.094c0 .55-.397 1.02-.94 1.11l-.893.149c-.425.07-.765.383-.93.78-.165.398-.143.854.107 1.204l.527.738c.32.447.269 1.06-.12 1.45l-.774.773a1.125 1.125 0 01-1.449.12l-.738-.527c-.35-.25-.806-.272-1.203-.107-.397.165-.71.505-.781.929l-.149.894c-.09.542-.56.94-1.11.94h-1.094c-.55 0-1.019-.398-1.11-.94l-.148-.894c-.071-.424-.384-.764-.781-.93-.398-.164-.854-.142-1.204.108l-.738.527c-.447.32-1.06.269-1.45-.12l-.773-.774a1.125 1.125 0 01-.12-1.45l.527-.737c.25-.35.273-.806.108-1.204-.165-.397-.505-.71-.93-.78l-.894-.15c-.542-.09-.94-.56-.94-1.109v-1.094c0-.55.398-1.02.94-1.11l.894-.149c.424-.07.765-.383.93-.78.165-.398.143-.854-.107-1.204l-.527-.738a1.125 1.125 0 01.12-1.45l.773-.773a1.125 1.125 0 011.45-.12l.737.527c.35.25.807.272 1.204.107.397-.165.71-.505.78-.929l.15-.894z"/><path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>',
            "shield-check": '<path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285z"/>',
            "arrow-right": '<path stroke-linecap="round" stroke-linejoin="round" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"/>',
            "cube": '<path stroke-linecap="round" stroke-linejoin="round" d="M21 7.5l-9-5.25L3 7.5m18 0l-9 5.25m9-5.25v9l-9 5.25M3 7.5l9 5.25M3 7.5v9l9 5.25m0-9v9"/>',
            "document-text": '<path stroke-linecap="round" stroke-linejoin="round" d="M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m0 12.75h7.5m-7.5 3H12M10.5 2.25H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z"/>',
        }
        return icons.get(name, icons["sparkles"])
    
    @staticmethod
    def render_icon(name: str, size: str = "24", color: str = "currentColor", stroke_width: str = "2") -> str:
        """Render Hero Icon as SVG."""
        path = HeroIcons.get_icon(name)
        return f'''<svg class="hero-icon" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{stroke_width}">
  {path}
</svg>'''


class AdvancedComponentRenderer:
    """Renders advanced visual components."""
    
    @staticmethod
    def render_process_flow(
        steps: List[str],
        theme: Any,
        orientation: Literal["horizontal", "vertical"] = "horizontal",
        show_arrows: bool = True,
    ) -> str:
        """Render process flow with connected steps."""
        if orientation == "horizontal":
            return AdvancedComponentRenderer._render_horizontal_flow(steps, theme, show_arrows)
        else:
            return AdvancedComponentRenderer._render_vertical_flow(steps, theme, show_arrows)
    
    @staticmethod
    def _render_horizontal_flow(steps: List[str], theme: Any, show_arrows: bool) -> str:
        """Horizontal flow layout."""
        steps_html = []
        for i, step in enumerate(steps):
            arrow_html = ""
            if show_arrows and i < len(steps) - 1:
                arrow_html = f'''<div class="flow-arrow">
          {HeroIcons.render_icon("arrow-right", "32", theme.accent, "3")}
        </div>'''
            
            steps_html.append(f'''<div class="flow-step">
        <div class="step-number">{i+1}</div>
        <div class="step-text">{escape_html(step)}</div>
      </div>
      {arrow_html}''')
        
        return f'<div class="process-flow horizontal">{"".join(steps_html)}</div>'
    
    @staticmethod
    def _render_vertical_flow(steps: List[str], theme: Any, show_arrows: bool) -> str:
        """Vertical flow layout."""
        steps_html = []
        for i, step in enumerate(steps):
            connector = ""
            if i < len(steps) - 1:
                connector = '<div class="flow-connector"></div>'
            
            steps_html.append(f'''<div class="flow-item">
        <div class="flow-step vertical">
          <div class="step-number">{i+1}</div>
          <div class="step-text">{escape_html(step)}</div>
        </div>
        {connector}
      </div>''')
        
        return f'<div class="process-flow vertical">{"".join(steps_html)}</div>'
    
    @staticmethod
    def render_bar_chart(
        data: List[Dict[str, Any]],
        theme: Any,
        max_value: Optional[float] = None,
    ) -> str:
        """Render bar chart visualization."""
        if not max_value:
            max_value = max([d.get("value", 0) for d in data])
        
        bars_html = []
        for item in data:
            value = item.get("value", 0)
            label = escape_html(item.get("label", ""))
            height_percent = (value / max_value * 100) if max_value > 0 else 0

            bars_html.append(f'''<div class="bar-item">
        <div class="bar-container">
          <div class="bar-fill" style="height: {height_percent}%;">
            <span class="bar-value">{escape_html(str(value))}</span>
          </div>
        </div>
        <div class="bar-label">{label}</div>
      </div>''')
        
        return f'<div class="bar-chart">{"".join(bars_html)}</div>'
    
    @staticmethod
    def render_timeline(
        events: List[Dict[str, Any]],
        theme: Any,
        orientation: Literal["horizontal", "vertical"] = "vertical",
    ) -> str:
        """Render timeline visualization."""
        events_html = []
        for i, event in enumerate(events):
            title = escape_html(event.get("title", ""))
            date = escape_html(event.get("date", ""))
            description = escape_html(event.get("description", ""))
            icon = event.get("icon", "clock")

            events_html.append(f'''<div class="timeline-event">
        <div class="timeline-marker">
          {HeroIcons.render_icon(icon, "28", theme.accent, "2.5")}
        </div>
        <div class="timeline-content">
          <div class="timeline-date">{date}</div>
          <div class="timeline-title">{title}</div>
          {f'<div class="timeline-desc">{description}</div>' if description else ''}
        </div>
      </div>''')
        
        return f'<div class="timeline {orientation}">{"".join(events_html)}</div>'
    
    @staticmethod
    def render_comparison(
        left: Dict[str, Any],
        right: Dict[str, Any],
        theme: Any,
    ) -> str:
        """Render side-by-side comparison."""
        left_label = escape_html(left.get("label", "Before"))
        left_content = escape_html(left.get("content", ""))
        left_stats = escape_html(left.get("stats", ""))
        right_label = escape_html(right.get("label", "After"))
        right_content = escape_html(right.get("content", ""))
        right_stats = escape_html(right.get("stats", ""))

        return f'''<div class="comparison">
      <div class="comparison-side left">
        <div class="comparison-label">{left_label}</div>
        <div class="comparison-content">{left_content}</div>
        {f'<div class="comparison-stats">{left_stats}</div>' if left.get("stats") else ''}
      </div>
      <div class="comparison-divider">
        <div class="vs-badge">VS</div>
      </div>
      <div class="comparison-side right">
        <div class="comparison-label">{right_label}</div>
        <div class="comparison-content">{right_content}</div>
        {f'<div class="comparison-stats highlight">{right_stats}</div>' if right.get("stats") else ''}
      </div>
    </div>'''
    
    @staticmethod
    def render_feature_grid(
        features: List[Dict[str, Any]],
        theme: Any,
        columns: int = 3,
    ) -> str:
        """Render feature grid with icons."""
        features_html = []
        for feature in features:
            icon = feature.get("icon", "sparkles")
            title = escape_html(feature.get("title", ""))
            description = escape_html(feature.get("description", ""))

            features_html.append(f'''<div class="feature-item">
        <div class="feature-icon">
          {HeroIcons.render_icon(icon, "48", theme.accent, "2")}
        </div>
        <div class="feature-title">{title}</div>
        <div class="feature-desc">{description}</div>
      </div>''')
        
        return f'<div class="feature-grid cols-{columns}">{"".join(features_html)}</div>'
    
    @staticmethod
    def render_stats_dashboard(
        stats: List[Dict[str, Any]],
        theme: Any,
    ) -> str:
        """Render stats dashboard with visual elements."""
        stats_html = []
        for stat in stats:
            value = escape_html(stat.get("value", ""))
            label = escape_html(stat.get("label", ""))
            change = escape_html(stat.get("change", ""))
            icon = stat.get("icon", "chart-bar")
            trend = stat.get("trend", "up")  # up, down, neutral

            # Validate trend to prevent CSS injection
            valid_trends = ["up", "down", "neutral"]
            safe_trend = trend if trend in valid_trends else "neutral"
            trend_class = f"trend-{safe_trend}"

            stats_html.append(f'''<div class="stat-card">
        <div class="stat-header">
          <div class="stat-icon">
            {HeroIcons.render_icon(icon, "36", theme.accent, "2")}
          </div>
          {f'<div class="stat-change {trend_class}">{change}</div>' if stat.get("change") else ''}
        </div>
        <div class="stat-value">{value}</div>
        <div class="stat-label">{label}</div>
      </div>''')
        
        return f'<div class="stats-dashboard">{"".join(stats_html)}</div>'
    
    @staticmethod
    def render_progress_bar(
        label: str,
        value: float,
        max_value: float,
        theme: Any,
        show_percentage: bool = True,
    ) -> str:
        """Render progress bar."""
        safe_label = escape_html(label)
        percentage = (value / max_value * 100) if max_value > 0 else 0

        return f'''<div class="progress-bar-container">
      <div class="progress-label">
        <span>{safe_label}</span>
        {f'<span class="progress-percentage">{percentage:.0f}%</span>' if show_percentage else ''}
      </div>
      <div class="progress-track">
        <div class="progress-fill" style="width: {percentage}%;"></div>
      </div>
    </div>'''

