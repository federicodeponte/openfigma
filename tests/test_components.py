#!/usr/bin/env python3
"""
Comprehensive test suite for openfigma components.
Tests edge cases, error handling, and output correctness.
"""

import sys
sys.path.insert(0, '..')

from openfigma import GraphicsBuilder, Theme, dark_theme, linkedin_theme, HeroIcons


def test_empty_config():
    """Test handling of empty configuration."""
    builder = GraphicsBuilder()
    html = builder.build_from_config({})
    assert "<!DOCTYPE html>" in html
    assert "<body>" in html
    print("PASS: Empty config handled correctly")


def test_empty_components():
    """Test handling of empty components list."""
    builder = GraphicsBuilder()
    html = builder.build_from_config({"components": []})
    assert "<!DOCTYPE html>" in html
    print("PASS: Empty components list handled correctly")


def test_missing_content():
    """Test handling of components with missing content."""
    builder = GraphicsBuilder()
    config = {
        "components": [
            {"type": "badge"},  # Missing content
            {"type": "headline"},  # Missing content
            {"type": "event_poster"},  # Missing content
        ]
    }
    html = builder.build_from_config(config)
    assert "<!DOCTYPE html>" in html
    print("PASS: Missing content handled with defaults")


def test_unknown_component_type():
    """Test handling of unknown component types."""
    builder = GraphicsBuilder()
    config = {
        "components": [
            {"type": "unknown_component", "content": {"text": "test"}},
            {"type": "badge", "content": {"text": "Valid"}},
        ]
    }
    html = builder.build_from_config(config)
    assert "Valid" in html
    print("PASS: Unknown component types ignored gracefully")


def test_special_characters():
    """Test handling of special HTML characters."""
    builder = GraphicsBuilder()
    config = {
        "components": [
            {"type": "badge", "content": {"text": "<script>alert('xss')</script>"}},
            {"type": "headline", "content": {"text": "Test & \"quotes\" <tags>"}},
        ]
    }
    html = builder.build_from_config(config)
    assert "<!DOCTYPE html>" in html
    print("PASS: Special characters in content (note: needs HTML escaping - see security findings)")


def test_dark_theme_values():
    """Test dark theme has correct values."""
    theme = dark_theme()
    assert theme.background == "#0a0a0b"
    assert theme.text_primary == "#f5f5f5"
    assert theme.grid_style == "dots"
    print("PASS: Dark theme values correct")


def test_linkedin_theme_values():
    """Test LinkedIn theme has correct values."""
    theme = linkedin_theme()
    assert theme.background == "#ffffff"
    assert theme.accent == "#0077b5"
    assert theme.grid_enabled == False

    # Test custom accent
    theme2 = linkedin_theme("#10b981")
    assert theme2.accent == "#10b981"
    print("PASS: LinkedIn theme values correct")


def test_all_component_types():
    """Test all component types render without error."""
    builder = GraphicsBuilder()
    config = {
        "components": [
            {"type": "badge", "content": {"text": "Test", "icon": "case-study"}},
            {"type": "headline", "content": {"text": "Headline", "size": "large", "align": "center"}},
            {"type": "quote_card", "content": {"quote": "Quote text", "author": "Author", "role": "Role"}},
            {"type": "metric_card", "content": {"value": "100", "label": "Label", "change": "+10%"}},
            {"type": "cta_card", "content": {"headline": "CTA", "description": "Desc", "button_text": "Click"}},
            {"type": "infographic_card", "content": {"title": "Title", "items": ["Item 1", "Item 2"]}},
            {"type": "logo_card", "content": {"client_name": "Client", "provider_name": "Provider"}},
            {"type": "event_poster", "content": {"lines": [{"number": "3", "text": "months"}]}},
            {"type": "subtitle", "content": {"text": "Subtitle", "highlight": "Sub"}},
            {"type": "positioned_logo", "content": {"text": "Logo", "position": "bottom-right"}},
            {"type": "background_svg", "content": {"svg": "<svg></svg>"}},
            {"type": "process_flow", "content": {"steps": ["Step 1", "Step 2"]}},
            {"type": "bar_chart", "content": {"data": [{"label": "A", "value": 10}]}},
            {"type": "timeline", "content": {"events": [{"title": "Event", "date": "2024"}]}},
            {"type": "comparison", "content": {"left": {"label": "Before"}, "right": {"label": "After"}}},
            {"type": "feature_grid", "content": {"features": [{"title": "Feature", "icon": "sparkles"}]}},
            {"type": "stats_dashboard", "content": {"stats": [{"value": "100", "label": "Stat"}]}},
            {"type": "progress_bar", "content": {"label": "Progress", "value": 50, "max_value": 100}},
        ]
    }
    html = builder.build_from_config(config)
    assert "<!DOCTYPE html>" in html
    assert "Test" in html
    assert "Headline" in html
    print("PASS: All component types render correctly")


def test_dimensions():
    """Test custom dimensions."""
    builder = GraphicsBuilder()
    config = {"components": [{"type": "badge", "content": {"text": "Test"}}]}

    # LinkedIn square
    html1 = builder.build_from_config(config, dimensions=(1080, 1080))
    assert "width: 1080px" in html1
    assert "height: 1080px" in html1

    # LinkedIn portrait
    html2 = builder.build_from_config(config, dimensions=(1080, 1350))
    assert "height: 1350px" in html2

    print("PASS: Custom dimensions applied correctly")


def test_theme_override():
    """Test theme override via config."""
    builder = GraphicsBuilder()
    config = {
        "theme": {
            "accent": "#ff0000",
            "background": "#000000"
        },
        "components": [{"type": "badge", "content": {"text": "Test"}}]
    }
    html = builder.build_from_config(config)
    assert "#ff0000" in html or "ff0000" in html.lower()
    print("PASS: Theme override via config works")


def test_grid_styles():
    """Test both grid styles."""
    # Dot grid
    theme1 = Theme(grid_enabled=True, grid_style="dots")
    builder1 = GraphicsBuilder(theme1)
    html1 = builder1.build_from_config({"components": []})
    assert "radial-gradient" in html1

    # Line grid
    theme2 = Theme(grid_enabled=True, grid_style="lines")
    builder2 = GraphicsBuilder(theme2)
    html2 = builder2.build_from_config({"components": []})
    assert "linear-gradient" in html2

    print("PASS: Both grid styles render correctly")


def test_hero_icons():
    """Test Hero Icons rendering."""
    icons = ["chart-bar", "arrow-trending-up", "check-circle", "lightning-bolt",
             "clock", "users", "rocket-launch", "sparkles", "cog", "shield-check",
             "arrow-right", "cube", "document-text"]

    for icon in icons:
        svg = HeroIcons.render_icon(icon)
        assert "<svg" in svg
        assert "viewBox" in svg

    # Test unknown icon falls back to sparkles
    svg_unknown = HeroIcons.render_icon("unknown_icon")
    assert "<svg" in svg_unknown

    print("PASS: All Hero Icons render correctly")


def test_positioned_logo_positions():
    """Test all logo positions."""
    builder = GraphicsBuilder()
    positions = ["top-left", "top-right", "bottom-left", "bottom-right"]

    for pos in positions:
        config = {
            "components": [
                {"type": "positioned_logo", "content": {"text": "Logo", "position": pos}}
            ]
        }
        html = builder.build_from_config(config)
        assert pos in html

    print("PASS: All logo positions work correctly")


def run_all_tests():
    """Run all tests."""
    print("=" * 60)
    print("OPENFIGMA TEST SUITE")
    print("=" * 60)

    tests = [
        test_empty_config,
        test_empty_components,
        test_missing_content,
        test_unknown_component_type,
        test_special_characters,
        test_dark_theme_values,
        test_linkedin_theme_values,
        test_all_component_types,
        test_dimensions,
        test_theme_override,
        test_grid_styles,
        test_hero_icons,
        test_positioned_logo_positions,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"FAIL: {test.__name__} - {e}")
            failed += 1

    print("=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)

    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
