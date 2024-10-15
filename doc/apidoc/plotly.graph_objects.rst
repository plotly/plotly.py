.. _graph-objects:

`plotly.graph_objects`: low-level interface to figures, traces and layout
=========================================

.. currentmodule:: plotly.graph_objs

:mod:`plotly.graph_objects` contains the building blocks of plotly :class:`Figure`: traces
(:class:`Scatter`, :class:`Bar`, ...) and :class:`Layout`
::

   >>> import plotly.graph_objects as go

Figure
------

.. autosummary::
   :toctree: generated/
   :template: class_figure.rst

   Figure


Layout
------

.. autosummary::
   :toctree: generated/
   :template: trace.rst

   Layout


Simple Traces
--------------

.. autosummary::
   :toctree: generated/
   :template: trace.rst

   Scatter
   Scattergl
   Bar
   Pie
   Heatmap
   Heatmapgl
   Image
   Contour
   Table

Distribution Traces
-------------

.. autosummary::
   :toctree: generated/
   :template: trace.rst

   Box
   Violin
   Histogram
   Histogram2d
   Histogram2dContour

Finance Traces
-------

.. autosummary::
   :toctree: generated/
   :template: trace.rst

   Ohlc
   Candlestick
   Waterfall
   Funnel
   Funnelarea
   Indicator

3D Traces
--

.. autosummary::
   :toctree: generated/
   :template: trace.rst

   Scatter3d
   Surface
   Mesh3d
   Cone
   Streamtube
   Volume
   Isosurface

Map Traces
----

.. autosummary::
   :toctree: generated/
   :template: trace.rst

   Scattergeo
   Choropleth
   Scattermap
   Choroplethmap
   Densitymap
   Scattermapbox
   Choroplethmapbox
   Densitymapbox

Specialized Traces
-----------

.. autosummary::
   :toctree: generated/
   :template: trace.rst

   Scatterpolar
   Scatterpolargl
   Barpolar
   Scatterternary
   Sunburst
   Treemap
   Icicle
   Sankey
   Splom
   Parcats
   Parcoords
   Carpet
   Scattercarpet
   Contourcarpet
