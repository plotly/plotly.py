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
    description: How to make tri-surf plots in Python with Plotly. Trisurfs are formed
      by replacing the boundaries of a compact surface by touching triangles.
    display_as: 3d_charts
    language: python
    layout: base
    name: Trisurf Plots
    order: 10
    page_type: u-guide
    permalink: python/trisurf/
    thumbnail: thumbnail/tri-surf2.jpg
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Version Check
Note: Trisurfs are available in version <b>1.11.0+</b><br>
Run  `pip install plotly --upgrade` to update your Plotly version

```python
import plotly
plotly.__version__
```

#### Torus

```python
import plotly.plotly as py
import plotly.figure_factory as FF
import plotly.graph_objs as go

import numpy as np
from scipy.spatial import Delaunay

u = np.linspace(0, 2*np.pi, 20)
v = np.linspace(0, 2*np.pi, 20)
u,v = np.meshgrid(u,v)
u = u.flatten()
v = v.flatten()

x = (3 + (np.cos(v)))*np.cos(u)
y = (3 + (np.cos(v)))*np.sin(u)
z = np.sin(v)

points2D = np.vstack([u,v]).T
tri = Delaunay(points2D)
simplices = tri.simplices

fig1 = FF.create_trisurf(x=x, y=y, z=z,
                         simplices=simplices,
                         title="Torus", aspectratio=dict(x=1, y=1, z=0.3))
py.iplot(fig1, filename="3dFolder/Torus")
```

#### Mobius Band

```python
import plotly.plotly as py
import plotly.figure_factory as FF
import plotly.graph_objs as go

import numpy as np
from scipy.spatial import Delaunay

u = np.linspace(0, 2*np.pi, 24)
v = np.linspace(-1, 1, 8)
u,v = np.meshgrid(u,v)
u = u.flatten()
v = v.flatten()

tp = 1 + 0.5*v*np.cos(u/2.)
x = tp*np.cos(u)
y = tp*np.sin(u)
z = 0.5*v*np.sin(u/2.)

points2D = np.vstack([u,v]).T
tri = Delaunay(points2D)
simplices = tri.simplices

fig1 = FF.create_trisurf(x=x, y=y, z=z,
                         colormap="Portland",
                         simplices=simplices,
                         title="Mobius Band")
py.iplot(fig1, filename="Mobius-Band")
```

#### Boy's Surface

```python
import plotly.plotly as py
import plotly.figure_factory as FF
import plotly.graph_objs as go

import numpy as np
from scipy.spatial import Delaunay

u=np.linspace(-np.pi/2, np.pi/2, 60)
v=np.linspace(0, np.pi, 60)
u,v=np.meshgrid(u,v)
u=u.flatten()
v=v.flatten()

x = (np.sqrt(2)*(np.cos(v)*np.cos(v))*np.cos(2*u) + np.cos(u)*np.sin(2*v))/(2 - np.sqrt(2)*np.sin(3*u)*np.sin(2*v))
y = (np.sqrt(2)*(np.cos(v)*np.cos(v))*np.sin(2*u) - np.sin(u)*np.sin(2*v))/(2 - np.sqrt(2)*np.sin(3*u)*np.sin(2*v))
z = (3*(np.cos(v)*np.cos(v)))/(2 - np.sqrt(2)*np.sin(3*u)*np.sin(2*v))

points2D = np.vstack([u, v]).T
tri = Delaunay(points2D)
simplices = tri.simplices

fig1 = FF.create_trisurf(x=x, y=y, z=z,
                         colormap=['rgb(50, 0, 75)', 'rgb(200, 0, 200)', '#c8dcc8'],
                         show_colorbar=True,
                         simplices=simplices,
                         title="Boy's Surface")
py.iplot(fig1, filename="Boy's Surface")
```

#### Change Colorscale Variable

```python
import plotly.plotly as py
import plotly.figure_factory as FF
import plotly.graph_objs as go

import numpy as np
from scipy.spatial import Delaunay

u = np.linspace(0, 2*np.pi, 20)
v = np.linspace(0, 2*np.pi, 20)
u,v = np.meshgrid(u,v)
u = u.flatten()
v = v.flatten()

x = (3 + (np.cos(v)))*np.cos(u)
y = (3 + (np.cos(v)))*np.sin(u)
z = np.sin(v)

points2D = np.vstack([u,v]).T
tri = Delaunay(points2D)
simplices = tri.simplices

# define a function that calculates the distance
# from the origin to use as the color variable
def dist_origin(x, y, z):
    return np.sqrt((1.0 * x)**2 + (1.0 * y)**2 + (1.0 * z)**2)

fig1 = FF.create_trisurf(x=x, y=y, z=z, color_func=dist_origin,
                         colormap = [(0.4, 0.15, 0), (1, 0.65, 0.12)],
                         show_colorbar=True,
                         simplices=simplices, title="Torus - Origin Distance Coloring",
                         aspectratio=dict(x=1, y=1, z=0.3))
py.iplot(fig1, filename="Torus - Origin Distance Coloring")
```

#### Diverging Colormap

```python
import plotly.plotly as py
import plotly.figure_factory as FF
import plotly.graph_objs as go

import numpy as np
from scipy.spatial import Delaunay

u = np.linspace(-np.pi, np.pi, 30)
v = np.linspace(-np.pi, np.pi, 30)
u, v = np.meshgrid(u,v)
u = u.flatten()
v = v.flatten()

x = u
y = u*np.cos(v)
z = u*np.sin(v)

points2D = np.vstack([u,v]).T
tri = Delaunay(points2D)
simplices = tri.simplices

# define a function for the color assignment
def dist_from_x_axis(x, y, z):
    return x

fig1 = FF.create_trisurf(x=x, y=y, z=z,
                         colormap=['rgb(255, 155, 120)', 'rgb(255, 153, 255)', ],
                         show_colorbar=True,
                         simplices=simplices, title="Light Cone",
                         showbackground=False, gridcolor='rgb(255, 20, 160)',
                         plot_edges=False, aspectratio=dict(x=1, y=1, z=0.75))
py.iplot(fig1, filename="Light Cone")
```

#### Reference

```python
help(FF.create_trisurf)
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade

import publisher
publisher.publish(
    'trisurf.ipynb', 'python/trisurf/', 'Trisurf Plots',
    'How to make tri-surf plots in Python with Plotly. Trisurfs are formed by replacing the boundaries of a compact surface by touching triangles.',
    title = 'Python Trisurf Plots | plotly',
    name = 'Trisurf Plots',
    has_thumbnail='true', thumbnail='thumbnail/tri-surf2.jpg',
    language='python',
    display_as='3d_charts', order=10,
    ipynb= '~notebook_demo/70')
```

```python

```
