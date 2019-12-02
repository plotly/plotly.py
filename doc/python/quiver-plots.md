---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.2.3
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
    version: 3.7.3
  plotly:
    description: How to make a quiver plot in Python. A quiver plot displays velocity
      vectors a arrows.
    display_as: scientific
    language: python
    layout: base
    name: Quiver Plots
    order: 11
    permalink: python/quiver-plots/
    thumbnail: thumbnail/quiver-plot.jpg
---

#### Basic Quiver Plot

```python
import plotly.figure_factory as ff

import numpy as np

x,y = np.meshgrid(np.arange(0, 2, .2), np.arange(0, 2, .2))
u = np.cos(x)*y
v = np.sin(x)*y

fig = ff.create_quiver(x, y, u, v)
fig.show()
```

#### Quiver Plot with Points

```python
import plotly.figure_factory as ff
import plotly.graph_objects as go

import numpy as np

x,y = np.meshgrid(np.arange(-2, 2, .2),
                  np.arange(-2, 2, .25))
z = x*np.exp(-x**2 - y**2)
v, u = np.gradient(z, .2, .2)

# Create quiver figure
fig = ff.create_quiver(x, y, u, v,
                       scale=.25,
                       arrow_scale=.4,
                       name='quiver',
                       line_width=1)

# Add points to figure
fig.add_trace(go.Scatter(x=[-.7, .75], y=[0,0],
                    mode='markers',
                    marker_size=12,
                    name='points'))

fig.show()
```

#### See also

[Cone plot](/python/cone-plot) for the 3D equivalent of quiver plots.

#### Reference

```python
help(ff.create_quiver)
```
