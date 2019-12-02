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
    description: How to make an animated heatmap in Python.
    display_as: animations
    language: python
    layout: base
    name: Heatmap Animation
    order: 4
    page_type: example_index
    permalink: python/heatmap-animation/
    thumbnail: thumbnail/heatmap_animation.gif
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Version Check
Note: Animations are available in version 1.12.10+
Run `pip install plotly --upgrade` to update your Plotly version.

```python
import plotly
plotly.__version__
```

#### Make the Grid
Our goal is to generate the contours plots of the bivariate normal distributions of mean vector (0,0), standard deviation vector (1,1), and correlation, $\rho$ , varying from `(−1, 1)`. Since we are making an online animation, we must create our grid first and upload it.

```python
import plotly.plotly as py
from plotly.grid_objs import Grid, Column

import time
import numpy as np
from scipy.stats import multivariate_normal as Nd

colorscale = [
    [0.0, 'rgb(25, 23, 10)'],
    [0.05, 'rgb(69, 48, 44)'],
    [0.1, 'rgb(114, 52, 47)'],
    [0.15, 'rgb(155, 58, 49)'],
    [0.2, 'rgb(194, 70, 51)'],
    [0.25, 'rgb(227, 91, 53)'],
    [0.3, 'rgb(250, 120, 56)'],
    [0.35, 'rgb(255, 152, 60)'],
    [0.4, 'rgb(255, 188, 65)'],
    [0.45, 'rgb(236, 220, 72)'],
    [0.5, 'rgb(202, 243, 80)'],
    [0.55, 'rgb(164, 252, 93)'],
    [0.6, 'rgb(123, 245, 119)'],
    [0.65, 'rgb(93, 225, 162)'],
    [0.7, 'rgb(84, 196, 212)'],
    [0.75, 'rgb(99, 168, 238)'],
    [0.8, 'rgb(139, 146, 233)'],
    [0.85, 'rgb(190, 139, 216)'],
    [0.9, 'rgb(231, 152, 213)'],
    [0.95, 'rgb(241, 180, 226)'],
    [1.0, 'rgb(206, 221, 250)']
]

# returns V=(X,Y)~N(m, Sigma)
def bivariate_N(m=[0., 0.], stdev=[1.0, 1.0], rho=0):
    cov = rho*stdev[0] * stdev[1] # covariance(X,Y)
    Sigma = np.array([[stdev[0]**2, cov], [cov, stdev[1]**2]]) # covariance  matrix
    return Nd(mean=m, cov=Sigma) # joint distribution of (X,Y), of mean  vector, m, and cov matrix, Sigma

# returns the pdf of the bivariate normal distribution
def pdf_bivariate_N(m, stdev, V):
    X = np.linspace(m[0] - 3*stdev[0], m[0] + 3*stdev[0], 100)
    Y = np.linspace(m[1] - 3*stdev[1], m[1] + 3*stdev[1], 100)
    x, y = np.meshgrid(X, Y)
    pos = np.empty(x.shape + (2, ))
    pos[:, :, 0] = x; pos[:, :, 1] = y
    z = V.pdf(pos)
    return X, Y, z

correls=[-0.95, -0.85, -0.75, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.75, 0.85, 0.95]

m=[0., 0.]
stdev=[1., 1.]
V=bivariate_N()
x, y=pdf_bivariate_N(m, stdev,  V)[:2]
my_columns=[Column(x, 'x'), Column(y, 'y')]
zvmax=[]
for k, rho in enumerate(correls):
    V = bivariate_N(rho = rho)
    z = pdf_bivariate_N(m, stdev, V)[2]
    zvmax.append(np.max(z))
    my_columns.append(Column(z, 'z{}'.format(k + 1)))
grid = Grid(my_columns)
py.grid_ops.upload(grid, 'norm-bivariate1'+str(time.time()), auto_open=False)
```

#### Make the Figure
Make the `Figure` which references columns from the grid we made. The `Figure` takes `Data`, `Layout` and `Frames`.

```python
data=[dict(type='heatmap',
           xsrc=grid.get_column_reference('x'),
           ysrc=grid.get_column_reference('y'),
           zsrc=grid.get_column_reference('z1'),
           zmin=0,
           zmax=zvmax[6],
           zsmooth='best',
           colorscale=colorscale,
           colorbar=dict(thickness=20, ticklen=4))]

title='Contour plot for bivariate normal distribution'+\
'<br> N(m=[0,0], sigma=[1,1], rho in (-1, 1))'

layout = dict(title=title,
              autosize=False,
              height=600,
              width=600,
              hovermode='closest',
              xaxis=dict(range=[-3, 3], autorange=False),
              yaxis=dict(range=[-3, 3], autorange=False),
              showlegend=False,
              updatemenus=[dict(type='buttons', showactive=False,
                                y=1, x=-0.05, xanchor='right',
                                yanchor='top', pad=dict(t=0, r=10),
                                buttons=[dict(label='Play',
                                              method='animate',
                                              args=[None,
                                                    dict(frame=dict(duration=100,
                                                                    redraw=True),
                                                    transition=dict(duration=0),
                                                    fromcurrent=True,
                                                    mode='immediate')])])])

frames=[dict(data=[dict(zsrc=grid.get_column_reference('z{}'.format(k + 1)),
                        zmax=zvmax[k])],
                        traces=[0],
                        name='frame{}'.format(k),
                        ) for k in range(len(correls))]


fig=dict(data=data, layout=layout, frames=frames)
py.icreate_animations(fig, filename='animheatmap'+str(time.time()))
```

#### Reference
For additional information and attributes for creating heatmaps in Plotly see: https://plot.ly/python/reference/#heatmap.
For more documentation on creating animations with Plotly, see https://plot.ly/python/#animations.

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

!pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'heatmap.ipynb', 'python/heatmap-animation/', 'Heatmap Animation | plotly',
    'How to make an animated heatmap in Python.',
    title='Heatmap Animation | plotly',
    name='Heatmap Animation',
    language='python',
    page_type='example_index', has_thumbnail='true', thumbnail='thumbnail/heatmap_animation.gif',
    ipynb= '~notebook_demo/131',
    display_as='animations', order=4)
```

```python

```
