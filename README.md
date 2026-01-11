# OpenFigma v2.2 - Universal Graphics Library

> Component-based, themeable graphics generation from JSON config. Professional LinkedIn posts, event posters, marketing materials.

## What's New in v2.2

- **Theme Presets**: `dark_theme()` and `linkedin_theme()` for instant professional styling
- **Dot Grid Pattern**: Alternative to line grids for modern aesthetics
- **Background SVG**: Add silhouettes and background shapes
- **Event Poster Components**: Stacked metrics, positioned logos, subtitles
- **Security**: HTML escaping for XSS prevention
- **LinkedIn Templates**: Quote, stats, tips, announcements, comparisons

## Components

### Basic Components
- `badge`: Top badge/label with optional icon
- `headline`: Large headline text with bold/muted parts
- `quote_card`: Testimonial/quote card with author
- `metric_card`: Statistics/metric display with change indicator
- `cta_card`: Call-to-action card with button
- `infographic_card`: Numbered process/steps display
- `logo_card`: Dual-brand footer

### Advanced Components
- `process_flow`: Connected steps with arrows (horizontal/vertical)
- `bar_chart`: Data visualization bars
- `timeline`: Event timeline with icons
- `comparison`: Before/After side-by-side
- `feature_grid`: Icon + text grid layouts (2-4 columns)
- `stats_dashboard`: Multi-metric cards with trends
- `progress_bar`: Progress indicators

### New in v2.2
- `event_poster`: Stacked metric lines (3 months / 40 founders / 100k EUR)
- `subtitle`: Event details with highlighted text
- `positioned_logo`: Logo in any corner
- `background_svg`: Background silhouettes

## Quick Start

### Installation
```bash
pip install -r requirements.txt
playwright install chromium  # For PNG conversion
```

### LinkedIn Post (Professional)
```python
from openfigma import GraphicsBuilder, linkedin_theme

builder = GraphicsBuilder(linkedin_theme())

config = {
    "components": [
        {"type": "badge", "content": {"text": "Career Tips"}},
        {"type": "headline", "content": {
            "text": "5 habits of highly effective leaders",
            "size": "large",
            "align": "center"
        }},
        {"type": "infographic_card", "content": {
            "title": "",
            "items": [
                "They prioritize deep work",
                "They give feedback in real-time",
                "They hire people smarter than themselves"
            ]
        }}
    ]
}

html = builder.build_from_config(config, dimensions=(1080, 1080))
```

### Dark Event Poster
```python
from openfigma import GraphicsBuilder, dark_theme

theme = dark_theme()
theme.grid_enabled = True  # Cyan dot grid

builder = GraphicsBuilder(theme)

config = {
    "components": [
        {"type": "event_poster", "content": {
            "lines": [
                {"number": "3", "text": "months", "size": "140px"},
                {"number": "40", "text": "founders", "size": "140px"},
                {"number": "100k", "text": "EUR", "size": "140px"},
            ]
        }},
        {"type": "subtitle", "content": {
            "text": "16th February - STATION F Paris, FR",
            "highlight": "STATION F"
        }},
        {"type": "positioned_logo", "content": {
            "text": "pioneers",
            "position": "bottom-right"
        }}
    ]
}

html = builder.build_from_config(config)
```

## Theme Presets

### LinkedIn Theme (Clean, Professional)
```python
from openfigma import linkedin_theme

# Default LinkedIn blue
theme = linkedin_theme()

# Custom accent colors
theme = linkedin_theme("#10b981")  # Green
theme = linkedin_theme("#8b5cf6")  # Purple
theme = linkedin_theme("#f59e0b")  # Orange
```

### Dark Theme (Event Posters)
```python
from openfigma import dark_theme

theme = dark_theme()
theme.grid_enabled = True      # Cyan dot grid
theme.grid_size = "25px"       # Grid spacing
theme.accent = "#22d3ee"       # Cyan accent
```

## Theme Options

```python
Theme(
    # Colors
    background="#ffffff",
    surface="#f8fafc",
    text_primary="#0f172a",
    text_secondary="#475569",
    accent="#0077b5",

    # Fonts
    font_family="'Inter', sans-serif",
    font_headline="800",

    # Grid
    grid_enabled=False,
    grid_style="dots",      # "dots" or "lines"
    grid_color="rgba(0,0,0,0.1)",
    grid_size="20px",

    # Background
    background_svg=None,    # SVG content for silhouettes
)
```

## Examples

See `examples/` folder:
- `linkedin_posts.py` - 6 LinkedIn post templates
- `linkedin_carousel.py` - Carousel slides, hiring posts, poll results
- `event_poster.py` - Dark event poster with city skyline

## Security

All user content is HTML-escaped to prevent XSS attacks. Input validation is applied to CSS class names and positions.

## Use Cases

- LinkedIn posts and carousels
- Event/conference posters
- Quote graphics
- Statistics highlights
- Job posting graphics
- Achievement announcements
- Before/after comparisons
- Process diagrams

## License

MIT - Use freely for your own projects.

---

v2.2.0 - LinkedIn templates, dark theme, security hardening
