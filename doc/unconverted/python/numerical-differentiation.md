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
    description: Learn how to differentiate a sequence or list of values numerically
    display_as: mathematics
    has_thumbnail: false
    language: python
    layout: base
    name: Numerical Differentiation
    order: 6
    page_type: example_index
    permalink: python/numerical-differentiation/
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

#### Differentiate the Sine Function
How to use numerical differentiation to plot the derivative of the sine function $y = sin(x)$:

```python
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

dy = np.zeros(y.shape,np.float)
dy[0:-1] = np.diff(y)/np.diff(x)
dy[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])

trace1 = go.Scatter(
    x=x,
    y=y,
    mode='lines',
    name='sin(x)'
)

trace2 = go.Scatter(
    x=x,
    y=dy,
    mode='lines',
    name='numerical derivative of sin(x)'
)

trace_data = [trace1, trace2]
py.iplot(trace_data, filename='numerical-differentiation')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'python_Numerical_Differentiation.ipynb', 'python/numerical-differentiation/', 'Numerical Differentiation | plotly',
    'Learn how to differentiate a sequence or list of values numerically',
    title='Numerical Differentiation in Python. | plotly',
    name='Numerical Differentiation',
    language='python',
    page_type='example_index', has_thumbnail='false', display_as='mathematics', order=6,
    ipynb= '~notebook_demo/102')
```

```python

```
