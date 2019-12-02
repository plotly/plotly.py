---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.7
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
    version: 3.7.2
  plotly:
    description: How to make a graph with multiple axes in python.
    display_as: file_settings
    language: python
    layout: base
    name: Multiple Axes
    order: 15
    permalink: python/multiple-axes/
    thumbnail: thumbnail/multiple-axes.jpg
---

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

#### Muliple Y-Axes Subplots

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
        title="yaxis title",
        titlefont=dict(
            color="#1f77b4"
        ),
        tickfont=dict(
            color="#1f77b4"
        )
    ),
    yaxis2=dict(
        title="yaxis2 title",
        titlefont=dict(
            color="#ff7f0e"
        ),
        tickfont=dict(
            color="#ff7f0e"
        ),
        anchor="free",
        overlaying="y",
        side="left",
        position=0.15
    ),
    yaxis3=dict(
        title="yaxis4 title",
        titlefont=dict(
            color="#d62728"
        ),
        tickfont=dict(
            color="#d62728"
        ),
        anchor="x",
        overlaying="y",
        side="right"
    ),
    yaxis4=dict(
        title="yaxis5 title",
        titlefont=dict(
            color="#9467bd"
        ),
        tickfont=dict(
            color="#9467bd"
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

#### Reference
All of the y-axis properties are found here: https://plot.ly/python/reference/#YAxis.  For more information on creating subplots see the [Subplots in Python](/python/subplots/) section.
