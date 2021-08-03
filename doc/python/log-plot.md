---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.2
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
    version: 3.7.7
  plotly:
    description: How to make Log plots in Python with Plotly.
    display_as: scientific
    language: python
    layout: base
    name: Log Plots
    order: 5
    permalink: python/log-plot/
    redirect_from: python/log-plots/
    thumbnail: thumbnail/log.jpg
---

This page shows examples of how to configure [2-dimensional Cartesian axes](/python/figure-structure/#2d-cartesian-trace-types-and-subplots) to follow a logarithmic rather than linear progression. [Configuring gridlines, ticks, tick labels and axis titles](/python/axes/) on logarithmic axes is done the same was as with [linear axes](/python/axes/).

### Logarithmic Axes with Plotly Express

[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/).

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

### Logarithmic Axes with Graph Objects

If Plotly Express does not provide a good starting point, it is also possible to use [the more generic `go.Figure` class from `plotly.graph_objects`](/python/graph-objects/).

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

See [function reference for `px.(scatter)`](https://plotly.com/python-api-reference/generated/plotly.express.scatter) or https://plotly.com/python/reference/layout/xaxis/#layout-xaxis-type for more information and chart attribute options!
