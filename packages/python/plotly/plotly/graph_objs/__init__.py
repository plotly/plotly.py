import sys

if sys.version_info < (3, 7):
    from ._waterfall import Waterfall
    from ._volume import Volume
    from ._violin import Violin
    from ._treemap import Treemap
    from ._table import Table
    from ._surface import Surface
    from ._sunburst import Sunburst
    from ._streamtube import Streamtube
    from ._splom import Splom
    from ._scatterternary import Scatterternary
    from ._scatterpolargl import Scatterpolargl
    from ._scatterpolar import Scatterpolar
    from ._scattermapbox import Scattermapbox
    from ._scattergl import Scattergl
    from ._scattergeo import Scattergeo
    from ._scattercarpet import Scattercarpet
    from ._scatter3d import Scatter3d
    from ._scatter import Scatter
    from ._sankey import Sankey
    from ._pointcloud import Pointcloud
    from ._pie import Pie
    from ._parcoords import Parcoords
    from ._parcats import Parcats
    from ._ohlc import Ohlc
    from ._mesh3d import Mesh3d
    from ._isosurface import Isosurface
    from ._indicator import Indicator
    from ._image import Image
    from ._histogram2dcontour import Histogram2dContour
    from ._histogram2d import Histogram2d
    from ._histogram import Histogram
    from ._heatmapgl import Heatmapgl
    from ._heatmap import Heatmap
    from ._funnelarea import Funnelarea
    from ._funnel import Funnel
    from ._densitymapbox import Densitymapbox
    from ._contourcarpet import Contourcarpet
    from ._contour import Contour
    from ._cone import Cone
    from ._choroplethmapbox import Choroplethmapbox
    from ._choropleth import Choropleth
    from ._carpet import Carpet
    from ._candlestick import Candlestick
    from ._box import Box
    from ._barpolar import Barpolar
    from ._bar import Bar
    from ._area import Area
    from ._layout import Layout
    from ._frame import Frame
    from ._figure import Figure
    from ._deprecations import Data
    from ._deprecations import Annotations
    from ._deprecations import Frames
    from ._deprecations import AngularAxis
    from ._deprecations import Annotation
    from ._deprecations import ColorBar
    from ._deprecations import Contours
    from ._deprecations import ErrorX
    from ._deprecations import ErrorY
    from ._deprecations import ErrorZ
    from ._deprecations import Font
    from ._deprecations import Legend
    from ._deprecations import Line
    from ._deprecations import Margin
    from ._deprecations import Marker
    from ._deprecations import RadialAxis
    from ._deprecations import Scene
    from ._deprecations import Stream
    from ._deprecations import XAxis
    from ._deprecations import YAxis
    from ._deprecations import ZAxis
    from ._deprecations import XBins
    from ._deprecations import YBins
    from ._deprecations import Trace
    from ._deprecations import Histogram2dcontour
    from . import waterfall
    from . import volume
    from . import violin
    from . import treemap
    from . import table
    from . import surface
    from . import sunburst
    from . import streamtube
    from . import splom
    from . import scatterternary
    from . import scatterpolargl
    from . import scatterpolar
    from . import scattermapbox
    from . import scattergl
    from . import scattergeo
    from . import scattercarpet
    from . import scatter3d
    from . import scatter
    from . import sankey
    from . import pointcloud
    from . import pie
    from . import parcoords
    from . import parcats
    from . import ohlc
    from . import mesh3d
    from . import isosurface
    from . import indicator
    from . import image
    from . import histogram2dcontour
    from . import histogram2d
    from . import histogram
    from . import heatmapgl
    from . import heatmap
    from . import funnelarea
    from . import funnel
    from . import densitymapbox
    from . import contourcarpet
    from . import contour
    from . import cone
    from . import choroplethmapbox
    from . import choropleth
    from . import carpet
    from . import candlestick
    from . import box
    from . import barpolar
    from . import bar
    from . import area
    from . import layout
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__, __dir__ = relative_import(
        __name__,
        [
            ".waterfall",
            ".volume",
            ".violin",
            ".treemap",
            ".table",
            ".surface",
            ".sunburst",
            ".streamtube",
            ".splom",
            ".scatterternary",
            ".scatterpolargl",
            ".scatterpolar",
            ".scattermapbox",
            ".scattergl",
            ".scattergeo",
            ".scattercarpet",
            ".scatter3d",
            ".scatter",
            ".sankey",
            ".pointcloud",
            ".pie",
            ".parcoords",
            ".parcats",
            ".ohlc",
            ".mesh3d",
            ".isosurface",
            ".indicator",
            ".image",
            ".histogram2dcontour",
            ".histogram2d",
            ".histogram",
            ".heatmapgl",
            ".heatmap",
            ".funnelarea",
            ".funnel",
            ".densitymapbox",
            ".contourcarpet",
            ".contour",
            ".cone",
            ".choroplethmapbox",
            ".choropleth",
            ".carpet",
            ".candlestick",
            ".box",
            ".barpolar",
            ".bar",
            ".area",
            ".layout",
        ],
        [
            "._waterfall.Waterfall",
            "._volume.Volume",
            "._violin.Violin",
            "._treemap.Treemap",
            "._table.Table",
            "._surface.Surface",
            "._sunburst.Sunburst",
            "._streamtube.Streamtube",
            "._splom.Splom",
            "._scatterternary.Scatterternary",
            "._scatterpolargl.Scatterpolargl",
            "._scatterpolar.Scatterpolar",
            "._scattermapbox.Scattermapbox",
            "._scattergl.Scattergl",
            "._scattergeo.Scattergeo",
            "._scattercarpet.Scattercarpet",
            "._scatter3d.Scatter3d",
            "._scatter.Scatter",
            "._sankey.Sankey",
            "._pointcloud.Pointcloud",
            "._pie.Pie",
            "._parcoords.Parcoords",
            "._parcats.Parcats",
            "._ohlc.Ohlc",
            "._mesh3d.Mesh3d",
            "._isosurface.Isosurface",
            "._indicator.Indicator",
            "._image.Image",
            "._histogram2dcontour.Histogram2dContour",
            "._histogram2d.Histogram2d",
            "._histogram.Histogram",
            "._heatmapgl.Heatmapgl",
            "._heatmap.Heatmap",
            "._funnelarea.Funnelarea",
            "._funnel.Funnel",
            "._densitymapbox.Densitymapbox",
            "._contourcarpet.Contourcarpet",
            "._contour.Contour",
            "._cone.Cone",
            "._choroplethmapbox.Choroplethmapbox",
            "._choropleth.Choropleth",
            "._carpet.Carpet",
            "._candlestick.Candlestick",
            "._box.Box",
            "._barpolar.Barpolar",
            "._bar.Bar",
            "._area.Area",
            "._layout.Layout",
            "._frame.Frame",
            "._figure.Figure",
            "._deprecations.Data",
            "._deprecations.Annotations",
            "._deprecations.Frames",
            "._deprecations.AngularAxis",
            "._deprecations.Annotation",
            "._deprecations.ColorBar",
            "._deprecations.Contours",
            "._deprecations.ErrorX",
            "._deprecations.ErrorY",
            "._deprecations.ErrorZ",
            "._deprecations.Font",
            "._deprecations.Legend",
            "._deprecations.Line",
            "._deprecations.Margin",
            "._deprecations.Marker",
            "._deprecations.RadialAxis",
            "._deprecations.Scene",
            "._deprecations.Stream",
            "._deprecations.XAxis",
            "._deprecations.YAxis",
            "._deprecations.ZAxis",
            "._deprecations.XBins",
            "._deprecations.YBins",
            "._deprecations.Trace",
            "._deprecations.Histogram2dcontour",
        ],
    )


if sys.version_info < (3, 7):
    try:
        import ipywidgets
        from distutils.version import LooseVersion

        if LooseVersion(ipywidgets.__version__) >= LooseVersion("7.0.0"):
            from ..graph_objs._figurewidget import FigureWidget
        del LooseVersion
        del ipywidgets
    except ImportError:
        pass
else:
    __all__.append("FigureWidget")
    orig_getattr = __getattr__

    def __getattr__(import_name):
        if import_name == "FigureWidget":
            try:
                import ipywidgets
                from distutils.version import LooseVersion

                if LooseVersion(ipywidgets.__version__) >= LooseVersion("7.0.0"):
                    from ..graph_objs._figurewidget import FigureWidget

                    return FigureWidget
            except ImportError:
                pass

        return orig_getattr(import_name)
