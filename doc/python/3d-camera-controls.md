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
    description: How to Control the Camera in your 3D Charts in Python with Plotly.
    display_as: 3d_charts
    language: python
    layout: base
    name: 3D Camera Controls
    order: 6
    permalink: python/3d-camera-controls/
    thumbnail: thumbnail/3d-camera-controls.jpg
---

### How camera controls work

The camera position and direction is determined by three vectors: *up*, *center*, *eye*. Their coordinates refer to the 3-d domain, i.e., `(0, 0, 0)` is always the center of the domain, no matter data values.
The `eye` vector determines the position of the camera. The default is $(x=1.25, y=1.25, z=1.25)$.

The `up` vector determines the `up` direction on the page. The default is $(x=0, y=0, z=1)$, that is, the z-axis points up.

The projection of the `center` point lies at the center of the view. By default it is $(x=0, y=0, z=0)$.


### Default parameters

```python
import plotly.graph_objects as go
import pandas as pd

# Read data from a csv
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

fig = go.Figure(data=go.Surface(z=z_data, showscale=False))
fig.update_layout(
    title='Mt Bruno Elevation',
    width=400, height=400,
    margin=dict(t=40, r=0, l=20, b=20)
)

name = 'default'
# Default parameters which are used when `layout.scene.camera` is not provided
camera = dict(
    up=dict(x=0, y=0, z=1),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=1.25, y=1.25, z=1.25)
)

fig.update_layout(scene_camera=camera, title=name)
fig.show()
```

### Changing the camera position by setting the eye parameter

#### Lower the View Point

by setting `eye.z` to a smaller value.

```python
import plotly.graph_objects as go
import pandas as pd

# Read data from a csv
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

fig = go.Figure(data=go.Surface(z=z_data, showscale=False))
fig.update_layout(
    title='Mt Bruno Elevation',
    width=400, height=400,
    margin=dict(t=30, r=0, l=20, b=10)
)

name = 'eye = (x:2, y:2, z:0.1)'
camera = dict(
    eye=dict(x=2, y=2, z=0.1)
)

fig.update_layout(scene_camera=camera, title=name)
fig.show()
```

#### X-Z plane

set `eye.x` and `eye.z` to zero

```python
import plotly.graph_objects as go
import pandas as pd

# Read data from a csv
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

fig = go.Figure(data=go.Surface(z=z_data, showscale=False))
fig.update_layout(
    title='Mt Bruno Elevation',
    width=400, height=400,
    margin=dict(t=30, r=0, l=20, b=10)
)

name = 'eye = (x:0., y:2.5, z:0.)'
camera = dict(
    eye=dict(x=0., y=2.5, z=0.)
)


fig.update_layout(scene_camera=camera, title=name)
fig.show()
```

#### Y-Z plane

```python
import plotly.graph_objects as go
import pandas as pd

# Read data from a csv
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

fig = go.Figure(data=go.Surface(z=z_data, showscale=False))
fig.update_layout(
    title='Mt Bruno Elevation',
    width=400, height=400,
    margin=dict(t=30, r=0, l=20, b=10)
)

name = 'eye = (x:2.5, y:0., z:0.)'
camera = dict(
    eye=dict(x=2.5, y=0., z=0.)
)

fig.update_layout(scene_camera=camera, title=name)
fig.show()
```

#### View from Above (X-Y plane)

```python
import plotly.graph_objects as go
import pandas as pd

# Read data from a csv
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

fig = go.Figure(data=go.Surface(z=z_data, showscale=False))
fig.update_layout(
    title='Mt Bruno Elevation',
    width=400, height=400,
    margin=dict(t=30, r=0, l=20, b=10)
)

name = 'eye = (x:0., y:0., z:2.5)'
camera = dict(
    eye=dict(x=0., y=0., z=2.5)
)

fig.update_layout(scene_camera=camera, title=name)
fig.show()
```

#### Zooming In
... by placing the camera closer to the origin (`eye` with a smaller norm)

```python
import plotly.graph_objects as go
import pandas as pd

# Read data from a csv
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

fig = go.Figure(data=go.Surface(z=z_data, showscale=False))
fig.update_layout(
    title='Mt Bruno Elevation',
    width=400, height=400,
    margin=dict(t=30, r=0, l=20, b=10)
)

name = 'eye = (x:0.1, y:0.1, z:1.5)'
camera = dict(
    eye=dict(x=0.1, y=0.1, z=1.5)
)

fig.update_layout(scene_camera=camera, title=name)
fig.show()
```

### Tilting the camera vertical by setting the up parameter

Tilt camera by changing the `up` vector: here the vertical of the view points in the `x` direction.

```python
import plotly.graph_objects as go
import pandas as pd

# Read data from a csv
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

fig = go.Figure(data=go.Surface(z=z_data, showscale=False))
fig.update_layout(
    title='Mt Bruno Elevation',
    width=400, height=400,
    margin=dict(t=30, r=0, l=20, b=10)
)

name = 'eye = (x:0., y:2.5, z:0.), point along x'
camera = dict(
    up=dict(x=1, y=0., z=0),
    eye=dict(x=0., y=2.5, z=0.)
)

fig.update_layout(scene_camera=camera, title=name)
fig.show()
```

Note when `up` does not correspond to the direction of an axis, you also need to set `layout.scene.dragmode='orbit'`.

```python
import math
import plotly.graph_objects as go
import pandas as pd

# Read data from a csv
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

fig = go.Figure(data=go.Surface(z=z_data, showscale=False))
fig.update_layout(
    title='Mt Bruno Elevation',
    width=400, height=400,
    margin=dict(t=30, r=0, l=20, b=10)
)

angle = math.pi / 4 # 45 degrees

name = 'vertical is along y+z'
camera = dict(
    up=dict(x=0, y=math.cos(angle), z=math.sin(angle)),
    eye=dict(x=2, y=0, z=0)
)

fig.update_layout(scene_camera=camera, scene_dragmode='orbit', title=name)
fig.show()
```

### Changing the focal point by setting center

You can change the focal point (a point which projection lies at the center of the view) by setting the `center` parameter of `camera`. Note how a part of the data is cropped below because the camera is looking up.

```python
import plotly.graph_objects as go
import pandas as pd

# Read data from a csv
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

fig = go.Figure(data=go.Surface(z=z_data, showscale=False))
fig.update_layout(
    title='Mt Bruno Elevation',
    width=400, height=400,
    margin=dict(t=25, r=0, l=20, b=30)
)

name = 'looking up'
camera = dict(
    center=dict(x=0, y=0, z=0.7))


fig.update_layout(scene_camera=camera, title=name)
fig.show()
```

#### Reference


See https://plot.ly/python/reference/#layout-scene-camera for more information and chart attribute options!
