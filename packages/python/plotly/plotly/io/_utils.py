import plotly
import plotly.graph_objs as go
from plotly.offline import get_plotlyjs_version
from plotly import optional_imports

import warnings
import psutil


def display_jupyter_version_warnings():
    parent_process = None
    try:
        parent_process = psutil.Process().parent().cmdline()[-1]
    except Exception:
        pass

    if parent_process is None:
        return
    elif "jupyter-notebook" in parent_process:
        jupyter_notebook = optional_imports.get_module("notebook")
        if jupyter_notebook.__version__ < "7":
            # Add warning about upgrading notebook
            warnings.warn(
                f"Plotly version >= 6 requires Jupyter Notebook >= 7 but you have {jupyter_notebook.__version__} installed.\n To upgrade Jupyter Notebook, please run `pip install notebook --upgrade`."
            )
    elif "jupyter-lab" in parent_process:
        jupyter_lab = optional_imports.get_module("jupyterlab")
        if jupyter_lab.__version__ < "3":
            # Add warning about upgrading jupyterlab
            warnings.warn(
                f"Plotly version >= 6 requires JupyterLab >= 3 but you have {jupyter_lab.__version__} installed. To upgrade JupyterLab, please run `pip install jupyterlab --upgrade`."
            )


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
