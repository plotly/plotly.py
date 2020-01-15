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
    description: How to format axes of 3d plots in Python with Plotly.
    display_as: 3d_charts
    language: python
    layout: base
    name: 3D Axes
    order: 1
    page_type: example_index
    permalink: python/3d-axes/
    thumbnail: thumbnail/3d-axes.png
---

### Range of axes

3D figures have an attribute in `layout` called `scene`, which contains
attributes such as `xaxis`, `yaxis` and `zaxis` parameters, in order to
set the range, title, ticks, color etc. of the axes.

For creating 3D charts, see [this page](https://plot.ly/python/3d-charts/).

```python
import plotly.graph_objects as go
import numpy as np
np.random.seed(1)

N = 70

fig = go.Figure(data=[go.Mesh3d(x=(70*np.random.randn(N)),
                   y=(55*np.random.randn(N)),
                   z=(40*np.random.randn(N)),
                   opacity=0.5,
                   color='rgba(244,22,100,0.6)'
                  )])

fig.update_layout(
    scene = dict(
        xaxis = dict(nticks=4, range=[-100,100],),
                     yaxis = dict(nticks=4, range=[-50,100],),
                     zaxis = dict(nticks=4, range=[-100,100],),),
    width=700,
    margin=dict(r=20, l=10, b=10, t=10))

fig.show()
```

### Fixed Ratio Axes

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

N = 50

fig = make_subplots(rows=2, cols=2,
                    specs=[[{'is_3d': True}, {'is_3d': True}],
                           [{'is_3d': True}, {'is_3d': True}]],
                    print_grid=False)
for i in [1,2]:
    for j in [1,2]:
        fig.append_trace(
            go.Mesh3d(
                x=(60*np.random.randn(N)),
                y=(25*np.random.randn(N)),
                z=(40*np.random.randn(N)),
                opacity=0.5,
              ),
            row=i, col=j)

fig.update_layout(width=700, margin=dict(r=10, l=10, b=10, t=10))
# fix the ratio in the top left subplot to be a cube
fig.update_layout(scene_aspectmode='cube')
# manually force the z-axis to appear twice as big as the other two
fig.update_layout(scene2_aspectmode='manual',
                  scene2_aspectratio=dict(x=1, y=1, z=2))
# draw axes in proportion to the proportion of their ranges
fig.update_layout(scene3_aspectmode='data')
# automatically produce something that is well proportioned using 'data' as the default
fig.update_layout(scene4_aspectmode='auto')
fig.show()
```

### Set Axes Title

```python
import plotly.graph_objects as go
import numpy as np

# Define random surface
N = 50
fig = go.Figure()
fig.add_trace(go.Mesh3d(x=(60*np.random.randn(N)),
                   y=(25*np.random.randn(N)),
                   z=(40*np.random.randn(N)),
                   opacity=0.5,
                   color='yellow'
                  ))
fig.add_trace(go.Mesh3d(x=(70*np.random.randn(N)),
                   y=(55*np.random.randn(N)),
                   z=(30*np.random.randn(N)),
                   opacity=0.5,
                   color='pink'
                  ))

fig.update_layout(scene = dict(
                    xaxis_title='X AXIS TITLE',
                    yaxis_title='Y AXIS TITLE',
                    zaxis_title='Z AXIS TITLE'),
                    width=700,
                    margin=dict(r=20, b=10, l=10, t=10))

fig.show()
```

### Ticks Formatting

```python
import plotly.graph_objects as go
import numpy as np

# Define random surface
N = 50
fig = go.Figure(data=[go.Mesh3d(x=(60*np.random.randn(N)),
                   y=(25*np.random.randn(N)),
                   z=(40*np.random.randn(N)),
                   opacity=0.5,
                   color='rgba(100,22,200,0.5)'
                  )])

# Different types of customized ticks
fig.update_layout(scene = dict(
                    xaxis = dict(
                        ticktext= ['TICKS','MESH','PLOTLY','PYTHON'],
                        tickvals= [0,50,75,-50]),
                    yaxis = dict(
                        nticks=5, tickfont=dict(
                            color='green',
                            size=12,
                            family='Old Standard TT, serif',),
                        ticksuffix='#'),
                    zaxis = dict(
                        nticks=4, ticks='outside',
                        tick0=0, tickwidth=4),),
                    width=700,
                    margin=dict(r=10, l=10, b=10, t=10)
                  )

fig.show()
```

### Background and Grid Color

```python
import plotly.graph_objects as go
import numpy as np

N = 50
fig = go.Figure(data=[go.Mesh3d(x=(30*np.random.randn(N)),
                   y=(25*np.random.randn(N)),
                   z=(30*np.random.randn(N)),
                   opacity=0.5,)])


# xaxis.backgroundcolor is used to set background color
fig.update_layout(scene = dict(
                    xaxis = dict(
                         backgroundcolor="rgb(200, 200, 230)",
                         gridcolor="white",
                         showbackground=True,
                         zerolinecolor="white",),
                    yaxis = dict(
                        backgroundcolor="rgb(230, 200,230)",
                        gridcolor="white",
                        showbackground=True,
                        zerolinecolor="white"),
                    zaxis = dict(
                        backgroundcolor="rgb(230, 230,200)",
                        gridcolor="white",
                        showbackground=True,
                        zerolinecolor="white",),),
                    width=700,
                    margin=dict(
                    r=10, l=10,
                    b=10, t=10)
                  )
fig.show()
```

### Disabling tooltip spikes

By default, guidelines originating from the tooltip point are drawn. It is possible to disable this behaviour with the `showspikes` parameter. In this example we only keep the `z` spikes (projection of the tooltip on the `x-y` plane). Hover on the data to show this behaviour.

```python
import plotly.graph_objects as go
import numpy as np

N = 50
fig = go.Figure(data=[go.Mesh3d(x=(30*np.random.randn(N)),
                   y=(25*np.random.randn(N)),
                   z=(30*np.random.randn(N)),
                   opacity=0.5,)])
fig.update_layout(scene=dict(xaxis_showspikes=False,
                             yaxis_showspikes=False))
fig.show()
```

```python

```
