# This module defines an image scraper for sphinx-gallery
# https://sphinx-gallery.github.io/
# which can be used by projects using plotly in their documentation.
import ast
import functools
import logging
import os
import textwrap
import warnings

import plotly
from plotly.basedatatypes import BaseFigure
from plotly.io._base_renderers import sphinx_gallery_figures

plotly.io.renderers.default = "sphinx_gallery_png"

# Fix-up markup for the figures of a code block, both the ones this scraper
# embeds and the repr-captured ones sphinx-gallery embeds itself (both sit in
# an ``output_subarea`` div). The card keeps the light background baked into
# the figures presentable on dark pages, detected via ``data-theme`` (themes
# with a toggle) or the OS preference (theme-less pages); on light pages it is
# invisible. The resize fixes up figures that drew while the page was still
# laying out and so can be sized to a container whose width then changed.
_CARD = "background:#fff;border-radius:0.25rem;padding:0.5rem"
_SELECTOR = "div.output_subarea:has(.plotly-graph-div)"
_FIXUP_HTML = (
    "<style>"
    f'html[data-theme="dark"] {_SELECTOR}{{{_CARD}}}'
    "@media (prefers-color-scheme: dark){"
    f'html:not([data-theme="light"]) {_SELECTOR}{{{_CARD}}}'
    "}"
    "</style>"
    "<script>"
    "if (!window.plotlySphinxGalleryResize) {"
    "window.plotlySphinxGalleryResize = true;"
    'window.addEventListener("load", function () {'
    'document.querySelectorAll(".plotly-graph-div").forEach('
    "function (gd) { Plotly.Plots.resize(gd); });"
    "});"
    "}"
    "</script>"
)


def plotly_sg_scraper(block, block_vars, gallery_conf, **kwargs):
    """Scrape Plotly figures for sphinx-gallery.

    Figures shown with ``fig.show()`` (using the ``sphinx_gallery_png``
    renderer, which importing this module selects) are embedded in the page
    as interactive HTML. Those figures, and ones displayed as the last
    expression of a code block, are also saved as static images for the
    gallery thumbnail when Kaleido is available. For parallel builds, see
    ``reset_renderer``.

    Parameters
    ----------
    block : tuple
        The (label, content, line_number) of the code block.
    block_vars : dict
        Dict of block variables.
    gallery_conf : dict
        Configuration of Sphinx-Gallery (unused, but part of the scraper
        interface).
    **kwargs : dict
        ``format`` sets the static image format, ``"png"`` (default) or
        ``"svg"``.

    Returns
    -------
    rst : str
        The reStructuredText embedding the figures.
    """
    image_format = kwargs.get("format", "png")
    if image_format not in ("png", "svg"):
        raise ValueError(f"format must be one of 'png' or 'svg', got {image_format!r}")
    image_path_iterator = block_vars["image_path_iterator"]
    figures = [(fig_dict, True) for fig_dict in sphinx_gallery_figures]
    repr_figure = _trailing_repr_figure(block, block_vars)
    if repr_figure is not None:
        fig_dict = repr_figure.to_dict()
        # A figure both shown and repr-displayed only needs one image.
        if fig_dict not in sphinx_gallery_figures:
            figures.append((fig_dict, False))
    try:
        export_available = _static_export_available()
        rst = ""
        for fig_dict, shown in figures:
            if export_available:
                # sphinx-gallery requires an image at every path taken from
                # the iterator, so don't consume paths when export failed.
                image_path = next(image_path_iterator)
                path_root = os.path.splitext(image_path)[0]
                _write_image(fig_dict, f"{path_root}.{image_format}", image_format)
            if shown:
                # Repr-displayed figures are embedded by sphinx-gallery
                # itself; their static image only serves as the thumbnail.
                rst += _inline_html(fig_dict)
        if figures:
            rst += _raw_html_rst(_FIXUP_HTML)
        return rst
    finally:
        # Don't let figures leak into the next block if writing one failed.
        del sphinx_gallery_figures[:]


def reset_renderer(gallery_conf, fname, *, when=None):
    """Select the ``sphinx_gallery_png`` renderer before each example.

    Parallel builds with sphinx-gallery < 0.22 need this, as their worker
    processes never import this module: add
    ``"plotly.io.sg_scraper.reset_renderer"`` to ``reset_modules`` in
    ``sphinx_gallery_conf``.
    """
    plotly.io.renderers.default = "sphinx_gallery_png"


def _trailing_repr_figure(block, block_vars):
    """Return the figure displayed via repr capture in this block, if any.

    Sphinx-gallery stores a code block's trailing expression value as ``___``
    in the example globals so that its repr can be embedded in the page.
    """
    figure = block_vars.get("example_globals", {}).get("___")
    if not isinstance(figure, BaseFigure):
        return None
    try:
        body = ast.parse(block[1]).body
    except SyntaxError:
        return None
    # ``___`` survives blocks without a trailing expression, so require one to
    # know the value was set by this block rather than an earlier one.
    if not (body and isinstance(body[-1], ast.Expr)):
        return None
    return figure


# Whether the shared export browser is "unstarted", "running", or "disabled"
_export_server_state = "unstarted"


def _start_export_server():
    """Keep one browser running for the whole build.

    Without it, every static image export launches and tears down a browser
    (~1.5 s each); with it, only the first does (~50 ms each after that).
    Kaleido stops the server atexit.
    """
    global _export_server_state
    if _export_server_state != "unstarted":
        return
    try:
        import kaleido

        from plotly.io import defaults

        # The options plotly.io.to_image would otherwise pass per export.
        kopts = {}
        if defaults.plotlyjs:
            kopts["plotlyjs"] = defaults.plotlyjs
        if defaults.mathjax:
            kopts["mathjax"] = defaults.mathjax
        if getattr(defaults, "headers", None):
            kopts["headers"] = defaults.headers
        kaleido.start_sync_server(silence_warnings=True, **kopts)
    except Exception:
        # Kaleido v0 keeps a persistent instance itself; the probe reports
        # any other problem
        _export_server_state = "disabled"
    else:
        _export_server_state = "running"


def _warn(msg, *args):
    """Log a warning, through Sphinx if possible so that builds can suppress
    it with ``suppress_warnings = ["plotly.sg_scraper"]``."""
    try:
        from sphinx.util.logging import getLogger
    except Exception:
        logging.getLogger(__name__).warning(msg, *args)
    else:
        getLogger(__name__).warning(msg, *args, type="plotly", subtype="sg_scraper")


def _abandon_export_server(exc):
    """Stop using the shared browser; return whether a retry makes sense."""
    global _export_server_state
    if _export_server_state != "running":
        return False
    _export_server_state = "disabled"
    _warn(
        "The shared plotly static image export browser failed with '%s: %s'; "
        "falling back to one browser per exported figure.",
        type(exc).__name__,
        exc,
    )
    try:
        import kaleido

        kaleido.stop_sync_server(silence_warnings=True)
    except Exception:
        pass
    return True


@functools.lru_cache(maxsize=None)  # functools.cache needs Python 3.9
def _static_export_available():
    """Whether static image export works, probed on the first scrape.

    Cached so that a build without Kaleido or a browser warns once (per
    worker, for parallel sphinx-gallery builds) instead of once per figure.
    """
    _start_export_server()
    try:
        _export_image({"data": []}, None, "png")
    except Exception as exc:
        _warn(
            "plotly static image export is unavailable, so example "
            "thumbnails will fall back to a placeholder image. Static "
            "export requires Kaleido and a Chromium-based browser "
            "(the `plotly_get_chrome` command installs one); see "
            "https://plotly.com/python/static-image-export/ for details. "
            "The failure was: %s: %s",
            type(exc).__name__,
            exc,
        )
        return False
    return True


def _inline_html(fig_dict):
    """Embed a figure into the rst directly, rather than via a file.

    The figure is wrapped in the same div that sphinx-gallery wraps captured
    HTML reprs in, so that the fix-up markup applies to both kinds of embed.
    """
    html = plotly.io.to_html(
        fig_dict,
        include_plotlyjs="cdn",
        full_html=False,
        default_width="100%",
        default_height=525,
        validate=False,
    )
    html = (
        '<div class="output_subarea output_html rendered_html output_result">\n'
        f"{html}\n"
        "</div>"
    )
    return _raw_html_rst(html)


def _raw_html_rst(html):
    return "\n.. raw:: html\n\n" + textwrap.indent(html, "    ") + "\n"


def _export_image(fig_dict, file, image_format):
    """Export one static image (to memory when `file` is None)."""

    def export():
        with warnings.catch_warnings():
            # The kopts the export server was started with already apply
            warnings.filterwarnings(
                "ignore", message="The kopts argument", category=UserWarning
            )
            if file is None:
                plotly.io.to_image(fig_dict, format=image_format, validate=False)
            else:
                plotly.io.write_image(
                    fig_dict, file, format=image_format, validate=False
                )

    try:
        export()
    except Exception as exc:
        # The shared browser can die mid-build (seen on CircleCI Linux);
        # retry with one browser per export.
        if not _abandon_export_server(exc):
            raise
        export()


def _write_image(fig_dict, file, image_format):
    """Write a static image, with a helpful message if that is not possible."""
    try:
        _export_image(fig_dict, file, image_format)
    except Exception as exc:
        raise RuntimeError(
            f"Writing {file} failed with:\n{type(exc).__name__}: {exc}\n"
            "See https://plotly.com/python/static-image-export/ for "
            "requirements and installation instructions."
        ) from exc
