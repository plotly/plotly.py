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
    description: How to make a streamline plot in Python. A streamline plot displays
      vector field data.
    display_as: scientific
    language: python
    layout: base
    name: Streamline Plots
    order: 12
    permalink: python/streamline-plots/
    thumbnail: thumbnail/streamline.jpg
---

A Streamline plot is a representation based on a 2-D vector field interpreted as a velocity field, consisting of closed curves tangent to the velocity field. In the case of a stationary velocity field, streamlines coincide with trajectories (see also the [Wikipedia page on streamlines, streaklines and pathlines](https://en.wikipedia.org/wiki/Streamlines,_streaklines,_and_pathlines)).

For the streamline figure factory, one needs to provide
- uniformly spaced ranges of `x` and `y` values (1D)
- 2-D velocity values `u` and `v` defined on the cross-product (`np.meshgrid(x, y)`) of `x` and `y`.

Velocity values are interpolated when determining the streamlines. Streamlines are initialized on the boundary of the `x-y` domain.

#### Basic Streamline Plot

```python
import plotly.figure_factory as ff

import numpy as np

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
Y, X = np.meshgrid(x, y)
u = -1 - X**2 + Y
v = 1 + X - Y**2

# Create streamline figure
fig = ff.create_streamline(x, y, u, v, arrow_scale=.1)
fig.show()
```

#### Streamline and Source Point Plot

```python
import plotly.figure_factory as ff
import plotly.graph_objects as go

import numpy as np

N = 50
x_start, x_end = -2.0, 2.0
y_start, y_end = -1.0, 1.0
x = np.linspace(x_start, x_end, N)
y = np.linspace(y_start, y_end, N)
X, Y = np.meshgrid(x, y)
source_strength = 5.0
x_source, y_source = -1.0, 0.0

# Compute the velocity field on the mesh grid
u = (source_strength/(2*np.pi) *
     (X - x_source)/((X - x_source)**2 + (Y - y_source)**2))
v = (source_strength/(2*np.pi) *
     (Y - y_source)/((X - x_source)**2 + (Y - y_source)**2))

# Create streamline figure
fig = ff.create_streamline(x, y, u, v,
                           name='streamline')

# Add source point
fig.add_trace(go.Scatter(x=[x_source], y=[y_source],
                          mode='markers',
                          marker_size=14,
                          name='source point'))

fig.show()
```

#### See also

For a 3D version of streamlines, use the trace `go.Streamtube` documented [here](/python/streamtube-plot/).

For representing the 2-D vector field as arrows, see the [quiver plot tutorial](/python/quiver-plots/).


#### Reference

```python
help(ff.create_streamline)
```
