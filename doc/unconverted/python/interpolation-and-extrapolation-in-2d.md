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
    description: Learn how to interpolation and extrapolate data in two dimensions
    display_as: mathematics
    has_thumbnail: false
    language: python
    layout: base
    name: Interpolation and Extrapolation in 2D
    order: 4
    page_type: example_index
    permalink: python/interpolation-and-extrapolation-in-2d/
    thumbnail: /images/static-image
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by dowloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Imports
The tutorial below imports [NumPy](http://www.numpy.org/), [Pandas](https://plot.ly/pandas/intro-to-pandas-tutorial/), and [SciPy](https://www.scipy.org/).

```python
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

import numpy as np
import pandas as pd
import scipy
```

#### Tips
Interpolation refers to the process of generating data points between already existing data points. Extrapolation is the process of generating points outside a given set of known data points.
<br/>(_inter_ and _extra_ are derived from Latin words meaning 'between' and 'outside' respectively)


#### Spline Interpolation
Interpolate for a set of points and generate the curve of best fit that intersects all the points.

```python
from scipy import interpolate

x = np.arange(-5.0, 5.0, 0.25)
y = np.arange(-5.0, 5.0, 0.25)
xx, yy = np.meshgrid(x, y)
z = np.sin(xx**2+yy**2)
f = interpolate.interp2d(x, y, z, kind='cubic')

xnew = np.arange(-5.0, 5.0, 1e-1)
ynew = np.arange(-5.0, 5.0, 1e-1)
znew = f(xnew, ynew)

trace1 = go.Scatter3d(
    x=x,
    y=y,
    z=z[0, :],
    mode='markers',
    name='Data',
    marker = dict(
        size = 7
    )
)

trace2 = go.Scatter3d(
    x=ynew,
    y=xnew,
    z=znew[0, :],
    marker=dict(
        size=3,
    ),
    name='Interpolated Data'
)

layout = go.Layout(
    title='Interpolation and Extrapolation in 2D',
    scene=dict(
            camera= dict(
                up=dict(x=0, y=0, z=1),
                center=dict(x=0, y=0, z=0),
                eye=dict(x=1, y=-1, z=0)
            )
    )
)

data = [trace1, trace2]

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='interpolation-and-extrapolation-2d')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'python_Interpolation_and_Extrapolation_in_2D.ipynb', 'python/interpolation-and-extrapolation-in-2d/', 'Interpolation and Extrapolation in 2D | plotly',
    'Learn how to interpolation and extrapolate data in two dimensions',
    title='Interpolation and Extrapolation in 2D in Python. | plotly',
    name='Interpolation and Extrapolation in 2D',
    language='python',
    page_type='example_index', has_thumbnail='false', display_as='mathematics', order=4,
    ipynb= '~notebook_demo/105')
```

```python

```
