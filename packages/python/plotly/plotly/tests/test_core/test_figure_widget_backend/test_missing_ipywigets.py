import pytest

# Use wildcard import to make sure FigureWidget is always included
from plotly.graph_objects import *
from plotly.missing_ipywidgets import FigureWidget as FigureWidgetMissingIPywidgets

try:
    import ipywidgets as _ipywidgets
    from packaging.version import Version as _Version

    if _Version(_ipywidgets.__version__) >= _Version("7.0.0"):
        missing_ipywidgets = False
    else:
        raise ImportError()
except Exception:
    missing_ipywidgets = True


if missing_ipywidgets:

    def test_import_figurewidget_without_ipywidgets():
        assert FigureWidget is FigureWidgetMissingIPywidgets

        with pytest.raises(ImportError):
            # ipywidgets import error raised on construction, not import
            FigureWidget()

else:

    def test_import_figurewidget_with_ipywidgets():
        from plotly.graph_objs._figurewidget import (
            FigureWidget as FigureWidgetWithIPywidgets,
        )

        assert FigureWidget is FigureWidgetWithIPywidgets
        fig = FigureWidget()
        assert isinstance(fig, FigureWidgetWithIPywidgets)
