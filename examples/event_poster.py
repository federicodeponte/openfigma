#!/usr/bin/env python3
"""
Event Poster Example - Pioneers-style accelerator poster
Demonstrates: dark theme, dot grid, background SVG, event_poster component
"""

import sys
sys.path.insert(0, '..')

from openfigma import GraphicsBuilder, dark_theme

# Paris skyline SVG (Eiffel Tower + buildings)
PARIS_SKYLINE_SVG = '''<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <!-- Buildings left -->
  <rect x="50" y="400" width="60" height="200"/>
  <rect x="120" y="350" width="80" height="250"/>
  <rect x="210" y="420" width="50" height="180"/>

  <!-- Eiffel Tower -->
  <path d="M450 600 L400 300 L380 300 L370 250 L390 250 L385 200 L400 150 L405 80 L410 150 L425 250 L445 250 L435 300 L415 300 L465 600 Z"/>
  <!-- Tower details -->
  <rect x="395" y="70" width="25" height="10"/>
  <rect x="370" y="350" width="75" height="15"/>
  <rect x="378" y="450" width="60" height="15"/>

  <!-- Buildings right -->
  <rect x="520" y="380" width="70" height="220"/>
  <rect x="600" y="350" width="90" height="250"/>
  <rect x="700" y="420" width="60" height="180"/>

  <!-- Small building details -->
  <rect x="60" y="410" width="10" height="15"/>
  <rect x="80" y="410" width="10" height="15"/>
  <rect x="135" y="360" width="15" height="20"/>
  <rect x="160" y="360" width="15" height="20"/>
  <rect x="185" y="360" width="15" height="20"/>
</svg>'''

# Pioneers icon (pixel/dot pattern)
PIONEERS_ICON = '''<svg width="20" height="20" viewBox="0 0 20 20" fill="currentColor">
  <rect x="2" y="2" width="4" height="4"/>
  <rect x="8" y="2" width="4" height="4"/>
  <rect x="14" y="2" width="4" height="4"/>
  <rect x="2" y="8" width="4" height="4"/>
  <rect x="14" y="8" width="4" height="4"/>
  <rect x="2" y="14" width="4" height="4"/>
  <rect x="8" y="14" width="4" height="4"/>
  <rect x="14" y="14" width="4" height="4"/>
</svg>'''


def create_pioneers_poster():
    """Create a pioneers-style accelerator event poster."""

    # Use dark theme with cyan accents
    theme = dark_theme()
    theme.grid_enabled = True
    theme.grid_size = "25px"
    theme.grid_dot_size = "2px"

    builder = GraphicsBuilder(theme=theme)

    config = {
        "components": [
            # Background city silhouette
            {
                "type": "background_svg",
                "content": {
                    "svg": PARIS_SKYLINE_SVG
                }
            },
            # Main event metrics
            {
                "type": "event_poster",
                "content": {
                    "align": "left",
                    "lines": [
                        {"number": "3", "text": "months", "size": "140px"},
                        {"number": "40", "text": "founders", "size": "140px"},
                        {"number": "100k", "text": "EUR", "size": "140px"},
                    ]
                }
            },
            # Event details
            {
                "type": "subtitle",
                "content": {
                    "text": "16th February - STATION F Paris, FR",
                    "highlight": "STATION F",
                    "align": "left"
                }
            },
            # Logo in corner
            {
                "type": "positioned_logo",
                "content": {
                    "text": "pioneers",
                    "position": "bottom-right",
                    "icon_svg": PIONEERS_ICON
                }
            }
        ]
    }

    return builder.build_from_config(config)


def create_startup_event():
    """Create a generic startup event poster."""

    theme = dark_theme()
    theme.grid_enabled = True
    theme.accent = "#8b5cf6"  # Purple accent
    theme.grid_color = "rgba(139, 92, 246, 0.25)"

    builder = GraphicsBuilder(theme=theme)

    config = {
        "components": [
            {
                "type": "event_poster",
                "content": {
                    "align": "left",
                    "lines": [
                        {"number": "500+", "text": "startups", "size": "120px"},
                        {"number": "50", "text": "investors", "size": "120px"},
                        {"number": "$2M", "text": "in prizes", "size": "120px"},
                    ]
                }
            },
            {
                "type": "subtitle",
                "content": {
                    "text": "March 15-17 - TechHub San Francisco",
                    "highlight": "TechHub",
                    "align": "left"
                }
            },
            {
                "type": "positioned_logo",
                "content": {
                    "text": "STARTUP SUMMIT 2026",
                    "position": "bottom-right"
                }
            }
        ]
    }

    return builder.build_from_config(config)


if __name__ == "__main__":
    # Generate pioneers poster
    html = create_pioneers_poster()

    with open("pioneers_poster.html", "w") as f:
        f.write(html)
    print("Generated: pioneers_poster.html")

    # Generate startup event poster
    html2 = create_startup_event()

    with open("startup_event.html", "w") as f:
        f.write(html2)
    print("Generated: startup_event.html")
