---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.1
  kernelspec:
    display_name: Python 2
    language: python
    name: python2
  plotly:
    description: How to make wireframe plots in Python
    display_as: 3d_charts
    language: python
    layout: base
    name: 3D Wireframe Plots
    order: 8
    permalink: python/3d-wireframe-plots/
    thumbnail: thumbnail/wireframe.jpg
---

<!-- #region {"deletable": true, "editable": true} -->
#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!
<!-- #endregion -->

<!-- #region {"deletable": true, "editable": true} -->
#### Basic Wireframe Plot
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

# Creating the data
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
xGrid, yGrid = np.meshgrid(y, x)
R = np.sqrt(xGrid ** 2 + yGrid ** 2)
z = np.sin(R)

# Creating the plot
lines = []
line_marker = dict(color='#0066FF', width=2)
for i, j, k in zip(xGrid, yGrid, z):
    lines.append(go.Scatter3d(x=i, y=j, z=k, mode='lines', line=line_marker))

layout = go.Layout(
    title='Wireframe Plot',
    scene=dict(
        xaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        yaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        zaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        )
    ),
    showlegend=False,
)
fig = go.Figure(data=lines, layout=layout)
py.iplot(fig, filename='wireframe_plot')
```

<!-- #region {"deletable": true, "editable": true} -->
#### Reference
<!-- #endregion -->

<!-- #region {"deletable": true, "editable": true} -->
See https://plot.ly/python/reference/#scatter3d for more information!
<!-- #endregion -->

```python deletable=true editable=true
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade

import publisher
publisher.publish(
    '3d-wireframe.ipynb', 'python/3d-wireframe-plots/', 'Python Wireframe Plots | plotly',
    'How to make wireframe plots in Python',
    title= '3D Wireframe Plots in Python | plotly',
    name = '3D Wireframe Plots',
    has_thumbnail='true', thumbnail='thumbnail/wireframe.jpg',
    language='python',
    display_as='3d_charts', order=8,
    ipynb= '~notebook_demo/68')
```

```python deletable=true editable=true

```
