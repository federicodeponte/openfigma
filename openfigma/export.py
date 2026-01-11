"""
PNG Export Module - Convert HTML graphics to PNG images.
Uses Playwright for headless browser rendering.
"""

import os
import tempfile
from pathlib import Path
from typing import Optional, Union


def html_to_png(
    html: str,
    output_path: Optional[str] = None,
    width: int = 1920,
    height: int = 1080,
) -> bytes:
    """
    Convert HTML to PNG image.

    Args:
        html: HTML string to render
        output_path: Optional path to save PNG file
        width: Viewport width (default 1920)
        height: Viewport height (default 1080)

    Returns:
        PNG image bytes
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        raise ImportError(
            "Playwright is required for PNG export. "
            "Install with: pip install playwright && playwright install chromium"
        )

    png_bytes = None

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": width, "height": height})

        # Write HTML to temp file and load it
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            f.write(html)
            temp_path = f.name

        try:
            page.goto(f"file://{temp_path}")
            page.wait_for_load_state("networkidle")

            # Take screenshot
            png_bytes = page.screenshot(type="png")

            if output_path:
                with open(output_path, 'wb') as f:
                    f.write(png_bytes)

        finally:
            os.unlink(temp_path)
            browser.close()

    return png_bytes


def export_config_to_png(
    config: dict,
    output_path: str,
    dimensions: tuple = (1920, 1080),
    theme=None,
) -> str:
    """
    Build graphic from config and export directly to PNG.

    Args:
        config: Component configuration dict
        output_path: Path to save PNG file
        dimensions: (width, height) tuple
        theme: Optional Theme object

    Returns:
        Path to saved PNG file
    """
    from .components import GraphicsBuilder

    builder = GraphicsBuilder(theme=theme)
    html = builder.build_from_config(config, dimensions=dimensions)

    html_to_png(html, output_path, width=dimensions[0], height=dimensions[1])
    return output_path


class PNGExporter:
    """Batch PNG exporter with browser reuse for performance."""

    def __init__(self):
        self._playwright = None
        self._browser = None

    def __enter__(self):
        from playwright.sync_api import sync_playwright
        self._playwright = sync_playwright().start()
        self._browser = self._playwright.chromium.launch()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._browser:
            self._browser.close()
        if self._playwright:
            self._playwright.stop()

    def export(
        self,
        html: str,
        output_path: str,
        width: int = 1920,
        height: int = 1080,
    ) -> str:
        """Export single HTML to PNG."""
        if not self._browser:
            raise RuntimeError("PNGExporter must be used as context manager")

        page = self._browser.new_page(viewport={"width": width, "height": height})

        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False) as f:
            f.write(html)
            temp_path = f.name

        try:
            page.goto(f"file://{temp_path}")
            page.wait_for_load_state("networkidle")
            page.screenshot(path=output_path, type="png")
        finally:
            os.unlink(temp_path)
            page.close()

        return output_path

    def export_batch(
        self,
        items: list,
        output_dir: str,
        dimensions: tuple = (1920, 1080),
    ) -> list:
        """
        Export multiple graphics to PNG.

        Args:
            items: List of (name, html) tuples or (name, config) tuples
            output_dir: Directory to save PNG files
            dimensions: (width, height) tuple

        Returns:
            List of saved file paths
        """
        from .components import GraphicsBuilder

        Path(output_dir).mkdir(parents=True, exist_ok=True)
        saved_paths = []

        for item in items:
            name, content = item

            # If content is a dict, build HTML from config
            if isinstance(content, dict):
                builder = GraphicsBuilder()
                html = builder.build_from_config(content, dimensions=dimensions)
            else:
                html = content

            output_path = os.path.join(output_dir, f"{name}.png")
            self.export(html, output_path, width=dimensions[0], height=dimensions[1])
            saved_paths.append(output_path)

        return saved_paths
