import base64
from _plotly_utils.basevalidators import (
    copy_to_readonly_numpy_array,
    is_homogeneous_array,
    to_typed_array_spec,
)
from packages.python.plotly._plotly_utils.optional_imports import get_module
import plotly
import plotly.graph_objs as go
from plotly.offline import get_plotlyjs_version

int8min = -128
int8max = 127
int16min = -32768
int16max = 32767
int32min = -2147483648
int32max = 2147483647

uint8max = 255
uint16max = 65535
uint32max = 4294967295

plotlyjsShortTypes = {
    "int8": "i1",
    "uint8": "u1",
    "int16": "i2",
    "uint16": "u2",
    "int32": "i4",
    "uint32": "u4",
    "float32": "f4",
    "float64": "f8",
}


def to_typed_array_spec(v):
    """
    Convert numpy array to plotly.js typed array spec
    If not possible return the original value
    """
    v = copy_to_readonly_numpy_array(v)

    np = get_module("numpy", should_load=False)
    if not isinstance(v, np.ndarray):
        return v

    dtype = str(v.dtype)

    # convert default Big Ints until we could support them in plotly.js
    if dtype == "int64":
        max = v.max()
        min = v.min()
        if max <= int8max and min >= int8min:
            v = v.astype("int8")
        elif max <= int16max and min >= int16min:
            v = v.astype("int16")
        elif max <= int32max and min >= int32min:
            v = v.astype("int32")
        else:
            return v

    elif dtype == "uint64":
        max = v.max()
        min = v.min()
        if max <= uint8max and min >= 0:
            v = v.astype("uint8")
        elif max <= uint16max and min >= 0:
            v = v.astype("uint16")
        elif max <= uint32max and min >= 0:
            v = v.astype("uint32")
        else:
            return v

    dtype = str(v.dtype)

    if dtype in plotlyjsShortTypes:
        arrObj = {
            "dtype": plotlyjsShortTypes[dtype],
            "bdata": base64.b64encode(v).decode("ascii"),
        }

        if v.ndim > 1:
            arrObj["shape"] = str(v.shape)[1:-1]

        return arrObj

    return v


def is_skipped_key(key):
    """
    Return whether any keys in the parent hierarchy are in the list of keys that
    are skipped for conversion to the typed array spec
    """
    skipped_keys = ["geojson", "layer", "range"]
    return any(skipped_key in key for skipped_key in skipped_keys)


def convert_to_base64(obj):
    if isinstance(obj, dict):
        for key, value in obj.items():
            if is_skipped_key(key):
                continue
            elif is_homogeneous_array(value):
                obj[key] = to_typed_array_spec(value)
            else:
                convert_to_base64(value)
    elif isinstance(obj, list) or isinstance(obj, tuple):
        for i, value in enumerate(obj):
            convert_to_base64(value)


def validate_coerce_fig_to_dict(fig, validate):
    from plotly.basedatatypes import BaseFigure

    if isinstance(fig, BaseFigure):
        fig_dict = fig.to_dict()
    elif isinstance(fig, dict):
        if validate:
            # This will raise an exception if fig is not a valid plotly figure
            fig_dict = plotly.graph_objs.Figure(fig).to_plotly_json()
        else:
            fig_dict = fig
    elif hasattr(fig, "to_plotly_json"):
        fig_dict = fig.to_plotly_json()
    else:
        raise ValueError(
            """
The fig parameter must be a dict or Figure.
    Received value of type {typ}: {v}""".format(
                typ=type(fig), v=fig
            )
        )

    # Add base64 conversion before sending to the front-end
    convert_to_base64(fig_dict)

    return fig_dict


def validate_coerce_output_type(output_type):
    if output_type == "Figure" or output_type == go.Figure:
        cls = go.Figure
    elif output_type == "FigureWidget" or (
        hasattr(go, "FigureWidget") and output_type == go.FigureWidget
    ):
        cls = go.FigureWidget
    else:
        raise ValueError(
            """
Invalid output type: {output_type}
    Must be one of: 'Figure', 'FigureWidget'"""
        )
    return cls


def plotly_cdn_url(cdn_ver=get_plotlyjs_version()):
    """Return a valid plotly CDN url."""
    return "https://cdn.plot.ly/plotly-{cdn_ver}.min.js".format(
        cdn_ver=cdn_ver,
    )
