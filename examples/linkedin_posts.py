#!/usr/bin/env python3
"""
LinkedIn Professional Post Templates - Canva-style
Clean, professional graphics for LinkedIn posts and carousels.
"""

import sys
sys.path.insert(0, '..')

from openfigma import GraphicsBuilder, Theme


def linkedin_theme() -> Theme:
    """Clean professional LinkedIn theme."""
    return Theme(
        background="#ffffff",
        surface="#f8fafc",
        text_primary="#0f172a",
        text_secondary="#475569",
        text_muted="#94a3b8",
        accent="#0077b5",  # LinkedIn blue
        accent_secondary="#00a0dc",
        border="#e2e8f0",
        border_light="#f1f5f9",
        gradient_primary="linear-gradient(135deg, #0077b5, #00a0dc)",
        gradient_text="linear-gradient(135deg, #0077b5, #00a0dc)",
        shadow_small="0 1px 3px rgba(0,0,0,0.08)",
        shadow_medium="0 4px 12px rgba(0,119,181,0.15)",
        grid_enabled=False,
    )


def quote_post():
    """Professional quote/testimonial post."""
    theme = linkedin_theme()
    builder = GraphicsBuilder(theme=theme)

    config = {
        "components": [
            {
                "type": "badge",
                "content": {"text": "Leadership Insight", "icon": "process"}
            },
            {
                "type": "quote_card",
                "content": {
                    "quote": "The best way to predict the future is to create it. Stop waiting for opportunities — build them.",
                    "author": "Sarah Chen",
                    "role": "CEO at TechVentures",
                    "emphasis": ["create it", "build them"]
                }
            },
            {
                "type": "logo_card",
                "content": {
                    "client_name": "TechVentures",
                    "provider_name": "LinkedIn"
                }
            }
        ]
    }

    return builder.build_from_config(config, dimensions=(1080, 1080))


def stats_post():
    """Statistics highlight post."""
    theme = linkedin_theme()
    theme.accent = "#10b981"  # Green for growth
    theme.gradient_primary = "linear-gradient(135deg, #10b981, #059669)"
    theme.gradient_text = "linear-gradient(135deg, #10b981, #059669)"

    builder = GraphicsBuilder(theme=theme)

    config = {
        "components": [
            {
                "type": "badge",
                "content": {"text": "2024 Results"}
            },
            {
                "type": "headline",
                "content": {
                    "text": "We helped 500+ startups scale their growth",
                    "size": "large",
                    "align": "center",
                    "muted_parts": ["We helped", "scale their growth"]
                }
            },
            {
                "type": "stats_dashboard",
                "content": {
                    "stats": [
                        {"value": "500+", "label": "Startups Helped", "icon": "rocket-launch", "change": "+127%", "trend": "up"},
                        {"value": "$2.4B", "label": "Funding Raised", "icon": "chart-bar", "change": "+89%", "trend": "up"},
                        {"value": "98%", "label": "Success Rate", "icon": "check-circle", "change": "+12%", "trend": "up"},
                    ]
                }
            }
        ]
    }

    return builder.build_from_config(config, dimensions=(1080, 1080))


def tips_post():
    """Tips/listicle post."""
    theme = linkedin_theme()
    theme.accent = "#8b5cf6"  # Purple
    theme.gradient_primary = "linear-gradient(135deg, #8b5cf6, #7c3aed)"
    theme.gradient_text = "linear-gradient(135deg, #8b5cf6, #7c3aed)"

    builder = GraphicsBuilder(theme=theme)

    config = {
        "components": [
            {
                "type": "badge",
                "content": {"text": "Career Tips", "icon": "process"}
            },
            {
                "type": "headline",
                "content": {
                    "text": "5 habits of highly effective leaders",
                    "size": "medium",
                    "align": "center",
                    "bold_parts": ["5 habits", "highly effective leaders"]
                }
            },
            {
                "type": "infographic_card",
                "content": {
                    "title": "",
                    "items": [
                        "They prioritize deep work over busywork",
                        "They give feedback in real-time",
                        "They hire people smarter than themselves",
                        "They protect their team's time",
                        "They celebrate small wins publicly"
                    ]
                }
            }
        ]
    }

    return builder.build_from_config(config, dimensions=(1080, 1350))


def announcement_post():
    """Professional announcement post."""
    theme = linkedin_theme()
    builder = GraphicsBuilder(theme=theme)

    config = {
        "components": [
            {
                "type": "badge",
                "content": {"text": "Announcement"}
            },
            {
                "type": "headline",
                "content": {
                    "text": "I'm thrilled to announce I've joined Acme Corp as Head of Product",
                    "size": "large",
                    "align": "center",
                    "bold_parts": ["thrilled", "Acme Corp", "Head of Product"]
                }
            },
            {
                "type": "cta_card",
                "content": {
                    "headline": "New Chapter",
                    "description": "After 5 amazing years at StartupXYZ, I'm excited to take on this new challenge. Grateful for everyone who supported me on this journey.",
                    "button_text": "Let's Connect"
                }
            }
        ]
    }

    return builder.build_from_config(config, dimensions=(1080, 1080))


def comparison_post():
    """Before/After comparison post."""
    theme = linkedin_theme()
    theme.accent = "#f59e0b"  # Orange/amber
    theme.gradient_primary = "linear-gradient(135deg, #f59e0b, #d97706)"
    theme.gradient_text = "linear-gradient(135deg, #f59e0b, #d97706)"

    builder = GraphicsBuilder(theme=theme)

    config = {
        "components": [
            {
                "type": "badge",
                "content": {"text": "Mindset Shift"}
            },
            {
                "type": "headline",
                "content": {
                    "text": "What changed when I stopped chasing perfection",
                    "size": "medium",
                    "align": "center",
                    "bold_parts": ["stopped chasing perfection"]
                }
            },
            {
                "type": "comparison",
                "content": {
                    "left": {
                        "label": "Before",
                        "content": "Spent weeks polishing every detail. Shipped rarely. Burned out constantly.",
                        "stats": "2 launches/year"
                    },
                    "right": {
                        "label": "After",
                        "content": "Ship fast, iterate faster. Learn from real feedback. Stay energized.",
                        "stats": "12 launches/year"
                    }
                }
            }
        ]
    }

    return builder.build_from_config(config, dimensions=(1080, 1080))


def metric_highlight():
    """Single metric highlight post."""
    theme = linkedin_theme()
    builder = GraphicsBuilder(theme=theme)

    config = {
        "components": [
            {
                "type": "badge",
                "content": {"text": "Milestone"}
            },
            {
                "type": "metric_card",
                "content": {
                    "value": "10K",
                    "label": "Newsletter Subscribers",
                    "change": "Started from 0 just 6 months ago"
                }
            },
            {
                "type": "subtitle",
                "content": {
                    "text": "Thank you for being part of this journey!",
                    "align": "center"
                }
            }
        ]
    }

    return builder.build_from_config(config, dimensions=(1080, 1080))


if __name__ == "__main__":
    posts = [
        ("linkedin_quote.html", quote_post()),
        ("linkedin_stats.html", stats_post()),
        ("linkedin_tips.html", tips_post()),
        ("linkedin_announcement.html", announcement_post()),
        ("linkedin_comparison.html", comparison_post()),
        ("linkedin_metric.html", metric_highlight()),
    ]

    for filename, html in posts:
        with open(filename, "w") as f:
            f.write(html)
        print(f"Generated: {filename}")

    print(f"\nCreated {len(posts)} LinkedIn post templates!")
