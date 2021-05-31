---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.6.0
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
    version: 3.7.6
  plotly:
    description: Creating and Updating Figures with Plotly's Python graphing library
    display_as: file_settings
    language: python
    layout: base
    name: Creating and Updating Figures
    order: 2
    page_type: example_index
    permalink: python/creating-and-updating-figures/
    redirect_from:
    - python/user-guide/
    - python/user-g/
    thumbnail: thumbnail/creating-and-updating-figures.png
    v4upgrade: true
---

The `plotly` Python package exists to create, manipulate and [render](/python/renderers/) graphical figures (i.e. charts, plots, maps and diagrams) represented by [data structures also referred to as figures](/python/figure-structure/). The rendering process uses the [Plotly.js JavaScript library](https://plotly.com/javascript/) under the hood although Python developers using this module very rarely need to interact with the Javascript library directly, if ever. Figures can be represented in Python either as dicts or as instances of the `plotly.graph_objects.Figure` class, and are serialized as text in [JavaScript Object Notation (JSON)](https://json.org/) before being passed to Plotly.js.

> Note: the recommended entry-point into the plotly package is the [high-level plotly.express module, also known as Plotly Express](/python/plotly-express/), which consists of Python functions which return fully-populated `plotly.graph_objects.Figure` objects. This page exists to document the structure of the data structure that these objects represent for users who wish to understand more about how to customize them, or assemble them from other `plotly.graph_objects` components.

### Figures As Dictionaries

At a low level, figures can be represented as dictionaries and displayed using functions from the `plotly.io` module. The `fig` dictionary in the example below describes a figure. It contains a single `bar` trace and a title.

```python
fig = dict({
    "data": [{"type": "bar",
              "x": [1, 2, 3],
              "y": [1, 3, 2]}],
    "layout": {"title": {"text": "A Figure Specified By Python Dictionary"}}
})

# To display the figure defined by this dict, use the low-level plotly.io.show function
import plotly.io as pio

pio.show(fig)
```

### Figures as Graph Objects

The [`plotly.graph_objects` module provides an automatically-generated hierarchy of classes](https://plotly.com/python-api-reference/plotly.graph_objects.html) called ["graph objects"](/python/graph-objects/) that may be used to represent figures, with a top-level class `plotly.graph_objects.Figure`.

> Note that the *recommended alternative* to working with Python dictionaries is to [create entire figures at once using Plotly Express](/python/plotly-express/) and to manipulate the resulting `plotly.graph_objects.Figure` objects as described in this page, wherever possible, rather than to assemble figures bottom-up from underlying graph objects. See ["When to use Graph Objects"](/python/graph-objects/).

Graph objects have several benefits compared to plain Python dictionaries.

1. Graph objects provide precise data validation. If you provide an invalid property name or an invalid property value as the key to a graph object, an exception will be raised with a helpful error message describing the problem. This is not the case if you use plain Python dictionaries and lists to build your figures.
2. Graph objects contain descriptions of each valid property as Python docstrings, with a [full API reference available](https://plotly.com/python-api-reference/). You can use these docstrings in the development environment of your choice to learn about the available properties as an alternative to consulting the online [Full Reference](/python/reference/index/).
3. Properties of graph objects can be accessed using both dictionary-style key lookup (e.g. `fig["layout"]`) or class-style property access (e.g. `fig.layout`).
4. Graph objects support higher-level convenience functions for making updates to already constructed figures (`.update_layout()`, `.add_trace()` etc) as described below.
5. Graph object constructors and update methods accept "magic underscores" (e.g. `go.Figure(layout_title_text="The Title")` rather than `dict(layout=dict(title=dict(text="The Title")))`) for more compact code, as described below.
6. Graph objects support attached rendering (`.show()`) and exporting functions (`.write_image()`) that automatically invoke the appropriate functions from [the `plotly.io` module](https://plotly.com/python-api-reference/plotly.io.html).


Below you can find an example of one way that the figure in the example above could be specified using a graph object instead of a dictionary.

```python
import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])],
    layout=go.Layout(
        title=go.layout.Title(text="A Figure Specified By A Graph Object")
    )
)

fig.show()
```

You can also create a graph object figure from a dictionary representation by passing the dictionary to the `go.Figure` constructor.

```python
import plotly.graph_objects as go

dict_of_fig = dict({
    "data": [{"type": "bar",
              "x": [1, 2, 3],
              "y": [1, 3, 2]}],
    "layout": {"title": {"text": "A Figure Specified By A Graph Object With A Dictionary"}}
})

fig = go.Figure(dict_of_fig)

fig.show()
```

##### Converting Graph Objects To Dictionaries and JSON

Graph objects can be turned into their Python dictionary representation using the `fig.to_dict()` method. You can also retrieve the JSON string representation of a graph object using the `fig.to_json()` method.

```python
import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])],
    layout=go.Layout(height=600, width=800)
)

fig.layout.template = None # to slim down the output

print("Dictionary Representation of A Graph Object:\n\n" + str(fig.to_dict()))
print("\n\n")
print("JSON Representation of A Graph Object:\n\n" + str(fig.to_json()))
print("\n\n")
```

### Representing Figures in Dash

[Dash](https://plotly.com/dash/) is the best way to build analytical apps in Python using Plotly figures. To run the app below, run `pip install dash`, click "Download" to get the code and run `python app.py`.

Get started  with [the official Dash docs](https://dash.plotly.com/installation) and **learn how to effortlessly [style](https://plotly.com/dash/design-kit/) & [deploy](https://plotly.com/dash/app-manager/) apps like this with <a class="plotly-red" href="https://plotly.com/dash/">Dash Enterprise</a>.**


```python hide_code=true
from IPython.display import IFrame
snippet_url = 'https://dash-gallery.plotly.host/python-docs-dash-snippets/'
IFrame(snippet_url + 'figure-structure', width='100%', height=630)
```

### Creating Figures

This section summarizes several ways to create new graph object figures with the `plotly.py` graphing library.

> The *recommended way* to create figures and populate them is to use [Plotly Express](/python/plotly-express/) but this page documents various other options for completeness


#### Plotly Express

[Plotly Express](https://plot.ly/python/plotly-express/) (included as the `plotly.express` module) is a high-level data visualization API that produces fully-populated graph object figures in single function-calls.

```python
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="A Plotly Express Figure")

# If you print the figure, you'll see that it's just a regular figure with data and layout
# print(fig)

fig.show()
```

#### Graph Objects `Figure` Constructor

As demonstrated above, you can build a complete figure by passing trace and layout specifications to the `plotly.graph_objects.Figure` constructor. These trace and layout specifications can be either dictionaries or graph objects.

In the following example, the traces are specified using graph objects and the layout is specified as a dictionary.

```python
import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])],
    layout=dict(title=dict(text="A Figure Specified By A Graph Object"))
)

fig.show()
```

#### Figure Factories

[Figure factories](/python/figure-factories) (included in `plotly.py` in the `plotly.figure_factory` module) are functions that produce graph object figures, often to satisfy the needs of specialized domains. Here's an example of using the `create_quiver()` figure factory to construct a graph object figure that displays a 2D quiver plot.

```python
import numpy as np
import plotly.figure_factory as ff

x1,y1 = np.meshgrid(np.arange(0, 2, .2), np.arange(0, 2, .2))
u1 = np.cos(x1)*y1
v1 = np.sin(x1)*y1

fig = ff.create_quiver(x1, y1, u1, v1)

fig.show()
```

#### Make Subplots

The `plotly.subplots.make_subplots()` function produces a graph object figure that is preconfigured with a grid of subplots that traces can be added to. The `add_trace()` function will be discussed more below.

```python
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2)

fig.add_trace(go.Scatter(y=[4, 2, 1], mode="lines"), row=1, col=1)
fig.add_trace(go.Bar(y=[2, 1, 3]), row=1, col=2)

fig.show()
```

### Updating Figures

Regardless of how a graph object figure was constructed, it can be updated by adding additional traces to it and modifying its properties.

#### Adding Traces

New traces can be added to a graph object figure using the `add_trace()` method. This method accepts a graph object trace (an instance of `go.Scatter`, `go.Bar`, etc.) and adds it to the figure. This allows you to start with an empty figure, and add traces to it sequentially. The `append_trace()` method does the same thing, although it does not return the figure.

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Bar(x=[1, 2, 3], y=[1, 3, 2]))

fig.show()
```

You can also add traces to a figure produced by a figure factory or Plotly Express.

```python
import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 title="Using The add_trace() method With A Plotly Express Figure")

fig.add_trace(
    go.Scatter(
        x=[2, 4],
        y=[4, 8],
        mode="lines",
        line=go.scatter.Line(color="gray"),
        showlegend=False)
)
fig.show()
```

#### Adding Traces To Subplots

If a figure was created using `plotly.subplots.make_subplots()`, then supplying the `row` and `col` arguments to `add_trace()` can be used to add a trace to a particular subplot.

```python
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2)

fig.add_trace(go.Scatter(y=[4, 2, 1], mode="lines"), row=1, col=1)
fig.add_trace(go.Bar(y=[2, 1, 3]), row=1, col=2)

fig.show()
```

This also works for figures created by Plotly Express using the `facet_row` and or `facet_col` arguments.

```python
import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", facet_col="species",
                 title="Adding Traces To Subplots Witin A Plotly Express Figure")

reference_line = go.Scatter(x=[2, 4],
                            y=[4, 8],
                            mode="lines",
                            line=go.scatter.Line(color="gray"),
                            showlegend=False)

fig.add_trace(reference_line, row=1, col=1)
fig.add_trace(reference_line, row=1, col=2)
fig.add_trace(reference_line, row=1, col=3)

fig.show()
```

#### Add Trace Convenience Methods

As an alternative to the `add_trace()` method, graph object figures have a family of methods of the form `add_{trace}` (where `{trace}` is the name of a trace type) for constructing and adding traces of each trace type.

Here is the previous subplot example, adapted to add the scatter trace using `fig.add_scatter()` and to add the bar trace using `fig.add_bar()`.

```python
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2)

fig.add_scatter(y=[4, 2, 1], mode="lines", row=1, col=1)
fig.add_bar(y=[2, 1, 3], row=1, col=2)

fig.show()
```

#### Magic Underscore Notation

To make it easier to work with nested properties, graph object constructors and many graph object methods support magic underscore notation.

This allows you to reference nested properties by joining together multiple nested property names with underscores.

For example, specifying the figure title in the figure constructor _without_ magic underscore notation requires setting the `layout` argument to `dict(title=dict(text="A Chart"))`.

Similarly, setting the line color of a scatter trace requires setting the `marker` property to `dict(color="crimson")`.

```python
import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Scatter(y=[1, 3, 2], line=dict(color="crimson"))],
    layout=dict(title=dict(text="A Graph Objects Figure Without Magic Underscore Notation"))
)

fig.show()
```

With magic underscore notation, you can accomplish the same thing by passing the figure constructor a keyword argument named `layout_title_text`, and by passing the `go.Scatter` constructor a keyword argument named `line_color`.

```python
import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Scatter(y=[1, 3, 2], line_color="crimson")],
    layout_title_text="A Graph Objects Figure With Magic Underscore Notation"
)

fig.show()
```

Magic underscore notation is supported throughout the graph objects API, and it can often significantly simplify operations involving deeply nested properties.

> Note: When you see keyword arguments with underscores passed to a graph object constructor or method, it is almost always safe to assume that it is an application of magic underscore notation. We have to say "almost always" rather than "always" because there are a few property names in the plotly schema that contain underscores: error_x, error_y, error_z, copy_xstyle, copy_ystyle, copy_zstyle, paper_bgcolor, and plot_bgcolor. These were added back in the early days of the library (2012-2013) before we standardized on banning underscores from property names.

#### Updating Figure Layouts

Graph object figures support an `update_layout()` method that may be used to update multiple nested properties of a figure's layout.

Here is an example of updating the text and font size of a figure's title using `update_layout()`.

```python
import plotly.graph_objects as go

fig = go.Figure(data=go.Bar(x=[1, 2, 3], y=[1, 3, 2]))

fig.update_layout(title_text="Using update_layout() With Graph Object Figures",
                  title_font_size=30)

fig.show()
```

Note that the following `update_layout()` operations are equivalent:

```python
fig.update_layout(title_text="update_layout() Syntax Example",
                  title_font_size=30)

fig.update_layout(title_text="update_layout() Syntax Example",
                  title_font=dict(size=30))


fig.update_layout(title=dict(text="update_layout() Syntax Example"),
                             font=dict(size=30))

fig.update_layout({"title": {"text": "update_layout() Syntax Example",
                             "font": {"size": 30}}})

fig.update_layout(title=go.layout.Title(text="update_layout() Syntax Example",
                                        font=go.layout.title.Font(size=30)))
```

#### Updating Traces

Graph object figures support an `update_traces()` method that may be used to update multiple nested properties of one or more of a figure's traces.

To show some examples, we will start with a figure that contains `bar` and `scatter` traces across two subplots.

```python
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2)

fig.add_scatter(y=[4, 2, 3.5], mode="markers",
                marker=dict(size=20, color="LightSeaGreen"),
                name="a", row=1, col=1)

fig.add_bar(y=[2, 1, 3],
            marker=dict(color="MediumPurple"),
            name="b", row=1, col=1)

fig.add_scatter(y=[2, 3.5, 4], mode="markers",
                marker=dict(size=20, color="MediumPurple"),
                name="c", row=1, col=2)

fig.add_bar(y=[1, 3, 2],
            marker=dict(color="LightSeaGreen"),
            name="d", row=1, col=2)

fig.show()
```

Note that both `scatter` and `bar` traces have a `marker.color` property to control their coloring. Here is an example of using `update_traces()` to modify the color of all traces.

```python
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2)

fig.add_scatter(y=[4, 2, 3.5], mode="markers",
                marker=dict(size=20, color="LightSeaGreen"),
                name="a", row=1, col=1)

fig.add_bar(y=[2, 1, 3],
            marker=dict(color="MediumPurple"),
            name="b", row=1, col=1)

fig.add_scatter(y=[2, 3.5, 4], mode="markers",
                marker=dict(size=20, color="MediumPurple"),
                name="c", row=1, col=2)

fig.add_bar(y=[1, 3, 2],
            marker=dict(color="LightSeaGreen"),
            name="d", row=1, col=2)

fig.update_traces(marker=dict(color="RoyalBlue"))

fig.show()
```

The `update_traces()` method supports a `selector` argument to control which traces should be updated. Only traces with properties that match the selector will be updated. Here is an example of using a selector to only update the color of the `bar` traces.

```python
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2)

fig.add_scatter(y=[4, 2, 3.5], mode="markers",
                marker=dict(size=20, color="LightSeaGreen"),
                name="a", row=1, col=1)

fig.add_bar(y=[2, 1, 3],
            marker=dict(color="MediumPurple"),
            name="b", row=1, col=1)

fig.add_scatter(y=[2, 3.5, 4], mode="markers",
                marker=dict(size=20, color="MediumPurple"),
                name="c", row=1, col=2)

fig.add_bar(y=[1, 3, 2],
            marker=dict(color="LightSeaGreen"),
            name="d", row=1, col=2)

fig.update_traces(marker=dict(color="RoyalBlue"),
                  selector=dict(type="bar"))

fig.show()
```

Magic underscore notation can be used in the selector to match nested properties. Here is an example of updating the color of all traces that were formally colored `"MediumPurple"`.

```python
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2)

fig.add_scatter(y=[4, 2, 3.5], mode="markers",
                marker=dict(size=20, color="LightSeaGreen"),
                name="a", row=1, col=1)

fig.add_bar(y=[2, 1, 3],
            marker=dict(color="MediumPurple"),
            name="b", row=1, col=1)

fig.add_scatter(y=[2, 3.5, 4], mode="markers",
                marker=dict(size=20, color="MediumPurple"),
                name="c", row=1, col=2)

fig.add_bar(y=[1, 3, 2],
            marker=dict(color="LightSeaGreen"),
            name="d", row=1, col=2)

fig.update_traces(marker_color="RoyalBlue",
                  selector=dict(marker_color="MediumPurple"))

fig.show()
```

For figures with subplots, the `update_traces()` method also supports `row` and `col` arguments to control which traces should be updated. Only traces in the specified subplot row and column will be updated. Here is an example of updating the color of all traces in the second subplot column.

```python
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2)

fig.add_scatter(y=[4, 2, 3.5], mode="markers",
                marker=dict(size=20, color="LightSeaGreen"),
                name="a", row=1, col=1)

fig.add_bar(y=[2, 1, 3],
            marker=dict(color="MediumPurple"),
            name="b", row=1, col=1)

fig.add_scatter(y=[2, 3.5, 4], mode="markers",
                marker=dict(size=20, color="MediumPurple"),
                name="c", row=1, col=2)

fig.add_bar(y=[1, 3, 2],
            marker=dict(color="LightSeaGreen"),
            name="d", row=1, col=2)

fig.update_traces(marker=dict(color="RoyalBlue"),
                  col=2)

fig.show()
```

The `update_traces()` method can also be used on figures produced by figure factories or Plotly Express. Here's an example of updating the regression lines produced by Plotly Express to be dotted.

```python
import pandas as pd
import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 facet_col="species", trendline="ols", title="Using update_traces() With Plotly Express Figures")

fig.update_traces(
    line=dict(dash="dot", width=4),
    selector=dict(type="scatter", mode="lines"))

fig.show()
```

### Overwrite Existing Properties When Using Update Methods

`update_layout()` and `update_traces()` have an `overwrite` keyword argument, defaulting to False, in which case updates are applied recursively to the _existing_ nested property structure. When set to True, the prior value of existing properties is overwritten with the provided value.

In the example below, the red color of markers is overwritten when updating `marker` in `update_traces()` with `overwrite=True`. Note that setting instead `marker_opacity` with the magic underscore would not overwrite `marker_color` because properties would be overwritten starting only at the level of `marker.opacity`.

```python
import plotly.graph_objects as go

fig = go.Figure(go.Bar(x=[1, 2, 3], y=[6, 4, 9],
                       marker_color="red")) # will be overwritten below

fig.update_traces(overwrite=True, marker={"opacity": 0.4})

fig.show()
```

#### Conditionally Updating Traces

Suppose the updates that you want to make to a collection of traces depend on the current values of certain trace properties. The `update_traces()` method cannot handle this situation, but the `for_each_trace()` method can!

As its first argument, the `for_each_trace()` method accepts a function that accepts and updates one trace at a time. Like `update_traces()`, `for_each_trace()` also accepts `selector`, `row`, and `col` arguments to control which traces should be considered.

Here is an example of using `for_each_trace()` to convert the only markers for the `"setosa"` to square symbols in a Plotly Express Figure.

**Note that this is possible because Plotly Express figures are made up of a separate trace for each column in the input data frame**

```python
import pandas as pd
import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 title="Conditionally Updating Traces In A Plotly Express Figure With for_each_trace()")

fig.for_each_trace(
    lambda trace: trace.update(marker_symbol="square") if trace.name == "setosa" else (),
)

fig.show()
```

#### Updating Figure Axes

Graph object figures support `update_xaxes()` and `update_yaxes()` methods that may be used to update multiple nested properties of one or more of a figure's axes. Here is an example of using `update_xaxes()` to disable the vertical grid lines across all subplots in a figure produced by Plotly Express.

```python
import pandas as pd
import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 facet_col="species", title="Using update_xaxes() With A Plotly Express Figure")

fig.update_xaxes(showgrid=False)

fig.show()
```

There are also `for_each_xaxis()` and `for_each_yaxis()` methods that are analogous to the `for_each_trace()` method described above. For non-cartesian subplot types (e.g. polar), there are additional `update_{type}` and `for_each_{type}` methods (e.g. `update_polar()`, `for_each_polar()`).

### Other Update Methods

Figures created with the plotly.py graphing library also support:

  - the `update_layout_images()` method in order to [update background layout images](/python/images/),
  - `update_annotations()` in order to [update annotations](/python/text-and-annotations/#multiple-annotations),
  - and `update_shapes()` in order to [update shapes](/python/shapes/).

#### Chaining Figure Operations

All of the figure update operations described above are methods that return a reference to the figure being modified. This makes it possible the chain multiple figure modification operations together into a single expression.

Here is an example of a chained expression that creates:

  - a faceted scatter plot with OLS trend lines using Plotly Express,
  - sets the title font size using `update_layout()`,
  - disables vertical grid lines using `update_xaxes()`,
  - updates the width and dash pattern of the trend lines using `update_traces()`,
  - and then displays the figure using `show()`.

```python
import plotly.express as px

df = px.data.iris()

(px.scatter(df, x="sepal_width", y="sepal_length", color="species",
            facet_col="species", trendline="ols",
            title="Chaining Multiple Figure Operations With A Plotly Express Figure")
 .update_layout(title_font_size=24)
 .update_xaxes(showgrid=False)
 .update_traces(
     line=dict(dash="dot", width=4),
     selector=dict(type="scatter", mode="lines"))
).show()
```

#### Property Assignment

Trace and layout properties can be updated using property assignment syntax. Here is an example of setting the figure title using property assignment.

```python
import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(x=[1, 2, 3], y=[1, 3, 2]))
fig.layout.title.text = "Using Property Assignment Syntax With A Graph Object Figure"
fig.show()
```

And here is an example of updating the bar outline using property assignment.

```python
import plotly.graph_objects as go

fig = go.Figure(data=go.Bar(x=[1, 2, 3], y=[1, 3, 2]))

fig.data[0].marker.line.width = 4
fig.data[0].marker.line.color = "black"

fig.show()
```
