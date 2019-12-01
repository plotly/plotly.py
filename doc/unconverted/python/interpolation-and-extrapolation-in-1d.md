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
    description: Learn how to interpolation and extrapolate data in one dimension
    display_as: mathematics
    has_thumbnail: false
    language: python
    layout: base
    name: Interpolation and Extrapolation in 1D
    order: 3
    page_type: example_index
    permalink: python/interpolation-and-extrapolation-in-1d/
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


#### Interpolation and Extrapolation
Interpolate and Extrapolate for a set of points and generate the curve of best fit that intersects all the points.

```python
points = np.array([(1, 1), (2, 4), (3, 1), (9, 3)])

x = points[:,0]
y = points[:,1]

z = np.polyfit(x, y, 3)
f = np.poly1d(z)

x_new = np.linspace(0, 10, 50)
y_new = f(x_new)

trace1 = go.Scatter(
    x=x,
    y=y,
    mode='markers',
    name='Data',
    marker=dict(
        size=12
    )
)

trace2 = go.Scatter(
    x=x_new,
    y=y_new,
    mode='lines',
    name='Fit'
)

annotation = go.Annotation(
    x=6,
    y=-4.5,
    text='$0.43X^3 - 0.56X^2 + 16.78X + 10.61$',
    showarrow=False
)

layout = go.Layout(
    title='Polynomial Fit in Python',
    annotations=[annotation]
)

data = [trace1, trace2]
fig = go.Figure(data=data, layout=layout)

py.iplot(fig, filename='interpolation-and-extrapolation')
```

#### Interpolation and Extrapolation of Y From X
Interpolation and Extrapolation of (x, y) points with pre-existant points and an array of specific x values.

```python
points = np.array([(1, 1), (2, 4), (3, 1), (9, 3)])

# get x and y vectors
x = points[:,0]
y = points[:,1]

# calculate polynomial
z = np.polyfit(x, y, 3)
f = np.poly1d(z)

# other x values
other_x = np.array([1.2, 1.34, 1.57, 1.7, 3.6, 3.8, 3.9, 4.0, 5.4, 6.6, 7.2, 7.3, 7.7, 8, 8.9, 9.1, 9.3])
other_y = f(other_x)

# calculate new x's and y's
x_new = np.linspace(0, 10, 50)
y_new = f(x_new)

# Creating the dataset, and generating the plot
trace1 = go.Scatter(
    x=x,
    y=y,
    mode='markers',
    name='Data',
    marker=dict(
        size=12
    )
)

trace2 = go.Scatter(
    x=other_x,
    y=other_y,
    name='Interpolated/Extrapolated Data',
    mode='markers',
    marker=dict(
        symbol='square-open',
        size=12
    )
)

layout = go.Layout(
    title='Interpolation and Extrapolation of Y From X',
)

data2 = [trace1, trace2]
fig2 = go.Figure(data=data2, layout=layout)

py.iplot(fig2, filename='interpolation-and-extrapolation-of-y-from-x')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'python_Interpolation_and_Extrapolation_in_1D.ipynb', 'python/interpolation-and-extrapolation-in-1d/', 'Interpolation and Extrapolation in 1D | plotly',
    'Learn how to interpolation and extrapolate data in one dimension',
    title='Interpolation and Extrapolation in 1D in Python. | plotly',
    name='Interpolation and Extrapolation in 1D',
    language='python',
    page_type='example_index', has_thumbnail='false', display_as='mathematics', order=3,
    ipynb= '~notebook_demo/106')
```

```python

```
