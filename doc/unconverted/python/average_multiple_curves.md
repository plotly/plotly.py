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
    description: Learn how to average the values of multiple curves with Python.
    display_as: mathematics
    has_thumbnail: false
    language: python
    layout: base
    name: Average Multiple Curves
    order: 9
    page_type: example_index
    permalink: python/average_multiple_curves/
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

#### Average of 2 Curves


Given two curves defined by functions $f$ and $g$ on $\mathbb{R} \rightarrow \mathbb{R}$, **the average curve** $h$ of $f$ and $g$ is defined by $h = \frac{f(x) + g(x)}{2} $ for $x \in \mathbb{R}$.

```python
x = np.linspace(0, 2*np.pi, 100)
f = np.sin(x)
g = np.cos(x)
h = [(f[j] + g[j])/2 for j in range(len(x))]

trace1 = go.Scatter(
    x=x,
    y=f,
    mode='lines',
    name='f(x)',
    marker=dict(
        color='rgb(220, 20, 60)'
    )
)

trace2 = go.Scatter(
    x=x,
    y=g,
    mode='lines',
    name='g(x)',
    marker=dict(
        color='rgb(100, 149, 237)'
    )
)

trace3 = go.Scatter(
    x=x,
    y=h,
    mode='markers+lines',
    name='Average of f and g',
    marker=dict(
        color='rgb(128, 0, 128)',
        symbol='diamond-open',
    )
)

data = [trace1, trace2, trace3]
py.iplot(data, filename='2-curves')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'python_Average_Multiple_Curves.ipynb', 'python/average_multiple_curves/', 'Average Multiple Curves | plotly',
    'Learn how to average the values of multiple curves with Python.',
    title='Average Multiple Curves in Python | plotly',
    name='Average Multiple Curves',
    language='python',
    page_type='example_index', has_thumbnail='false', display_as='mathematics', order=9,
    ipynb= '~notebook_demo/107')
```

```python

```
