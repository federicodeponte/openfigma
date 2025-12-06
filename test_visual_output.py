#!/usr/bin/env python3
"""
Visual quality test - generate actual PNG outputs for inspection.
"""

import asyncio
import base64
from pathlib import Path

# Test if we can import from installed package
try:
    from openfigma import GraphicsBuilder
    print("✅ Imported from installed openfigma package")
except ImportError:
    # Fallback to local
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from openfigma import GraphicsBuilder
    print("✅ Imported from local openfigma")

from playwright.async_api import async_playwright


async def html_to_png(html: str, output_path: Path):
    """Convert HTML to PNG."""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        try:
            page = await browser.new_page(viewport={"width": 1920, "height": 1080})
            await page.set_content(html, wait_until="networkidle")
            await page.screenshot(path=str(output_path), full_page=False, type="png")
        finally:
            await browser.close()


async def test_visual_quality():
    """Generate real PNGs and inspect quality."""
    print("🎨 Visual Quality Test - Generating PNGs")
    print("=" * 70)
    
    builder = GraphicsBuilder()
    output_dir = Path.home() / "Desktop" / "openfigma_audit"
    output_dir.mkdir(exist_ok=True)
    
    # Test 1: Dark theme hero
    print("\n1️⃣  Dark theme hero...")
    config1 = {
        "theme": {
            "background": "#0a0a0b",
            "surface": "rgba(255, 255, 255, 0.03)",
            "text_primary": "#f5f5f5",
            "text_secondary": "rgba(255, 255, 255, 0.6)",
            "accent": "#6366f1",
            "border": "rgba(255, 255, 255, 0.06)",
        },
        "components": [
            {"type": "badge", "content": {"text": "Case Study", "icon": "case-study"}},
            {"type": "headline", "content": {"text": "10x Revenue Growth in 6 Months", "size": "xlarge"}},
            {"type": "logo_card", "content": {"client_name": "TechCorp", "provider_name": "SCAILE"}}
        ]
    }
    html1 = builder.build_from_config(config1)
    await html_to_png(html1, output_dir / "1_hero_dark.png")
    print(f"   ✅ Saved: {output_dir / '1_hero_dark.png'}")
    
    # Test 2: Light theme stats
    print("\n2️⃣  Light theme stats dashboard...")
    config2 = {
        "theme": {
            "background": "#ffffff",
            "accent": "#10b981",
        },
        "components": [
            {"type": "badge", "content": {"text": "Performance", "icon": "case-study"}},
            {"type": "headline", "content": {"text": "Key Results", "size": "large"}},
            {
                "type": "stats_dashboard",
                "content": {
                    "stats": [
                        {"value": "10x", "label": "Growth", "change": "+900%", "icon": "arrow-trending-up", "trend": "up"},
                        {"value": "2.4M", "label": "Users", "change": "+850%", "icon": "users", "trend": "up"},
                        {"value": "97%", "label": "Retention", "change": "+15%", "icon": "check-circle", "trend": "up"}
                    ]
                }
            }
        ]
    }
    html2 = builder.build_from_config(config2)
    await html_to_png(html2, output_dir / "2_stats_light.png")
    print(f"   ✅ Saved: {output_dir / '2_stats_light.png'}")
    
    # Test 3: Process flow
    print("\n3️⃣  Process flow...")
    config3 = {
        "theme": {"accent": "#8b5cf6"},
        "components": [
            {"type": "badge", "content": {"text": "Process", "icon": "process"}},
            {"type": "headline", "content": {"text": "4-Step Transformation", "size": "medium"}},
            {
                "type": "process_flow",
                "content": {
                    "steps": ["Discover", "Design", "Implement", "Optimize"],
                    "orientation": "horizontal",
                    "show_arrows": True
                }
            }
        ]
    }
    html3 = builder.build_from_config(config3)
    await html_to_png(html3, output_dir / "3_process.png")
    print(f"   ✅ Saved: {output_dir / '3_process.png'}")
    
    # Test 4: Data chart
    print("\n4️⃣  Bar chart...")
    config4 = {
        "theme": {"accent": "#f59e0b"},
        "components": [
            {"type": "headline", "content": {"text": "Quarterly Revenue Growth", "size": "medium"}},
            {
                "type": "bar_chart",
                "content": {
                    "data": [
                        {"label": "Q1", "value": 100},
                        {"label": "Q2", "value": 320},
                        {"label": "Q3", "value": 680},
                        {"label": "Q4", "value": 1000}
                    ]
                }
            }
        ]
    }
    html4 = builder.build_from_config(config4)
    await html_to_png(html4, output_dir / "4_chart.png")
    print(f"   ✅ Saved: {output_dir / '4_chart.png'}")
    
    # Test 5: Before/After
    print("\n5️⃣  Comparison...")
    config5 = {
        "theme": {"accent": "#ef4444"},
        "components": [
            {"type": "badge", "content": {"text": "Results", "icon": "case-study"}},
            {
                "type": "comparison",
                "content": {
                    "left": {"label": "Before", "content": "Manual processes, slow growth", "stats": "$100K MRR"},
                    "right": {"label": "After", "content": "Automated systems, rapid scaling", "stats": "$1M MRR"}
                }
            }
        ]
    }
    html5 = builder.build_from_config(config5)
    await html_to_png(html5, output_dir / "5_comparison.png")
    print(f"   ✅ Saved: {output_dir / '5_comparison.png'}")
    
    # Test 6: Feature grid
    print("\n6️⃣  Feature grid...")
    config6 = {
        "theme": {"accent": "#3b82f6"},
        "components": [
            {"type": "headline", "content": {"text": "Our Services", "size": "medium"}},
            {
                "type": "feature_grid",
                "content": {
                    "features": [
                        {"icon": "lightning-bolt", "title": "Fast", "description": "Results in hours"},
                        {"icon": "shield-check", "title": "Secure", "description": "Enterprise-grade"},
                        {"icon": "sparkles", "title": "AI-Powered", "description": "Advanced automation"}
                    ],
                    "columns": 3
                }
            }
        ]
    }
    html6 = builder.build_from_config(config6)
    await html_to_png(html6, output_dir / "6_features.png")
    print(f"   ✅ Saved: {output_dir / '6_features.png'}")
    
    print("\n" + "=" * 70)
    print(f"✅ Generated 6 graphics in: {output_dir}")
    print(f"📂 Opening folder...")
    
    import subprocess
    subprocess.run(["open", str(output_dir)])


if __name__ == "__main__":
    asyncio.run(test_visual_quality())

