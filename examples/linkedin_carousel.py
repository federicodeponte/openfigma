#!/usr/bin/env python3
"""
LinkedIn Carousel Templates - Multi-slide posts
Professional carousel slides for educational content, guides, etc.
"""

import sys
sys.path.insert(0, '..')

from openfigma import GraphicsBuilder, linkedin_theme, Theme


def carousel_cover():
    """Carousel cover slide - hook the reader."""
    theme = linkedin_theme("#8b5cf6")  # Purple
    builder = GraphicsBuilder(theme=theme)

    config = {
        "components": [
            {
                "type": "badge",
                "content": {"text": "Swipe to learn"}
            },
            {
                "type": "headline",
                "content": {
                    "text": "7 Mistakes Killing Your Cold Emails",
                    "size": "xlarge",
                    "align": "center",
                    "bold_parts": ["7 Mistakes", "Cold Emails"]
                }
            },
            {
                "type": "subtitle",
                "content": {
                    "text": "(And how to fix them today)",
                    "align": "center"
                }
            },
            {
                "type": "positioned_logo",
                "content": {
                    "text": "@yourhandle",
                    "position": "bottom-right"
                }
            }
        ]
    }

    return builder.build_from_config(config, dimensions=(1080, 1350))


def carousel_slide(number: int, title: str, description: str, accent: str = "#8b5cf6"):
    """Single carousel content slide."""
    theme = linkedin_theme(accent)
    builder = GraphicsBuilder(theme=theme)

    config = {
        "components": [
            {
                "type": "event_poster",
                "content": {
                    "align": "left",
                    "lines": [
                        {"number": f"#{number}", "text": "", "size": "80px"},
                    ]
                }
            },
            {
                "type": "headline",
                "content": {
                    "text": title,
                    "size": "large",
                    "align": "left"
                }
            },
            {
                "type": "quote_card",
                "content": {
                    "quote": description,
                }
            },
            {
                "type": "positioned_logo",
                "content": {
                    "text": "@yourhandle",
                    "position": "bottom-right"
                }
            }
        ]
    }

    return builder.build_from_config(config, dimensions=(1080, 1350))


def carousel_cta():
    """Carousel final CTA slide."""
    theme = linkedin_theme("#10b981")  # Green for action
    builder = GraphicsBuilder(theme=theme)

    config = {
        "components": [
            {
                "type": "headline",
                "content": {
                    "text": "Found this helpful?",
                    "size": "large",
                    "align": "center"
                }
            },
            {
                "type": "cta_card",
                "content": {
                    "headline": "Let's Connect!",
                    "description": "Follow me for daily tips on sales, marketing, and startup growth.",
                    "button_text": "Follow @yourhandle"
                }
            },
            {
                "type": "feature_grid",
                "content": {
                    "columns": 3,
                    "features": [
                        {"icon": "check-circle", "title": "Like", "description": "If useful"},
                        {"icon": "users", "title": "Share", "description": "Help others"},
                        {"icon": "sparkles", "title": "Save", "description": "For later"},
                    ]
                }
            }
        ]
    }

    return builder.build_from_config(config, dimensions=(1080, 1350))


def hiring_post():
    """We're hiring post."""
    theme = linkedin_theme("#0077b5")
    builder = GraphicsBuilder(theme=theme)

    config = {
        "components": [
            {
                "type": "badge",
                "content": {"text": "We're Hiring!"}
            },
            {
                "type": "headline",
                "content": {
                    "text": "Senior Product Designer",
                    "size": "xlarge",
                    "align": "center"
                }
            },
            {
                "type": "feature_grid",
                "content": {
                    "columns": 2,
                    "features": [
                        {"icon": "cube", "title": "Remote", "description": "Work from anywhere"},
                        {"icon": "chart-bar", "title": "$150-180k", "description": "Competitive salary"},
                        {"icon": "users", "title": "Small Team", "description": "15 people"},
                        {"icon": "rocket-launch", "title": "Series A", "description": "Well funded"},
                    ]
                }
            },
            {
                "type": "cta_card",
                "content": {
                    "headline": "",
                    "description": "Join us in building the future of design tools",
                    "button_text": "Apply Now"
                }
            }
        ]
    }

    return builder.build_from_config(config, dimensions=(1080, 1080))


def achievement_post():
    """Personal achievement/milestone post."""
    theme = linkedin_theme("#f59e0b")  # Gold/amber
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
                    "value": "1M+",
                    "label": "Content Views This Year",
                    "change": "Started posting consistently 12 months ago"
                }
            },
            {
                "type": "timeline",
                "content": {
                    "orientation": "vertical",
                    "events": [
                        {"date": "Jan 2025", "title": "Started posting daily", "icon": "rocket-launch"},
                        {"date": "Jun 2025", "title": "Hit 10K followers", "icon": "users"},
                        {"date": "Dec 2025", "title": "1M+ views milestone", "icon": "sparkles"},
                    ]
                }
            }
        ]
    }

    return builder.build_from_config(config, dimensions=(1080, 1350))


def poll_results():
    """Poll results visualization."""
    theme = linkedin_theme("#0077b5")
    builder = GraphicsBuilder(theme=theme)

    config = {
        "components": [
            {
                "type": "badge",
                "content": {"text": "Poll Results"}
            },
            {
                "type": "headline",
                "content": {
                    "text": "What's your biggest challenge with remote work?",
                    "size": "medium",
                    "align": "center"
                }
            },
            {
                "type": "bar_chart",
                "content": {
                    "data": [
                        {"label": "Communication", "value": 42},
                        {"label": "Focus", "value": 31},
                        {"label": "Work-Life Balance", "value": 18},
                        {"label": "Loneliness", "value": 9},
                    ]
                }
            },
            {
                "type": "subtitle",
                "content": {
                    "text": "2,847 votes • Thanks for participating!",
                    "align": "center"
                }
            }
        ]
    }

    return builder.build_from_config(config, dimensions=(1080, 1080))


if __name__ == "__main__":
    posts = [
        ("carousel_cover.html", carousel_cover()),
        ("carousel_slide_1.html", carousel_slide(1, "Writing novels instead of bullets", "Your emails are too long. Nobody reads walls of text. Keep it under 100 words.")),
        ("carousel_slide_2.html", carousel_slide(2, "No clear CTA", "What do you want them to do? Be specific. One email = one action.")),
        ("carousel_slide_3.html", carousel_slide(3, "Making it about you", "They don't care about your product. They care about their problems. Lead with value.")),
        ("carousel_cta.html", carousel_cta()),
        ("hiring_post.html", hiring_post()),
        ("achievement_post.html", achievement_post()),
        ("poll_results.html", poll_results()),
    ]

    for filename, html in posts:
        with open(filename, "w") as f:
            f.write(html)
        print(f"Generated: {filename}")

    print(f"\nCreated {len(posts)} templates!")
