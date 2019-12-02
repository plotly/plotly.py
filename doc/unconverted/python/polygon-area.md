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
    description: Learn how to find the area of any simple polygon
    display_as: mathematics
    has_thumbnail: false
    language: python
    layout: base
    name: Polygon Area
    order: 8
    page_type: example_index
    permalink: python/polygon-area/
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

#### Area of a Square
Sort the defined corners of a polygon, calculate the angles between each pair of points and calculate the area contained.

```python
def PolygonSort(corners):
    n = len(corners)
    cx = float(sum(x for x, y in corners)) / n
    cy = float(sum(y for x, y in corners)) / n
    cornersWithAngles = []
    for x, y in corners:
        an = (np.arctan2(y - cy, x - cx) + 2.0 * np.pi) % (2.0 * np.pi)
        cornersWithAngles.append((x, y, an))
    cornersWithAngles.sort(key = lambda tup: tup[2])
    return map(lambda (x, y, an): (x, y), cornersWithAngles)

def PolygonArea(corners):
    n = len(corners)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area

corners = [(0, 0), (1, 1), (0, 1), (1, 0)]
corners_sorted = PolygonSort(corners)
area = PolygonArea(corners_sorted)

x = [corner[0] for corner in corners_sorted]
y = [corner[1] for corner in corners_sorted]

annotation = go.Annotation(
    x=1.5,
    y=1.0,
    text='The area of the polygon is approximately %s' % (area),
    showarrow=False
)

trace1 = go.Scatter(
    x=x,
    y=y,
    mode='markers',
    fill='tonexty',
)

layout = go.Layout(
    annotations=[annotation],
    xaxis=dict(
        range=[-1, 2]
    ),
    yaxis=dict(
        range=[-1, 2]
    )
)

trace_data = [trace1]
fig = go.Figure(data=trace_data, layout=layout)

py.iplot(fig, filename='square-area')
```

#### Area of a Polygon

```python
def PolygonSort(corners):
    n = len(corners)
    cx = float(sum(x for x, y in corners)) / n
    cy = float(sum(y for x, y in corners)) / n
    cornersWithAngles = []
    for x, y in corners:
        an = (np.arctan2(y - cy, x - cx) + 2.0 * np.pi) % (2.0 * np.pi)
        cornersWithAngles.append((x, y, an))
    cornersWithAngles.sort(key = lambda tup: tup[2])
    return map(lambda (x, y, an): (x, y), cornersWithAngles)

def PolygonArea(corners):
    n = len(corners)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area

corners = [(0, 0), (3, 0), (2, 10), (3, 4), (1, 5.5)]
corners_sorted = PolygonSort(corners)
area = PolygonArea(corners_sorted)

x = [corner[0] for corner in corners_sorted]
y = [corner[1] for corner in corners_sorted]

annotation = go.Annotation(
    x=5.5,
    y=8.0,
    text='The area of the polygon is approximately %s' % (area),
    showarrow=False
)

trace1 = go.Scatter(
    x=x,
    y=y,
    mode='markers',
    fill='tozeroy',
)

layout = go.Layout(
    annotations=[annotation],
    xaxis=dict(
        range=[-1, 9]
    ),
    yaxis=dict(
        range=[-1, 12]
    )
)

trace_data = [trace1]
fig = go.Figure(data=trace_data, layout=layout)

py.iplot(fig, filename='polygon-area')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'python_Polygon_Area.ipynb', 'python/polygon-area/', 'Polygon Area | plotly',
    'Learn how to find the area of any simple polygon',
    title='Polygon Area in Python. | plotly',
    name='Polygon Area',
    language='python',
    page_type='example_index', has_thumbnail='false', display_as='mathematics', order=8,
    ipynb= '~notebook_demo/100')
```

```python

```
