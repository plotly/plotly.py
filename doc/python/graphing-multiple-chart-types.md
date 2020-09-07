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
    description: How to design figures with multiple chart types in python.
    display_as: file_settings
    language: python
    layout: base
    name: Multiple Chart Types
    order: 18
    page_type: u-guide
    permalink: python/graphing-multiple-chart-types/
    thumbnail: thumbnail/multiple-chart-type.jpg
---

### Chart Types versus Trace Types

Plotly's [figure data structure](/python/figure-structure/) supports defining [subplots](/python/subplots/) of [various types](/python/mixed-subplots/) (e.g. [cartesian](/python/axes/), [polar](/python/polar-chart/), [3-dimensional](/python/3d-charts/), [maps](/python/maps/) etc) with attached traces of [various compatible types](/python/figure-structure/) (e.g. scatter, bar, choropleth, surface etc). This means that **Plotly figures are not constrained to representing a fixed set of "chart types"** such as scatter plots only or bar charts only or line charts only: any subplot can contain multiple traces of different types.


### Multiple Trace Types with Plotly Express

[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/).

Plotly Express exposes a number of functions such as `px.scatter()` and `px.choropleth()` which generally speaking only contain traces of the same type, with exceptions made for [trendlines](/python/linear-fits/) and [marginal distribution plots](/python/marginal-plots/).

Figures produced with Plotly Express functions support the `add_trace()` method documented below, just like figures created with [graph objects](/python/graph-objects/) so it is easy to start with a Plotly Express figure containing only traces of a given type, and add traces of another type.

```python
import plotly.express as px

fruits = ["apples", "oranges", "bananas"]
fig = px.line(x=fruits, y=[1,3,2], color=px.Constant("This year"),
             labels=dict(x="Fruit", y="Amount", color="Time Period"))
fig.add_bar(x=fruits, y=[2,1,3], name="Last year")
fig.show()
```

#### Line Chart and a Bar Chart

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=[0, 1, 2, 3, 4, 5],
        y=[1.5, 1, 1.3, 0.7, 0.8, 0.9]
    ))

fig.add_trace(
    go.Bar(
        x=[0, 1, 2, 3, 4, 5],
        y=[1, 0.5, 0.7, -1.2, 0.3, 0.4]
    ))

fig.show()
```

#### A Contour and Scatter Plot of the Method of Steepest Descent

```python
import plotly.graph_objects as go

# Load data
import json
import six.moves.urllib

response = six.moves.urllib.request.urlopen(
    "https://raw.githubusercontent.com/plotly/datasets/master/steepest.json")

data = json.load(response)

# Create figure
fig = go.Figure()

fig.add_trace(
    go.Contour(
        z=data["contour_z"][0],
        y=data["contour_y"][0],
        x=data["contour_x"][0],
        ncontours=30,
        showscale=False
    )
)

fig.add_trace(
    go.Scatter(
        x=data["trace_x"],
        y=data["trace_y"],
        mode="markers+lines",
        name="steepest",
        line=dict(
            color="black"
        )
    )
)

fig.show()
```

#### Reference
See https://plotly.com/python/reference/ for more information and attribute options!