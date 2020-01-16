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

   Figure  


Layout
------

.. autosummary::
   :toctree: generated/

   Layout
   layout



Simple charts
--------------

.. autosummary::
   :toctree: generated/

   Scatter
   scatter
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

   Box
   Violin
   Histogram
   Histogram2d
   Histogram2dContour

Finance
-------

.. autosummary::
   :toctree: generated/

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
