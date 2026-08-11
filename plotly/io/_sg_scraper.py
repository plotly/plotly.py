# This module defines an image scraper for sphinx-gallery
# https://sphinx-gallery.github.io/
# which can be used by projects using plotly in their documentation.
import os

import plotly
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
    html_names = []
    try:
        for fig_dict, image_path in zip(sphinx_gallery_figures, image_path_iterator):
            # sphinx-gallery hands out one path per image; the HTML file sits
            # next to the image it is the interactive counterpart of.
            path_root = os.path.splitext(image_path)[0]
            _write_image(fig_dict, f"{path_root}.{image_format}", image_format)
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
    finally:
        # Don't let figures leak into the next block if writing one failed.
        del sphinx_gallery_figures[:]
    # Use the `figure_rst` helper function to generate rST for image files
    return figure_rst(html_names, gallery_conf["src_dir"])


def _write_image(fig_dict, file, image_format):
    """Write a static image, with a helpful message if that is not possible."""
    try:
        plotly.io.write_image(fig_dict, file, format=image_format, validate=False)
    except Exception as exc:
        raise RuntimeError(
            f"Kaleido and a compatible browser are required to use the "
            f"`sphinx_gallery_png` renderer, but writing {file} failed with: "
            f"{type(exc).__name__}: {exc}\n"
            "See https://plotly.com/python/static-image-export/ for "
            "installation instructions. Alternatively, you can use the "
            "`sphinx_gallery` renderer without this scraper (note that "
            "thumbnails can only be generated with the `sphinx_gallery_png` "
            "renderer)."
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
