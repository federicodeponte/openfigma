# OpenFigma v2 - Universal Graphics Library

> Component-based, themeable graphics generation from JSON config. DRY components, Hero Icons, full customization.

## 🎨 What's New in v2

- **Component System**: Reusable, composable components
- **JSON Config**: Build any graphic from config
- **Theme Support**: Colors, fonts, spacing per client
- **Hero Icons**: 12+ built-in icons
- **Advanced Components**: Charts, flows, timelines, comparisons
- **Scalable**: Works for any business/use case

## 📦 Components

### Basic Components
- `badge`: Top badge/label
- `headline`: Large headline text
- `quote_card`: Testimonial/quote card
- `metric_card`: Statistics/metric display
- `cta_card`: Call-to-action card
- `infographic_card`: Process/steps display
- `logo_card`: Branding footer

### Advanced Components
- `process_flow`: Connected steps with arrows
- `bar_chart`: Data visualization
- `timeline`: Event timeline with icons
- `comparison`: Before/After side-by-side
- `feature_grid`: Icon + text grid layouts
- `stats_dashboard`: Multi-metric displays
- `progress_bar`: Progress indicators

## 🚀 Quick Start

### Installation
```bash
pip install -r requirements.txt
playwright install chromium  # For PNG conversion
```

### Basic Usage
```python
from openfigma import GraphicsBuilder

builder = GraphicsBuilder()

config = {
    "theme": {
        "accent": "#6366f1",
        "background": "#ffffff"
    },
    "components": [
        {
            "type": "badge",
            "content": {"text": "Case Study", "icon": "case-study"}
        },
        {
            "type": "headline",
            "content": {"text": "Amazing Results", "size": "large"}
        },
        {
            "type": "logo_card",
            "content": {
                "client_name": "TechCorp",
                "provider_name": "SCAILE"
            }
        }
    ]
}

html = builder.build_from_config(config)
# Returns HTML that can be converted to PNG
```

### Custom Theme
```python
from openfigma import GraphicsBuilder, Theme

custom_theme = Theme(
    accent="#ff6b6b",
    background="#1a1a1a",
    text_primary="#ffffff",
    grid_enabled=False
)

builder = GraphicsBuilder(theme=custom_theme)
html = builder.build_from_config(config)
```

## 📊 Examples

See `examples/` folder for complete examples:
- `basic.py` - Simple graphics
- `advanced.py` - Charts, flows, timelines
- `custom_theme.py` - Brand-specific themes

## 🎨 Theme Options

```python
Theme(
    # Colors
    accent="#6366f1",
    background="#f8f8f8",
    surface="#ffffff",
    text_primary="#1a1a1a",
    
    # Fonts
    font_family="'Inter', sans-serif",
    font_headline="800",
    
    # Spacing
    padding_large="60px",
    gap_medium="24px",
    
    # Grid
    grid_enabled=False,
    
    # ... 30+ options
)
```

## 🎯 Use Cases

- Blog graphics
- Social media posts
- Marketing materials
- Case study visuals
- Dashboard screenshots
- Process diagrams
- Data visualizations

## 📄 License

MIT - Use freely for your own projects.

## 🔗 Links

- [Blog Writer (openblog)](https://github.com/federicodeponte/openblog) - Uses openfigma
- [Original v1](./diagrams/) - AI/ML pipeline diagrams

---

v2.0 - Rebuilt as universal graphics library
