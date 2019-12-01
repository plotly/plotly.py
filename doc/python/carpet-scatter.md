---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.1
  kernel_info:
    name: python3
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
    version: 3.6.8
  plotly:
    description: How to make carpet scatter plots in Python with Plotly.
    display_as: scientific
    language: python
    layout: base
    name: Carpet Scatter Plot
    order: 16
    page_type: u-guide
    permalink: python/carpet-scatter/
    thumbnail: thumbnail/scattercarpet.jpg
---


### Basic Carpet Plot

```python inputHidden=false outputHidden=false
import plotly.graph_objects as go

fig = go.Figure(go.Carpet(
    a = [4, 4, 4, 4.5, 4.5, 4.5, 5, 5, 5, 6, 6, 6],
    b = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
    y = [2, 3.5, 4, 3, 4.5, 5, 5.5, 6.5, 7.5, 8, 8.5, 10],
    aaxis = dict(
      tickprefix = 'a = ',
      ticksuffix = 'm',
      smoothing = 1,
      minorgridcount = 9
      ),
    baxis = dict(
      tickprefix = 'b = ',
      ticksuffix = 'Pa',
      smoothing = 1,
      minorgridcount = 9
      )
))

fig.show()
```

### Add Carpet Scatter Trace

```python inputHidden=false outputHidden=false
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Carpet(
    a = [4, 4, 4, 4.5, 4.5, 4.5, 5, 5, 5, 6, 6, 6],
    b = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
    y = [2, 3.5, 4, 3, 4.5, 5, 5.5, 6.5, 7.5, 8, 8.5, 10],
    aaxis = dict(
      tickprefix = 'a = ',
      ticksuffix = 'm',
      smoothing = 1,
      minorgridcount = 9
      ),
    baxis = dict(
      tickprefix = 'b = ',
      ticksuffix = 'Pa',
      smoothing = 1,
      minorgridcount = 9
      )
))

fig.add_trace(go.Scattercarpet(
    a = [4, 4.5, 5, 6],
    b = [2.5, 2.5, 2.5, 2.5],
    line = dict(
      shape = 'spline',
      smoothing = 1,
      color = 'blue'
    )
))

fig.show()
```

### Add Multiple Scatter Traces

```python inputHidden=false outputHidden=false
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Carpet(
    a = [0.1,0.2,0.3],
    b = [1,2,3],
    y = [[1,2.2,3],[1.5,2.7,3.5],[1.7,2.9,3.7]],
    cheaterslope = 1,
    aaxis = dict(
        title = "a",
        tickmode = "linear",
        dtick = 0.05
    ),
    baxis = dict(
        title = "b",
        tickmode = "linear",
        dtick = 0.05
    )
))

fig.add_trace(go.Scattercarpet(
    name = "b = 1.5",
    a = [0.05, 0.15, 0.25, 0.35],
    b = [1.5, 1.5, 1.5, 1.5]
))

fig.add_trace(go.Scattercarpet(
    name = "b = 2",
    a = [0.05, 0.15, 0.25, 0.35],
    b = [2, 2, 2, 2]
))

fig.add_trace(go.Scattercarpet(
    name = "b = 2.5",
    a = [0.05, 0.15, 0.25, 0.35],
    b = [2.5, 2.5, 2.5, 2.5]
))

fig.add_trace(go.Scattercarpet(
    name = "a = 0.15",
    a = [0.15, 0.15, 0.15, 0.15],
    b = [0.5, 1.5, 2.5, 3.5],
    line = dict(
        smoothing = 1,
        shape = "spline"
    )
))

fig.add_trace(go.Scattercarpet(
    name = "a = 0.2",
    a = [0.2, 0.2, 0.2, 0.2],
    b = [0.5, 1.5, 2.5, 3.5],
    line = dict(
        smoothing = 1,
        shape = "spline"
    ),
      marker = dict(
        size = [10, 20, 30, 40],
        color = ["#000", "#f00", "#ff0", "#fff"]
      )
))

fig.add_trace(go.Scattercarpet(
    name = "a = 0.25",
    a = [0.25, 0.25, 0.25, 0.25],
    b = [0.5, 1.5, 2.5, 3.5],
    line = dict(
        smoothing = 1,
        shape = "spline"
    )
))

fig.update_layout(
    title = "scattercarpet extrapolation, clipping, and smoothing",
    hovermode = "closest"
)

fig.show()
```

### Reference


See https://plot.ly/python/reference/#scattercarpet for more information and chart attribute options!
