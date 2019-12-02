.. _graph-objects:

`plotly.graph_objects`: low-level interface to figures, traces and layout
=========================================

.. currentmodule:: plotly.graph_objects

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



Simple charts
--------------

.. autosummary::
   :toctree: generated/
   :template: trace.rst

   Scatter
   Scattergl
   Bar
   Pie
   Heatmap
   Image
   Contour
   Table

Distributions
-------------

.. autosummary::
   :toctree: generated/
   :template: trace.rst

   Box
   Violin
   Histogram
   Histogram2d
   Histogram2dContour

Finance
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

3D
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

Maps
----

.. autosummary::
   :toctree: generated/
   :template: trace.rst

   Scattergeo
   Choropleth
   Scattermapbox
   Choroplethmapbox
   Densitymapbox

Specialized
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
   Sankey
   Splom
   Parcats
   Parcoords
   Carpet
   Scattercarpet
   Contourcarpet
