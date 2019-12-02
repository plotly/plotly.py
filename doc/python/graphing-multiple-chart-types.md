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
    description: How to design figures with multiple chart types in python.
    display_as: file_settings
    language: python
    layout: base
    name: Multiple Chart Types
    order: 17
    page_type: u-guide
    permalink: python/graphing-multiple-chart-types/
    thumbnail: thumbnail/multiple-chart-type.jpg
---

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
See https://plot.ly/python/reference/ for more information and attribute options!
