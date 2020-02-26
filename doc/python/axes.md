---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: "1.2"
      jupytext_version: 1.3.0
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
    description:
      How to adjust axes properties in python. Includes examples of linear
      and logarithmic axes, axes titles, styling and coloring axes and grid lines,
      and more.
    display_as: file_settings
    language: python
    layout: base
    name: Axes
    order: 13
    permalink: python/axes/
    thumbnail: thumbnail/axes.png
---

This tutorial explain how to set the properties of 2-dimensional Cartesian axes, namely [`go.layout.XAxis`](/python/reference/#layout-xaxis) and [`go.layout.YAxis`](python/reference/#layout-xaxis). Other kinds of axes are described in other tutorials:

- [3D axes](/python/3d-axes) The axis object is [`go.layout.Scene`](/python/reference/#layout-scene)
- [Polar axes](/python/polar-chart/). The axis object is [`go.layout.Polar`](/python/reference/#layout-polar)
- [Ternary axes](/python/ternary-plots). The axis object is [`go.layout.Ternary`](/python/reference/#layout-ternary)
- [Geo axes](/python/map-configuration/). The axis object is [`go.layout.Geo`](/python/reference/#layout-geo)
- [Mapbox axes](/python/mapbox-layers/). The axis object is [`go.layout.Mapbox`](/python/reference/#layout-mapbox)
- [Color axes](/python/colorscales/). The axis object is [`go.layout.Coloraxis`](/python/reference/#layout-coloraxis).

**See also** the tutorials on [subplots](/python/subplots) and [multiple axes](/python/multiple-axes/).

The different types of Cartesian axes are

- 'linear'
- 'log' (see the [example below](#logarithmic-axes))
- 'date' (see the [tutorial on timeseries](/python/time-series/))
- 'category' (see for example [Bar Charts](/python/bar-charts/))
- 'multicategory' (see the [example below](<#subcategory-(multicategory)-axes>))

#### Logarithmic Axes

The `type` axis property can be set to `'log'` to arrange axis ticks in log-scale.

Here is an example of updating the x and y axes of a figure to be in log scale.

```python
import plotly.express as px
import numpy as np

x = np.arange(10)

fig = px.scatter(x=x, y=x**3,
                log_x=True, log_y=True)

fig.show()
```

```python
import plotly.graph_objects as go

fig = go.Figure(data=[
    go.Scatter(
        x=[1, 10, 20, 30, 40, 50, 60, 70, 80],
        y=[80, 70, 60, 50, 40, 30, 20, 10, 1]
    ),
    go.Scatter(
        x=[1, 10, 20, 30, 40, 50, 60, 70, 80],
        y=[1, 10, 20, 30, 40, 50, 60, 70, 80]
    )
])

fig.update_xaxes(type="log")
fig.update_yaxes(type="log")

fig.show()
```

### Forcing an axis to be categorical

If you pass string values for the `x` or `y` parameter, plotly will automatically set the corresponding axis type to `category`, with the exception of string of numbers, in which case the axis is linear. It is however possible to force the axis type by setting explicitely `xaxis_type` to be `category`.

```python
import plotly.express as px
fig = px.bar(x=[1, 2, 4, 10], y =[8, 6, 11, 5])
fig.update_layout(xaxis_type='category',
                  title_text='Bar chart with categorical axes')
fig.show()
```

#### Subcategory (Multicategory) Axes

A two-level categorical axis can be created by specifying a trace's `x` or `y` property as a 2-dimensional lists. The first sublist represents the outer categorical value while the second sublist represents the inner categorical value.

Here is an example that creates a figure with 4 horizontal `box` traces with a 2-level categorical y-axis.

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Box(
  x = [2, 3, 1, 5],
  y = [['First', 'First', 'First', 'First'],
       ["A", "A", "A", "A"]],
  name = "A",
  orientation = "h"
))

fig.add_trace(go.Box(
  x = [8, 3, 6, 5],
  y = [['First', 'First', 'First', 'First'],
       ["B", "B", "B", "B"]],
  name = "B",
  orientation = "h"
))

fig.add_trace(go.Box(
  x = [2, 3, 2, 5],
  y = [['Second', 'Second', 'Second', 'Second'],
       ["C", "C", "C", "C"]],
  name = "C",
  orientation = "h"
))

fig.add_trace(go.Box(
  x = [7.5, 3, 6, 4],
  y = [['Second', 'Second', 'Second', 'Second'],
       ["D", "D", "D", "D"]],
  name = "D",
  orientation = "h"
))

fig.update_layout(title_text="Multi-category axis",)

fig.show()
```

#### Toggling Axes Lines, Ticks, Labels, and Autorange

The different groups of Cartesian axes properties are

- tick values (locations of tick marks) and tick labels. Tick labels are placed at tick values.
- lines: grid lines (passing through tick values), axis lines, zero lines
- title of the axis
- range of the axis
- domain of the axis

#### Tick Placement, Color, and Style

##### Toggling axis tick marks

Axis tick marks are disabled by default for the default `plotly` theme, but they can easily be turned on by setting the `ticks` axis property to `"inside"` (to place ticks inside plotting area) or `"outside"` (to place ticks outside the plotting area).

Here is an example of turning on inside x-axis and y-axis ticks in a faceted figure created using Plotly Express. Note how the `col` argument to `update_yaxes` is used to only turn on the y-axis ticks for the left-most subplot.

```python
import plotly.express as px
df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", facet_col="species")
fig.update_xaxes(ticks="inside")
fig.update_yaxes(ticks="inside", col=1)

fig.show()
```

##### Set number of tick marks (and grid lines)

The approximate number of ticks displayed for an axis can be specified using the `nticks` axis property.

Here is an example of updating the y-axes of a figure created using Plotly Express to display approximately 20 ticks.

```python
import plotly.express as px
df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", facet_col="species")
fig.update_yaxes(nticks=20)

fig.show()
```

##### Set start position and distance between ticks

The `tick0` and `dtick` axis properties can be used to control to placement of axis ticks as follows: If specified, a tick will fall exactly on the location of `tick0` and additional ticks will be added in both directions at intervals of `dtick`.

Here is an example of updating the y axis of a figure created using Plotly Express to position the ticks at intervals of 0.5, starting at 0.25.

```python
import plotly.express as px
df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", facet_col="species")
fig.update_yaxes(tick0=0.25, dtick=0.5)

fig.show()
```

##### Set exact location of axis ticks

It is possible to configure an axis to display ticks at a set of predefined locations by setting the `tickvals` property to an array of positions.

Here is an example of setting the exact location of ticks on the y axes of a figure created using Plotly Express.

```python
import plotly.express as px
df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", facet_col="species")
fig.update_yaxes(tickvals=[5.1, 5.9, 6.3, 7.5])

fig.show()
```

##### Style tick marks

As discussed above, tick marks are disabled by default in the default `plotly` theme, but they can be enabled by setting the `ticks` axis property to `"inside"` (to place ticks inside plotting area) or `"outside"` (to place ticks outside the plotting area).

The appearance of these tick marks can be customized by setting their length (`ticklen`), width (`tickwidth`), and color (`tickcolor`).

Here is an example of enabling and styling the tick marks of a faceted figure created using Plotly Express. Note how the `col` argument to `update_yaxes` is used to only turn on and style the y-axis ticks for the left-most subplot.

```python
import plotly.express as px
df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", facet_col="species")
fig.update_xaxes(ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10)
fig.update_yaxes(ticks="outside", tickwidth=2, tickcolor='crimson', ticklen=10, col=1)

fig.show()
```

##### Toggling axis labels

The axis tick mark labels can be disabled by setting the `showticklabels` axis property to `False`.

Here is an example of disabling tick labels in all subplots for a faceted figure created using Plotly Express.

```python
import plotly.express as px
df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", facet_col="species")
fig.update_xaxes(showticklabels=False)
fig.update_yaxes(showticklabels=False)

fig.show()
```

##### Set axis label rotation and font

The orientation of the axis tick mark labels is configured using the `tickangle` axis property. The value of `tickangle` is the angle of rotation, in the clockwise direction, of the labels from vertical in units of degrees. The font family, size, and color for the tick labels are stored under the `tickfont` axis property.

Here is an example of rotating the x-axis tick labels by 45 degrees, and customizing their font properties, in a faceted histogram figure created using Plotly Express.

```python
import plotly.express as px
df = px.data.tips()

fig = px.histogram(df, x="sex", y="tip", histfunc='sum', facet_col='smoker')
fig.update_xaxes(tickangle=45, tickfont=dict(family='Rockwell', color='crimson', size=14))

fig.show()
```

#### Enumerated Ticks with Tickvals and Ticktext

The `tickvals` and `ticktext` axis properties can be used together to display custom tick label text at custom locations along an axis. They should be set to lists of the same length where the `tickvals` list contains positions along the axis, and `ticktext` contains the strings that should be displayed at the corresponding positions.

Here is an example.

```python
import plotly.graph_objects as go
import pandas as pd

# Load and filter Apple stock data for 2016
apple_df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv",
    parse_dates=["Date"],
    index_col="Date"
)

apple_df_2016 = apple_df["2016"]

# Create figure and add line
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=apple_df_2016.index,
    y=apple_df_2016["AAPL.High"],
    mode="lines"
))

# Set custom x-axis labels
fig.update_xaxes(
    ticktext=["End of Q1", "End of Q2", "End of Q3", "End of Q4"],
    tickvals=["2016-04-01", "2016-07-01", "2016-10-01", apple_df_2016.index.max()],
)

# Prefix y-axis tick labels with dollar sign
fig.update_yaxes(tickprefix="$")

# Set figure title
fig.update_layout(title_text="Apple Stock Price")

fig.show()
```

### Axis lines: grid and zerolines

##### Toggling Axis grid lines

Axis grid lines can be disabled by setting the `showgrid` property to `False` for the x and/or y axis.

Here is an example of setting `showgrid` to `False` in the graph object figure constructor.

```python
import plotly.express as px

fig = px.line(y=[1, 0])
fig.update_layout(xaxis_showgrid=False, yaxis_showgrid=False)
fig.show()
```

##### Toggling Axis zero lines

The lines passing through zero can be disabled as well by setting the `zeroline` axis property to `False`

```python
import plotly.express as px

fig = px.line(y=[1, 0])

fig.update_layout(
    xaxis=dict(showgrid=False, zeroline=False),
    yaxis=dict(showgrid=False, zeroline=False),
)
fig.show()
```

##### Toggle grid and zerolines with update axis methods

Axis properties can be also updated for figures after they are constructed using the `update_xaxes` and `update_yaxes` graph object figure methods.

Here is an example that disables the x and y axis grid and zero lines using `update_xaxes` and `update_yaxes`.

```python
import plotly.express as px

fig = px.line(y=[1, 0])
fig.update_xaxes(showgrid=False, zeroline=False)
fig.update_yaxes(showgrid=False, zeroline=False)

fig.show()
```

##### Toggle grid and zerolines for figure created with Plotly Express

An advantage of using the `update_xaxis` and `update_yaxis` methods is that these updates will (by default) apply to all axes in the figure. This is especially useful when customizing figures created using Plotly Express, figure factories, or `make_subplots`.

Here is an example of disabling all grid and zero lines in a faceted figure created by Plotly Express.

```python
import plotly.express as px
df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", facet_col="species")
fig.update_xaxes(showgrid=False, zeroline=False)
fig.update_yaxes(showgrid=False, zeroline=False)

fig.show()
```

#### Styling and Coloring Axes and the Zero-Line

##### Styling axis lines

The `showline` axis property controls the visibility of the axis line, and the `linecolor` and `linewidth` axis properties control the color and width of the axis line.

Here is an example of enabling the x and y axis lines, and customizing their width and color, for a faceted histogram created with Plotly Express.

```python
import plotly.express as px
df = px.data.tips()

fig = px.histogram(df, x="sex", y="tip", histfunc='sum', facet_col='smoker')
fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
fig.update_yaxes(showline=True, linewidth=2, linecolor='black')

fig.show()
```

##### Mirroring axis lines

Axis lines can be mirrored to the opposite side of the plotting area by setting the `mirror` axis property to `True`.

Here is an example of mirroring the x and y axis lines in a faceted histogram created using Plotly Express.

```python
import plotly.express as px
df = px.data.tips()

fig = px.histogram(df, x="sex", y="tip", histfunc='sum', facet_col='smoker')
fig.update_xaxes(showline=True, linewidth=2, linecolor='black', mirror=True)
fig.update_yaxes(showline=True, linewidth=2, linecolor='black', mirror=True)

fig.show()
```

##### Styling grid lines

The width and color of axis grid lines are controlled by the `gridwidth` and `gridcolor` axis properties.

Here is an example of customizing the grid line width and color for a faceted scatter plot created with Plotly Express

```python
import plotly.express as px
df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", facet_col="species")
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')

fig.show()
```

##### Styling zero lines

The width and color of axis zero lines are controlled by the `zerolinewidth` and `zerolinecolor` axis properties.

Here is an example of configuring the zero line width and color for a simple figure using the `update_xaxes` and `update_yaxes` graph object figure methods.

```python
import plotly.express as px

fig = px.line(y=[1, 0])

fig.update_xaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')
fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='LightPink')

fig.show()
```

#### Set and Style Axes Title Labels

##### Set axis title text

Axis titles are set using the nested `title.text` property of the x or y axis. Here is an example of creating a new figure and using `update_xaxes` and `update_yaxes`, with magic underscore notation, to set the axis titles.

```python
import plotly.express as px

fig = px.line(y=[1, 0])

fig.update_xaxes(title_text='Time')
fig.update_yaxes(title_text='Value A')

fig.show()
```

### Set axis title position

This example sets `standoff` attribute to cartesian axes to determine the distance between the tick labels and the axis title. Note that the axis title position is always constrained within the margins, so the actual standoff distance is always less than the set or default value. By default [automargin](https://plot.ly/python/setting-graph-size/#automatically-adjust-margins) is `True` in Plotly template for the cartesian axis, so the margins will be pushed to fit the axis title at given standoff distance.

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scatter(
    mode = "lines+markers",
    y = [4, 1, 3],
    x = ["December", "January", "February"]))

fig.update_layout(
    xaxis = dict(
        tickangle = 90,
        title_text = "Month",
        title_font = {"size": 20},
        title_standoff = 25),
    yaxis = dict(
        title_text = "Temperature",
        title_standoff = 25))

fig.show()
```

##### Set axis title font

Here is an example that configures the font family, size, and color for the axis titles in a figure created using Plotly Express.

```python
import plotly.express as px
df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", facet_col="species")
fig.update_xaxes(title_font=dict(size=18, family='Courier', color='crimson'))
fig.update_yaxes(title_font=dict(size=18, family='Courier', color='crimson'))

fig.show()
```

#### Setting the Range of Axes Manually

The visible x and y axis range can be configured manually by setting the `range` axis property to a list of two values, the lower and upper boundary.

Here's an example of manually specifying the x and y axis range for a faceted scatter plot created with Plotly Express.

```python
import plotly.express as px
df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", facet_col="species")
fig.update_xaxes(range=[1.5, 4.5])
fig.update_yaxes(range=[3, 9])

fig.show()
```

### Fixed Ratio Axes

The `scaleanchor` and `scaleratio` axis properties can be used to force a fixed ratio of pixels per unit between two axes.

Here is an example of anchoring the scale of the x and y axis with a scale ratio of 1. Notice how the zoom box is constrained to prevent the distortion of the shape of the line plot.

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x = [0,1,1,0,0,1,1,2,2,3,3,2,2,3],
    y = [0,0,1,1,3,3,2,2,3,3,1,1,0,0]
))

fig.update_layout(
    width = 800,
    height = 500,
    title = "fixed-ratio axes",
    yaxis = dict(
      scaleanchor = "x",
      scaleratio = 1,
    )
)

fig.show()
```

### Fixed Ratio Axes with Compressed domain

If an axis needs to be compressed (either due to its own `scaleanchor` and `scaleratio` or those of the other axis), `constrain` determines how that happens: by increasing the "range" (default), or by decreasing the "domain".

```python
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(
    x = [0,1,1,0,0,1,1,2,2,3,3,2,2,3],
    y = [0,0,1,1,3,3,2,2,3,3,1,1,0,0]
))
fig.update_layout(
    width = 800,
    height = 500,
    title = "fixed-ratio axes with compressed axes",
    xaxis = dict(
      range=[-1,4],  # sets the range of xaxis
      constrain="domain",  # meanwhile compresses the xaxis by decreasing its "domain"
    ),
    yaxis = dict(
      scaleanchor = "x",
      scaleratio = 1,
    ),
)
fig.show()
```

##### Decreasing the domain spanned by an axis

In the example below, the x and y axis are anchored together, and the range of the `xaxis` is set manually. By default, plotly extends the range of the axis (overriding the `range` parameter) to fit in the figure `domain`. You can restrict the `domain` to force the axis to span only the set range, by setting `constrain='domain'` as below.

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x = [0,1,1,0,0,1,1,2,2,3,3,2,2,3],
    y = [0,0,1,1,3,3,2,2,3,3,1,1,0,0]
))

fig.update_layout(
    width = 800,
    height = 500,
    title = "fixed-ratio axes",
    yaxis = dict(
      scaleanchor = "x",
      scaleratio = 1,
    ),
    xaxis = dict(
        range=(-0.5, 3.5),
        constrain='domain'
    )
)

fig.show()
```

### Fixed Ratio Axes with Compressed domain

If an axis needs to be compressed (either due to its own `scaleanchor` and `scaleratio` or those of the other axis), `constrain` determines how that happens: by increasing the "range" (default), or by decreasing the "domain".

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x = [0,1,1,0,0,1,1,2,2,3,3,2,2,3],
    y = [0,0,1,1,3,3,2,2,3,3,1,1,0,0]
))

fig.update_layout(
    width = 800,
    height = 500,
    title = "fixed-ratio axes with compressed axes",
    xaxis = dict(
      range=[-1,4],  # sets the range of xaxis
      constrain="domain",  # meanwhile compresses the xaxis by decreasing its "domain"
    ),
    yaxis = dict(
      scaleanchor = "x",
      scaleratio = 1,
    ),
)

fig.show()
```

#### Reversed Axes

You can tell plotly's automatic axis range calculation logic to reverse the direction of an axis by setting the `autorange` axis property to `"reversed"`.

Here is an example of reversing the direction of the y axes for a faceted scatter plot created using Plotly Express.

```python
import plotly.express as px
df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", facet_col="species")
fig.update_yaxes(autorange="reversed")

fig.show()
```

#### Reversed Axes with Range ( Min/Max ) Specified

The direction of an axis can be reversed when manually setting the range extents by specifying a list containing the upper bound followed by the lower bound (rather that the lower followed by the upper) as the `range` axis property.

Here is an example of manually setting the reversed range of the y axes in a faceted scatter plot figure created using Plotly Express.

```python
import plotly.express as px
df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", facet_col="species")
fig.update_yaxes(range=[9, 3])

fig.show()
```

### Axis range for log axis type

If you are using a `log` type of axis and you want to set the range of the axis, you have to give the `log10` value of the bounds when using `fig.update_xaxes` or `fig.update_layout`. However, with `plotly.express` functions you pass directly the values of the range bounds (`plotly.express` then computes the appropriate values to pass to the figure layout).

```python
import plotly.express as px
import numpy as np

x = np.linspace(1, 200, 30)
fig = px.scatter(x=x, y=x**3, log_x=True, log_y=True, range_x=[0.8, 250])
fig.show()
```

```python
import plotly.graph_objects as go
import numpy as np

x = np.linspace(1, 200, 30)
fig = go.Figure(go.Scatter(x=x, y=x**3))
fig.update_xaxes(type="log", range=[np.log10(0.8), np.log10(250)])
fig.update_yaxes(type="log")
fig.show()
```

#### <code>nonnegative</code>, <code>tozero</code>, and <code>normal</code> Rangemode

The axis auto-range calculation logic can be configured using the `rangemode` axis parameter.

If `rangemode` is `"normal"` (the default), the range is computed based on the min and max values of the input data. If `"tozero"`, the range will always include zero. If `"nonnegative"`, the range will not extend below zero, regardless of the input data.

Here is an example of configuring a faceted scatter plot created using Plotly Express to always include zero for both the x and y axes.

```python
import plotly.express as px
df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length", facet_col="species")
fig.update_xaxes(rangemode="tozero")
fig.update_yaxes(rangemode="tozero")

fig.show()
```

#### Setting the domain of the axis

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x = [0,1,1,0,0,1,1,2,2,3,3,2,2,3],
    y = [0,0,1,1,3,3,2,2,3,3,1,1,0,0]
))
fig.update_xaxes(domain=(0.25, 0.75))
fig.update_yaxes(domain=(0.25, 0.75))
fig.show()
```

#### Reference

See https://plot.ly/python/reference/#layout-xaxis and https://plot.ly/python/reference/#layout-yaxis for more information and chart attribute options!
