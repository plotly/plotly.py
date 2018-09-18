from ._violin import Violin
from plotly.graph_objs import violin
from ._table import Table
from plotly.graph_objs import table
from ._surface import Surface
from plotly.graph_objs import surface
from ._streamtube import Streamtube
from plotly.graph_objs import streamtube
from ._splom import Splom
from plotly.graph_objs import splom
from ._scatterternary import Scatterternary
from plotly.graph_objs import scatterternary
from ._scatterpolargl import Scatterpolargl
from plotly.graph_objs import scatterpolargl
from ._scatterpolar import Scatterpolar
from plotly.graph_objs import scatterpolar
from ._scattermapbox import Scattermapbox
from plotly.graph_objs import scattermapbox
from ._scattergl import Scattergl
from plotly.graph_objs import scattergl
from ._scattergeo import Scattergeo
from plotly.graph_objs import scattergeo
from ._scattercarpet import Scattercarpet
from plotly.graph_objs import scattercarpet
from ._scatter3d import Scatter3d
from plotly.graph_objs import scatter3d
from ._scatter import Scatter
from plotly.graph_objs import scatter
from ._sankey import Sankey
from plotly.graph_objs import sankey
from ._pointcloud import Pointcloud
from plotly.graph_objs import pointcloud
from ._pie import Pie
from plotly.graph_objs import pie
from ._parcoords import Parcoords
from plotly.graph_objs import parcoords
from ._ohlc import Ohlc
from plotly.graph_objs import ohlc
from ._mesh3d import Mesh3d
from plotly.graph_objs import mesh3d
from ._histogram2dcontour import Histogram2dContour
from plotly.graph_objs import histogram2dcontour
from ._histogram2d import Histogram2d
from plotly.graph_objs import histogram2d
from ._histogram import Histogram
from plotly.graph_objs import histogram
from ._heatmapgl import Heatmapgl
from plotly.graph_objs import heatmapgl
from ._heatmap import Heatmap
from plotly.graph_objs import heatmap
from ._contourcarpet import Contourcarpet
from plotly.graph_objs import contourcarpet
from ._contour import Contour
from plotly.graph_objs import contour
from ._cone import Cone
from plotly.graph_objs import cone
from ._choropleth import Choropleth
from plotly.graph_objs import choropleth
from ._carpet import Carpet
from plotly.graph_objs import carpet
from ._candlestick import Candlestick
from plotly.graph_objs import candlestick
from ._box import Box
from plotly.graph_objs import box
from ._bar import Bar
from plotly.graph_objs import bar
from ._area import Area
from plotly.graph_objs import area
from ._layout import Layout
from plotly.graph_objs import layout
from ._frame import Frame
from ._figure import Figure

try:
    import ipywidgets
    from ._figurewidget import FigureWidget
except ImportError:
    pass

from ._deprecations import (
    Data, Annotations, Frames, AngularAxis, Annotation, ColorBar, Contours,
    ErrorX, ErrorY, ErrorZ, Font, Legend, Line, Margin, Marker, RadialAxis,
    Scene, Stream, XAxis, YAxis, ZAxis, XBins, YBins, Trace, Histogram2dcontour
)
