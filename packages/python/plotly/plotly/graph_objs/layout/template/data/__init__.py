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
    from ._scatter import Scatter
    from ._scatterpolar import Scatterpolar
    from ._scatterpolargl import Scatterpolargl
    from ._scattermapbox import Scattermapbox
    from ._scattergl import Scattergl
    from ._scattergeo import Scattergeo
    from ._scattercarpet import Scattercarpet
    from ._scatter3d import Scatter3d
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
    from ._histogram import Histogram
    from ._histogram2d import Histogram2d
    from ._histogram2dcontour import Histogram2dContour
    from ._heatmap import Heatmap
    from ._heatmapgl import Heatmapgl
    from ._funnel import Funnel
    from ._funnelarea import Funnelarea
    from ._densitymapbox import Densitymapbox
    from ._contour import Contour
    from ._contourcarpet import Contourcarpet
    from ._cone import Cone
    from ._choropleth import Choropleth
    from ._choroplethmapbox import Choroplethmapbox
    from ._carpet import Carpet
    from ._candlestick import Candlestick
    from ._box import Box
    from ._bar import Bar
    from ._barpolar import Barpolar
    from ._area import Area
else:
    from _plotly_utils.importers import relative_import

    __all__, __getattr__ = relative_import(
        __name__,
        [],
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
            "._scatter.Scatter",
            "._scatterpolar.Scatterpolar",
            "._scatterpolargl.Scatterpolargl",
            "._scattermapbox.Scattermapbox",
            "._scattergl.Scattergl",
            "._scattergeo.Scattergeo",
            "._scattercarpet.Scattercarpet",
            "._scatter3d.Scatter3d",
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
            "._histogram.Histogram",
            "._histogram2d.Histogram2d",
            "._histogram2dcontour.Histogram2dContour",
            "._heatmap.Heatmap",
            "._heatmapgl.Heatmapgl",
            "._funnel.Funnel",
            "._funnelarea.Funnelarea",
            "._densitymapbox.Densitymapbox",
            "._contour.Contour",
            "._contourcarpet.Contourcarpet",
            "._cone.Cone",
            "._choropleth.Choropleth",
            "._choroplethmapbox.Choroplethmapbox",
            "._carpet.Carpet",
            "._candlestick.Candlestick",
            "._box.Box",
            "._bar.Bar",
            "._barpolar.Barpolar",
            "._area.Area",
        ],
    )
