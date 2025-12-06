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
)

from .advanced import (
    HeroIcons,
    AdvancedComponentRenderer,
)

__version__ = "1.0.0"

__all__ = [
    "GraphicsBuilder",
    "Theme",
    "ComponentRenderer",
    "HeroIcons",
    "AdvancedComponentRenderer",
]

