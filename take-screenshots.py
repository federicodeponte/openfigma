#!/usr/bin/env python3
"""Take screenshots of case study HTML files at exact 1080x1350 dimensions."""

import os
import subprocess
from pathlib import Path

# Install playwright if needed
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    subprocess.run(["pip3", "install", "playwright"], check=True)
    subprocess.run(["python3", "-m", "playwright", "install", "chromium"], check=True)
    from playwright.sync_api import sync_playwright

DIAGRAMS_DIR = Path(__file__).parent / "diagrams"
EXPORTS_DIR = Path(__file__).parent / "exports"
EXPORTS_DIR.mkdir(exist_ok=True)

# Case study files to screenshot
case_studies = [
    ("case-study-1-headline.html", "case-study-1.png"),
    ("case-study-2-quote.html", "case-study-2.png"),
    ("case-study-3-metric-10x.html", "case-study-3.png"),
    ("case-study-4-metric-6x.html", "case-study-4.png"),
    ("case-study-5-cta.html", "case-study-5.png"),
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    
    for html_file, png_file in case_studies:
        html_path = DIAGRAMS_DIR / html_file
        if not html_path.exists():
            print(f"Skipping {html_file} - not found")
            continue
            
        # Create page with exact viewport
        page = browser.new_page(viewport={"width": 1080, "height": 1350})
        
        # Load the HTML file
        page.goto(f"file://{html_path.absolute()}")
        page.wait_for_load_state("networkidle")
        
        # Take screenshot
        output_path = EXPORTS_DIR / png_file
        page.screenshot(path=str(output_path), full_page=False)
        print(f"✓ {png_file}")
        
        page.close()
    
    browser.close()

print(f"\nAll screenshots saved to {EXPORTS_DIR}")

