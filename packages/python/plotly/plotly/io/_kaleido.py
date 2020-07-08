from __future__ import absolute_import
from six import string_types
import os
import plotly
from plotly.io._utils import validate_coerce_fig_to_dict

try:
    from kaleido.scopes.plotly import PlotlyScope

    scope = PlotlyScope()

    # Compute absolute path to the 'plotly/package_data/' directory
    root_dir = os.path.dirname(os.path.abspath(plotly.__file__))
    package_dir = os.path.join(root_dir, "package_data")
    scope.plotlyjs = os.path.join(package_dir, "plotly.min.js")
    scope.mathjax = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js"
except ImportError:
    PlotlyScope = None
    scope = None


def to_image(
    fig, format=None, width=None, height=None, scale=None, validate=True, engine="auto"
):
    """
    Convert a figure to a static image bytes string

    Parameters
    ----------
    fig:
        Figure object or dict representing a figure

    format: str or None
        The desired image format. One of
          - 'png'
          - 'jpg' or 'jpeg'
          - 'webp'
          - 'svg'
          - 'pdf'
          - 'eps' (Requires the poppler library to be installed and on the PATH)

        If not specified, will default to:
             - `plotly.io.kaleido.scope.default_format` if engine is "kaleido"
             - `plotly.io.orca.config.default_format` if engine is "orca"

    width: int or None
        The width of the exported image in layout pixels. If the `scale`
        property is 1.0, this will also be the width of the exported image
        in physical pixels.

        If not specified, will default to:
             - `plotly.io.kaleido.scope.default_width` if engine is "kaleido"
             - `plotly.io.orca.config.default_width` if engine is "orca"

    height: int or None
        The height of the exported image in layout pixels. If the `scale`
        property is 1.0, this will also be the height of the exported image
        in physical pixels.

        If not specified, will default to:
             - `plotly.io.kaleido.scope.default_height` if engine is "kaleido"
             - `plotly.io.orca.config.default_height` if engine is "orca"

    scale: int or float or None
        The scale factor to use when exporting the figure. A scale factor
        larger than 1.0 will increase the image resolution with respect
        to the figure's layout pixel dimensions. Whereas as scale factor of
        less than 1.0 will decrease the image resolution.

        If not specified, will default to:
             - `plotly.io.kaleido.scope.default_scale` if engine is "kaleido"
             - `plotly.io.orca.config.default_scale` if engine is "orca"


    validate: bool
        True if the figure should be validated before being converted to
        an image, False otherwise.

    engine: str
        Image export engine to use:
         - "kaleido": Use Kaleido for image export
         - "orca": Use Orca for image export
         - "auto" (default): Use Kaleido if installed, otherwise use orca

    Returns
    -------
    bytes
        The image data
    """
    # Handle engine
    # -------------
    if engine == "auto":
        if scope is not None:
            engine = "kaleido"
        else:
            engine = "orca"

    if engine == "orca":
        # Fall back to legacy orca image export path
        from ._orca import to_image as to_image_orca

        return to_image_orca(
            fig,
            format=format,
            width=width,
            height=height,
            scale=scale,
            validate=validate,
        )
    elif engine != "kaleido":
        raise ValueError(
            "Invalid image export engine specified: {engine}".format(
                engine=repr(engine)
            )
        )

    # Raise informative error message if Kaleido is not installed
    if scope is None:
        raise ValueError(
            """
Image export using the "kaleido" engine requires the kaleido package,
which can be installed using pip:
    $ pip install -U kaleido 
"""
        )

    # Validate figure
    # ---------------
    fig_dict = validate_coerce_fig_to_dict(fig, validate)
    img_bytes = scope.transform(
        fig_dict, format=format, width=width, height=height, scale=scale
    )

    return img_bytes


def write_image(
    fig,
    file,
    format=None,
    scale=None,
    width=None,
    height=None,
    validate=True,
    engine="auto",
):
    """
    Convert a figure to a static image and write it to a file or writeable
    object

    Parameters
    ----------
    fig:
        Figure object or dict representing a figure

    file: str or writeable
        A string representing a local file path or a writeable object
        (e.g. an open file descriptor)

    format: str or None
        The desired image format. One of
          - 'png'
          - 'jpg' or 'jpeg'
          - 'webp'
          - 'svg'
          - 'pdf'
          - 'eps' (Requires the poppler library to be installed and on the PATH)

        If not specified and `file` is a string then this will default to the
        file extension. If not specified and `file` is not a string then this
        will default to:
            - `plotly.io.kaleido.scope.default_format` if engine is "kaleido"
            - `plotly.io.orca.config.default_format` if engine is "orca"

    width: int or None
        The width of the exported image in layout pixels. If the `scale`
        property is 1.0, this will also be the width of the exported image
        in physical pixels.

        If not specified, will default to:
            - `plotly.io.kaleido.scope.default_width` if engine is "kaleido"
            - `plotly.io.orca.config.default_width` if engine is "orca"

    height: int or None
        The height of the exported image in layout pixels. If the `scale`
        property is 1.0, this will also be the height of the exported image
        in physical pixels.

        If not specified, will default to:
            - `plotly.io.kaleido.scope.default_height` if engine is "kaleido"
            - `plotly.io.orca.config.default_height` if engine is "orca"

    scale: int or float or None
        The scale factor to use when exporting the figure. A scale factor
        larger than 1.0 will increase the image resolution with respect
        to the figure's layout pixel dimensions. Whereas as scale factor of
        less than 1.0 will decrease the image resolution.

        If not specified, will default to:
            - `plotly.io.kaleido.scope.default_scale` if engine is "kaleido"
            - `plotly.io.orca.config.default_scale` if engine is "orca"

    validate: bool
        True if the figure should be validated before being converted to
        an image, False otherwise.

    engine: str
        Image export engine to use:
         - "kaleido": Use Kaleido for image export
         - "orca": Use Orca for image export
         - "auto" (default): Use Kaleido if installed, otherwise use orca

    Returns
    -------
    None
    """
    # Check if file is a string
    # -------------------------
    file_is_str = isinstance(file, string_types)

    # Infer format if not specified
    # -----------------------------
    if file_is_str and format is None:
        _, ext = os.path.splitext(file)
        if ext:
            format = ext.lstrip(".")
        else:
            raise ValueError(
                """
Cannot infer image type from output path '{file}'.
Please add a file extension or specify the type using the format parameter.
For example:

    >>> import plotly.io as pio
    >>> pio.write_image(fig, file_path, format='png')
""".format(
                    file=file
                )
            )

    # Request image
    # -------------
    # Do this first so we don't create a file if image conversion fails
    img_data = to_image(
        fig,
        format=format,
        scale=scale,
        width=width,
        height=height,
        validate=validate,
        engine=engine,
    )

    # Open file
    # ---------
    if file_is_str:
        with open(file, "wb") as f:
            f.write(img_data)
    else:
        file.write(img_data)


__all__ = ["to_image", "write_image", "scope"]
