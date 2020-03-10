---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: "1.1"
      jupytext_version: 1.1.1
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
    description: How to make 3D scatter plots in Python with Plotly.
    display_as: 3d_charts
    language: python
    layout: base
    name: 3D Scatter Plots
    order: 2
    page_type: example_index
    permalink: python/3d-scatter-plots/
    thumbnail: thumbnail/3d-scatter.jpg
---

## 3D scatter plot with Plotly Express

[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on "tidy" data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/).

Like the [2D scatter plot](https://plot.ly/python/line-and-scatter/) `px.scatter`, the 3D function `px.scatter_3d` plots individual data in three-dimensional space.

```python
import plotly.express as px
df = px.data.iris()
fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
              color='species')
fig.show()
```

A 4th dimension of the data can be represented thanks to the color of the markers. Also, values from the `species` column are used below to assign symbols to markers.

```python
import plotly.express as px
df = px.data.iris()
fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
                    color='petal_length', symbol='species')
fig.show()
```

#### Style 3d scatter plot

It is possible to customize the style of the figure through the parameters of `px.scatter_3d` for some options, or by updating the traces or the layout of the figure through `fig.update`.

```python
import plotly.express as px
df = px.data.iris()
fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
              color='petal_length', size='petal_length', size_max=18,
              symbol='species', opacity=0.7)

# tight layout
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
```

### 3D Scatter Plot with go.Scatter3d

#### Basic 3D Scatter Plot

If Plotly Express does not provide a good starting point, it is also possible to use the more generic `go.Scatter3D` from `plotly.graph_objs`.
Like the [2D scatter plot](https://plot.ly/python/line-and-scatter/) `go.Scatter`, `go.Scatter3d` plots individual data in three-dimensional space.

```python
import plotly.graph_objects as go
import numpy as np

# Helix equation
t = np.linspace(0, 10, 50)
x, y, z = np.cos(t), np.sin(t), t

fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z,
                                   mode='markers')])
fig.show()
```

#### 3D Scatter Plot with Colorscaling and Marker Styling

```python
import plotly.graph_objects as go
import numpy as np

# Helix equation
t = np.linspace(0, 20, 100)
x, y, z = np.cos(t), np.sin(t), t

fig = go.Figure(data=[go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
        size=12,
        color=z,                # set color to an array/list of desired values
        colorscale='Viridis',   # choose a colorscale
        opacity=0.8
    )
)])

# tight layout
fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
fig.show()
```

### Dash App

[Dash](https://plot.ly/products/dash/) is an Open Source Python library which can help you convert plotly figures into a reactive, web-based application. Below is a simple example of a dashboard created using Dash. Its [source code](https://github.com/plotly/simple-example-chart-apps/tree/master/dash-3dscatterplot) can easily be deployed to a PaaS.

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-3dscatterplot/", width="100%", height="950px",frameBorder="0")
```

```python
from IPython.display import IFrame
IFrame(src= "https://dash-simple-apps.plotly.host/dash-3dscatterplot/code", width="100%", height="500px",frameBorder="0")
```

#### Reference

See https://plot.ly/python/reference/#scatter3d for more information and chart attribute options!
