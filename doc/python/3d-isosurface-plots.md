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
    description: How to make 3D Isosurface Plots in Python with Plotly.
    display_as: 3d_charts
    language: python
    layout: base
    name: 3D Isosurface Plots
    order: 11
    page_type: u-guide
    permalink: python/3d-isosurface-plots/
    redirect_from: python/isosurfaces-with-marching-cubes/
    thumbnail: thumbnail/isosurface.jpg
---

With ``go.Isosurface``, you can plot [isosurface contours](https://en.wikipedia.org/wiki/Isosurface) of a scalar field ``value``, which is defined on ``x``, ``y`` and ``z`` coordinates.

#### Basic Isosurface

In this first example, we plot the isocontours of values ``isomin=2`` and ``isomax=6``. In addition, portions of the sides of the coordinate domains for which the value is between ``isomin`` and ``isomax`` (named the ``caps``) are colored. Please rotate the figure to visualize both the internal surfaces and the caps surfaces on the sides.

```python
import plotly.graph_objects as go

fig= go.Figure(data=go.Isosurface(
    x=[0,0,0,0,1,1,1,1],
    y=[1,0,1,0,1,0,1,0],
    z=[1,1,0,0,1,1,0,0],
    value=[1,2,3,4,5,6,7,8],
    isomin=2,
    isomax=6,
))

fig.show()
```

### Removing caps when visualizing isosurfaces

For a clearer visualization of internal surfaces, it is possible to remove the caps (color-coded surfaces on the sides of the visualization domain). Caps are visible by default.

```python
import plotly.graph_objects as go
import numpy as np

X, Y, Z = np.mgrid[-5:5:40j, -5:5:40j, -5:5:40j]

# ellipsoid
values = X * X * 0.5 + Y * Y + Z * Z * 2

fig = go.Figure(data=go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=values.flatten(),
    isomin=10,
    isomax=40,
    caps=dict(x_show=False, y_show=False)
    ))
fig.show()
```

### Modifying the number of isosurfaces

```python
import plotly.graph_objects as go
import numpy as np

X, Y, Z = np.mgrid[-5:5:40j, -5:5:40j, -5:5:40j]

# ellipsoid
values = X * X * 0.5 + Y * Y + Z * Z * 2

fig = go.Figure(data=go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=values.flatten(),
    isomin=10,
    isomax=50,
    surface_count=5, # number of isosurfaces, 2 by default: only min and max
    colorbar_nticks=5, # colorbar ticks correspond to isosurface values
    caps=dict(x_show=False, y_show=False)
    ))
fig.show()
```

### Changing the opacity of isosurfaces

```python
import plotly.graph_objects as go
import numpy as np

X, Y, Z = np.mgrid[-5:5:40j, -5:5:40j, -5:5:40j]

# ellipsoid
values = X * X * 0.5 + Y * Y + Z * Z * 2

fig = go.Figure(data=go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=values.flatten(),
    opacity=0.6,
    isomin=10,
    isomax=50,
    surface_count=3,
    caps=dict(x_show=False, y_show=False)
    ))
fig.show()
```

#### Isosurface with Addtional Slices

Here we visualize slices parallel to the axes on top of isosurfaces. For a clearer visualization, the `fill` ratio of isosurfaces is decreased below 1 (completely filled).

```python
import plotly.graph_objects as go
import numpy as np

X, Y, Z = np.mgrid[-5:5:40j, -5:5:40j, -5:5:40j]

# ellipsoid
values = X * X * 0.5 + Y * Y + Z * Z * 2

fig = go.Figure(data=go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=values.flatten(),
    isomin=5,
    isomax=50,
    surface_fill=0.4,
    caps=dict(x_show=False, y_show=False),
    slices_z=dict(show=True, locations=[-1, -3,]),
    slices_y=dict(show=True, locations=[0]),
    ))
fig.show()
```

#### Multiple Isosurfaces with Caps

```python
import plotly.graph_objects as go
import numpy as np

X, Y, Z = np.mgrid[-5:5:40j, -5:5:40j, 0:5:20j]

values = X * X * 0.5 + Y * Y + Z * Z * 2

fig = go.Figure(data=go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=values.flatten(),
    isomin=30,
    isomax=50,
    surface=dict(count=3, fill=0.7, pattern='odd'),
    caps=dict(x_show=True, y_show=True),
    ))
fig.show()
```

### Changing the default colorscale of isosurfaces

```python
import plotly.graph_objects as go
import numpy as np

X, Y, Z = np.mgrid[-5:5:40j, -5:5:40j, -5:5:40j]

# ellipsoid
values = X * X * 0.5 + Y * Y + Z * Z * 2

fig = go.Figure(data=go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=values.flatten(),
    colorscale='BlueRed',
    isomin=10,
    isomax=50,
    surface_count=3,
    caps=dict(x_show=False, y_show=False)
    ))
fig.show()
```

### Customizing the layout and appearance of isosurface plots

```python
import plotly.graph_objects as go
import numpy as np

X, Y, Z = np.mgrid[-5:5:40j, -5:5:40j, 0:5:20j]

values = X * X * 0.5 + Y * Y + Z * Z * 2

fig = go.Figure(data=go.Isosurface(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    value=values.flatten(),
    isomin=30,
    isomax=50,
    surface=dict(count=3, fill=0.7, pattern='odd'),
    showscale=False, # remove colorbar
    caps=dict(x_show=True, y_show=True),
    ))

fig.update_layout(
    margin=dict(t=0, l=0, b=0), # tight layout
    scene_camera_eye=dict(x=1.86, y=0.61, z=0.98))
fig.show()
```

#### Reference
See https://plot.ly/python/reference/#isosurface for more information and chart attribute options!

