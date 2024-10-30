---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.8.8
  plotly:
    description: The structure of a figure - data, traces and layout explained.
    display_as: file_settings
    language: python
    layout: base
    name: The Figure Data Structure
    order: 1
    page_type: u-guide
    permalink: python/figure-structure/
    thumbnail: thumbnail/violin.jpg
---

### Overview

The `plotly` Python package exists to [create, manipulate](/python/creating-and-updating-figures/) and [render](/python/renderers/) graphical figures (i.e. charts, plots, maps and diagrams) represented by data structures also referred to as figures. The rendering process uses the [Plotly.js JavaScript library](https://plotly.com/javascript/) under the hood although Python developers using this module very rarely need to interact with the Javascript library directly, if ever. Figures can be represented in Python either as dicts or as instances of the `plotly.graph_objects.Figure` class, and are serialized as text in [JavaScript Object Notation (JSON)](https://json.org/) before being passed to Plotly.js.

> Note: the recommended entry-point into the plotly package is the [high-level plotly.express module, also known as Plotly Express](/python/plotly-express/), which consists of Python functions which return fully-populated `plotly.graph_objects.Figure` objects. This page exists to document the architecture of the data structure that these objects represent, for users who wish to understand more about how to customize them, or assemble them from [other `plotly.graph_objects` components](/python/graph-objects/).

Viewing the underlying data structure for any `plotly.graph_objects.Figure` object, including those returned by Plotly Express, can be done via `print(fig)` or, in JupyterLab, with the special `fig.show("json")` renderer. Figures also support `fig.to_dict()` and `fig.to_json()` methods. `print()`ing the figure will result in the often-verbose `layout.template` key being represented as ellipses `'...'` for brevity.

```python
import plotly.express as px

fig = px.line(x=["a","b","c"], y=[1,3,2], title="sample figure")
print(fig)
fig.show()
```

### Accessing figure structures in Dash

[Dash](https://plotly.com/dash/) is the best way to build analytical apps in Python using Plotly figures. To run the app below, run `pip install dash`, click "Download" to get the code and run `python app.py`.

Get started  with [the official Dash docs](https://dash.plotly.com/installation) and **learn how to effortlessly [style](https://plotly.com/dash/design-kit/) & [deploy](https://plotly.com/dash/app-manager/) apps like this with <a class="plotly-red" href="https://plotly.com/dash/">Dash Enterprise</a>.**


```python hide_code=true
from IPython.display import IFrame
snippet_url = 'https://python-docs-dash-snippets.herokuapp.com/python-docs-dash-snippets/'
IFrame(snippet_url + 'figure-structure', width='100%', height=1200)
```

<div style="font-size: 0.9em;"><div style="width: calc(100% - 30px); box-shadow: none; border: thin solid rgb(229, 229, 229);"><div style="padding: 5px;"><div><p><strong>Sign up for Dash Club</strong> → Free cheat sheets plus updates from Chris Parmer and Adam Schroeder delivered to your inbox every two months. Includes tips and tricks, community apps, and deep dives into the Dash architecture.
<u><a href="https://go.plotly.com/dash-club?utm_source=Dash+Club+2022&utm_medium=graphing_libraries&utm_content=inline">Join now</a></u>.</p></div></div></div></div>


### Figures as Trees of Attributes

Plotly.js supports inputs adhering to a well-defined schema, whose overall architecture is explained in this page and which is exhaustively documented in the [Figure Reference](/python/reference/index/) (which is itself generated from a [machine-readable JSON representation of the schema](https://raw.githubusercontent.com/plotly/plotly.js/master/dist/plot-schema.json)). Figures are represented as trees with named nodes called "attributes". The root node of the tree has three top-level attributes: `data`, `layout` and `frames` (see below).

Attributes are referred to in text and in the [Figure Reference](/python/reference/index/) by their full "path" i.e. the dot-delimited concatenation of their parents. For example `"layout.width"` refers to the attribute whose key is `"width"` inside a dict which is the value associated with a key `"layout"` at the root of the figure. If one of the parents is a list rather than a dict, a set of brackets is inserted in the path when referring to the attribute in the abstract, e.g. `"layout.annotations[].text"`. Finally, as explained below, the top-level "data" attribute defines a list of typed objects called "traces" with the schema dependent upon the type, and these attributes' paths are listed in the [Figure Reference](/python/reference/index/) as `"data[type=scatter].name"`.

The [`plotly.graph_objects` module contains an automatically-generated hierarchy of  Python classes](/python/graph-objects/) which represent non-leaf attributes in the figure schema and provide a Pythonic API for them. When [manipulating a `plotly.graph_objects.Figure` object](/python/creating-and-updating-figures/), attributes can be set either directly using Python object attributes e.g. `fig.layout.title.font.family="Open Sans"` or using [update methods and "magic underscores"](/python/creating-and-updating-figures/#magic-underscore-notation) e.g. `fig.update_layout(title_font_family="Open Sans")`

When building a figure, it is *not necessary to populate every attribute* of every object. At render-time, [the JavaScript layer will compute default values](/python/figure-introspection/) for each required unspecified attribute, depending upon the ones that are specified, as documented in the [Figure Reference](/python/reference/index/). An example of this would be `layout.xaxis.range`, which may be specified explicitly, but if not will be computed based on the range of `x` values for every trace linked to that axis. The JavaScript layer will ignore unknown attributes or malformed values, although the `plotly.graph_objects` module provides Python-side validation for attribute values. Note also that if [the `layout.template` key is present (as it is by default)](/python/templates/) then default values will be drawn first from the contents of the template and only if missing from there will the JavaScript layer infer further defaults. The built-in template can be disabled by setting `layout.template="none"`.

### The Top-Level `data` Attribute

The first of the three top-level attributes of a figure is `data`, whose value must be a list of dicts referred to as "traces".

* Each trace has one of more than 40 possible types (see below for a list organized by subplot type, including e.g. [`scatter`](/python/line-and-scatter/), [`bar`](/python/bar-charts/), [`pie`](/python/pie-charts/), [`surface`](/python/3d-surface-plots/), [`choropleth`](/python/choropleth-maps/) etc), and represents a set of related graphical marks in a figure. Each trace must have a `type` attribute which defines the other allowable attributes.
* Each trace is drawn on a single [subplot](/python/subplots/) whose type must be compatible with the trace's type, or is its own subplot (see below).
* Traces may have a single [legend](/python/legend/) entry, with the exception of pie and funnelarea traces (see below).
* Certain trace types support [continuous color, with an associated colorbar](/python/colorscales/), which can be controlled by attributes either within the trace, or within the layout when using the [coloraxis attribute](/python/colorscales/).


### The Top-Level `layout` Attribute

The second of the three top-level attributes of a figure is `layout`, whose value is referred to in text as "the layout" and must be a dict, containing attributes that control positioning and configuration of non-data-related parts of the figure such as:

  * Dimensions and margins, which define the bounds of "paper coordinates" (see below)
  * Figure-wide defaults: [templates](/python/templates/), [fonts](/python/figure-labels/), colors, hover-label and modebar defaults
  * [Title](/python/figure-labels/) and [legend](/python/legend/) (positionable in container and/or paper coordinates)
  * [Color axes and associated color bars](/python/colorscales/) (positionable in paper coordinates)
  * Subplots of various types on which can be drawn multiple traces and which are positioned in paper coordinates:
    * `xaxis`, `yaxis`, `xaxis2`, `yaxis3` etc: X and Y cartesian axes, the intersections of which are cartesian subplots
    * `scene`, `scene2`, `scene3` etc: 3d scene subplots
    * `ternary`, `ternary2`, `ternary3`, `polar`, `polar2`, `polar3`, `geo`, `geo2`, `geo3`, `map`, `map2`, `map3`, `smith`, `smith2` etc: ternary, polar, geo, map or smith subplots
  * Non-data marks which can be positioned in paper coordinates, or in data coordinates linked to 2d cartesian subplots:
    * `annotations`: [textual annotations with or without arrows](/python/text-and-annotations/)
    * `shapes`: [lines, rectangles, ellipses or open or closed paths](/python/shapes/)
    * `images`: [background or decorative images](/python/images/)
  * Controls which can be positioned in paper coordinates and which can trigger Plotly.js functions when interacted with by a user:
    * `updatemenus`: [single buttons, toggles](/python/custom-buttons/) and [dropdown menus](/python/dropdowns/)
    * `sliders`: [slider controls](/python/sliders/)

### The Top-Level `frames` Attribute

The third of the three top-level attributes of a figure is `frames`, whose value must be a list of dicts that define sequential frames in an [animated plot](/python/animations/). Each frame contains its own data attribute as well as other parameters. Animations are usually triggered and controlled via controls defined in layout.sliders and/or layout.updatemenus

### The `config` Object

At [render-time](/python/renderers/), it is also possible to control certain figure behaviors which are not considered part of the figure proper i.e. the behavior of the "modebar" and how the figure relates to mouse actions like scrolling etc. The object that contains these options is called the [`config`, and has its own documentation page](/python/configuration-options/). It is exposed in Python as the `config` keyword argument of the `.show()` method on `plotly.graph_objects.Figure` objects.

### Positioning With Paper, Container Coordinates, or Axis Domain Coordinates

Various figure components configured within the layout of the figure support positioning attributes named `x` or `y`, whose values may be specified in "paper coordinates" (sometimes referred to as "plot fractions" or "normalized coordinates"). Examples include `layout.xaxis.domain` or `layout.legend.x` or `layout.annotation[].x`.

Positioning in paper coordinates is *not* done in absolute pixel terms, but rather in terms relative to a coordinate system defined with an origin `(0,0)` at `(layout.margin.l, layout.margin.b)` and a point `(1,1)` at `(layout.width-layout.margin.r, layout.height-layout.margin.t)` (note: `layout.margin` values are pixel values, as are `layout.width` and `layout.height`). Paper coordinate values less than 0 or greater than 1 are permitted, and refer to areas within the plot margins.

To position an object in "paper" coordinates, the corresponding axis reference
is set to `"paper"`. For instance a shape's `xref` attribute would be set to
`"paper"` so that the `x` value of the shape refers to its position in paper
coordinates.

Note that the contents of the `layout.margin` attribute are by default computed based on the position and dimensions of certain items like the title or legend, and may be made dependent on the position and dimensions of tick labels as well when setting the `layout.xaxis.automargin` attribute to `True`. This has the effect of automatically increasing the margin values and therefore shrinking the physical area defined between the `(0,0)` and `(1,1)` points. Positioning certain items at paper coordinates less than 0 or greater than 1 will also trigger this behavior. The `layout.width` and `layout.height`, however, are taken as givens, so a figure will never grow or shrink based on its contents.

The figure title may be positioned using "container coordinates" which have `(0,0)` and `(1,1)` anchored at the bottom-left and top-right of the figure, respectively, and therefore are independent of the values of layout.margin.

Furthermore, shapes, annotations, and images can be placed relative to an axis's
domain so that, for instance, an `x` value of `0.5` would place the object
halfway along the x-axis, regardless of the domain as specified in the
`layout.xaxis.domain` attribute. This behavior can be specified by adding
`' domain'` to the axis reference in the axis referencing attribute of the object.
For example, setting `yref = 'y2 domain'` for a shape will refer to the length
and position of the axis named `y2`.

### 2D Cartesian Trace Types and Subplots

The most commonly-used kind of subplot is a [two-dimensional Cartesian subplot](/python/axes/). Traces compatible with these subplots support `xaxis` and `yaxis` attributes whose values must refer to corresponding objects in the layout portion of the figure. For example, if `xaxis="x"`, and `yaxis="y"` (which is the default) then this trace is drawn on the subplot at the intersection of the axes configured under `layout.xaxis` and `layout.yaxis`, but if `xaxis="x2"` and `yaxis="y3"` then the trace is drawn at the intersection of the axes configured under `layout.xaxis2` and `layout.yaxis3`. Note that attributes such as `layout.xaxis` and `layout.xaxis2` etc do not have to be explicitly defined, in which case default values will be inferred. Multiple traces of different types can be drawn on the same subplot.

X- and Y-axes support the `type` attribute, which enables them to represent [continuous values (`type="linear"`, `type="log"`)](/python/axes/), [temporal values (`type="date"`)](/python/time-series/) or [categorical values (`type="category"`, `type="multicategory`)](/python/bar-charts/). Axes can also be overlaid on top of one another to create [dual-axis or multiple-axis charts](/python/multiple-axes/). 2-d cartesian subplots lend themselves very well to creating ["small multiples" figures, also known as facet or trellis plots](/python/facet-plots/).

The following trace types are compatible with 2d-cartesian subplots via the `xaxis` and `yaxis` attributes:

* scatter-like trace types: [`scatter`](/python/line-and-scatter/) and [`scattergl`](/python/webgl-vs-svg/), which can be used to draw [scatter plots](/python/line-and-scatter/), [line plots and curves](/python/line-charts/), [time-series plots](/python/time-series/), [bubble charts](/python/bubble-charts/), [dot plots](/python/dot-plots/) and [filled areas](/python/filled-area-plots/) and also support [error bars](/python/error-bars/)
* [`bar`](/python/bar-charts/), [`funnel`](/python/funnel-charts/), [`waterfall`](/python/waterfall-charts/): bar-like trace types which can also be used to draw [timelines and Gantt charts](/python/gantt/)
* [`histogram`](/python/histograms/): an *aggregating* bar-like trace type
* [`box`](/python/box-plots/) and [`violin`](/python/box-plots/): 1-dimensional distribution-like trace types
* [`histogram2d`](/python/2D-Histogram/) and [`histogram2dcontour`](/python/2d-histogram-contour/): 2-dimensional distribution-like density trace types
* [`image`](/python/imshow/), [`heatmap`](/python/heatmaps/) and [`contour`](/python/contour-plots/): matrix trace types
* [`ohlc`](/python/ohlc-charts/) and [`candlestick`](/python/candlestick-charts/): stock-like trace types
* [`carpet`](/python/carpet-plot/): a special trace type for building [carpet plots](/python/carpet-plot/), in that other traces can use as subplots (see below)
* [`splom`](/python/splom/): multi-dimensional scatter plots which implicitly refer to many 2-d cartesian subplots at once.

### 3D, Polar, Ternary and Smith Trace Types and Subplots

Beyond 2D cartesian subplots, figures can include [three-dimensional cartesian subplots](/python/3d-charts/), [polar subplots](/python/polar-chart/), [ternary subplots](/python/ternary-plots/) and [smith subplots](/python/smith-charts/). The following trace types support attributes named `scene`, `polar`, `smith` or `ternary`, whose values must refer to corresponding objects in the layout portion of the figure i.e. `ternary="ternary2"` etc. Note that attributes such as `layout.scene` and `layout.ternary2` etc do not have to be explicitly defined, in which case default values will be inferred. Multiple traces of a compatible type can be placed on the same subplot.

The following trace types are compatible with 3D subplots via the `scene` attribute, which contains special [camera controls](/python/3d-camera-controls/):

* [`scatter3d`](/python/3d-scatter-plots/), which can be used to draw [individual markers](/python/3d-scatter-plots/), [3d bubble charts](/python/3d-bubble-charts/) and [lines and curves](/python/3d-line-plots/)
* [`surface`](/python/3d-surface-plots/) and [`mesh`](/python/3d-mesh/): 3d surface trace types
* [`cone`](/python/cone-plot/) and [`streamtube`](/python/streamtube-plot/): 3d vector field trace types
* [`volume`](/python/3d-volume-plots/) and [`isosurface`](/python/3d-isosurface-plots/): 3d volume trace types

The following trace types are compatible with polar subplots via the `polar` attribute:

* scatter-like trace types: [`scatterpolar` and `scatterpolargl`](/python/polar-chart/), which can be used to draw individual markers, [curves and filled areas (i.e. radar or spider charts)](/python/radar-chart/)
* [`barpolar`](/python/wind-rose-charts/): useful for [wind roses](/python/wind-rose-charts/) and other polar bar charts

The following trace types are compatible with ternary subplots via the `ternary` attribute:

* [`scatterternary`](/python/ternary-plots/), which can be used to draw individual markers, [curves and filled areas](/python/ternary-contour/)

The following trace types are compatible with smith subplots via the `smith` attribute:

* [`scattersmith`](/python/smith-charts/), which can be used to draw individual markers, curves and filled areas

### Map Trace Types and Subplots

Figures can include two different types of map subplots: [geo subplots for outline maps](/python/map-configuration/) and [tile-based maps](/python/tile-map-layers/). The following trace types support attributes named `geo` or `map`, whose values must refer to corresponding objects in the layout i.e. `geo="geo2"` etc.  Note that attributes such as `layout.geo2` and `layout.map` etc do not have to be explicitly defined, in which case default values will be inferred. Multiple traces of a compatible type can be placed on the same subplot.

The following trace types are compatible with geo subplots via the `geo` attribute:

* [`scattergeo`](/python/scatter-plots-on-maps/), which can be used to draw [individual markers](/python/scatter-plots-on-maps/), [line and curves](/python/lines-on-maps/) and filled areas on outline maps
* [`choropleth`](/python/choropleth-maps/): [colored polygons](/python/choropleth-maps/) on outline maps

The following trace types are compatible with tile map subplots via the `map` attribute:

* [`scattermap`](/python/tile-scatter-maps/), which can be used to draw [individual markers](/python/tile-scatter-maps/), [lines and curves](/python/lines-on-tile-maps/) and [filled areas](/python/filled-area-tile-maps/) on tile maps
* [`choroplethmap`](/python/tile-county-choropleth/): colored polygons on tile maps
* [`densitymap`](/python/tile-density-heatmaps/): density heatmaps on tile maps

### Traces Which Are Their Own Subplots

Certain trace types cannot share subplots, and hence have no attribute to map to a corresponding subplot in the layout. Instead, these traces are their own subplot and support a `domain` attribute for position, which enables the trace to be positioned in paper coordinates (see below). With the exception of `pie` and `funnelarea`, such traces also do not support legends (see below)

The following trace types are their own subplots and support a domain attribute:

* [`pie`](/python/pie-charts/) and [`funnelarea`](/python/waterfall-charts/): one-level part-to-whole relationships with legend items
* [`sunburst`](/python/sunburst-charts/) and [`treemap`](/python/treemaps/): hierarchical multi-level part-to-whole relationships
* [`parcoords`](/python/parallel-coordinates-plot/) and [`parcats`](/python/parallel-categories-diagram/): continuous and categorical multidimensional figures with [parallel coordinates](/python/parallel-coordinates-plot/) and [parallel sets](/python/parallel-categories-diagram/)
* [`sankey`](/python/sankey-diagram/): [flow diagrams](/python/sankey-diagram/)
* [`table`](/python/table/): [text-based tables](/python/table/)
* [`indicator`](/python/indicator/): big numbers, [gauges](/python/gauge-charts/), and [bullet charts](/python/bullet-charts/)

### Carpet Trace Types and Subplots

Certain trace types use [traces of type `carpet` as a subplot](/python/carpet-plot/). These support a `carpet` attribute whose value must match the value of the `carpet` attribute of the `carpet` trace they are to be drawn on. Multiple compatible traces can be placed on the same `carpet` trace.

The following trace types are compatible with `carpet` trace subplots via the `carpet` attribute:

* [`scattercarpet`](/python/carpet-scatter/), which can be used to draw individual markers, curves and filled areas
* [`contourcarpet`](/python/carpet-plot/)

### Trace Types, Legends and Color Bars

Traces of most types can be optionally associated with a single legend item in the [legend](/python/legend/). Whether or not a given trace appears in the legend is controlled via the `showlegend` attribute. Traces which are their own subplots (see above) do not support this, with the exception of traces of type `pie` and `funnelarea` for which every distinct color represented in the trace gets a separate legend item. Users may show or hide traces by clicking or double-clicking on their associated legend item. Traces that support legend items also support the `legendgroup` attribute, and all traces with the same legend group are treated the same way during click/double-click interactions.

The fact that legend items are linked to traces means that when using [discrete color](/python/discrete-color/), a figure must have one trace per color in order to get a meaningful legend. [Plotly Express has robust support for discrete color](/python/discrete-color/) to make this easy.

Traces which support [continuous color](/python/colorscales/) can also be associated with color axes in the layout via the `coloraxis` attribute. Multiple traces can be linked to the same color axis. Color axes have a legend-like component called color bars. Alternatively, color axes can be configured within the trace itself.

```python

```
