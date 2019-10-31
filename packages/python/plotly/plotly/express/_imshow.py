import plotly.graph_objs as go
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
    if dt in _integer_types:
        return _integer_ranges[dt][1]
    else:
        return img[np.isfinite(img)].max()


def imshow(img, zmin=None, zmax=None, origin=None, colorscale=None, showticks=True):
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
        datatypes (ie [0-255] for uint8 images, [0, 65535] for uint16 images, etc.), and
        to the min and max values of the image for an image of floats.

    origin : str, 'upper' or 'lower' (default 'upper')
        position of the [0, 0] pixel of the image array, in the upper left or lower left
        corner. The convention 'upper' is typically used for matrices and images.

    colorscale : str
        colormap used to map scalar data to colors (for a 2D image). This parameter is not used for
        RGB or RGBA images.

    showticks : bool, default True
        if False, no tick labels are shown for pixel indices.

    Returns
    -------
    fig : graph_objects.Figure containing the displayed image

    See also
    --------

    plotly.graph_objects.Image : image trace
    plotly.graph_objects.Heatmap : heatmap trace

    Notes
    -----

    In order to update and customize the returned figure, use `go.Figure.update_traces` or `go.Figure.update_layout`.
    """
    img = np.asanyarray(img)
    # Cast bools to uint8 (also one byte)
    if img.dtype == np.bool:
        img = 255 * img.astype(np.uint8)

    # For 2d data, use Heatmap trace
    if img.ndim == 2:
        if colorscale is None:
            colorscale = "gray"
        trace = go.Heatmap(z=img, zmin=zmin, zmax=zmax, colorscale=colorscale)
        autorange = True if origin == "lower" else "reversed"
        layout = dict(
            xaxis=dict(scaleanchor="y", constrain="domain"),
            yaxis=dict(autorange=autorange, constrain="domain"),
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
            "px.imshow only accepts 2D grayscale, RGB or RGBA images. "
            "An image of shape %s was provided" % str(img.shape)
        )
    fig = go.Figure(data=trace, layout=layout)
    if not showticks:
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)
    return fig
