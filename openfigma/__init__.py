"""
OpenFigma - Component-based graphics library
Generate beautiful, customizable graphics from JSON config.

Usage:
    from openfigma import GraphicsBuilder, Theme
    
    builder = GraphicsBuilder()
    html = builder.build_from_config(config)
"""

from .components import (
    GraphicsBuilder,
    Theme,
    ComponentRenderer,
    dark_theme,
    linkedin_theme,
)

from .advanced import (
    HeroIcons,
    AdvancedComponentRenderer,
)

from .export import (
    html_to_png,
    export_config_to_png,
    PNGExporter,
)

__version__ = "2.2.0"

__all__ = [
    "GraphicsBuilder",
    "Theme",
    "ComponentRenderer",
    "HeroIcons",
    "AdvancedComponentRenderer",
    "dark_theme",
    "linkedin_theme",
    "html_to_png",
    "export_config_to_png",
    "PNGExporter",
]

