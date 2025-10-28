---
description: How to make Log plots in Python with Plotly.
redirect_from: python/log-plots/
---
This page shows examples of how to configure [2-dimensional Cartesian axes](figure-structure.md#2d-cartesian-trace-types-and-subplots) to follow a logarithmic rather than linear progression. [Configuring gridlines, ticks, tick labels and axis titles](axes.md) on logarithmic axes is done the same was as with [linear axes](axes.md).

### Logarithmic Axes with Plotly Express

[Plotly Express](plotly-express.md) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](px-arguments.md) and produces [easy-to-style figures](styling-plotly-express.md).

All of Plotly Express' 2-D Cartesian functions include the `log_x` and `log_y` keyword arguments, which can be set to `True` to set the corresponding axis to a logarithmic scale:

```python
import plotly.express as px
df = px.data.gapminder().query("year == 2007")

fig = px.scatter(df, x="gdpPercap", y="lifeExp", hover_name="country", log_x=True)
fig.show()
```

Setting the range of a logarithmic axis with Plotly Express works the same was as with linear axes: using the `range_x` and `range_y` keywords. Note that you cannot set the range to include 0 or less.

```python
import plotly.express as px
df = px.data.gapminder().query("year == 2007")

fig = px.scatter(df, x="gdpPercap", y="lifeExp", hover_name="country",
                 log_x=True, range_x=[1,100000], range_y=[0,100])
fig.show()
```

#### Adding minor ticks

_new in 5.8_

You can position and style minor ticks using `minor`. This takes a `dict` of properties to apply to minor ticks. See the [figure reference](reference/graph_objects/layout-package/XAxis.md#plotly.graph_objects.layout.XAxis.minor) for full details on the accepted keys in this dict.

In this example we set the tick length with `ticklen`, add the ticks on the inside with `ticks="inside"`, and turn grid lines on with `howgrid=True`.

```python
import plotly.express as px
df = px.data.gapminder().query("year == 2007")

fig = px.scatter(df, x="gdpPercap", y="lifeExp", hover_name="country",
                 log_x=True, range_x=[1,100000], range_y=[0,100])

fig.update_xaxes(minor=dict(ticks="inside", ticklen=6, showgrid=True))

fig.show()
```

#### Controlling Minor Log Labels

*New in 6.3*

You can control how minor log labels are displayed using the `minorloglabels` attribute. Set to `"complete"` to show complete digits, or `None` for no labels. By default, minor log labels use `"small digits"`, as shown in the previous example.

```python
import plotly.express as px

df = px.data.gapminder().query("year == 2007")

fig = px.scatter(
    df, x="gdpPercap",
    y="lifeExp",
    hover_name="country",
    log_x=True,
    range_x=[1,100000],
    range_y=[0,100]
)

fig.update_xaxes(
    minor=dict(
        ticks="inside",
        ticklen=6,
        showgrid=True
    ),
    minorloglabels="complete"
)

fig.show()
```

### Logarithmic Axes with Graph Objects

If Plotly Express does not provide a good starting point, it is also possible to use [the more generic `go.Figure` class from `plotly.graph_objects`](graph-objects.md).

```python
import plotly.graph_objects as go
import plotly.express as px
df = px.data.gapminder().query("year == 2007")

fig = go.Figure()

fig.add_trace(go.Scatter(mode="markers", x=df["gdpPercap"], y=df["lifeExp"] ))

fig.update_xaxes(type="log")
fig.show()
```

Setting the range of a logarithmic axis with `plotly.graph_objects` is *very different* than setting the range of linear axes: the range is set using the exponent rather than the actual value:


```python
import plotly.graph_objects as go
import plotly.express as px
df = px.data.gapminder().query("year == 2007")

fig = go.Figure()

fig.add_trace(go.Scatter(mode="markers", x=df["gdpPercap"], y=df["lifeExp"] ))

fig.update_xaxes(type="log", range=[0,5]) # log range: 10^0=1, 10^5=100000
fig.update_yaxes(range=[0,100]) # linear range
fig.show()
```

#### Reference

See [function reference for `px.(scatter)`](reference/plotly-express.md#plotly.express.scatter) or [`go.layout.XAxis.type`](reference/graph_objects/layout-package/XAxis.md#plotly.graph_objects.layout.XAxis.type) for more information and chart attribute options!
