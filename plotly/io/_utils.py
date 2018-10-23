from __future__ import absolute_import

import plotly
from plotly.basedatatypes import BaseFigure
import plotly.graph_objs as go


def validate_coerce_fig_to_dict(fig, validate):
    if isinstance(fig, BaseFigure):
        fig_dict = fig.to_dict()
    elif isinstance(fig, dict):
        if validate:
            # This will raise an exception if fig is not a valid plotly figure
            fig_dict = plotly.graph_objs.Figure(fig).to_plotly_json()
        else:
            fig_dict = fig
    else:
        raise ValueError("""
The fig parameter must be a dict or Figure.
    Received value of type {typ}: {v}""".format(typ=type(fig), v=fig))
    return fig_dict


def validate_coerce_output_type(output_type):
    if output_type == 'Figure' or output_type == go.Figure:
        cls = go.Figure
    elif (output_type == 'FigureWidget' or
          (hasattr(go, 'FigureWidget') and output_type == go.FigureWidget)):
        cls = go.FigureWidget
    else:
        raise ValueError("""
Invalid output type: {output_type}
    Must be one of: 'Figure', 'FigureWidget'""")
    return cls