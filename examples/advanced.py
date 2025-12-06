#!/usr/bin/env python3
"""
Test advanced graphics components - proper visual graphics library.
Demonstrates process flows, charts, timelines, comparisons, etc.
"""

import asyncio
import sys
import base64
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from service.graphics_generator import GraphicsGenerator


async def test_advanced_graphics():
    """Test advanced visual graphics."""
    print("🎨 Testing Advanced Visual Graphics Library")
    print("=" * 70)
    
    generator = GraphicsGenerator()
    
    # Test 1: Process Flow with Icons
    print("\n📝 Test 1: Process Flow")
    print("-" * 70)
    
    config_flow = {
        "theme": {
            "accent": "#6366f1",
            "accent_secondary": "#8b5cf6",
        },
        "components": [
            {
                "type": "badge",
                "content": {"text": "Our Process", "icon": "case-study"}
            },
            {
                "type": "process_flow",
                "content": {
                    "steps": [
                        "Discovery & Research",
                        "Strategy Development",
                        "Execution & Launch",
                        "Optimization"
                    ],
                    "orientation": "horizontal",
                    "show_arrows": True
                }
            },
            {
                "type": "logo_card",
                "content": {"client_name": "Client", "provider_name": "SCAILE"}
            }
        ]
    }
    
    result1 = await generator.generate_from_config(config_flow)
    if result1.success:
        if result1.image_url.startswith('data:image'):
            header, encoded = result1.image_url.split(',', 1)
            image_data = base64.b64decode(encoded)
            output_path = Path.home() / "Desktop" / "test_flow.png"
            with open(output_path, 'wb') as f:
                f.write(image_data)
            print(f"✅ Generated! Saved to: {output_path}")
    
    # Test 2: Data Visualization (Bar Chart)
    print("\n📝 Test 2: Bar Chart")
    print("-" * 70)
    
    config_chart = {
        "theme": {
            "accent": "#10b981",
            "accent_secondary": "#059669",
            "gradient_primary": "linear-gradient(135deg, #10b981, #059669)",
        },
        "components": [
            {
                "type": "badge",
                "content": {"text": "Growth Metrics", "icon": "case-study"}
            },
            {
                "type": "headline",
                "content": {
                    "text": "Revenue Growth 2024",
                    "size": "medium",
                    "align": "center"
                }
            },
            {
                "type": "bar_chart",
                "content": {
                    "data": [
                        {"label": "Q1", "value": 250},
                        {"label": "Q2", "value": 380},
                        {"label": "Q3", "value": 520},
                        {"label": "Q4", "value": 680}
                    ],
                    "max_value": 700
                }
            },
            {
                "type": "logo_card",
                "content": {"client_name": "Client", "provider_name": "SCAILE"}
            }
        ]
    }
    
    result2 = await generator.generate_from_config(config_chart)
    if result2.success:
        if result2.image_url.startswith('data:image'):
            header, encoded = result2.image_url.split(',', 1)
            image_data = base64.b64decode(encoded)
            output_path = Path.home() / "Desktop" / "test_chart.png"
            with open(output_path, 'wb') as f:
                f.write(image_data)
            print(f"✅ Generated! Saved to: {output_path}")
    
    # Test 3: Timeline
    print("\n📝 Test 3: Timeline")
    print("-" * 70)
    
    config_timeline = {
        "theme": {
            "accent": "#f59e0b",
            "accent_secondary": "#d97706",
            "gradient_primary": "linear-gradient(135deg, #f59e0b, #d97706)",
        },
        "components": [
            {
                "type": "badge",
                "content": {"text": "Journey", "icon": "case-study"}
            },
            {
                "type": "headline",
                "content": {
                    "text": "Our Story",
                    "size": "large",
                    "align": "center"
                }
            },
            {
                "type": "timeline",
                "content": {
                    "events": [
                        {
                            "date": "Jan 2024",
                            "title": "Partnership Begins",
                            "description": "Kicked off with initial strategy session",
                            "icon": "rocket-launch"
                        },
                        {
                            "date": "Mar 2024",
                            "title": "First Campaign Launch",
                            "description": "Launched comprehensive SEO strategy",
                            "icon": "sparkles"
                        },
                        {
                            "date": "Jun 2024",
                            "title": "Major Milestone",
                            "description": "Achieved 300% traffic increase",
                            "icon": "chart-bar"
                        }
                    ],
                    "orientation": "vertical"
                }
            },
            {
                "type": "logo_card",
                "content": {"client_name": "Client", "provider_name": "SCAILE"}
            }
        ]
    }
    
    result3 = await generator.generate_from_config(config_timeline)
    if result3.success:
        if result3.image_url.startswith('data:image'):
            header, encoded = result3.image_url.split(',', 1)
            image_data = base64.b64decode(encoded)
            output_path = Path.home() / "Desktop" / "test_timeline.png"
            with open(output_path, 'wb') as f:
                f.write(image_data)
            print(f"✅ Generated! Saved to: {output_path}")
    
    # Test 4: Before/After Comparison
    print("\n📝 Test 4: Comparison")
    print("-" * 70)
    
    config_comparison = {
        "theme": {
            "accent": "#3b82f6",
            "accent_secondary": "#2563eb",
        },
        "components": [
            {
                "type": "badge",
                "content": {"text": "Results", "icon": "case-study"}
            },
            {
                "type": "comparison",
                "content": {
                    "left": {
                        "label": "Before",
                        "content": "Manual processes, slow turnaround",
                        "stats": "2-3 weeks"
                    },
                    "right": {
                        "label": "After",
                        "content": "Automated workflows, instant delivery",
                        "stats": "2-3 hours"
                    }
                }
            },
            {
                "type": "logo_card",
                "content": {"client_name": "Client", "provider_name": "SCAILE"}
            }
        ]
    }
    
    result4 = await generator.generate_from_config(config_comparison)
    if result4.success:
        if result4.image_url.startswith('data:image'):
            header, encoded = result4.image_url.split(',', 1)
            image_data = base64.b64decode(encoded)
            output_path = Path.home() / "Desktop" / "test_comparison.png"
            with open(output_path, 'wb') as f:
                f.write(image_data)
            print(f"✅ Generated! Saved to: {output_path}")
    
    # Test 5: Feature Grid with Icons
    print("\n📝 Test 5: Feature Grid")
    print("-" * 70)
    
    config_features = {
        "theme": {
            "accent": "#8b5cf6",
            "accent_secondary": "#7c3aed",
        },
        "components": [
            {
                "type": "badge",
                "content": {"text": "Features", "icon": "case-study"}
            },
            {
                "type": "headline",
                "content": {
                    "text": "What We Offer",
                    "size": "medium"
                }
            },
            {
                "type": "feature_grid",
                "content": {
                    "features": [
                        {
                            "icon": "lightning-bolt",
                            "title": "Fast Delivery",
                            "description": "Get results in hours, not weeks"
                        },
                        {
                            "icon": "shield-check",
                            "title": "Enterprise Security",
                            "description": "Bank-level encryption & compliance"
                        },
                        {
                            "icon": "users",
                            "title": "Expert Support",
                            "description": "24/7 dedicated account management"
                        }
                    ],
                    "columns": 3
                }
            },
            {
                "type": "logo_card",
                "content": {"client_name": "Client", "provider_name": "SCAILE"}
            }
        ]
    }
    
    result5 = await generator.generate_from_config(config_features)
    if result5.success:
        if result5.image_url.startswith('data:image'):
            header, encoded = result5.image_url.split(',', 1)
            image_data = base64.b64decode(encoded)
            output_path = Path.home() / "Desktop" / "test_features.png"
            with open(output_path, 'wb') as f:
                f.write(image_data)
            print(f"✅ Generated! Saved to: {output_path}")
    
    # Test 6: Stats Dashboard
    print("\n📝 Test 6: Stats Dashboard")
    print("-" * 70)
    
    config_stats = {
        "theme": {
            "accent": "#ef4444",
            "accent_secondary": "#dc2626",
            "gradient_primary": "linear-gradient(135deg, #ef4444, #dc2626)",
            "gradient_text": "linear-gradient(135deg, #ef4444, #dc2626)",
        },
        "components": [
            {
                "type": "badge",
                "content": {"text": "Performance", "icon": "case-study"}
            },
            {
                "type": "headline",
                "content": {
                    "text": "Key Metrics",
                    "size": "medium"
                }
            },
            {
                "type": "stats_dashboard",
                "content": {
                    "stats": [
                        {
                            "value": "10x",
                            "label": "Traffic Growth",
                            "change": "+250%",
                            "icon": "arrow-trending-up",
                            "trend": "up"
                        },
                        {
                            "value": "2.4s",
                            "label": "Page Load Time",
                            "change": "-60%",
                            "icon": "lightning-bolt",
                            "trend": "up"
                        },
                        {
                            "value": "94%",
                            "label": "Customer Satisfaction",
                            "change": "+12%",
                            "icon": "check-circle",
                            "trend": "up"
                        }
                    ]
                }
            },
            {
                "type": "logo_card",
                "content": {"client_name": "Client", "provider_name": "SCAILE"}
            }
        ]
    }
    
    result6 = await generator.generate_from_config(config_stats)
    if result6.success:
        if result6.image_url.startswith('data:image'):
            header, encoded = result6.image_url.split(',', 1)
            image_data = base64.b64decode(encoded)
            output_path = Path.home() / "Desktop" / "test_stats.png"
            with open(output_path, 'wb') as f:
                f.write(image_data)
            print(f"✅ Generated! Saved to: {output_path}")
            import subprocess
            subprocess.run(['open', str(output_path)])
    
    print("\n" + "=" * 70)
    print("✅ All tests complete!")
    print("📁 Check your Desktop for 6 graphics:")
    print("   - test_flow.png (Process Flow)")
    print("   - test_chart.png (Bar Chart)")
    print("   - test_timeline.png (Timeline)")
    print("   - test_comparison.png (Before/After)")
    print("   - test_features.png (Feature Grid)")
    print("   - test_stats.png (Stats Dashboard)")


if __name__ == "__main__":
    asyncio.run(test_advanced_graphics())

