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
    description: How to make Tri-Surf plots in Python with Plotly.
    display_as: 3d_charts
    language: python
    layout: base
    name: Surface Triangulation
    order: 11
    page_type: u-guide
    permalink: python/surface-triangulation/
    thumbnail: thumbnail/trisurf.jpg
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Defining and plotting triangulated surfaces
#### with Plotly `Mesh3d`


A triangulation of a compact surface is a finite collection of triangles that cover the surface in  such a way that every point on the surface is in a triangle,  and  the intersection of any two triangles is either void, a common edge or a common vertex. A triangulated surface is called tri-surface.



The triangulation of a surface defined as the graph of a continuous function, $z=f(x,y), (x,y)\in D\subset\mathbb{R}^2$ or in a parametric form:
$$x=x(u,v), y=y(u,v), z=z(u,v), (u,v)\in U\subset\mathbb{R}^2,$$
is the image through $f$,respectively through the parameterization, of the Delaunay triangulation or an user defined triangulation of the planar domain $D$, respectively $U$.

The Delaunay triangulation of a planar region is defined and illustrated in a Python Plotly tutorial posted [here](https://plot.ly/python/alpha-shapes/).

If the planar region $D$  ($U$) is rectangular, then one defines a meshgrid on it, and the points
of the grid are the input  points for the `scipy.spatial.Delaunay` function that defines the planar triangulation of $D$, respectively $U$.



### Triangulation of the Moebius band ###


The Moebius band is parameterized by:

$$\begin{align*}
x(u,v)&=(1+0.5 v\cos(u/2))\cos(u)\\
y(u,v)&=(1+0.5 v\cos(u/2))\sin(u)\quad\quad u\in[0,2\pi],\: v\in[-1,1]\\
z(u,v)&=0.5 v\sin(u/2)
\end{align*}
$$


Define a meshgrid on the rectangle $U=[0,2\pi]\times[-1,1]$:

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
import matplotlib.cm as cm
from scipy.spatial import Delaunay

u=np.linspace(0,2*np.pi, 24)
v=np.linspace(-1,1, 8)
u,v=np.meshgrid(u,v)
u=u.flatten()
v=v.flatten()

#evaluate the parameterization at the flattened u and v
tp=1+0.5*v*np.cos(u/2.)
x=tp*np.cos(u)
y=tp*np.sin(u)
z=0.5*v*np.sin(u/2.)

#define 2D points, as input data for the Delaunay triangulation of U
points2D=np.vstack([u,v]).T
tri = Delaunay(points2D)#triangulate the rectangle U
```

`tri.simplices` is a `np.array` of integers, of shape (`ntri`,3), where `ntri` is the number of triangles generated  by `scipy.spatial.Delaunay`.
Each row in this array contains  three indices,  i, j, k, such that points2D[i,:], points2D[j,:], points2D[k,:]  are vertices of a triangle in the Delaunay triangularization of the rectangle $U$.


```python
print tri.simplices.shape, '\n', tri.simplices[0]
```

The images  of the `points2D` through the surface parameterization are 3D points. The same simplices define the triangles on the surface.


Setting   a combination of  keys in `Mesh3d` leads to generating and plotting of a tri-surface, in the same way as `plot_trisurf` in matplotlib  or `trisurf` in Matlab does.

We note that `Mesh3d` with different combination of keys can generate  [alpha-shapes](https://plot.ly/python/alpha-shapes/).


In order to plot a tri-surface, we choose a colormap, and associate to each triangle on the surface,  the  color in colormap, corresponding to  the normalized mean value of z-coordinates of the triangle vertices.


Define a function that maps a mean z-value to a matplotlib color, converted to a Plotly color:

```python
def map_z2color(zval, colormap, vmin, vmax):
    #map the normalized value zval to a corresponding color in the colormap

    if vmin>vmax:
        raise ValueError('incorrect relation between vmin and vmax')
    t=(zval-vmin)/float((vmax-vmin))#normalize val
    R, G, B, alpha=colormap(t)
    return 'rgb('+'{:d}'.format(int(R*255+0.5))+','+'{:d}'.format(int(G*255+0.5))+\
           ','+'{:d}'.format(int(B*255+0.5))+')'

```

To plot the triangles on a surface,  we set in Plotly `Mesh3d` the lists of x, y, respectively z- coordinates of the vertices, and the lists of indices, i, j, k, for x, y, z coordinates of  all  vertices:

```python
def tri_indices(simplices):
    #simplices is a numpy array defining the simplices of the triangularization
    #returns the lists of indices i, j, k

    return ([triplet[c] for triplet in simplices] for c in range(3))

def plotly_trisurf(x, y, z, simplices, colormap=cm.RdBu, plot_edges=None):
    #x, y, z are lists of coordinates of the triangle vertices
    #simplices are the simplices that define the triangularization;
    #simplices  is a numpy array of shape (no_triangles, 3)
    #insert here the  type check for input data

    points3D=np.vstack((x,y,z)).T
    tri_vertices=map(lambda index: points3D[index], simplices)# vertices of the surface triangles
    zmean=[np.mean(tri[:,2]) for tri in tri_vertices ]# mean values of z-coordinates of
                                                      #triangle vertices
    min_zmean=np.min(zmean)
    max_zmean=np.max(zmean)
    facecolor=[map_z2color(zz,  colormap, min_zmean, max_zmean) for zz in zmean]
    I,J,K=tri_indices(simplices)

    triangles=go.Mesh3d(x=x,
                     y=y,
                     z=z,
                     facecolor=facecolor,
                     i=I,
                     j=J,
                     k=K,
                     name=''
                    )

    if plot_edges is None:# the triangle sides are not plotted
        return [triangles]
    else:
        #define the lists Xe, Ye, Ze, of x, y, resp z coordinates of edge end points for each triangle
        #None separates data corresponding to two consecutive triangles
        lists_coord=[[[T[k%3][c] for k in range(4)]+[ None]   for T in tri_vertices]  for c in range(3)]
        Xe, Ye, Ze=[reduce(lambda x,y: x+y, lists_coord[k]) for k in range(3)]

        #define the lines to be plotted
        lines=go.Scatter3d(x=Xe,
                        y=Ye,
                        z=Ze,
                        mode='lines',
                        line=dict(color= 'rgb(50,50,50)', width=1.5)
               )
        return [triangles, lines]
```

Call this  function for data associated to Moebius band:

```python
data1=plotly_trisurf(x,y,z, tri.simplices, colormap=cm.RdBu, plot_edges=True)
```

Set the  layout of the plot:

```python
axis = dict(
showbackground=True,
backgroundcolor="rgb(230, 230,230)",
gridcolor="rgb(255, 255, 255)",
zerolinecolor="rgb(255, 255, 255)",
    )

layout = go.Layout(
         title='Moebius band triangulation',
         width=800,
         height=800,
         scene=dict(
         xaxis=dict(axis),
         yaxis=dict(axis),
         zaxis=dict(axis),
        aspectratio=dict(
            x=1,
            y=1,
            z=0.5
        ),
        )
        )

fig1 = go.Figure(data=data1, layout=layout)

py.iplot(fig1, filename='Moebius-band-trisurf')
```

### Triangularization of the surface $z=\sin(-xy)$, defined over a disk ###


We consider polar coordinates on the disk, $D(0, 1)$, centered at origin and of radius 1, and define
a meshgrid on the set of points $(r, \theta)$, with $r\in[0,1]$ and $\theta\in[0,2\pi]$:

```python
n=12 # number of radii
h=1.0/(n-1)
r = np.linspace(h, 1.0, n)
theta= np.linspace(0, 2*np.pi, 36)

r,theta=np.meshgrid(r,theta)
r=r.flatten()
theta=theta.flatten()

#Convert polar coordinates to cartesian coordinates (x,y)
x=r*np.cos(theta)
y=r*np.sin(theta)
x=np.append(x, 0)#  a trick to include the center of the disk in the set of points. It was avoided
                 # initially when we defined r=np.linspace(h, 1.0, n)
y=np.append(y,0)
z = np.sin(-x*y)

points2D=np.vstack([x,y]).T
tri=Delaunay(points2D)
```

Plot the  surface with a modified layout:

```python
data2=plotly_trisurf(x,y,z, tri.simplices, colormap=cm.cubehelix, plot_edges=None)
fig2 = go.Figure(data=data2, layout=layout)
fig2['layout'].update(dict(title='Triangulated surface',
                          scene=dict(camera=dict(eye=dict(x=1.75,
                                                          y=-0.7,
                                                          z= 0.75)
                                                )
                                    )))

py.iplot(fig2, filename='trisurf-cubehx')
```

This example is also given as a demo for matplotlib [`plot_trisurf`](http://matplotlib.org/examples/mplot3d/trisurf3d_demo.html).


### Plotting tri-surfaces from data stored in  ply-files ###


A PLY (Polygon File Format or Stanford Triangle Format) format is a format for storing graphical objects
that are represented by  a triangulation of an object, resulted usually from scanning that object. A Ply file contains the coordinates of vertices, the codes for faces (triangles) and other elements, as well as the color for faces or the normal direction to faces.

In the following we show how we can read a ply file via the Python package, `plyfile`. This package can be installed with `pip`.

We choose a ply file from a list  provided [here](http://people.sc.fsu.edu/~jburkardt/data/ply/ply.html).

```python
!pip install plyfile
from plyfile import PlyData, PlyElement

import urllib2
req = urllib2.Request('http://people.sc.fsu.edu/~jburkardt/data/ply/chopper.ply')
opener = urllib2.build_opener()
f = opener.open(req)
plydata = PlyData.read(f)
```

Read the file header:

```python
for element in plydata.elements:
    print element

nr_points=plydata.elements[0].count
nr_faces=plydata.elements[1].count
```

Read the vertex coordinates:

```python
points=np.array([plydata['vertex'][k] for k in range(nr_points)])
points[0]

x,y,z=zip(*points)

faces=[plydata['face'][k][0] for k in range(nr_faces)]
faces[0]
```

Now we can get data for a Plotly plot of the graphical object read from the ply file:

```python
data3=plotly_trisurf(x,y,z, faces, colormap=cm.RdBu, plot_edges=None)

title="Trisurf from a PLY file<br>"+\
                "Data Source:<a href='http://people.sc.fsu.edu/~jburkardt/data/ply/airplane.ply'> [1]</a>"

noaxis=dict(showbackground=False,
            showline=False,
            zeroline=False,
            showgrid=False,
            showticklabels=False,
            title=''
          )

fig3 = go.Figure(data=data3, layout=layout)
fig3['layout'].update(dict(title=title,
                           width=1000,
                           height=1000,
                           scene=dict(xaxis=noaxis,
                                      yaxis=noaxis,
                                      zaxis=noaxis,
                                      aspectratio=dict(x=1, y=1, z=0.4),
                                      camera=dict(eye=dict(x=1.25, y=1.25, z= 1.25)
                                     )
                           )
                     ))

py.iplot(fig3, filename='Chopper-Ply-cls')
```

This a version of the same object plotted along with  triangle edges:

```python
from IPython.display import HTML
HTML('<iframe src=https://plot.ly/~empet/13734/trisurf-from-a-ply-file-data-source-1/ \
     width=800 height=800></iframe>')

```

#### Reference
See https://plot.ly/python/reference/ for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade

import publisher
publisher.publish(
    'triangulation.ipynb', 'python/surface-triangulation/', 'Surface Triangulation',
    'How to make Tri-Surf plots in Python with Plotly.',
    title = 'Python Surface Triangulation | plotly',
    name = 'Surface Triangulation',
    has_thumbnail='true', thumbnail='thumbnail/trisurf.jpg',
    language='python',
    display_as='3d_charts', order=11,
    ipynb= '~notebook_demo/71')
```

```python

```
