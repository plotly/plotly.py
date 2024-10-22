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
    version: 3.8.0
  plotly:
    description: How to make a graph with multiple axes (dual y-axis plots, plots
      with secondary axes) in python.
    display_as: file_settings
    language: python
    layout: base
    name: Multiple Axes
    order: 16
    permalink: python/multiple-axes/
    thumbnail: thumbnail/multiple-axes.jpg
---

### Multiple Y Axes and Plotly Express

[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/).

> *Note*: At this time, Plotly Express does not support multiple Y axes on a single figure. To make such a figure, use the [`make_subplots()`](/python/subplots/) function in conjunction with [graph objects](/python/graph-objects/) as documented below.


#### Two Y Axes

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig.add_trace(
    go.Scatter(x=[1, 2, 3], y=[40, 50, 60], name="yaxis data"),
    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=[2, 3, 4], y=[4, 5, 6], name="yaxis2 data"),
    secondary_y=True,
)

# Add figure title
fig.update_layout(
    title_text="Double Y Axis Example"
)

# Set x-axis title
fig.update_xaxes(title_text="xaxis title")

# Set y-axes titles
fig.update_yaxes(title_text="<b>primary</b> yaxis title", secondary_y=False)
fig.update_yaxes(title_text="<b>secondary</b> yaxis title", secondary_y=True)

fig.show()
```

### Multiple axes in Dash

[Dash](https://plotly.com/dash/) is the best way to build analytical apps in Python using Plotly figures. To run the app below, run `pip install dash`, click "Download" to get the code and run `python app.py`.

Get started  with [the official Dash docs](https://dash.plotly.com/installation) and **learn how to effortlessly [style](https://plotly.com/dash/design-kit/) & [deploy](https://plotly.com/dash/app-manager/) apps like this with <a class="plotly-red" href="https://plotly.com/dash/">Dash Enterprise</a>.**


```python hide_code=true
from IPython.display import IFrame
snippet_url = 'https://python-docs-dash-snippets.herokuapp.com/python-docs-dash-snippets/'
IFrame(snippet_url + 'multiple-axes', width='100%', height=1200)
```

<div style="font-size: 0.9em;"><div style="width: calc(100% - 30px); box-shadow: none; border: thin solid rgb(229, 229, 229);"><div style="padding: 5px;"><div><p><strong>Sign up for Dash Club</strong> → Free cheat sheets plus updates from Chris Parmer and Adam Schroeder delivered to your inbox every two months. Includes tips and tricks, community apps, and deep dives into the Dash architecture.
<u><a href="https://go.plotly.com/dash-club?utm_source=Dash+Club+2022&utm_medium=graphing_libraries&utm_content=inline">Join now</a></u>.</p></div></div></div></div>


#### Multiple Y-Axes Subplots

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(rows=2, cols=2,
                    specs=[[{"secondary_y": True}, {"secondary_y": True}],
                           [{"secondary_y": True}, {"secondary_y": True}]])

# Top left
fig.add_trace(
    go.Scatter(x=[1, 2, 3], y=[2, 52, 62], name="yaxis data"),
    row=1, col=1, secondary_y=False)

fig.add_trace(
    go.Scatter(x=[1, 2, 3], y=[40, 50, 60], name="yaxis2 data"),
    row=1, col=1, secondary_y=True,
)

# Top right
fig.add_trace(
    go.Scatter(x=[1, 2, 3], y=[2, 52, 62], name="yaxis3 data"),
    row=1, col=2, secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=[1, 2, 3], y=[40, 50, 60], name="yaxis4 data"),
    row=1, col=2, secondary_y=True,
)

# Bottom left
fig.add_trace(
    go.Scatter(x=[1, 2, 3], y=[2, 52, 62], name="yaxis5 data"),
    row=2, col=1, secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=[1, 2, 3], y=[40, 50, 60], name="yaxis6 data"),
    row=2, col=1, secondary_y=True,
)

# Bottom right
fig.add_trace(
    go.Scatter(x=[1, 2, 3], y=[2, 52, 62], name="yaxis7 data"),
    row=2, col=2, secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=[1, 2, 3], y=[40, 50, 60], name="yaxis8 data"),
    row=2, col=2, secondary_y=True,
)

fig.show()
```

#### Multiple Axes

Low-level API for creating a figure with multiple axes

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3],
    y=[4, 5, 6],
    name="yaxis1 data"
))


fig.add_trace(go.Scatter(
    x=[2, 3, 4],
    y=[40, 50, 60],
    name="yaxis2 data",
    yaxis="y2"
))

fig.add_trace(go.Scatter(
    x=[4, 5, 6],
    y=[40000, 50000, 60000],
    name="yaxis3 data",
    yaxis="y3"
))

fig.add_trace(go.Scatter(
    x=[5, 6, 7],
    y=[400000, 500000, 600000],
    name="yaxis4 data",
    yaxis="y4"
))


# Create axis objects
fig.update_layout(
    xaxis=dict(
        domain=[0.3, 0.7]
    ),
    yaxis=dict(
        title=dict(
            text="yaxis title",
            font=dict(
                color="#1f77b4"
            )
        ),
    ),
    yaxis2=dict(
        title=dict(
            text="yaxis2 title",
            font=dict(
                color="#ff7f0e"
            )
        ),
        anchor="free",
        overlaying="y",
        side="left",
        position=0.15
    ),
    yaxis3=dict(
        title=dict(
            text="yaxis3 title",
            font=dict(
                color="#d62728"
            )
        ),
        anchor="x",
        overlaying="y",
        side="right"
    ),
    yaxis4=dict(
        title=dict(
            text="yaxis4 title",
            font=dict(
                color="#9467bd"
            )
        ),
        anchor="free",
        overlaying="y",
        side="right",
        position=0.85
    )
)

# Update layout properties
fig.update_layout(
    title_text="multiple y-axes example",
    width=800,
)

fig.show()
```

#### Automatically Shifting Axes

*New in 5.12*

To automatically reposition axes to avoid overlap with other axes with the same `overlaying` value, set `autoshift=True`. For `autoshift` to work on an axis, you'll also need to set `anchor="free"` on that axis.

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6], name="yaxis data"))

fig.add_trace(go.Scatter(x=[2, 3, 4], y=[40, 50, 60], name="yaxis2 data", yaxis="y2"))

fig.add_trace(
    go.Scatter(x=[4, 5, 6], y=[1000, 2000, 3000], name="yaxis3 data", yaxis="y3")
)

fig.add_trace(
    go.Scatter(x=[3, 4, 5], y=[400, 500, 600], name="yaxis4 data", yaxis="y4")
)


fig.update_layout(
    xaxis=dict(domain=[0.25, 0.75]),
    yaxis=dict(
        title="yaxis title",
    ),
    yaxis2=dict(
        title="yaxis2 title",
        overlaying="y",
        side="right",
    ),
    yaxis3=dict(title="yaxis3 title", anchor="free", overlaying="y", autoshift=True),
    yaxis4=dict(
        title="yaxis4 title",
        anchor="free",
        overlaying="y",
        autoshift=True,
    ),
)

fig.update_layout(
    title_text="Shifting y-axes with autoshift",
)

fig.show()

```

### Shift Axes by a Specific Number of Pixels

*New in 5.12*

Set a `shift` value on an axis to shift an axis by that number of pixels. A positive value shifts an axis to the right. A negative value shifts it to the left. Here, we shift `yaxis4` 100 pixels further to the left.

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6], name="yaxis data"))

fig.add_trace(go.Scatter(x=[2, 3, 4], y=[40, 50, 60], name="yaxis2 data", yaxis="y2"))

fig.add_trace(
    go.Scatter(x=[4, 5, 6], y=[1000, 2000, 3000], name="yaxis3 data", yaxis="y3")
)

fig.add_trace(
    go.Scatter(x=[3, 4, 5], y=[400, 500, 600], name="yaxis4 data", yaxis="y4")
)


fig.update_layout(
    xaxis=dict(domain=[0.25, 0.75]),
    yaxis=dict(
        title="yaxis title",
    ),
    yaxis2=dict(
        title="yaxis2 title",
        overlaying="y",
        side="right",
    ),
    yaxis3=dict(title="yaxis3 title", anchor="free", overlaying="y", autoshift=True),
    yaxis4=dict(
        title="yaxis4 title",
        anchor="free",
        overlaying="y",
        autoshift=True,
        shift=-100,
    ),
)

fig.update_layout(
    title_text="Shifting y-axes by a specific number of pixels",
)

fig.show()

```

### Sync Axes Ticks


*New in 5.13*

With overlayed axes, each axis by default has its own number of ticks. You can sync the number of ticks on a cartesian axis with another one it overlays by setting `tickmode="sync"`. In this example, we sync the ticks on the `"Total bill amount"` axis with the `"Total number of diners"` axis that it overlays.

```python
import plotly.graph_objects as go
from plotly.data import tips

df = tips()

summed_values = df.groupby(by="day", as_index=False).sum(numeric_only=True)
day_order_mapping = {"Thur": 0, "Fri": 1, "Sat": 2, "Sun": 3}
summed_values["order"] = summed_values["day"].apply(lambda day: day_order_mapping[day])
summed_values = summed_values.sort_values(by="order")

days_of_week = summed_values["day"].values
total_bills = summed_values["total_bill"].values
number_of_diners = summed_values["size"].values


fig = go.Figure(
    data=go.Bar(
        x=days_of_week,
        y=number_of_diners,
        name="Total number of diners",
        marker=dict(color="paleturquoise"),
    )
)

fig.add_trace(
    go.Scatter(
        x=days_of_week,
        y=total_bills,
        yaxis="y2",
        name="Total bill amount",
        marker=dict(color="crimson"),
    )
)

fig.update_layout(
    legend=dict(orientation="h"),
    yaxis=dict(
        title=dict(text="Total number of diners"),
        side="left",
        range=[0, 250],
    ),
    yaxis2=dict(
        title=dict(text="Total bill amount"),
        side="right",
        range=[0, 2000],
        overlaying="y",
        tickmode="sync",
    ),
)

fig.show()

```

#### Reference
All of the y-axis properties are found here: https://plotly.com/python/reference/layout/yaxis/.  For more information on creating subplots see the [Subplots in Python](/python/subplots/) section.
