from __future__ import absolute_import

# Require that numpy exists for figure_factory
import numpy

from plotly.figure_factory._2d_density import create_2d_density
from plotly.figure_factory._annotated_heatmap import create_annotated_heatmap
from plotly.figure_factory._candlestick import create_candlestick
from plotly.figure_factory._dendrogram import create_dendrogram
from plotly.figure_factory._distplot import create_distplot
from plotly.figure_factory._gantt import create_gantt
from plotly.figure_factory._ohlc import create_ohlc
from plotly.figure_factory._quiver import create_quiver
from plotly.figure_factory._scatterplot import create_scatterplotmatrix
from plotly.figure_factory._streamline import create_streamline
from plotly.figure_factory._table import create_table
from plotly.figure_factory._trisurf import create_trisurf
from plotly.figure_factory._violin import create_violin
