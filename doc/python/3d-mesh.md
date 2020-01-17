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
    version: 3.7.3
  plotly:
    description: How to make 3D Mesh Plots
    display_as: 3d_charts
    language: python
    layout: base
    name: 3D Mesh Plots
    order: 10
    page_type: u-guide
    permalink: python/3d-mesh/
    thumbnail: thumbnail/3d-mesh.jpg
---

### Simple 3D Mesh example ###

`go.Mesh3d` draws a 3D set of triangles with vertices given by `x`, `y` and `z`. If only coordinates are given, an algorithm such as [Delaunay triangulation](https://en.wikipedia.org/wiki/Delaunay_triangulation) is used to draw the triangles. Otherwise the triangles can be given using the `i`, `j` and `k` parameters (see examples below).

```python
import plotly.graph_objects as go
import numpy as np

# Download data set from plotly repo
pts = np.loadtxt(np.DataSource().open('https://raw.githubusercontent.com/plotly/datasets/master/mesh_dataset.txt'))
x, y, z = pts.T

fig = go.Figure(data=[go.Mesh3d(x=x, y=y, z=z, color='lightpink', opacity=0.50)])
fig.show()
```

### 3D Mesh example with Alphahull


The `alphahull` parameter sets the shape of the mesh. If the value is -1 (default value) then [Delaunay triangulation](https://en.wikipedia.org/wiki/Delaunay_triangulation) is used. If >0 then the [alpha-shape algorithm](https://en.wikipedia.org/wiki/Alpha_shape) is used. If 0, the [convex hull](https://en.wikipedia.org/wiki/Convex_hull) is represented (resulting in a convex body).

```python
import plotly.graph_objects as go
import numpy as np

pts = np.loadtxt(np.DataSource().open('https://raw.githubusercontent.com/plotly/datasets/master/mesh_dataset.txt'))
x, y, z = pts.T

fig = go.Figure(data=[go.Mesh3d(x=x, y=y, z=z,
                   alphahull=5,
                   opacity=0.4,
                   color='cyan')])
fig.show()
```

### Mesh Tetrahedron

In this example we use the `ì`, `j` and `k` parameters to specify manually the geometry of the triangles of the mesh.

```python
import plotly.graph_objects as go

fig = go.Figure(data=[
    go.Mesh3d(
        x=[0, 1, 2, 0],
        y=[0, 0, 1, 2],
        z=[0, 2, 0, 1],
        colorbar_title='z',
        colorscale=[[0, 'gold'],
                    [0.5, 'mediumturquoise'],
                    [1, 'magenta']],
        # Intensity of each vertex, which will be interpolated and color-coded
        intensity=[0, 0.33, 0.66, 1],
        # i, j and k give the vertices of triangles
        # here we represent the 4 triangles of the tetrahedron surface
        i=[0, 0, 0, 1],
        j=[1, 2, 3, 2],
        k=[2, 3, 1, 3],
        name='y',
        showscale=True
    )
])

fig.show()
```

### Mesh Cube

```python
import plotly.graph_objects as go
import numpy as np

fig = go.Figure(data=[
    go.Mesh3d(
        # 8 vertices of a cube
        x=[0, 0, 1, 1, 0, 0, 1, 1],
        y=[0, 1, 1, 0, 0, 1, 1, 0],
        z=[0, 0, 0, 0, 1, 1, 1, 1],
        colorbar_title='z',
        colorscale=[[0, 'gold'],
                    [0.5, 'mediumturquoise'],
                    [1, 'magenta']],
        # Intensity of each vertex, which will be interpolated and color-coded
        intensity = np.linspace(0, 1, 8, endpoint=True),
        # i, j and k give the vertices of triangles
        i = [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
        j = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
        k = [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
        name='y',
        showscale=True
    )
])

fig.show()
```

### Intensity values defined on vertices or cells

The `intensitymode` attribute of `go.Mesh3d` can be set to `vertex` (default mode, in which case intensity values are interpolated between values defined on vertices), or to `cell` (value of the whole cell, no interpolation). Note that the `intensity` parameter should have the same length as the number of vertices or cells, depending on the `intensitymode`.  

Whereas the previous example used the default `intensitymode='vertex'`, we plot here the same mesh with `intensitymode='cell'`.

```python
import plotly.graph_objects as go
fig = go.Figure(data=[
    go.Mesh3d(
        # 8 vertices of a cube
        x=[0, 0, 1, 1, 0, 0, 1, 1],
        y=[0, 1, 1, 0, 0, 1, 1, 0],
        z=[0, 0, 0, 0, 1, 1, 1, 1],
        colorbar_title='z',
        colorscale=[[0, 'gold'],
                    [0.5, 'mediumturquoise'],
                    [1, 'magenta']],
        # Intensity of each vertex, which will be interpolated and color-coded
        intensity = np.linspace(0, 1, 12, endpoint=True),
        intensitymode='cell',
        # i, j and k give the vertices of triangles
        i = [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
        j = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
        k = [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
        name='y',
        showscale=True
    )
])

fig.show()
```

## Reference
See https://plot.ly/python/reference/#mesh3d for more information and chart attribute options!
