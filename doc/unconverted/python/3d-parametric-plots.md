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
    description: How to 3D Parameteric Plots in Python
    display_as: 3d_charts
    language: python
    layout: base
    name: Parametric Plots
    order: 9
    permalink: python/3d-parametric-plots/
    thumbnail: thumbnail/parametric.jpg
---

<!-- #region {"deletable": true, "editable": true} -->
#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!
<!-- #endregion -->

<!-- #region {"deletable": true, "editable": true} -->
#### Basic Parametric Plot
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

s = np.linspace(0, 2 * np.pi, 240)
t = np.linspace(0, np.pi, 240)
tGrid, sGrid = np.meshgrid(s, t)

r = 2 + np.sin(7 * sGrid + 5 * tGrid)  # r = 2 + sin(7s+5t)
x = r * np.cos(sGrid) * np.sin(tGrid)  # x = r*cos(s)*sin(t)
y = r * np.sin(sGrid) * np.sin(tGrid)  # y = r*sin(s)*sin(t)
z = r * np.cos(tGrid)                  # z = r*cos(t)

surface = go.Surface(x=x, y=y, z=z)
data = [surface]

layout = go.Layout(
    title='Parametric Plot',
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
    )
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='Parametric_plot')
```

<!-- #region {"deletable": true, "editable": true} -->
#### Parameteric Plot with Colorscale
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

dphi, dtheta = np.pi / 250.0, np.pi / 250.0
[phi, theta] = np.mgrid[0:np.pi + dphi * 1.5:dphi, 0:2 * np.pi +
                        dtheta * 1.5:dtheta]
m0 = 4; m1 = 3; m2 = 2; m3 = 3; m4 = 6; m5 = 2; m6 = 6; m7 = 4;

# Applying the parametric equation..
r = (np.sin(m0 * phi) ** m1 + np.cos(m2 * phi) ** m3 +
     np.sin(m4 * theta) ** m5 + np.cos(m6 * theta) ** m7)
x = r * np.sin(phi) * np.cos(theta)
y = r * np.cos(phi)
z = r * np.sin(phi) * np.sin(theta)


surface = go.Surface(x=x, y=y, z=z, colorscale='Viridis')
data = [surface]
layout = go.Layout(
    title='Another Parametric Plot',
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
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='parametric-plot-viridis')
```

<!-- #region {"deletable": true, "editable": true} -->
#### Reference
<!-- #endregion -->

<!-- #region {"deletable": true, "editable": true} -->
See https://plot.ly/python/reference/#surface for more information!
<!-- #endregion -->

```python deletable=true editable=true
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade

import publisher
publisher.publish(
    '3d-parametric.ipynb', 'python/3d-parametric-plots/', '3D Parametric Plots | plotly',
    'How to 3D Parameteric Plots in Python',
    title= '3D Parametric Plots in Python | plotly',
    name = 'Parametric Plots',
    has_thumbnail='true', thumbnail='thumbnail/parametric.jpg',
    language='python',
    display_as='3d_charts', order=9,
    ipynb= '~notebook_demo/69')
```

```python deletable=true editable=true

```
