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
    name: python2
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
    description: How to make carpet contour plots in Python with Plotly.
    display_as: scientific
    language: python
    layout: base
    name: Carpet Contour Plot
    order: 15
    page_type: u-guide
    permalink: python/carpet-contour/
    thumbnail: thumbnail/contourcarpet.jpg
---

### Basic Carpet Plot

Set the `x` and `y` coorindates, using `x` and `y` attributes. If `x` coorindate values are ommitted a cheater plot will be created. To save parameter values use `a` and `b` attributes. To make changes to the axes, use `aaxis` or `baxis` attributes. For a more detailed list of axes attributes refer to [python reference](https://plot.ly/python/reference/#carpet-aaxis).

```python
import plotly.graph_objects as go

fig = go.Figure(go.Carpet(
    a = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3],
    b = [4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],
    x = [2, 3, 4, 5, 2.2, 3.1, 4.1, 5.1, 1.5, 2.5, 3.5, 4.5],
    y = [1, 1.4, 1.6, 1.75, 2, 2.5, 2.7, 2.75, 3, 3.5, 3.7, 3.75],
    aaxis = dict(
        tickprefix = 'a = ',
        smoothing = 0,
        minorgridcount = 9,
        type = 'linear'
    ),
    baxis = dict(
        tickprefix = 'b = ',
        smoothing = 0,
        minorgridcount = 9,
        type = 'linear'
    )
))

fig.show()
```

### Add Contours

```python inputHidden=false outputHidden=false
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Contourcarpet(
    a = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3],
    b = [4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],
    z = [1, 1.96, 2.56, 3.0625, 4, 5.0625, 1, 7.5625, 9, 12.25, 15.21, 14.0625],
    autocontour = False,
    contours = dict(
        start = 1,
        end = 14,
        size = 1
    ),
    line = dict(
        width = 2,
        smoothing = 0
    ),
    colorbar = dict(
       len = 0.4,
        y = 0.25
    )
))

fig.add_trace(go.Carpet(
    a = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3],
    b = [4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6],
    x = [2, 3, 4, 5, 2.2, 3.1, 4.1, 5.1, 1.5, 2.5, 3.5, 4.5],
    y = [1, 1.4, 1.6, 1.75, 2, 2.5, 2.7, 2.75, 3, 3.5, 3.7, 3.75],
    aaxis = dict(
        tickprefix = 'a = ',
        smoothing = 0,
        minorgridcount = 9,
        type = 'linear'
    ),
    baxis = dict(
        tickprefix = 'b = ',
        smoothing = 0,
        minorgridcount = 9,
        type = 'linear'
    )
))

fig.show()
```

### Add Multiple Traces

```python inputHidden=false outputHidden=false
import plotly.graph_objects as go
import json
from urllib.request import urlopen

url = "https://raw.githubusercontent.com/bcdunbar/datasets/master/airfoil_data.json"
data = json.load(urlopen(url))


fig=go.Figure()

fig.add_trace(go.Carpet(
    a = data[0]['a'],
    b = data[0]['b'],
    x = data[0]['x'],
    y = data[0]['y'],
    baxis = dict(
      startline = False,
      endline = False,
      showticklabels = "none",
      smoothing = 0,
      showgrid = False
    ),
    aaxis = dict(
      startlinewidth = 2,
      startline = True,
      showticklabels = "none",
      endline = True,
      showgrid = False,
      endlinewidth = 2,
      smoothing = 0
    )
))

fig.add_trace(go.Contourcarpet(
    z = data[1]['z'],
    autocolorscale = False,
    zmax = 1,
    name = "Pressure",
    colorscale = "Viridis",
    zmin = -8,
    colorbar = dict(
      y = 0,
      yanchor = "bottom",
      titleside = "right",
      len = 0.75,
      title = "Pressure coefficient, c<sub>p</sub>"
    ),
    contours = dict(
      start = -1,
      size = 0.025,
      end = 1.000,
      showlines = False
    ),
    line = dict(
      smoothing = 0
    ),
    autocontour = False,
    zauto = False
))

fig.add_trace(go.Contourcarpet(
    z = data[2]['z'],
    opacity = 0.300,
    showlegend = True,
    name = "Streamlines",
    autocontour = True,
    ncontours = 50,
    contours = dict(
      coloring = "none"
    ),
    line = dict(
      color = "white",
      width = 1
    )
))

fig.add_trace(go.Contourcarpet(
    z = data[3]['z'],
    showlegend = True,
    name = "Pressure<br>contours",
    autocontour = False,
    line = dict(
        color = "rgba(0, 0, 0, 0.5)",
        smoothing = 1
    ),
    contours = dict(
        size = 0.250,
        start = -4,
        coloring = "none",
        end = 1.000,
        showlines = True
      )
))

fig.add_trace(go.Scatter(
    x = data[4]['x'],
    y = data[4]['y'],
    legendgroup = "g1",
    name = "Surface<br>pressure",
    mode = "lines",
    hoverinfo = "skip",
    line = dict(
      color = "rgba(255, 0, 0, 0.5)",
      width = 1,
      shape = "spline",
      smoothing = 1
    ),
    fill = "toself",
    fillcolor = "rgba(255, 0, 0, 0.2)"
))

fig.add_trace(go.Scatter(
    x = data[5]['x'],
    y = data[5]['y'],
    showlegend = False,
    legendgroup = "g1",
    mode = "lines",
    hoverinfo = "skip",
    line = dict(
      color = "rgba(255, 0, 0, 0.3)",
      width = 1
    )
))

fig.add_trace(go.Scatter(
    x = data[6]['x'],
    y = data[6]['y'],
    showlegend = False,
    legendgroup = "g1",
    name = "cp",
    text = data[6]['text'],
    hoverinfo = "text",
    mode = "lines",
    line = dict(
      color = "rgba(255, 0, 0, 0.2)",
      width = 0
    )
))

fig.update_layout(
    yaxis = dict(
      zeroline = False,
      range = [-1.800,1.800],
      showgrid = False
    ),
    dragmode = "pan",
    height = 700,
    xaxis = dict(
      zeroline = False,
      scaleratio = 1,
      scaleanchor = 'y',
      range = [-3.800,3.800],
      showgrid = False
    ),
    title = "Flow over a Karman-Trefftz airfoil",
    hovermode = "closest",
    margin = dict(
      r = 60,
      b = 40,
      l = 40,
      t = 80
    ),
    width = 900
)

fig.show()
```

### Reference

See https://plot.ly/python/reference/#contourcarpet for more information and chart attribute options!
