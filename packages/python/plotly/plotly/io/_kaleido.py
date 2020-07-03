from six import string_types
import os
from plotly.io._utils import validate_coerce_fig_to_dict

try:
    from kaleido.scopes.plotly import PlotlyScope

    scope = PlotlyScope()
except ImportError:
    PlotlyScope = None
    scope = None


def to_image(fig, format=None, width=None, height=None, scale=None, validate=True):
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

        If not specified, will default to `plotly.io.kaleido.scope.default_format`

    width: int or None
        The width of the exported image in layout pixels. If the `scale`
        property is 1.0, this will also be the width of the exported image
        in physical pixels.

        If not specified, will default to `plotly.io.kaleido.scope.default_width`

    height: int or None
        The height of the exported image in layout pixels. If the `scale`
        property is 1.0, this will also be the height of the exported image
        in physical pixels.

        If not specified, will default to `plotly.io.kaleido.scope.default_height`

    scale: int or float or None
        The scale factor to use when exporting the figure. A scale factor
        larger than 1.0 will increase the image resolution with respect
        to the figure's layout pixel dimensions. Whereas as scale factor of
        less than 1.0 will decrease the image resolution.

        If not specified, will default to `plotly.io.kaleido.scope.default_scale`

    validate: bool
        True if the figure should be validated before being converted to
        an image, False otherwise.

    Returns
    -------
    bytes
        The image data
    """
    # Raise informative error message if Kaleido is not installed
    if scope is None:
        raise ValueError(
            """
Image export requires the kaleido package, which can be installed using pip:
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
    fig, file, format=None, scale=None, width=None, height=None, validate=True
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
          - 'eps' (Requires the poppler library to be installed)

        If not specified and `file` is a string then this will default to the
        file extension. If not specified and `file` is not a string then this
        will default to `plotly.io.config.default_format`

    width: int or None
        The width of the exported image in layout pixels. If the `scale`
        property is 1.0, this will also be the width of the exported image
        in physical pixels.

        If not specified, will default to `plotly.io.config.default_width`

    height: int or None
        The height of the exported image in layout pixels. If the `scale`
        property is 1.0, this will also be the height of the exported image
        in physical pixels.

        If not specified, will default to `plotly.io.config.default_height`

    scale: int or float or None
        The scale factor to use when exporting the figure. A scale factor
        larger than 1.0 will increase the image resolution with respect
        to the figure's layout pixel dimensions. Whereas as scale factor of
        less than 1.0 will decrease the image resolution.

        If not specified, will default to `plotly.io.config.default_scale`

    validate: bool
        True if the figure should be validated before being converted to
        an image, False otherwise.

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
        fig, format=format, scale=scale, width=width, height=height, validate=validate
    )

    # Open file
    # ---------
    if file_is_str:
        with open(file, "wb") as f:
            f.write(img_data)
    else:
        file.write(img_data)


__all__ = ["to_image", "write_image", "scope"]
