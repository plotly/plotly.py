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

The `plotly` Python package exists to [create, manipulate](creating-and-updating-figures.md) and [render](renderers.md) graphical figures (i.e. charts, plots, maps and diagrams) represented by data structures also referred to as figures. The rendering process uses the [Plotly.js JavaScript library](https://plotly.com/javascript/) under the hood although Python developers using this module very rarely need to interact with the Javascript library directly, if ever. Figures can be represented in Python either as dicts or as instances of the `plotly.graph_objects.Figure` class, and are serialized as text in [JavaScript Object Notation (JSON)](https://json.org/) before being passed to Plotly.js.

> Note: the recommended entry-point into the plotly package is the [high-level plotly.express module, also known as Plotly Express](plotly-express.md), which consists of Python functions which return fully-populated `plotly.graph_objects.Figure` objects. This page exists to document the architecture of the data structure that these objects represent, for users who wish to understand more about how to customize them, or assemble them from [other `plotly.graph_objects` components](graph-objects.md).

Viewing the underlying data structure for any `plotly.graph_objects.Figure` object, including those returned by Plotly Express, can be done via `print(fig)` or, in JupyterLab, with the special `fig.show("json")` renderer. Figures also support `fig.to_dict()` and `fig.to_json()` methods. `print()`ing the figure will result in the often-verbose `layout.template` key being represented as ellipses `'...'` for brevity.

```python
import plotly.express as px

fig = px.line(x=["a","b","c"], y=[1,3,2], title="sample figure")
print(fig)
fig.show()
```

**Output:**
```
Figure({
    'data': [{'hovertemplate': 'x=%{x}<br>y=%{y}<extra></extra>',
              'legendgroup': '',
              'line': {'color': '#636efa', 'dash': 'solid'},
              'marker': {'symbol': 'circle'},
              'mode': 'lines',
              'name': '',
              'orientation': 'v',
              'showlegend': False,
              'type': 'scatter',
              'x': array(['a', 'b', 'c'], dtype=object),
              'xaxis': 'x',
              'y': {'bdata': 'AQMC', 'dtype': 'i1'},
              'yaxis': 'y'}],
    'layout': {'legend': {'tracegroupgap': 0},
               'template': '...',
               'title': {'text': 'sample figure'},
               'xaxis': {'anchor': 'y', 'domain': [0.0, 1.0], 'title': {'text': 'x'}},
               'yaxis': {'anchor': 'x', 'domain': [0.0, 1.0], 'title': {'text': 'y'}}}
})
```
<div>                        <script type="text/javascript">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>
        <script charset="utf-8" src="https://cdn.plot.ly/plotly-3.1.0.min.js" integrity="sha256-Ei4740bWZhaUTQuD6q9yQlgVCMPBz6CZWhevDYPv93A=" crossorigin="anonymous"></script>                <div id="plotly-div-1" class="plotly-graph-div" style="height:100%; width:100%;"></div>            <script type="text/javascript">                window.PLOTLYENV=window.PLOTLYENV || {};                                if (document.getElementById("plotly-div-1")) {                    Plotly.newPlot(                        "plotly-div-1",                        [{"hovertemplate":"x=%{x}\u003cbr\u003ey=%{y}\u003cextra\u003e\u003c\u002fextra\u003e","legendgroup":"","line":{"color":"#636efa","dash":"solid"},"marker":{"symbol":"circle"},"mode":"lines","name":"","orientation":"v","showlegend":false,"x":["a","b","c"],"xaxis":"x","y":{"dtype":"i1","bdata":"AQMC"},"yaxis":"y","type":"scatter"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermap":[{"type":"scattermap","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"title":{"text":"x"}},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"y"}},"legend":{"tracegroupgap":0},"title":{"text":"sample figure"}},                        {"responsive": true}                    )                };            </script>        </div>

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

Plotly.js supports inputs adhering to a well-defined schema, whose overall architecture is explained in this page and which is exhaustively documented in the [Figure Reference](reference/index.md) (which is itself generated from a [machine-readable JSON representation of the schema](https://raw.githubusercontent.com/plotly/plotly.js/master/dist/plot-schema.json)). Figures are represented as trees with named nodes called "attributes". The root node of the tree has three top-level attributes: `data`, `layout` and `frames` (see below).

Attributes are referred to in text and in the [Figure Reference](reference/index.md) by their full "path" i.e. the dot-delimited concatenation of their parents. For example `"layout.width"` refers to the attribute whose key is `"width"` inside a dict which is the value associated with a key `"layout"` at the root of the figure. If one of the parents is a list rather than a dict, a set of brackets is inserted in the path when referring to the attribute in the abstract, e.g. `"layout.annotations[].text"`. Finally, as explained below, the top-level "data" attribute defines a list of typed objects called "traces" with the schema dependent upon the type, and these attributes' paths are listed in the [Figure Reference](reference/index.md) as `"data[type=scatter].name"`.

The [`plotly.graph_objects` module contains an automatically-generated hierarchy of  Python classes](graph-objects.md) which represent non-leaf attributes in the figure schema and provide a Pythonic API for them. When [manipulating a `plotly.graph_objects.Figure` object](creating-and-updating-figures.md), attributes can be set either directly using Python object attributes e.g. `fig.layout.title.font.family="Open Sans"` or using [update methods and "magic underscores"](../creating-and-updating-figures/#magic-underscore-notation) e.g. `fig.update_layout(title_font_family="Open Sans")`

When building a figure, it is *not necessary to populate every attribute* of every object. At render-time, [the JavaScript layer will compute default values](figure-introspection.md) for each required unspecified attribute, depending upon the ones that are specified, as documented in the [Figure Reference](reference/index.md). An example of this would be `layout.xaxis.range`, which may be specified explicitly, but if not will be computed based on the range of `x` values for every trace linked to that axis. The JavaScript layer will ignore unknown attributes or malformed values, although the `plotly.graph_objects` module provides Python-side validation for attribute values. Note also that if [the `layout.template` key is present (as it is by default)](templates.md) then default values will be drawn first from the contents of the template and only if missing from there will the JavaScript layer infer further defaults. The built-in template can be disabled by setting `layout.template="none"`.

### The Top-Level `data` Attribute

The first of the three top-level attributes of a figure is `data`, whose value must be a list of dicts referred to as "traces".

* Each trace has one of more than 40 possible types (see below for a list organized by subplot type, including e.g. [`scatter`](line-and-scatter.md), [`bar`](bar-charts.md), [`pie`](pie-charts.md), [`surface`](3d-surface-plots.md), [`choropleth`](choropleth-maps.md) etc), and represents a set of related graphical marks in a figure. Each trace must have a `type` attribute which defines the other allowable attributes.
* Each trace is drawn on a single [subplot](subplots.md) whose type must be compatible with the trace's type, or is its own subplot (see below).
* Traces may have a single [legend](legend.md) entry, with the exception of pie and funnelarea traces (see below).
* Certain trace types support [continuous color, with an associated colorbar](colorscales.md), which can be controlled by attributes either within the trace, or within the layout when using the [coloraxis attribute](colorscales.md).


### The Top-Level `layout` Attribute

The second of the three top-level attributes of a figure is `layout`, whose value is referred to in text as "the layout" and must be a dict, containing attributes that control positioning and configuration of non-data-related parts of the figure such as:

  * Dimensions and margins, which define the bounds of "paper coordinates" (see below)
  * Figure-wide defaults: [templates](templates.md), [fonts](figure-labels.md), colors, hover-label and modebar defaults
  * [Title](figure-labels.md) and [legend](legend.md) (positionable in container and/or paper coordinates)
  * [Color axes and associated color bars](colorscales.md) (positionable in paper coordinates)
  * Subplots of various types on which can be drawn multiple traces and which are positioned in paper coordinates:
    * `xaxis`, `yaxis`, `xaxis2`, `yaxis3` etc: X and Y cartesian axes, the intersections of which are cartesian subplots
    * `scene`, `scene2`, `scene3` etc: 3d scene subplots
    * `ternary`, `ternary2`, `ternary3`, `polar`, `polar2`, `polar3`, `geo`, `geo2`, `geo3`, `map`, `map2`, `map3`, `smith`, `smith2` etc: ternary, polar, geo, map or smith subplots
  * Non-data marks which can be positioned in paper coordinates, or in data coordinates linked to 2d cartesian subplots:
    * `annotations`: [textual annotations with or without arrows](text-and-annotations.md)
    * `shapes`: [lines, rectangles, ellipses or open or closed paths](shapes.md)
    * `images`: [background or decorative images](images.md)
  * Controls which can be positioned in paper coordinates and which can trigger Plotly.js functions when interacted with by a user:
    * `updatemenus`: [single buttons, toggles](custom-buttons.md) and [dropdown menus](dropdowns.md)
    * `sliders`: [slider controls](sliders.md)

### The Top-Level `frames` Attribute

The third of the three top-level attributes of a figure is `frames`, whose value must be a list of dicts that define sequential frames in an [animated plot](animations.md). Each frame contains its own data attribute as well as other parameters. Animations are usually triggered and controlled via controls defined in layout.sliders and/or layout.updatemenus

### The `config` Object

At [render-time](renderers.md), it is also possible to control certain figure behaviors which are not considered part of the figure proper i.e. the behavior of the "modebar" and how the figure relates to mouse actions like scrolling etc. The object that contains these options is called the [`config`, and has its own documentation page](configuration-options.md). It is exposed in Python as the `config` keyword argument of the `.show()` method on `plotly.graph_objects.Figure` objects.

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

The most commonly-used kind of subplot is a [two-dimensional Cartesian subplot](axes.md). Traces compatible with these subplots support `xaxis` and `yaxis` attributes whose values must refer to corresponding objects in the layout portion of the figure. For example, if `xaxis="x"`, and `yaxis="y"` (which is the default) then this trace is drawn on the subplot at the intersection of the axes configured under `layout.xaxis` and `layout.yaxis`, but if `xaxis="x2"` and `yaxis="y3"` then the trace is drawn at the intersection of the axes configured under `layout.xaxis2` and `layout.yaxis3`. Note that attributes such as `layout.xaxis` and `layout.xaxis2` etc do not have to be explicitly defined, in which case default values will be inferred. Multiple traces of different types can be drawn on the same subplot.

X- and Y-axes support the `type` attribute, which enables them to represent [continuous values (`type="linear"`, `type="log"`)](axes.md), [temporal values (`type="date"`)](time-series.md) or [categorical values (`type="category"`, `type="multicategory`)](bar-charts.md). Axes can also be overlaid on top of one another to create [dual-axis or multiple-axis charts](multiple-axes.md). 2-d cartesian subplots lend themselves very well to creating ["small multiples" figures, also known as facet or trellis plots](facet-plots.md).

The following trace types are compatible with 2d-cartesian subplots via the `xaxis` and `yaxis` attributes:

* scatter-like trace types: [`scatter`](line-and-scatter.md) and [`scattergl`](webgl-vs-svg.md), which can be used to draw [scatter plots](line-and-scatter.md), [line plots and curves](line-charts.md), [time-series plots](time-series.md), [bubble charts](bubble-charts.md), [dot plots](dot-plots.md) and [filled areas](filled-area-plots.md) and also support [error bars](error-bars.md)
* [`bar`](bar-charts.md), [`funnel`](funnel-charts.md), [`waterfall`](waterfall-charts.md): bar-like trace types which can also be used to draw [timelines and Gantt charts](gantt.md)
* [`histogram`](histograms.md): an *aggregating* bar-like trace type
* [`box`](box-plots.md) and [`violin`](box-plots.md): 1-dimensional distribution-like trace types
* [`histogram2d`](2D-Histogram.md) and [`histogram2dcontour`](2d-histogram-contour.md): 2-dimensional distribution-like density trace types
* [`image`](imshow.md), [`heatmap`](heatmaps.md) and [`contour`](contour-plots.md): matrix trace types
* [`ohlc`](ohlc-charts.md) and [`candlestick`](candlestick-charts.md): stock-like trace types
* [`carpet`](carpet-plot.md): a special trace type for building [carpet plots](carpet-plot.md), in that other traces can use as subplots (see below)
* [`splom`](splom.md): multi-dimensional scatter plots which implicitly refer to many 2-d cartesian subplots at once.

### 3D, Polar, Ternary and Smith Trace Types and Subplots

Beyond 2D cartesian subplots, figures can include [three-dimensional cartesian subplots](3d-charts.md), [polar subplots](polar-chart.md), [ternary subplots](ternary-plots.md) and [smith subplots](smith-charts.md). The following trace types support attributes named `scene`, `polar`, `smith` or `ternary`, whose values must refer to corresponding objects in the layout portion of the figure i.e. `ternary="ternary2"` etc. Note that attributes such as `layout.scene` and `layout.ternary2` etc do not have to be explicitly defined, in which case default values will be inferred. Multiple traces of a compatible type can be placed on the same subplot.

The following trace types are compatible with 3D subplots via the `scene` attribute, which contains special [camera controls](3d-camera-controls.md):

* [`scatter3d`](3d-scatter-plots.md), which can be used to draw [individual markers](3d-scatter-plots.md), [3d bubble charts](3d-bubble-charts.md) and [lines and curves](3d-line-plots.md)
* [`surface`](3d-surface-plots.md) and [`mesh`](3d-mesh.md): 3d surface trace types
* [`cone`](cone-plot.md) and [`streamtube`](streamtube-plot.md): 3d vector field trace types
* [`volume`](3d-volume-plots.md) and [`isosurface`](3d-isosurface-plots.md): 3d volume trace types

The following trace types are compatible with polar subplots via the `polar` attribute:

* scatter-like trace types: [`scatterpolar` and `scatterpolargl`](polar-chart.md), which can be used to draw individual markers, [curves and filled areas (i.e. radar or spider charts)](radar-chart.md)
* [`barpolar`](wind-rose-charts.md): useful for [wind roses](wind-rose-charts.md) and other polar bar charts

The following trace types are compatible with ternary subplots via the `ternary` attribute:

* [`scatterternary`](ternary-plots.md), which can be used to draw individual markers, [curves and filled areas](ternary-contour.md)

The following trace types are compatible with smith subplots via the `smith` attribute:

* [`scattersmith`](smith-charts.md), which can be used to draw individual markers, curves and filled areas

### Map Trace Types and Subplots

Figures can include two different types of map subplots: [geo subplots for outline maps](map-configuration.md) and [tile-based maps](tile-map-layers.md). The following trace types support attributes named `geo` or `map`, whose values must refer to corresponding objects in the layout i.e. `geo="geo2"` etc.  Note that attributes such as `layout.geo2` and `layout.map` etc do not have to be explicitly defined, in which case default values will be inferred. Multiple traces of a compatible type can be placed on the same subplot.

The following trace types are compatible with geo subplots via the `geo` attribute:

* [`scattergeo`](scatter-plots-on-maps.md), which can be used to draw [individual markers](scatter-plots-on-maps.md), [line and curves](lines-on-maps.md) and filled areas on outline maps
* [`choropleth`](choropleth-maps.md): [colored polygons](choropleth-maps.md) on outline maps

The following trace types are compatible with tile map subplots via the `map` attribute:

* [`scattermap`](tile-scatter-maps.md), which can be used to draw [individual markers](tile-scatter-maps.md), [lines and curves](lines-on-tile-maps.md) and [filled areas](filled-area-tile-maps.md) on tile maps
* [`choroplethmap`](tile-county-choropleth.md): colored polygons on tile maps
* [`densitymap`](tile-density-heatmaps.md): density heatmaps on tile maps

### Traces Which Are Their Own Subplots

Certain trace types cannot share subplots, and hence have no attribute to map to a corresponding subplot in the layout. Instead, these traces are their own subplot and support a `domain` attribute for position, which enables the trace to be positioned in paper coordinates (see below). With the exception of `pie` and `funnelarea`, such traces also do not support legends (see below)

The following trace types are their own subplots and support a domain attribute:

* [`pie`](pie-charts.md) and [`funnelarea`](waterfall-charts.md): one-level part-to-whole relationships with legend items
* [`sunburst`](sunburst-charts.md) and [`treemap`](treemaps.md): hierarchical multi-level part-to-whole relationships
* [`parcoords`](parallel-coordinates-plot.md) and [`parcats`](parallel-categories-diagram.md): continuous and categorical multidimensional figures with [parallel coordinates](parallel-coordinates-plot.md) and [parallel sets](parallel-categories-diagram.md)
* [`sankey`](sankey-diagram.md): [flow diagrams](sankey-diagram.md)
* [`table`](table.md): [text-based tables](table.md)
* [`indicator`](indicator.md): big numbers, [gauges](gauge-charts.md), and [bullet charts](bullet-charts.md)

### Carpet Trace Types and Subplots

Certain trace types use [traces of type `carpet` as a subplot](carpet-plot.md). These support a `carpet` attribute whose value must match the value of the `carpet` attribute of the `carpet` trace they are to be drawn on. Multiple compatible traces can be placed on the same `carpet` trace.

The following trace types are compatible with `carpet` trace subplots via the `carpet` attribute:

* [`scattercarpet`](carpet-scatter.md), which can be used to draw individual markers, curves and filled areas
* [`contourcarpet`](carpet-plot.md)

### Trace Types, Legends and Color Bars

Traces of most types can be optionally associated with a single legend item in the [legend](legend.md). Whether or not a given trace appears in the legend is controlled via the `showlegend` attribute. Traces which are their own subplots (see above) do not support this, with the exception of traces of type `pie` and `funnelarea` for which every distinct color represented in the trace gets a separate legend item. Users may show or hide traces by clicking or double-clicking on their associated legend item. Traces that support legend items also support the `legendgroup` attribute, and all traces with the same legend group are treated the same way during click/double-click interactions.

The fact that legend items are linked to traces means that when using [discrete color](discrete-color.md), a figure must have one trace per color in order to get a meaningful legend. [Plotly Express has robust support for discrete color](discrete-color.md) to make this easy.

Traces which support [continuous color](colorscales.md) can also be associated with color axes in the layout via the `coloraxis` attribute. Multiple traces can be linked to the same color axis. Color axes have a legend-like component called color bars. Alternatively, color axes can be configured within the trace itself.

```python

```
