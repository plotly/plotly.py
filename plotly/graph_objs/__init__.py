# ruff: noqa: F401
import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..graph_objects import Waterfall
    from ..graph_objects import Volume
    from ..graph_objects import Violin
    from ..graph_objects import Treemap
    from ..graph_objects import Table
    from ..graph_objects import Surface
    from ..graph_objects import Sunburst
    from ..graph_objects import Streamtube
    from ..graph_objects import Splom
    from ..graph_objects import Scatterternary
    from ..graph_objects import Scattersmith
    from ..graph_objects import Scatterpolargl
    from ..graph_objects import Scatterpolar
    from ..graph_objects import Scattermapbox
    from ..graph_objects import Scattermap
    from ..graph_objects import Scattergl
    from ..graph_objects import Scattergeo
    from ..graph_objects import Scattercarpet
    from ..graph_objects import Scatter3d
    from ..graph_objects import Scatter
    from ..graph_objects import Sankey
    from ..graph_objects import Pie
    from ..graph_objects import Parcoords
    from ..graph_objects import Parcats
    from ..graph_objects import Ohlc
    from ..graph_objects import Mesh3d
    from ..graph_objects import Isosurface
    from ..graph_objects import Indicator
    from ..graph_objects import Image
    from ..graph_objects import Icicle
    from ..graph_objects import Histogram2dContour
    from ..graph_objects import Histogram2d
    from ..graph_objects import Histogram
    from ..graph_objects import Heatmap
    from ..graph_objects import Funnelarea
    from ..graph_objects import Funnel
    from ..graph_objects import Densitymapbox
    from ..graph_objects import Densitymap
    from ..graph_objects import Contourcarpet
    from ..graph_objects import Contour
    from ..graph_objects import Cone
    from ..graph_objects import Choroplethmapbox
    from ..graph_objects import Choroplethmap
    from ..graph_objects import Choropleth
    from ..graph_objects import Carpet
    from ..graph_objects import Candlestick
    from ..graph_objects import Box
    from ..graph_objects import Barpolar
    from ..graph_objects import Bar
    from ..graph_objects import Layout
    from ..graph_objects import Frame
    from ..graph_objects import Figure
    from ..graph_objects import Data
    from ..graph_objects import Annotations
    from ..graph_objects import Frames
    from ..graph_objects import AngularAxis
    from ..graph_objects import Annotation
    from ..graph_objects import ColorBar
    from ..graph_objects import Contours
    from ..graph_objects import ErrorX
    from ..graph_objects import ErrorY
    from ..graph_objects import ErrorZ
    from ..graph_objects import Font
    from ..graph_objects import Legend
    from ..graph_objects import Line
    from ..graph_objects import Margin
    from ..graph_objects import Marker
    from ..graph_objects import RadialAxis
    from ..graph_objects import Scene
    from ..graph_objects import Stream
    from ..graph_objects import XAxis
    from ..graph_objects import YAxis
    from ..graph_objects import ZAxis
    from ..graph_objects import XBins
    from ..graph_objects import YBins
    from ..graph_objects import Trace
    from ..graph_objects import Histogram2dcontour
    from ..graph_objects import waterfall
    from ..graph_objects import volume
    from ..graph_objects import violin
    from ..graph_objects import treemap
    from ..graph_objects import table
    from ..graph_objects import surface
    from ..graph_objects import sunburst
    from ..graph_objects import streamtube
    from ..graph_objects import splom
    from ..graph_objects import scatterternary
    from ..graph_objects import scattersmith
    from ..graph_objects import scatterpolargl
    from ..graph_objects import scatterpolar
    from ..graph_objects import scattermapbox
    from ..graph_objects import scattermap
    from ..graph_objects import scattergl
    from ..graph_objects import scattergeo
    from ..graph_objects import scattercarpet
    from ..graph_objects import scatter3d
    from ..graph_objects import scatter
    from ..graph_objects import sankey
    from ..graph_objects import pie
    from ..graph_objects import parcoords
    from ..graph_objects import parcats
    from ..graph_objects import ohlc
    from ..graph_objects import mesh3d
    from ..graph_objects import isosurface
    from ..graph_objects import indicator
    from ..graph_objects import image
    from ..graph_objects import icicle
    from ..graph_objects import histogram2dcontour
    from ..graph_objects import histogram2d
    from ..graph_objects import histogram
    from ..graph_objects import heatmap
    from ..graph_objects import funnelarea
    from ..graph_objects import funnel
    from ..graph_objects import densitymapbox
    from ..graph_objects import densitymap
    from ..graph_objects import contourcarpet
    from ..graph_objects import contour
    from ..graph_objects import cone
    from ..graph_objects import choroplethmapbox
    from ..graph_objects import choroplethmap
    from ..graph_objects import choropleth
    from ..graph_objects import carpet
    from ..graph_objects import candlestick
    from ..graph_objects import box
    from ..graph_objects import barpolar
    from ..graph_objects import bar
    from ..graph_objects import layout
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [
            "..graph_objects.waterfall",
            "..graph_objects.volume",
            "..graph_objects.violin",
            "..graph_objects.treemap",
            "..graph_objects.table",
            "..graph_objects.surface",
            "..graph_objects.sunburst",
            "..graph_objects.streamtube",
            "..graph_objects.splom",
            "..graph_objects.scatterternary",
            "..graph_objects.scattersmith",
            "..graph_objects.scatterpolargl",
            "..graph_objects.scatterpolar",
            "..graph_objects.scattermapbox",
            "..graph_objects.scattermap",
            "..graph_objects.scattergl",
            "..graph_objects.scattergeo",
            "..graph_objects.scattercarpet",
            "..graph_objects.scatter3d",
            "..graph_objects.scatter",
            "..graph_objects.sankey",
            "..graph_objects.pie",
            "..graph_objects.parcoords",
            "..graph_objects.parcats",
            "..graph_objects.ohlc",
            "..graph_objects.mesh3d",
            "..graph_objects.isosurface",
            "..graph_objects.indicator",
            "..graph_objects.image",
            "..graph_objects.icicle",
            "..graph_objects.histogram2dcontour",
            "..graph_objects.histogram2d",
            "..graph_objects.histogram",
            "..graph_objects.heatmap",
            "..graph_objects.funnelarea",
            "..graph_objects.funnel",
            "..graph_objects.densitymapbox",
            "..graph_objects.densitymap",
            "..graph_objects.contourcarpet",
            "..graph_objects.contour",
            "..graph_objects.cone",
            "..graph_objects.choroplethmapbox",
            "..graph_objects.choroplethmap",
            "..graph_objects.choropleth",
            "..graph_objects.carpet",
            "..graph_objects.candlestick",
            "..graph_objects.box",
            "..graph_objects.barpolar",
            "..graph_objects.bar",
            "..graph_objects.layout",
        ],
        [
            "..graph_objects.Waterfall",
            "..graph_objects.Volume",
            "..graph_objects.Violin",
            "..graph_objects.Treemap",
            "..graph_objects.Table",
            "..graph_objects.Surface",
            "..graph_objects.Sunburst",
            "..graph_objects.Streamtube",
            "..graph_objects.Splom",
            "..graph_objects.Scatterternary",
            "..graph_objects.Scattersmith",
            "..graph_objects.Scatterpolargl",
            "..graph_objects.Scatterpolar",
            "..graph_objects.Scattermapbox",
            "..graph_objects.Scattermap",
            "..graph_objects.Scattergl",
            "..graph_objects.Scattergeo",
            "..graph_objects.Scattercarpet",
            "..graph_objects.Scatter3d",
            "..graph_objects.Scatter",
            "..graph_objects.Sankey",
            "..graph_objects.Pie",
            "..graph_objects.Parcoords",
            "..graph_objects.Parcats",
            "..graph_objects.Ohlc",
            "..graph_objects.Mesh3d",
            "..graph_objects.Isosurface",
            "..graph_objects.Indicator",
            "..graph_objects.Image",
            "..graph_objects.Icicle",
            "..graph_objects.Histogram2dContour",
            "..graph_objects.Histogram2d",
            "..graph_objects.Histogram",
            "..graph_objects.Heatmap",
            "..graph_objects.Funnelarea",
            "..graph_objects.Funnel",
            "..graph_objects.Densitymapbox",
            "..graph_objects.Densitymap",
            "..graph_objects.Contourcarpet",
            "..graph_objects.Contour",
            "..graph_objects.Cone",
            "..graph_objects.Choroplethmapbox",
            "..graph_objects.Choroplethmap",
            "..graph_objects.Choropleth",
            "..graph_objects.Carpet",
            "..graph_objects.Candlestick",
            "..graph_objects.Box",
            "..graph_objects.Barpolar",
            "..graph_objects.Bar",
            "..graph_objects.Layout",
            "..graph_objects.Frame",
            "..graph_objects.Figure",
            "..graph_objects.Data",
            "..graph_objects.Annotations",
            "..graph_objects.Frames",
            "..graph_objects.AngularAxis",
            "..graph_objects.Annotation",
            "..graph_objects.ColorBar",
            "..graph_objects.Contours",
            "..graph_objects.ErrorX",
            "..graph_objects.ErrorY",
            "..graph_objects.ErrorZ",
            "..graph_objects.Font",
            "..graph_objects.Legend",
            "..graph_objects.Line",
            "..graph_objects.Margin",
            "..graph_objects.Marker",
            "..graph_objects.RadialAxis",
            "..graph_objects.Scene",
            "..graph_objects.Stream",
            "..graph_objects.XAxis",
            "..graph_objects.YAxis",
            "..graph_objects.ZAxis",
            "..graph_objects.XBins",
            "..graph_objects.YBins",
            "..graph_objects.Trace",
            "..graph_objects.Histogram2dcontour",
        ],
    )


if sys.version_info < (3, 7) or TYPE_CHECKING:
    try:
        import ipywidgets as _ipywidgets
        from packaging.version import Version as _Version

        if _Version(_ipywidgets.__version__) >= _Version("7.0.0"):
            from ..graph_objects._figurewidget import FigureWidget
        else:
            raise ImportError()
    except Exception:
        from ..missing_anywidget import FigureWidget
else:
    __all__.append("FigureWidget")
    orig_getattr = __getattr__

    def __getattr__(import_name):
        if import_name == "FigureWidget":
            try:
                import ipywidgets
                from packaging.version import Version

                if Version(ipywidgets.__version__) >= Version("7.0.0"):
                    from ..graph_objects._figurewidget import FigureWidget

                    return FigureWidget
                else:
                    raise ImportError()
            except Exception:
                from ..missing_anywidget import FigureWidget

                return FigureWidget
            else:
                raise ImportError()

        return orig_getattr(import_name)
