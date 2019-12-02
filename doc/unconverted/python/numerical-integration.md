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
    description: Learn how to integrate a sequence or list of values numerically
    display_as: mathematics
    has_thumbnail: false
    language: python
    layout: base
    name: Numerical Integration
    order: 7
    page_type: example_index
    permalink: python/numerical-integration/
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

#### Integrate the Sine Function
How to use numerical integration to find the area of $y = sin(x)$ between $0$ and $2\pi$.

```python
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

trace1 = go.Scatter(
    x=x,
    y=y,
    mode='lines',
)

# use numpy's built in trapezoid-rule integration tool
dy = np.trapz(y, x)

annotation = go.Annotation(
    x=4.5,
    y=1.25,
    text='Numerical Integration of sin(x) is approximately %s' % (dy),
    showarrow=False
)

layout = go.Layout(
    annotations=[annotation]
)

trace_data = [trace1]
fig = go.Figure(data=trace_data, layout=layout)

py.iplot(fig, filename='1d-numerical-integration')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'python_Numerical_Integration.ipynb', 'python/numerical-integration/', 'Numerical Integration | plotly',
    'Learn how to integrate a sequence or list of values numerically',
    title='Numerical Integration in Python. | plotly',
    name='Numerical Integration',
    language='python',
    page_type='example_index', has_thumbnail='false', display_as='mathematics', order=7,
    ipynb= '~notebook_demo/101')
```

```python

```
