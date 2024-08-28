---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.1
  kernelspec:
    display_name: Python 3 (ipykernel)
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
    version: 3.10.11
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

#### Grouped Bar and Scatter Chart

*New in 5.12*

In this example, we display individual data points with a grouped scatter chart and show averages using a grouped bar chart. `offsetgroup` links the bar trace for smoker with the scatter trace for smoker, and the bar trace for non-smoker with the scatter trace for non-smoker. If you deselect a trace using the legend, other traces maintain the position of the traces they are linked to.

```python
import plotly.graph_objects as go
from plotly import data

df = data.tips()[data.tips()["day"] == "Sun"]

mean_values_df = df.groupby(by=["sex", "smoker"], as_index=False).mean(
    numeric_only=True
)

smoker_mean = mean_values_df[mean_values_df.smoker == "Yes"].sort_values(
    by="tip", ascending=False
)
non_smoker_mean = mean_values_df[mean_values_df.smoker == "No"].sort_values(
    by="tip", ascending=False
)

smoker = df[df.smoker == "Yes"].sort_values(by="tip", ascending=False)
non_smoker = df[df.smoker == "No"].sort_values(by="tip", ascending=False)

fig = go.Figure(
    layout=dict(
        xaxis=dict(categoryorder="category descending"),
        yaxis=dict(range=[0, 7]),
        scattermode="group",
        legend=dict(groupclick="toggleitem"),
    )
)

fig.add_trace(
    go.Bar(
        x=smoker_mean.sex,
        y=smoker_mean.tip,
        name="Average",
        marker_color="IndianRed",
        offsetgroup="smoker",
        legendgroup="smoker",
        legendgrouptitle_text="Smoker",
    )
)


fig.add_trace(
    go.Scatter(
        x=smoker.sex,
        y=smoker.tip,
        mode="markers",
        name="Individual tips",
        marker=dict(color="LightSlateGrey", size=5),
        offsetgroup="smoker",
        legendgroup="smoker",
    )
)

fig.add_trace(
    go.Bar(
        x=non_smoker_mean.sex,
        y=non_smoker_mean.tip,
        name="Average",
        marker_color="LightSalmon",
        offsetgroup="non-smoker",
        legendgroup="non-smoker",
        legendgrouptitle_text="Non-Smoker",
    )
)


fig.add_trace(
    go.Scatter(
        x=non_smoker.sex,
        y=non_smoker.tip,
        mode="markers",
        name="Individual tips",
        marker=dict(color="LightSteelBlue", size=5),
        offsetgroup="non-smoker",
        legendgroup="non-smoker",
    )
)

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
import urllib

response = urllib.request.urlopen(
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

#### Trace Zorder

*New in 5.21*

You can move a trace in front of or behind another trace by setting its `zorder`. All traces have a default `zorder` of `0`. In the following example, we set `zorder` on the bar trace to `1` to move it in front of the scatter trace.

```python
import plotly.graph_objects as go

x = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
y_bar = [10, 15, 7, 10, 17, 15, 14, 20, 16, 19, 15, 17]
y_area = [12, 13, 10, 14, 15, 13, 16, 18, 15, 17, 14, 16]

area_trace = go.Scatter(
    x=x,
    y=y_area,
    fill="tozeroy",
    mode="lines+markers",
    name="Area Trace with default `zorder` of 0",
    line=dict(color="lightsteelblue"),
)

bar_trace = go.Bar(
    x=x,
    y=y_bar,
    name="Bar Trace with `zorder` of 1",
    zorder=1,
    marker=dict(color="lightslategray"),
)

fig = go.Figure(data=[area_trace, bar_trace])

fig.show()

```

#### Reference
See https://plotly.com/python/reference/ for more information and attribute options!
