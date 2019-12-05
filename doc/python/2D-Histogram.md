---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.0
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
    version: 3.7.5
  plotly:
    description: How to make 2D Histograms in Python with Plotly.
    display_as: statistical
    language: python
    layout: base
    name: 2D Histograms
    order: 6
    page_type: u-guide
    permalink: python/2D-Histogram/
    thumbnail: thumbnail/histogram2d.jpg
---

### 2D Histogram of a Bivariate Normal Distribution ###

```python
import plotly.graph_objects as go

import numpy as np
np.random.seed(1)

x = np.random.randn(500)
y = np.random.randn(500)+1

fig = go.Figure(go.Histogram2d(
        x=x,
        y=y
    ))
fig.show()
```

### 2D Histogram Binning and Styling Options ###

```python
import plotly.graph_objects as go

import numpy as np

x = np.random.randn(500)
y = np.random.randn(500)+1

fig = go.Figure(go.Histogram2d(x=x, y=y, histnorm='probability',
        autobinx=False,
        xbins=dict(start=-3, end=3, size=0.1),
        autobiny=False,
        ybins=dict(start=-2.5, end=4, size=0.1),
        colorscale=[[0, 'rgb(12,51,131)'], [0.25, 'rgb(10,136,186)'], [0.5, 'rgb(242,211,56)'], [0.75, 'rgb(242,143,56)'], [1, 'rgb(217,30,30)']]
    ))
fig.show()
```
### Sharing bin settings between 2D Histograms
This example shows how to use [bingroup](https://plot.ly/python/reference/#histogram-bingroup) attribute to have a compatible bin settings for both histograms. To define `start`, `end` and `size` value of x-axis and y-axis seperatly, set [ybins](https://plot.ly/python/reference/#histogram2dcontour-ybins) and `xbins`.

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(2,2)
fig.add_trace(go.Histogram2d(
    x = [ 1, 2, 2, 3, 4 ],
    y = [ 1, 2, 2, 3, 4 ],
    coloraxis = "coloraxis",
    xbins = {'start':1, 'size':1}), 1,1)
fig.add_trace(go.Histogram2d(
    x = [ 4, 5, 5, 5, 6 ],
    y = [ 4, 5, 5, 5, 6 ],
    coloraxis = "coloraxis",
    ybins = {'start': 3, 'size': 1}),1,2)
fig.add_trace(go.Histogram2d(
    x = [ 1, 2, 2, 3, 4 ],
    y = [ 1, 2, 2, 3, 4 ],
    bingroup = 1,
    coloraxis = "coloraxis",
    xbins = {'start':1, 'size':1}), 2,1)
fig.add_trace(go.Histogram2d(
    x = [ 4, 5, 5, 5, 6 ],
    y = [ 4, 5, 5, 5, 6 ],
    bingroup = 1,
    coloraxis = "coloraxis",
    ybins = {'start': 3, 'size': 1}),2,2)
fig.show()
```

### 2D Histogram Overlaid with a Scatter Chart ###

```python
import plotly.graph_objects as go

import numpy as np

x0 = np.random.randn(100)/5. + 0.5  # 5. enforces float division
y0 = np.random.randn(100)/5. + 0.5
x1 = np.random.rand(50)
y1 = np.random.rand(50) + 1.0

x = np.concatenate([x0, x1])
y = np.concatenate([y0, y1])

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x0,
    y=y0,
    mode='markers',
    showlegend=False,
    marker=dict(
        symbol='x',
        opacity=0.7,
        color='white',
        size=8,
        line=dict(width=1),
    )
))
fig.add_trace(go.Scatter(
    x=x1,
    y=y1,
    mode='markers',
    showlegend=False,
    marker=dict(
        symbol='circle',
        opacity=0.7,
        color='white',
        size=8,
        line=dict(width=1),
    )
))
fig.add_trace(go.Histogram2d(
    x=x,
    y=y,
    colorscale='YlGnBu',
    zmax=10,
    nbinsx=14,
    nbinsy=14,
    zauto=False,
))

fig.update_layout(
    xaxis=dict( ticks='', showgrid=False, zeroline=False, nticks=20 ),
    yaxis=dict( ticks='', showgrid=False, zeroline=False, nticks=20 ),
    autosize=False,
    height=550,
    width=550,
    hovermode='closest',

)

fig.show()
```

#### Reference
See https://plot.ly/python/reference/#histogram2d for more information and chart attribute options!
