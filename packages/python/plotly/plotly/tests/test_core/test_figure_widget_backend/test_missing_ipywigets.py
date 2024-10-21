import pytest

# Use wildcard import to make sure FigureWidget is always included
from plotly.graph_objects import *
from plotly.missing_anywidget import FigureWidget as FigureWidgetMissingAnywidget

try:
    import anywidget as _anywidget
    from packaging.version import Version as _Version

    if _Version(_anywidget.__version__) >= _Version("7.0.0"):
        missing_anywidget = False
    else:
        raise ImportError()
except Exception:
    missing_anywidget = True


if missing_anywidget:

    def test_import_figurewidget_without_anywidget():
        assert FigureWidget is FigureWidgetMissingAnywidget

        with pytest.raises(ImportError):
            # anywidget import error raised on construction, not import
            FigureWidget()

else:

    def test_import_figurewidget_with_anywidget():
        from plotly.graph_objs._figurewidget import (
            FigureWidget as FigureWidgetWithAnywidget,
        )

        assert FigureWidget is FigureWidgetWithAnywidget
        fig = FigureWidget()
        assert isinstance(fig, FigureWidgetWithAnywidget)
