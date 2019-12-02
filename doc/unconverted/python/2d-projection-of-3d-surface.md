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
    description: How to project 3D Surface plots in 2D with Plotly.
    display_as: 3d_charts
    language: python
    layout: base
    name: Projection of 3D Surface
    order: 19
    page_type: u-guide
    permalink: python/2d-projection-of-3d-surface/
    thumbnail: thumbnail/projection-3d.jpg
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!



#### Projections of a 3d surface onto planes


This example will demonstrate how to create heatmaps of projections of a 3d surface onto planes perpendicular to the z, x, respectively y-direction. Usually surfaces in the 3d space are colored with  a colormap associated to the normalized range of the z coordinates of points on that surface.
Recently, Plotly devised a method to color a surface according to a custom color function.

Namely, if $x, y, z$ are numpy arrays of shape (m, n), defined by a discretization (via a meshgrid) of a surface z=f(x,y) or in parametric form, $x=x(u,v), y=y(u,v), z=z(u,v)$, then a custom function, `Color(x,y,z)`, returns a numpy array `C`, of the same shape as z, and the surface is colored by a colormap, according to the values in `C`.


This method allows to project a surface onto planes perpendicular to the z, x or y-direction in the 3d space
and interpret the projection as a planar surface colored according to the z, x or y value at each point
of the coresponding plane.

First, define the surface and its discretization:

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

xx=np.linspace(-3.5, 3.5, 100)
yy=np.linspace(-3.5, 3.5, 100)
x,y=np.meshgrid(xx, yy)
z=np.exp(-(x-1)**2-y**2)-10*(x**3+y**4-x/5)*np.exp(-(x**2+y**2))
```

#### Color according to normalized z-values

```python
colorscale=[[0.0, 'rgb(20,29,67)'],
           [0.1, 'rgb(28,76,96)'],
           [0.2, 'rgb(16,125,121)'],
           [0.3, 'rgb(92,166,133)'],
           [0.4, 'rgb(182,202,175)'],
           [0.5, 'rgb(253,245,243)'],
           [0.6, 'rgb(230,183,162)'],
           [0.7, 'rgb(211,118,105)'],
           [0.8, 'rgb(174,63,95)'],
           [0.9, 'rgb(116,25,93)'],
           [1.0, 'rgb(51,13,53)']]
```

#### Add hover text for the surface:

```python
textz = [['x: '+'{:0.5f}'.format(x[i][j])+'<br>y: '+'{:0.5f}'.format(y[i][j])+
        '<br>z: '+'{:0.5f}'.format(z[i][j]) for j in range(z.shape[1])] for i in range(z.shape[0])]

trace1= go.Surface(
    x=tuple(x),
    y=tuple(y),
    z=tuple(z),
    colorscale=colorscale,
    text=textz,
    hoverinfo='text',
)
```

#### Set Plot Layout:

```python
axis = dict(
showbackground=True,
backgroundcolor="rgb(230, 230,230)",
showgrid=False,
zeroline=False,
showline=False)

ztickvals=list(range(-6,4))
layout = go.Layout(title="Projections of a surface onto coordinate planes" ,
                autosize=False,
                width=700,
                height=600,
                scene=dict(xaxis=dict(axis, range=[-3.5, 3.5]),
                            yaxis=dict(axis, range=[-3.5, 3.5]),
                            zaxis=dict(axis , tickvals=ztickvals),
                            aspectratio=dict(x=1,
                                             y=1,
                                             z=0.95)
                           )
                )
```

#### Discretization of each Plane
The surface projections will be plotted in the planes of equations
`Z=np.min(z)-2`, `X=np.min(xx)`, respectively `Y=np.min(yy)`.

```python
z_offset=(np.min(z)-2)*np.ones(z.shape)#
x_offset=np.min(xx)*np.ones(z.shape)
y_offset=np.min(yy)*np.ones(z.shape)
```

Define the color functions and the color numpy arrays, `C_z`, `C_x`, `C_y`, corresponding to each plane:<br>
Define the 3-tuples of coordinates to be displayed at hovering the mouse over the projections.
The first two coordinates give the position in the projection plane, whereas the third one  is used
for assigning the color, just in the same way the coordinate z is used for the z-direction projection.

```python
proj_z=lambda x, y, z: z#projection in the z-direction
colorsurfz=proj_z(x,y,z)
proj_x=lambda x, y, z: x
colorsurfx=proj_z(x,y,z)
proj_y=lambda x, y, z: y
colorsurfy=proj_z(x,y,z)

textx=[['y: '+'{:0.5f}'.format(y[i][j])+'<br>z: '+'{:0.5f}'.format(z[i][j])+
        '<br>x: '+'{:0.5f}'.format(x[i][j]) for j in range(z.shape[1])]  for i in range(z.shape[0])]
texty=[['x: '+'{:0.5f}'.format(x[i][j])+'<br>z: '+'{:0.5f}'.format(z[i][j]) +
        '<br>y: '+'{:0.5f}'.format(y[i][j]) for j in range(z.shape[1])] for i in range(z.shape[0])]

tracex = go.Surface(z=list(z),
                x=list(x_offset),
                y=list(y),
                colorscale=colorscale,
                showlegend=False,
                showscale=False,
                surfacecolor=colorsurfx,
                text=textx,
                hoverinfo='text'
               )
tracey = go.Surface(z=list(z),
                x=list(x),
                y=list(y_offset),
                colorscale=colorscale,
                showlegend=False,
                showscale=False,
                surfacecolor=colorsurfy,
                text=texty,
                hoverinfo='text'
               )
tracez = go.Surface(z=list(z_offset),
                x=list(x),
                y=list(y),
                colorscale=colorscale,
                showlegend=False,
                showscale=False,
                surfacecolor=colorsurfx,
                text=textz,
                hoverinfo='text'
               )

data=[trace1, tracex, tracey, tracez]
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/csshref="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade

import publisher
publisher.publish(
    'Plotly-project-3d-onto-a-plane.ipynb', 'python/2d-projection-of-3d-surface/', 'Projection of 3D Surface',
    'How to project 3D Surface plots in 2D with Plotly.',
    title = '2D Projection of 3D surface | plotly',
    has_thumbnail='true', thumbnail='thumbnail/projection-3d.jpg',
    language='python',
    display_as='3d_charts', order=19,
    ipynb= '~notebook_demo/79')
```

```python

```
