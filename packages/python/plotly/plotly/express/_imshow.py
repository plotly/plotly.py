import plotly.graph_objs as go
from _plotly_utils.basevalidators import ColorscaleValidator
from ._core import apply_default_cascade
from io import BytesIO
import base64
from .imshow_utils import rescale_intensity, _integer_ranges, _integer_types
import pandas as pd
from .png import Writer, from_array
import numpy as np

try:
    import xarray

    xarray_imported = True
except ImportError:
    xarray_imported = False
try:
    from PIL import Image

    pil_imported = True
except ImportError:
    pil_imported = False

_float_types = []


def _array_to_b64str(img, backend="pil", compression=4, ext="png"):
    """Converts a numpy array of uint8 into a base64 png string.

    Parameters
    ----------
    img: ndarray of uint8
        array image
    backend: str
        'auto', 'pil' or 'pypng'. If 'auto', Pillow is used if installed,
        otherwise pypng.
    compression: int, between 0 and 9
        compression level to be passed to the backend
    ext: str, 'png' or 'jpg'
        compression format used to generate b64 string
    """
    # PIL and pypng error messages are quite obscure so we catch invalid compression values
    if compression < 0 or compression > 9:
        raise ValueError("compression level must be between 0 and 9.")
    alpha = False
    if img.ndim == 2:
        mode = "L"
    elif img.ndim == 3 and img.shape[-1] == 3:
        mode = "RGB"
    elif img.ndim == 3 and img.shape[-1] == 4:
        mode = "RGBA"
        alpha = True
    else:
        raise ValueError("Invalid image shape")
    if backend == "auto":
        backend = "pil" if pil_imported else "pypng"
    if ext != "png" and backend != "pil":
        raise ValueError("jpg binary strings are only available with PIL backend")

    if backend == "pypng":
        ndim = img.ndim
        sh = img.shape
        if ndim == 3:
            img = img.reshape((sh[0], sh[1] * sh[2]))
        w = Writer(
            sh[1], sh[0], greyscale=(ndim == 2), alpha=alpha, compression=compression
        )
        img_png = from_array(img, mode=mode)
        prefix = "data:image/png;base64,"
        with BytesIO() as stream:
            w.write(stream, img_png.rows)
            base64_string = prefix + base64.b64encode(stream.getvalue()).decode("utf-8")
    else:  # pil
        if not pil_imported:
            raise ImportError(
                "pillow needs to be installed to use `backend='pil'. Please"
                "install pillow or use `backend='pypng'."
            )
        pil_img = Image.fromarray(img)
        if ext == "jpg" or ext == "jpeg":
            prefix = "data:image/jpeg;base64,"
            ext = "jpeg"
        else:
            prefix = "data:image/png;base64,"
            ext = "png"
        with BytesIO() as stream:
            pil_img.save(stream, format=ext, compress_level=compression)
            base64_string = prefix + base64.b64encode(stream.getvalue()).decode("utf-8")
    return base64_string


def _vectorize_zvalue(z, mode="max"):
    alpha = 255 if mode == "max" else 0
    if z is None:
        return z
    elif np.isscalar(z):
        return [z] * 3 + [alpha]
    elif len(z) == 1:
        return list(z) * 3 + [alpha]
    elif len(z) == 3:
        return list(z) + [alpha]
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
    labels={},
    x=None,
    y=None,
    color_continuous_scale=None,
    color_continuous_midpoint=None,
    range_color=None,
    title=None,
    template=None,
    width=None,
    height=None,
    aspect=None,
    contrast_rescaling=None,
    binary_string=None,
    binary_backend="auto",
    binary_compression_level=4,
    binary_format="png",
):
    """
    Display an image, i.e. data on a 2D regular raster.

    Parameters
    ----------

    img: array-like image, or xarray
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
        Overridden by range_color.

    origin : str, 'upper' or 'lower' (default 'upper')
        position of the [0, 0] pixel of the image array, in the upper left or lower left
        corner. The convention 'upper' is typically used for matrices and images.

    labels : dict with str keys and str values (default `{}`)
        Sets names used in the figure for axis titles (keys ``x`` and ``y``),
        colorbar title and hoverlabel (key ``color``). The values should correspond
        to the desired label to be displayed. If ``img`` is an xarray, dimension
        names are used for axis titles, and long name for the colorbar title
        (unless overridden in ``labels``). Possible keys are: x, y, and color.

    x, y: list-like, optional
        x and y are used to label the axes of single-channel heatmap visualizations and
        their lengths must match the lengths of the second and first dimensions of the
        img argument. They are auto-populated if the input is an xarray.

    color_continuous_scale : str or list of str
        colormap used to map scalar data to colors (for a 2D image). This parameter is
        not used for RGB or RGBA images. If a string is provided, it should be the name
        of a known color scale, and if a list is provided, it should be a list of CSS-
        compatible colors.

    color_continuous_midpoint : number
        If set, computes the bounds of the continuous color scale to have the desired
        midpoint. Overridden by range_color or zmin and zmax.

    range_color : list of two numbers
        If provided, overrides auto-scaling on the continuous color scale, including
        overriding `color_continuous_midpoint`. Also overrides zmin and zmax. Used only
        for single-channel images.

    title : str
        The figure title.

    template : str or dict or plotly.graph_objects.layout.Template instance
        The figure template name or definition.

    width : number
        The figure width in pixels.

    height: number
        The figure height in pixels.

    aspect: 'equal', 'auto', or None
      - 'equal': Ensures an aspect ratio of 1 or pixels (square pixels)
      - 'auto': The axes is kept fixed and the aspect ratio of pixels is
        adjusted so that the data fit in the axes. In general, this will
        result in non-square pixels.
      - if None, 'equal' is used for numpy arrays and 'auto' for xarrays
        (which have typically heterogeneous coordinates)

    contrast_rescaling: 'minmax', 'infer', or None
        how to determine data values corresponding to the bounds of the color
        range, when zmin or zmax are not passed. If `minmax`, the min and max
        values of the image are used. If `infer`, a heuristic based on the image
        data type is used.

    binary_string: bool, default None
        if True, the image data are first rescaled and encoded as uint8 and
        then passed to plotly.js as a b64 PNG string. If False, data are passed
        unchanged as a numerical array. Setting to True may lead to performance
        gains, at the cost of a loss of precision depending on the original data
        type. If None, use_binary_string is set to True for multichannel (eg) RGB
        arrays, and to False for single-channel (2D) arrays. 2D arrays are
        represented as grayscale and with no colorbar if use_binary_string is
        True.

    binary_backend: str, 'auto' (default), 'pil' or 'pypng'
        Third-party package for the transformation of numpy arrays to
        png b64 strings. If 'auto', Pillow is used if installed,  otherwise
        pypng.

    binary_compression_level: int, between 0 and 9 (default 4)
        png compression level to be passed to the backend when transforming an
        array to a png b64 string. Increasing `binary_compression` decreases the
        size of the png string, but the compression step takes more time. For most
        images it is not worth using levels greater than 5, but it's possible to
        test `len(fig.data[0].source)` and to time the execution of `imshow` to
        tune the level of compression. 0 means no compression (not recommended).

    binary_format: str, 'png' (default) or 'jpg'
        compression format used to generate b64 string. 'png' is recommended
        since it uses lossless compression, but 'jpg' (lossy) compression can
        result if smaller binary strings for natural images.

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

    If an xarray is passed, dimensions names and coordinates are used for
    axes labels and ticks.
    """
    args = locals()
    apply_default_cascade(args)
    labels = labels.copy()
    # ----- Define x and y, set labels if img is an xarray -------------------
    if xarray_imported and isinstance(img, xarray.DataArray):
        if binary_string:
            raise ValueError(
                "It is not possible to use binary image strings for xarrays."
                "Please pass your data as a numpy array instead using"
                "`img.values`"
            )
        y_label, x_label = img.dims[0], img.dims[1]
        # np.datetime64 is not handled correctly by go.Heatmap
        for ax in [x_label, y_label]:
            if np.issubdtype(img.coords[ax].dtype, np.datetime64):
                img.coords[ax] = img.coords[ax].astype(str)
        if x is None:
            x = img.coords[x_label]
        if y is None:
            y = img.coords[y_label]
        if aspect is None:
            aspect = "auto"
        if labels.get("x", None) is None:
            labels["x"] = x_label
        if labels.get("y", None) is None:
            labels["y"] = y_label
        if labels.get("color", None) is None:
            labels["color"] = xarray.plot.utils.label_from_attrs(img)
            labels["color"] = labels["color"].replace("\n", "<br>")
    else:
        if hasattr(img, "columns") and hasattr(img.columns, "__len__"):
            if x is None:
                x = img.columns
            if labels.get("x", None) is None and hasattr(img.columns, "name"):
                labels["x"] = img.columns.name or ""
        if hasattr(img, "index") and hasattr(img.index, "__len__"):
            if y is None:
                y = img.index
            if labels.get("y", None) is None and hasattr(img.index, "name"):
                labels["y"] = img.index.name or ""

        if labels.get("x", None) is None:
            labels["x"] = ""
        if labels.get("y", None) is None:
            labels["y"] = ""
        if labels.get("color", None) is None:
            labels["color"] = ""
        if aspect is None:
            aspect = "equal"

    # --- Set the value of binary_string (forbidden for pandas)
    if isinstance(img, pd.DataFrame):
        if binary_string:
            raise ValueError("Binary strings cannot be used with pandas arrays")
        is_dataframe = True
    else:
        is_dataframe = False

    # --------------- Starting from here img is always a numpy array --------
    img = np.asanyarray(img)

    # Default behaviour of binary_string: True for RGB images, False for 2D
    if binary_string is None:
        binary_string = img.ndim >= 3 and not is_dataframe

    # Cast bools to uint8 (also one byte)
    if img.dtype == np.bool:
        img = 255 * img.astype(np.uint8)

    if range_color is not None:
        zmin = range_color[0]
        zmax = range_color[1]

    # -------- Contrast rescaling: either minmax or infer ------------------
    if contrast_rescaling is None:
        contrast_rescaling = "minmax" if img.ndim == 2 else "infer"

    # We try to set zmin and zmax only if necessary, because traces have good defaults
    if contrast_rescaling == "minmax":
        # When using binary_string and minmax we need to set zmin and zmax to rescale the image
        if (zmin is not None or binary_string) and zmax is None:
            zmax = img.max()
        if (zmax is not None or binary_string) and zmin is None:
            zmin = img.min()
    else:
        # For uint8 data and infer we let zmin and zmax to be None if passed as None
        if zmax is None and img.dtype != np.uint8:
            zmax = _infer_zmax_from_type(img)
        if zmin is None and zmax is not None:
            zmin = 0

        # For 2d data, use Heatmap trace, unless binary_string is True
    if img.ndim == 2 and not binary_string:
        if y is not None and img.shape[0] != len(y):
            raise ValueError(
                "The length of the y vector must match the length of the first "
                + "dimension of the img matrix."
            )
        if x is not None and img.shape[1] != len(x):
            raise ValueError(
                "The length of the x vector must match the length of the second "
                + "dimension of the img matrix."
            )
        trace = go.Heatmap(x=x, y=y, z=img, coloraxis="coloraxis1")
        autorange = True if origin == "lower" else "reversed"
        layout = dict(yaxis=dict(autorange=autorange))
        if aspect == "equal":
            layout["xaxis"] = dict(scaleanchor="y", constrain="domain")
            layout["yaxis"]["constrain"] = "domain"
        colorscale_validator = ColorscaleValidator("colorscale", "imshow")
        layout["coloraxis1"] = dict(
            colorscale=colorscale_validator.validate_coerce(
                args["color_continuous_scale"]
            ),
            cmid=color_continuous_midpoint,
            cmin=zmin,
            cmax=zmax,
        )
        if labels["color"]:
            layout["coloraxis1"]["colorbar"] = dict(title_text=labels["color"])

    # For 2D+RGB data, use Image trace
    elif img.ndim == 3 and img.shape[-1] in [3, 4] or (img.ndim == 2 and binary_string):
        rescale_image = True  # to check whether image has been modified
        if zmin is not None and zmax is not None:
            zmin, zmax = (
                _vectorize_zvalue(zmin, mode="min"),
                _vectorize_zvalue(zmax, mode="max"),
            )
        if binary_string:
            if zmin is None and zmax is None:  # no rescaling, faster
                img_rescaled = img
                rescale_image = False
            elif img.ndim == 2:
                img_rescaled = rescale_intensity(
                    img, in_range=(zmin[0], zmax[0]), out_range=np.uint8
                )
            else:
                img_rescaled = np.dstack(
                    [
                        rescale_intensity(
                            img[..., ch],
                            in_range=(zmin[ch], zmax[ch]),
                            out_range=np.uint8,
                        )
                        for ch in range(img.shape[-1])
                    ]
                )
            img_str = _array_to_b64str(
                img_rescaled,
                backend=binary_backend,
                compression=binary_compression_level,
                ext=binary_format,
            )
            trace = go.Image(source=img_str)
        else:
            colormodel = "rgb" if img.shape[-1] == 3 else "rgba256"
            trace = go.Image(z=img, zmin=zmin, zmax=zmax, colormodel=colormodel)
        layout = {}
        if origin == "lower":
            layout["yaxis"] = dict(autorange=True)
    else:
        raise ValueError(
            "px.imshow only accepts 2D single-channel, RGB or RGBA images. "
            "An image of shape %s was provided" % str(img.shape)
        )

    layout_patch = dict()
    for attr_name in ["height", "width"]:
        if args[attr_name]:
            layout_patch[attr_name] = args[attr_name]
    if args["title"]:
        layout_patch["title_text"] = args["title"]
    elif args["template"].layout.margin.t is None:
        layout_patch["margin"] = {"t": 60}
    fig = go.Figure(data=trace, layout=layout)
    fig.update_layout(layout_patch)
    # Hover name, z or color
    if binary_string and rescale_image and not np.all(img == img_rescaled):
        # we rescaled the image, hence z is not displayed in hover since it does
        # not correspond to img values
        hovertemplate = "%s: %%{x}<br>%s: %%{y}<extra></extra>" % (
            labels["x"] or "x",
            labels["y"] or "y",
        )
    else:
        if trace["type"] == "heatmap":
            hover_name = "%{z}"
        elif img.ndim == 2:
            hover_name = "%{z[0]}"
        elif img.ndim == 3 and img.shape[-1] == 3:
            hover_name = "[%{z[0]}, %{z[1]}, %{z[2]}]"
        else:
            hover_name = "%{z}"
        hovertemplate = "%s: %%{x}<br>%s: %%{y}<br>%s: %s<extra></extra>" % (
            labels["x"] or "x",
            labels["y"] or "y",
            labels["color"] or "color",
            hover_name,
        )
    fig.update_traces(hovertemplate=hovertemplate)
    if labels["x"]:
        fig.update_xaxes(title_text=labels["x"])
    if labels["y"]:
        fig.update_yaxes(title_text=labels["y"])
    fig.update_layout(template=args["template"], overwrite=True)
    return fig
