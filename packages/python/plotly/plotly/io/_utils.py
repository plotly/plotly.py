from _plotly_utils.basevalidators import is_homogeneous_array, to_typed_array_spec
import plotly
import plotly.graph_objs as go
from plotly.offline import get_plotlyjs_version


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
    for trace in fig_dict["data"]:
        for key, value in trace.items():
            if is_homogeneous_array(value):
                print("to typed array: key:", key, "value:", value)
                trace[key] = to_typed_array_spec(value)

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
