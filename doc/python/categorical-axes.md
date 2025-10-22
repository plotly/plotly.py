---
description: How to use categorical axes in Python with Plotly.
---
This page shows examples of how to configure [2-dimensional Cartesian axes](figure-structure.md#2d-cartesian-trace-types-and-subplots) to visualize categorical (i.e. qualitative, nominal or ordinal data as opposed to continuous numerical data). Such axes are a natural fit for bar charts, waterfall charts, funnel charts, heatmaps, violin charts and box plots, but can also be used with scatter plots and line charts. [Configuring gridlines, ticks, tick labels and axis titles](axes.md) on logarithmic axes is done the same was as with [linear axes](axes.md).

### 2-D Cartesian Axis Type and Auto-Detection

The different types of Cartesian axes are configured via the `xaxis.type` or `yaxis.type` attribute, which can take on the following values:

- `'linear'` (see the [linear axes tutorial](axes.md))
- `'log'` (see the [log plot tutorial](log-plot.md))
- `'date'` (see the [tutorial on timeseries](time-series.md))
- `'category'` see below
- `'multicategory'` see below

The axis type is auto-detected by looking at data from the first [trace](figure-structure.md) linked to this axis:

* First check for `multicategory`, then `date`, then `category`, else default to `linear` (`log` is never automatically selected)
* `multicategory` is just a shape test: is the array nested?
* `date` and `category`: require **more than twice as many distinct date or category strings as distinct numbers** in order to choose that axis type.
	* Both of these test an evenly-spaced sample of at most 1000 values

### Forcing an axis to be categorical

It is possible to force the axis type by setting explicitly `xaxis_type`. In the example below the automatic X axis type would be `linear` (because there are not more than twice as many unique strings as unique numbers) but we force it to be `category`.

```python
import plotly.express as px
fig = px.bar(x=["a", "a", "b", 3], y = [1,2,3,4])
fig.update_xaxes(type='category')
fig.show()
```

### Categorical Axes and Trace Types

Every cartesian trace type is compatible with categorical axes, not just `bar`.

Scatter plots where one axis is categorical are often known as [dot plots](dot-plots.md).

```python
import plotly.express as px
df = px.data.medals_long()

fig = px.scatter(df, y="nation", x="count", color="medal", symbol="medal")
fig.update_traces(marker_size=10)
fig.show()
```

[Box plots]() and [violin plots]() are often shown with one categorical and one continuous axis.

```python
import plotly.express as px
df = px.data.tips()

fig = px.box(df, x="sex", y="total_bill", color="smoker")
fig.show()
```

```python
import plotly.express as px
df = px.data.tips()

fig = px.violin(df, x="sex", y="total_bill", color="smoker")
fig.show()
```

### Controlling the Category Order with Plotly Express

[Plotly Express](plotly-express.md) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](px-arguments.md) and produces [easy-to-style figures](styling-plotly-express.md).

By default, Plotly Express lays out categorical data in the order in which it appears in the underlying data. Every 2-d cartesian Plotly Express function also includes a `category_orders` keyword argument which can be used to control the order in which categorical axes are drawn, but beyond that can also control [the order in which discrete colors appear in the legend](discrete-color.md), and [the order in which facets are laid out](facet-plots.md).

```python
import plotly.express as px
df = px.data.tips()
fig = px.bar(df, x="day", y="total_bill", color="smoker", barmode="group", facet_col="sex",
             category_orders={"day": ["Thur", "Fri", "Sat", "Sun"],
                              "smoker": ["Yes", "No"],
                              "sex": ["Male", "Female"]})
fig.show()
```

### Automatically Sorting Categories by Name or Total Value

Whether using Plotly Express or not, categories can be sorted alphabetically or by value using the `categoryorder` attribute:

Set `categoryorder` to `"category ascending"` or `"category descending"` for the alphanumerical order of the category names or `"total ascending"` or `"total descending"` for numerical order of values. [categoryorder](reference/graph_objects/layout-package/XAxis.md#plotly.graph_objects.layout.XAxis.categoryorder) for more information. Note that sorting the bars by a particular trace isn't possible right now - it's only possible to sort by the total values. Of course, you can always sort your data _before_ plotting it if you need more customization.

This example orders the categories **alphabetically** with `categoryorder: 'category ascending'`

```python
import plotly.graph_objects as go

x=['b', 'a', 'c', 'd']
fig = go.Figure(go.Bar(x=x, y=[2,5,1,9], name='Montreal'))
fig.add_trace(go.Bar(x=x, y=[1, 4, 9, 16], name='Ottawa'))
fig.add_trace(go.Bar(x=x, y=[6, 8, 4.5, 8], name='Toronto'))

fig.update_layout(barmode='stack')
fig.update_xaxes(categoryorder='category ascending')
fig.show()
```

This example orders the categories **by total value** with `categoryorder: 'total descending'`

```python
import plotly.graph_objects as go

x=['b', 'a', 'c', 'd']
fig = go.Figure(go.Bar(x=x, y=[2,5,1,9], name='Montreal'))
fig.add_trace(go.Bar(x=x, y=[1, 4, 9, 16], name='Ottawa'))
fig.add_trace(go.Bar(x=x, y=[6, 8, 4.5, 8], name='Toronto'))

fig.update_layout(barmode='stack')
fig.update_xaxes(categoryorder='total ascending')
fig.show()
```

This example shows how to control category order when using `plotly.graph_objects` by defining `categoryorder` to "array" to derive the ordering from the attribute `categoryarray`.

```python
import plotly.graph_objects as go

x=['b', 'a', 'c', 'd']
fig = go.Figure(go.Bar(x=x, y=[2,5,1,9], name='Montreal'))
fig.add_trace(go.Bar(x=x, y=[1, 4, 9, 16], name='Ottawa'))
fig.add_trace(go.Bar(x=x, y=[6, 8, 4.5, 8], name='Toronto'))

fig.update_layout(barmode='stack')
fig.update_xaxes(categoryorder='array', categoryarray= ['d','a','c','b'])
fig.show()
```
### Gridlines, Ticks and Tick Labels


By default, gridlines and ticks are not shown on categorical axes but they can be activated:

```python
import plotly.express as px

fig = px.bar(x=["A","B","C"], y=[1,3,2])
fig.update_xaxes(showgrid=True, ticks="outside")
fig.show()
```

By default, ticks and gridlines appear on the categories but the `tickson` attribute can be used to move them to the category boundaries:

```python
import plotly.express as px

fig = px.bar(x=["A","B","C"], y=[1,3,2])
fig.update_xaxes(showgrid=True, ticks="outside", tickson="boundaries")
fig.show()
```

### Multi-categorical Axes

A two-level categorical axis (also known as grouped or hierarchical categories, or sub-categories) can be created by specifying a trace's `x` or `y` property as a 2-dimensional lists. The first sublist represents the outer categorical value while the second sublist represents the inner categorical value. This is only possible with `plotly.graph_objects` at the moment, and not Plotly Express.

Passing in a two-dimensional list as the `x` or `y` value of a trace causes [the `type` of the corresponding axis](axes.md) to be set to `multicategory`.

Here is an example that creates a figure with 2 `bar` traces with a 2-level categorical x-axis.

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Bar(
  x = [['First', 'First', 'Second', 'Second'],
       ["A", "B", "A", "B"]],
  y = [2, 3, 1, 5],
  name = "Adults",
))

fig.add_trace(go.Bar(
  x = [['First', 'First', 'Second', 'Second'],
       ["A", "B", "A", "B"]],
  y = [8, 3, 6, 5],
  name = "Children",
))

fig.update_layout(title_text="Multi-category axis")

fig.show()
```
### Reference

See the [full reference for `go.layout.xaxis`](reference/graph_objects/layout-package/XAxis.md) for more information and chart attribute options!
