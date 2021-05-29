---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.1
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
    description: How to make 2D Histograms in Python with Plotly.
    display_as: statistical
    language: python
    layout: base
    name: 2D Histograms
    order: 5
    page_type: u-guide
    permalink: python/2D-Histogram/
    redirect_from:
    - python/2d-histogram/
    - python/2d-histograms/
    thumbnail: thumbnail/histogram2d.jpg
---

## 2D Histograms or Density Heatmaps

A 2D histogram, also known as a density heatmap, is the 2-dimensional generalization of a [histogram](/python/histograms/) which resembles a [heatmap](/python/heatmaps/) but is computed by grouping a set of points specified by their `x` and `y` coordinates into bins, and applying an aggregation function such as `count` or `sum` (if `z` is provided) to compute the color of the tile representing the bin. This kind of visualization (and the related [2D histogram contour, or density contour](https://plotly.com/python/2d-histogram-contour/)) is often used to manage over-plotting, or situations where showing large data sets as [scatter plots](/python/line-and-scatter/) would result in points overlapping each other and hiding patterns. For data sets of more than a few thousand points, a better approach than the ones listed here would be to [use Plotly with Datashader](/python/datashader/) to precompute the aggregations before displaying the data with Plotly.

## Density Heatmaps with Plotly Express

[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/). The Plotly Express function `density_heatmap()` can be used to produce density heatmaps.

```python
import plotly.express as px
df = px.data.tips()

fig = px.density_heatmap(df, x="total_bill", y="tip")
fig.show()
```

The number of bins can be controlled with `nbinsx` and `nbinsy` and the [color scale](/python/colorscales/) with `color_continuous_scale`.

```python
import plotly.express as px
df = px.data.tips()

fig = px.density_heatmap(df, x="total_bill", y="tip", nbinsx=20, nbinsy=20, color_continuous_scale="Viridis")
fig.show()
```

Marginal plots can be added to visualize the 1-dimensional distributions of the two variables. Here we use a marginal [`histogram`](/python/histograms/). Other allowable values are `violin`, `box` and `rug`.

```python
import plotly.express as px
df = px.data.tips()

fig = px.density_heatmap(df, x="total_bill", y="tip", marginal_x="histogram", marginal_y="histogram")
fig.show()
```

Density heatmaps can also be [faceted](/python/facet-plots/):

```python
import plotly.express as px
df = px.data.tips()

fig = px.density_heatmap(df, x="total_bill", y="tip", facet_row="sex", facet_col="smoker")
fig.show()
```

### Other aggregation functions than `count`

By passing in a `z` value and a `histfunc`, density heatmaps can perform basic aggregation operations. Here we show average Sepal Length grouped by Petal Length and Petal Width for the Iris dataset.

```python
import plotly.express as px
df = px.data.iris()

fig = px.density_heatmap(df, x="petal_length", y="petal_width", z="sepal_length", histfunc="avg")
fig.show()
```

### 2D Histograms with Graph Objects

To build this kind of figure using [graph objects](/python/graph-objects/) without using Plotly Express, we can use the `go.Histogram2d` class.


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
This example shows how to use [bingroup](https://plotly.com/python/reference/histogram/#histogram-bingroup) attribute to have a compatible bin settings for both histograms. To define `start`, `end` and `size` value of x-axis and y-axis separately, set [ybins](https://plotly.com/python/reference/histogram2dcontour/#histogram2dcontour-ybins) and `xbins`.

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
See https://plotly.com/python/reference/histogram2d/ for more information and chart attribute options!
