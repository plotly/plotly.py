---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: "1.1"
      jupytext_version: 1.1.1
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
    version: 3.7.3
  plotly:
    description: Creating and Updating Figures from Python
    display_as: file_settings
    language: python
    layout: base
    name: Creating and Updating Figures
    page_type: example_index
    permalink: python/creating-and-updating-figures/
    redirect_from:
      - python/user-guide/
      - python/user-g/
    thumbnail: thumbnail/creating-and-updating-figures.png
    v4upgrade: true
    order: 2
---

### Representing Figures

#### Figures as dictionaries

The goal of plotly.py is to provide a pleasant Python interface for creating figure specifications for display in the Plotly.js JavaScript library. In Plotly.js, a figure is specified by a declarative JSON data structure, and so the ultimate responsibility of plotly.py is to produce Python dictionaries that can be serialized into a JSON data structure that represents a valid figure.

As a concrete example, here is a Python dictionary that represents a figure containing a single bar trace and a title.

```python
fig = {
    "data": [{"type": "bar",
              "x": [1, 2, 3],
              "y": [1, 3, 2]}],
    "layout": {"title": {"text": "A Bar Chart"}}
}

# To display the figure defined by this dict, use the low-level plotly.io.show function
import plotly.io as pio
pio.show(fig)
```

The value of the top-level `"data"` key is a list of trace specifications. Each trace specification has a special `"type"` key that indicates the trace type that is being defined (e.g. a `"bar"`, `"scatter"`, `"contour"`, etc.). The rest of the keys in the trace specification are used to configure the properties of the trace of this type.

The value of the top-level `"layout"` key is a dictionary that specifies the properties of the figure's layout. In contrast to trace configuration options that apply to individual traces, the layout configuration options apply to the figure as a whole, customizing items like the axes, annotations, shapes, legend, and more.

The [_Full Reference_](https://plot.ly/python/reference/) page contains descriptions of all of the supported trace and layout options.

If working from the _Full Reference_ to build figures as Python dictionaries and lists suites your needs, go for it! This is a perfectly valid way to use plotly.py to build figures. On the other hand, if you would like an API that offers a bit more assistance, read on to learn about graph objects.

#### Figures as graph objects

As an alternative to working with Python dictionaries, plotly.py provides a hierarchy of classes called "graph objects" that may be used to construct figures. Graph objects have several benefits compared to plain dictionaries.

1.  Graph objects provide precise data validation. So if you provide an invalid property name or an invalid property value, an exception will be raised with a helpful error message describing the problem.
2.  Graph objects contain descriptions of each property as Python docstrings. You can use these docstrings to learn about the available properties as an alternative to consulting the _Full Reference_.
3.  Properties of graph objects can be accessed using dictionary-style key lookup (e.g. `fig["layout"]`) or class-style property access (e.g. `fig.layout`).
4.  Graph objects support higher-level convenience functions for making updates to already constructed figures, as described below.

Graph objects are stored in a hierarchy of modules under the `plotly.graph_objects` package. Here is an example of one way that the figure above could be constructed using graph objects.

```python
import plotly.graph_objects as go
fig = go.Figure(
    data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])],
    layout=go.Layout(
        title=go.layout.Title(text="A Bar Chart")
    )
)
fig.show()
```

You can also create a graph object figure from a dictionary representation by passing the dictionary to the figure constructor.

```python
import plotly.graph_objects as go
fig = go.Figure({
    "data": [{"type": "bar",
              "x": [1, 2, 3],
              "y": [1, 3, 2]}],
    "layout": {"title": {"text": "A Bar Chart"}}
})
fig.show()
```

Once you have a figure as a graph object, you can retrieve the dictionary representation using the `fig.to_dict()` method. You can also retrieve the JSON string representation using the `fig.to_json()` method.

### Creating figures

This section summarizes several ways to create new graph object figures with plotly.py

#### Constructor

As demonstrated above, you can build a complete figure by passing trace and layout specifications to the `plotly.graph_objects.Figure` constructor. These trace and layout specifications can be either dictionaries or graph objects. Here, for example, the traces are specified using graph objects and the layout is specified as a dictionary.

```python
import plotly.graph_objects as go
fig = go.Figure(
    data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])],
    layout=dict(title=dict(text="A Bar Chart"))
)
fig.show()
```

#### Plotly express

Plotly express (included as the `plotly.express` module) is a high-level data exploration API that produces graph object figures.

```python
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

# If you print fig, you'll see that it's just a regular figure with data and layout
# print(fig)

fig.show()
```

#### Figure factories

Figure factories (included in plotly.py in the `plotly.figure_factory` module) are functions that produce graph object figures, often to satisfy the needs of specialized domains. Here's an example of using the `create_quiver` figure factory to construct a graph object figure that displays a 2D quiver plot.

```python
import numpy as np
import plotly.figure_factory as ff
x1,y1 = np.meshgrid(np.arange(0, 2, .2), np.arange(0, 2, .2))
u1 = np.cos(x1)*y1
v1 = np.sin(x1)*y1

fig = ff.create_quiver(x1, y1, u1, v1)
fig.show()
```

#### Make subplots

The `plotly.subplots.make_subplots` function produces a graph object figure that is preconfigured with a grid of subplots that traces can be added to. The `add_trace` function will be discussed more below.

```python
from plotly.subplots import make_subplots
fig = make_subplots(rows=1, cols=2)
fig.add_trace(go.Scatter(y=[4, 2, 1], mode="lines"), row=1, col=1)
fig.add_trace(go.Bar(y=[2, 1, 3]), row=1, col=2)
fig.show()
```

### Updating figures

Regardless of how a graph object figure was constructed, it can be updated by adding additional traces and modifying its properties.

#### Adding traces

New traces can be added to a graph object figure using the `add_trace` method. This method accepts a graph object trace (an instance of `go.Scatter`, `go.Bar`, etc.) and adds it to the figure. This allows you to start with an empty figure, and add traces to it sequentially.

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
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
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

#### Adding traces to subplots

If a figure was created using `plotly.subplots.make_subplots`, then the `row` and `col` argument to `add_trace` can be used to add a trace to a particular subplot.

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
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", facet_col="species")
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

#### Add trace convenience methods

As an alternative to the `add_trace` method, graph object figures have a family of methods of the form `add_{trace}`, where `{trace}` is the name of a trace type, for constructing and adding traces of each trace type. Here is the previous subplot example, adapted to add the scatter trace using `fig.add_scatter` and to add the bar trace using `fig.add_bar`.

```python
from plotly.subplots import make_subplots
fig = make_subplots(rows=1, cols=2)
fig.add_scatter(y=[4, 2, 1], mode="lines", row=1, col=1)
fig.add_bar(y=[2, 1, 3], row=1, col=2)
fig.show()
```

#### Magic underscore notation

To make it easier to work with nested properties graph object constructors, and many graph object methods, support magic underscore notation. This allows you to reference nested properties by joining together multiple nested property names with underscores.

For example, specifying the figure title in the figure constructor _without_ magic underscore notation requires setting the `layout` argument to `dict(title=dict(text="A Chart"))`. Similarly, setting the line color of a scatter trace requires setting the `marker` property to `dict(color="crimson")`.

```python
import plotly.graph_objects as go
fig = go.Figure(
    data=[go.Scatter(y=[1, 3, 2], line=dict(color="crimson"))],
    layout=dict(title=dict(text="A Chart"))
)
fig.show()
```

With magic underscore notation, you can accomplish the same thing by passing the figure constructor a keyword argument named `layout_title_text`, and by passing the `go.Scatter` constructor a keyword argument named `line_color`.

```python
import plotly.graph_objects as go
fig = go.Figure(
    data=[go.Scatter(y=[1, 3, 2], line_color="crimson")],
    layout_title_text="A Chart"
)
fig.show()
```

Magic underscore notation is supported throughout the graph objects API, and it can often significantly simplify operations involving deeply nested properties.

> Note: When you see keyword arguments with underscores passed to a graph object constructor or method, it is almost always safe to assume that it is an application of magic underscore notation. We have to say "almost always" rather than "always" because there are a few property names in the plotly schema that contain underscores: error_x, error_y, error_z, copy_xstyle, copy_ystyle, copy_zstyle, paper_bgcolor, and plot_bgcolor. These were added back in the early days of the library (2012-2013) before we standardized on banning underscores from property names.

#### The update layout method

Graph object figures support an `update_layout` method that may be used to update multiple nested properties of a figure's layout. Here is an example of updating the text and font size of a figure's title using `update_layout`.

```python
import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(x=[1, 2, 3], y=[1, 3, 2]))
fig.update_layout(title_text="A Bar Chart",
                  title_font_size=30)
fig.show()
```

Note that the following `update_layout` operations are equivalent:

```python
fig.update_layout(title_text="A Bar Chart",
                  title_font_size=30)

fig.update_layout(title_text="A Bar Chart",
                  title_font=dict(size=30))


fig.update_layout(title=dict(text="A Bar Chart"),
                             font=dict(size=30))

fig.update_layout({"title": {"text": "A Bar Chart",
                             "font": {"size": 30}}})

fig.update_layout(
    title=go.layout.Title(text="A Bar Chart",
                          font=go.layout.title.Font(size=30)));
```

#### The update traces method

Graph object figures support an `update_traces` method that may be used to update multiple nested properties of one or more of a figure's traces. To show some examples, we will start with a figure that contains bar and scatter traces across two subplots.

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

Note that both `scatter` and `bar` traces have a `marker.color` property to control their coloring. Here is an example of using `update_traces` to modify the color of all traces.

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

The `update_traces` method supports a `selector` argument to control which traces should be updated. Only traces with properties that match the selector will be updated. Here is an example of using a selector to only update the color of the `bar` traces

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

For figures with subplots, the `update_traces` method also supports `row` and `col` arguments to control which traces should be updated. Only traces in the specified subplot row and column will be updated. Here is an example of updating the color of all traces in the second subplot column

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

The `update_traces` method can also be used on figures produced by figure factories or Plotly Express. Here's an example of updating the regression lines produced by Plotly Express to be dotted.

```python
import pandas as pd
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", facet_col="species", trendline="ols")
fig.update_traces(
    line=dict(dash="dot", width=4),
    selector=dict(type="scatter", mode="lines"))
fig.show()
```

### Overwrite existing properties when using update methods

`update_layout` and `update_traces` have an `overwrite` keyword argument, defaulting to False, in which case updates are applied recursively to the _existing_ nested property structure. When set to True, the prior value of existing properties is overwritten with the provided value.

In the example below, the red color of markers is overwritten when updating `marker` in `update_traces` with `overwrite=True`. Note that setting instead `marker_opacity` with the magic underscore would not overwrite `marker_color` because properties would be overwritten starting only at the level of `marker.opacity`.

```python
import plotly.graph_objects as go
fig = go.Figure(go.Bar(x=[1, 2, 3], y=[6, 4, 9],
                       marker_color="red")) # will be overwritten below
fig.update_traces(
    overwrite=True,
    marker={"opacity": 0.4}
                 )
fig.show()
```

#### The for each trace method

Suppose the updates that you want to make to a collection of traces depend on the current values of certain trace properties. The `update_traces` method cannot handle this situation, but the `for_each_trace` method can.

As its first argument, the `for_each_trace` method accepts a function that accepts and updates one trace at a time. Like `update_traces`, `for_each_trace` also accepts `selector`, `row`, and `col` arguments to control which traces should be considered.

Here is an example of using `for_each_trace` to replace the equal-sign with a colon in the legend name of each trace in a figure produced by Plotly Express.

```python
import pandas as pd
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

fig.for_each_trace(
    lambda trace: trace.update(name=trace.name.replace("=", ": ")),
)

fig.show()
```

#### The update axis methods

Graph object figures support `update_xaxes` and `update_yaxes` methods that may be used to update multiple nested properties of one or more of a figure's axes. Here is an example of using `update_xaxes` to disable the vertical grid lines across all subplots in a figure produced by Plotly Express.

```python
import pandas as pd
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", facet_col="species")
fig.update_xaxes(showgrid=False)
fig.show()
```

There are also `for_each_xaxis` and `for_each_yaxis` methods that are analogous to the `for_each_trace` method described above. For non-cartesian subplot types (e.g. polar), there are additional `update_{type}` and `for_each_{type}` methods (e.g. `update_polar`, `for_each_polar`).

### Other update methods

`go` figures also support `update_layout_images` in order to [update background layout images](/python/images/), `update_annotations` in order to [update annotations](/python/text-and-annotations/#multiple-annotations), and `update-shapes` in order to [update shapes](/python/shapes/).

#### Chaining figure operations

All of the figure update operations described above are methods that return a reference to the figure being modified. This makes it possible the chain multiple figure modification operations together into a single expression.

Here is an example of a chained expression that creates a faceted scatter plot with OLS trend lines using Plotly Express, sets the title font size using `update_layout`, disables vertical grid lines using `update_xaxes`, updates the width and dash pattern of the trend lines using `update_traces`, and then displays the figure using `show`.

```python
import plotly.express as px
df = px.data.iris()
(px.scatter(df, x="sepal_width", y="sepal_length", color="species",
            facet_col="species", trendline="ols", title="Iris Dataset")
 .update_layout(title_font_size=24)
 .update_xaxes(showgrid=False)
 .update_traces(
     line=dict(dash="dot", width=4),
     selector=dict(type="scatter", mode="lines"))
).show()
```

#### Property assignment

Trace and layout properties can be updated using property assignment syntax. Here is an example of setting the figure title using property assignment.

```python
import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(x=[1, 2, 3], y=[1, 3, 2]))
fig.layout.title.text = "A Bar Chart"
fig.show()
```

And here is an example of updating the bar outline using property assignment

```python
import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(x=[1, 2, 3], y=[1, 3, 2]))
fig.data[0].marker.line.width = 4
fig.data[0].marker.line.color = "black"
fig.show()
```
