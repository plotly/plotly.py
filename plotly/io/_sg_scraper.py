# This module defines an image scraper for sphinx-gallery
# https://sphinx-gallery.github.io/
# which can be used by projects using plotly in their documentation.
# This module monkey-patches plotly.offline.plot, so we do not
# import it in __init__.py
import inspect, os

import plotly
plotly_plot = plotly.offline.plot
from glob import glob
import shutil

def _patched_plotly_plot(*args, **kwargs):
    """
    Monkey-patched version of plotly.offline.plot, in order to save
    html file with the same name as python script. Also, a static
    png file is saved.
    """
    stack = inspect.stack()
    # Name of script from which plot function was called is retrieved
    filename = stack[1].filename # let's hope this is robust...
    filename_root, _ = os.path.splitext(filename)
    filename_html = filename_root + '.html'
    filename_png = filename_root + '.png'
    figure = plotly.tools.return_figure_from_figure_or_data(*(args, True))
    res = plotly_plot(*args, auto_open=False,
		    filename=filename_html)
    plotly.io.write_image(figure, filename_png)
    return res

plotly.offline.plot = _patched_plotly_plot


def plotly_sg_scraper(block, block_vars, gallery_conf, **kwargs):
    """Scrape Plotly figures.

    Since the monkey-patched version of plotly.offline.plot generates
    both html and static png files, we simply crawl these files and give
    them the appropriate path.

    Parameters
    ----------
    block : tuple
        A tuple containing the (label, content, line_number) of the block.
    block_vars : dict
        Dict of block variables.
    gallery_conf : dict
        Contains the configuration of Sphinx-Gallery
    **kwargs : dict
        Additional keyword arguments to pass to
        :meth:`~matplotlib.figure.Figure.savefig`, e.g. ``format='svg'``.
        The ``format`` kwarg in particular is used to set the file extension
        of the output file (currently only 'png' and 'svg' are supported).

    Returns
    -------
    rst : str
        The ReSTructuredText that will be rendered to HTML containing
        the images.

    Notes
    -----
    Add this function to the image scrapers 
    """
    examples_dirs = gallery_conf['examples_dirs']
    if isinstance(examples_dirs, (list, tuple)):
        examples_dirs = examples_dirs[0]
    pngs = sorted(glob(os.path.join(examples_dirs,
                            '*.png')))
    htmls = sorted(glob(os.path.join(examples_dirs,
                            '*.html')))
    image_path_iterator = block_vars['image_path_iterator']
    image_names = list()
    seen = set()
    for html, png in zip(htmls, pngs):
        if png not in seen:
            seen |= set(png)
            this_image_path_png = image_path_iterator.__next__()
            this_image_path_html = (os.path.splitext(
                                    this_image_path_png)[0] + '.html')
            image_names.append(this_image_path_html)
            shutil.move(png, this_image_path_png)
            shutil.move(html, this_image_path_html)
    # Use the `figure_rst` helper function to generate rST for image files
    return figure_rst(image_names, gallery_conf['src_dir'])


def figure_rst(figure_list, sources_dir):
    """Generate RST for a list of PNG filenames.

    Depending on whether we have one or more figures, we use a
    single rst call to 'image' or a horizontal list.

    Parameters
    ----------
    figure_list : list
        List of strings of the figures' absolute paths.
    sources_dir : str
        absolute path of Sphinx documentation sources

    Returns
    -------
    images_rst : str
        rst code to embed the images in the document
    """

    figure_paths = [os.path.relpath(figure_path, sources_dir)
                    .replace(os.sep, '/').lstrip('/')
                    for figure_path in figure_list]
    images_rst = ""
    figure_name = figure_paths[0]
    ext = os.path.splitext(figure_name)[1]
    figure_path = os.path.join('images', os.path.basename(figure_name))
    images_rst = SINGLE_HTML % figure_path
    return images_rst


SINGLE_HTML = """
.. raw:: html
    :file: %s
"""

