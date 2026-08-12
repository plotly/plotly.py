# This module defines an image scraper for sphinx-gallery
# https://sphinx-gallery.github.io/
# which can be used by projects using plotly in their documentation.
import ast
import functools
import logging
import os
import textwrap

import plotly
from plotly.basedatatypes import BaseFigure
from plotly.io._base_renderers import sphinx_gallery_figures

plotly.io.renderers.default = "sphinx_gallery_png"


def plotly_sg_scraper(block, block_vars, gallery_conf, **kwargs):
    """Scrape Plotly figures for galleries of examples using
    sphinx-gallery.

    Examples should use ``plotly.io.show()`` (or the equivalent
    ``fig.show()``) to display the figure with the custom
    ``sphinx_gallery_png`` renderer, which is made the default renderer as a
    side effect of importing this module.

    Every figure shown that way is written to the gallery image directory
    twice: once as an interactive HTML file, which is embedded in the page,
    and once as a static image, which sphinx-gallery uses to generate the
    thumbnail of the example.

    A figure that is instead displayed by making it the last expression of a
    code block (sphinx-gallery's repr capture) gets a static image too, so
    that it can also serve as the thumbnail; its HTML is embedded by
    sphinx-gallery itself.

    Static image export requires Kaleido and a Chromium-based browser; when
    unavailable, a warning is emitted once per build and the examples fall
    back to placeholder thumbnails, with the interactive figures unaffected.

    Parameters
    ----------
    block : tuple
        A tuple containing the (label, content, line_number) of the block.
    block_vars : dict
        Dict of block variables.
    gallery_conf : dict
        Contains the configuration of Sphinx-Gallery
    **kwargs : dict
        Additional keyword arguments.
        The ``format`` kwarg is used to set the file extension
        of the static images (currently only 'png' and 'svg' are supported).

    Returns
    -------
    rst : str
        The ReSTructuredText that will be rendered to HTML containing
        the images.

    Notes
    -----
    Add this function to the image scrapers
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
        if not _static_export_available():
            # No images means no thumbnails, and sphinx-gallery requires an
            # image for every path taken from the iterator, so embed shown
            # figures inline instead of via files.
            return "".join(
                _inline_html(fig_dict) for fig_dict, shown in figures if shown
            )
        html_names = []
        for (fig_dict, shown), image_path in zip(figures, image_path_iterator):
            # sphinx-gallery hands out one path per image; the HTML file sits
            # next to the image it is the interactive counterpart of.
            path_root = os.path.splitext(image_path)[0]
            _write_image(fig_dict, f"{path_root}.{image_format}", image_format)
            if not shown:
                # Repr-displayed: sphinx-gallery embeds the HTML itself, the
                # static image only makes the figure available as a thumbnail.
                continue
            plotly.io.write_html(
                fig_dict,
                file=f"{path_root}.html",
                include_plotlyjs="cdn",
                full_html=False,
                default_width="100%",
                default_height=525,
                validate=False,
            )
            html_names.append(f"{path_root}.html")
        # Use the `figure_rst` helper function to generate rST for image files
        return figure_rst(html_names, gallery_conf["src_dir"])
    finally:
        # Don't let figures leak into the next block if writing one failed.
        del sphinx_gallery_figures[:]


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


# Whether static image export works at all, probed on the first scrape so
# that a build without Kaleido or a browser warns once (per worker, for
# parallel sphinx-gallery builds) instead of once per figure.
_export_available = None


def _static_export_available():
    global _export_available
    if _export_available is None:
        try:
            plotly.io.to_image({"data": []}, format="png", validate=False)
        except Exception as exc:
            _export_available = False
            try:
                from sphinx.util.logging import getLogger

                warn = functools.partial(
                    getLogger(__name__).warning, type="plotly", subtype="sg_scraper"
                )
            except Exception:
                warn = logging.getLogger(__name__).warning
            warn(
                "plotly static image export is unavailable, so example "
                "thumbnails will fall back to a placeholder image. Static "
                "export requires Kaleido and a Chromium-based browser; see "
                "https://plotly.com/python/static-image-export/ for "
                "installation instructions. The failure was: %s: %s",
                type(exc).__name__,
                exc,
            )
        else:
            _export_available = True
    return _export_available


def _inline_html(fig_dict):
    """Embed a figure into the rst directly, rather than via a file."""
    html = plotly.io.to_html(
        fig_dict,
        include_plotlyjs="cdn",
        full_html=False,
        default_width="100%",
        default_height=525,
        validate=False,
    )
    return "\n.. raw:: html\n\n" + textwrap.indent(html, "    ") + "\n"


def _write_image(fig_dict, file, image_format):
    """Write a static image, with a helpful message if that is not possible."""
    try:
        plotly.io.write_image(fig_dict, file, format=image_format, validate=False)
    except Exception as exc:
        raise RuntimeError(
            f"Writing {file} failed with:\n{type(exc).__name__}: {exc}\n"
            "See https://plotly.com/python/static-image-export/ for "
            "requirements and installation instructions."
        ) from exc


def figure_rst(figure_list, sources_dir):
    """Generate RST for a list of HTML filenames.

    Parameters
    ----------
    figure_list : list
        List of strings of the figures' absolute paths.
    sources_dir : str
        absolute path of Sphinx documentation sources (unused, kept for
        compatibility with the equivalent sphinx-gallery helper)

    Returns
    -------
    images_rst : str
        rst code to embed the images in the document
    """
    # The HTML files live in the "images" directory next to the document that
    # includes them, so the paths are relative to that document.
    return "".join(
        SINGLE_HTML % ("images/" + os.path.basename(figure_path))
        for figure_path in figure_list
    )


SINGLE_HTML = """
.. raw:: html
    :file: %s
"""
