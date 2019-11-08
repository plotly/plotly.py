import plotly.graph_objs as go
from _plotly_utils.basevalidators import ColorscaleValidator
from ._core import apply_default_cascade
import numpy as np  # is it fine to depend on np here?

_float_types = []

# Adapted from skimage.util.dtype
_integer_types = (
    np.byte,
    np.ubyte,  # 8 bits
    np.short,
    np.ushort,  # 16 bits
    np.intc,
    np.uintc,  # 16 or 32 or 64 bits
    np.int_,
    np.uint,  # 32 or 64 bits
    np.longlong,
    np.ulonglong,
)  # 64 bits
_integer_ranges = {t: (np.iinfo(t).min, np.iinfo(t).max) for t in _integer_types}


def _vectorize_zvalue(z):
    if z is None:
        return z
    elif np.isscalar(z):
        return [z] * 3 + [1]
    elif len(z) == 1:
        return list(z) * 3 + [1]
    elif len(z) == 3:
        return list(z) + [1]
    elif len(z) == 4:
        return z
    else:
        raise ValueError(
            "zmax can be a scalar, or an iterable of length 1, 3 or 4. "
            "A value of %s was passed for zmax." % str(z)
        )


def _infer_zmax_from_type(img):
    dt = img.dtype.type
    rtol = 1.05
    if dt in _integer_types:
        return _integer_ranges[dt][1]
    else:
        im_max = img[np.isfinite(img)].max()
        if im_max <= 1 * rtol:
            return 1
        elif im_max <= 255 * rtol:
            return 255
        elif im_max <= 65535 * rtol:
            return 65535
        else:
            return 2 ** 32


def imshow(
    img,
    zmin=None,
    zmax=None,
    origin=None,
    color_continuous_scale=None,
    color_continuous_midpoint=None,
    range_color=None,
    title=None,
    template=None,
    width=None,
    height=None,
):
    """
    Display an image, i.e. data on a 2D regular raster.

    Parameters
    ----------

    img: array-like image
        The image data. Supported array shapes are

        - (M, N): an image with scalar data. The data is visualized
          using a colormap.
        - (M, N, 3): an image with RGB values.
        - (M, N, 4): an image with RGBA values, i.e. including transparency.

    zmin, zmax : scalar or iterable, optional
        zmin and zmax define the scalar range that the colormap covers. By default,
        zmin and zmax correspond to the min and max values of the datatype for integer
        datatypes (ie [0-255] for uint8 images, [0, 65535] for uint16 images, etc.). For
        a multichannel image of floats, the max of the image is computed and zmax is the
        smallest power of 256 (1, 255, 65535) greater than this max value,
        with a 5% tolerance. For a single-channel image, the max of the image is used.

    origin : str, 'upper' or 'lower' (default 'upper')
        position of the [0, 0] pixel of the image array, in the upper left or lower left
        corner. The convention 'upper' is typically used for matrices and images.

    color_continuous_scale : str or list of str
        colormap used to map scalar data to colors (for a 2D image). This parameter is
        not used for RGB or RGBA images. If a string is provided, it should be the name
        of a known color scale, and if a list is provided, it should be a list of CSS-
        compatible colors.

    color_continuous_midpoint : number
        If set, computes the bounds of the continuous color scale to have the desired
        midpoint.

    range_color : list of two numbers
        If provided, overrides auto-scaling on the continuous color scale, including
        overriding `color_continuous_midpoint`.

    title : str
        The figure title.

    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name or definition.

    width : number
        The figure width in pixels.

    height: number
        The figure height in pixels, defaults to 600.

    Returns
    -------
    fig : graph_objects.Figure containing the displayed image

    See also
    --------

    plotly.graph_objects.Image : image trace
    plotly.graph_objects.Heatmap : heatmap trace

    Notes
    -----

    In order to update and customize the returned figure, use
    `go.Figure.update_traces` or `go.Figure.update_layout`.
    """
    args = locals()
    apply_default_cascade(args)

    img = np.asanyarray(img)
    # Cast bools to uint8 (also one byte)
    if img.dtype == np.bool:
        img = 255 * img.astype(np.uint8)

    # For 2d data, use Heatmap trace
    if img.ndim == 2:
        trace = go.Heatmap(z=img, zmin=zmin, zmax=zmax, coloraxis="coloraxis1")
        autorange = True if origin == "lower" else "reversed"
        layout = dict(
            xaxis=dict(scaleanchor="y", constrain="domain"),
            yaxis=dict(autorange=autorange, constrain="domain"),
        )
        colorscale_validator = ColorscaleValidator("colorscale", "imshow")
        range_color = range_color or [None, None]
        layout["coloraxis1"] = dict(
            colorscale=colorscale_validator.validate_coerce(
                args["color_continuous_scale"]
            ),
            cmid=color_continuous_midpoint,
            cmin=range_color[0],
            cmax=range_color[1],
        )

    # For 2D+RGB data, use Image trace
    elif img.ndim == 3 and img.shape[-1] in [3, 4]:
        if zmax is None and img.dtype is not np.uint8:
            zmax = _infer_zmax_from_type(img)
        zmin, zmax = _vectorize_zvalue(zmin), _vectorize_zvalue(zmax)
        trace = go.Image(z=img, zmin=zmin, zmax=zmax)
        layout = {}
        if origin == "lower":
            layout["yaxis"] = dict(autorange=True)
    else:
        raise ValueError(
            "px.imshow only accepts 2D single-channel, RGB or RGBA images. "
            "An image of shape %s was provided" % str(img.shape)
        )

    layout_patch = dict()
    for v in ["title", "height", "width"]:
        if args[v]:
            layout_patch[v] = args[v]
    if "title" not in layout_patch and args["template"].layout.margin.t is None:
        layout_patch["margin"] = {"t": 60}
    fig = go.Figure(data=trace, layout=layout)
    fig.update_layout(layout_patch)
    fig.update_layout(template=args["template"], overwrite=True)
    return fig
