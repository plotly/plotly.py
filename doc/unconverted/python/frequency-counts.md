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
    description: Learn how to perform frequency counts using Python.
    display_as: statistics
    has_thumbnail: false
    language: python
    layout: base
    name: Frequency Counts
    order: 2
    page_type: example_index
    permalink: python/frequency-counts/
    thumbnail: /images/static-image
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by dowloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Imports
The tutorial below imports [numpy](http://www.numpy.org/), [pandas](https://plot.ly/pandas/intro-to-pandas-tutorial/), and [scipy](https://www.scipy.org/)

```python
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

import numpy as np
import pandas as pd
import scipy
```

#### Make the Data


We are generating a 1D dataset from a `Weibull Distribution` which has the distrubution

$$
\begin{align*}
X = \log(U)^{\frac{1}{a}}
\end{align*}
$$

where $U$ is drawn from the `Uniform Distribution`.

```python
x=np.random.weibull(1.25, size=1000)
print(x[:10])
```

#### Histogram


By using a histogram, we can properly divide a 1D dataset into bins with a particular size or width, so as to form a discrete probability distribution

```python
trace = go.Histogram(x=x, xbins=dict(start=np.min(x), size=0.25, end=np.max(x)),
                   marker=dict(color='rgb(0, 0, 100)'))

layout = go.Layout(
    title="Histogram Frequency Counts"
)

fig = go.Figure(data=go.Data([trace]), layout=layout)
py.iplot(fig, filename='histogram-freq-counts')
```

#### Larger Bins


We can experiment with our bin size and the histogram by grouping the data into larger intervals

```python
trace = go.Histogram(x=x, xbins=dict(start=np.min(x), size=0.75, end=np.max(x)),
                   marker=dict(color='rgb(0, 0, 100)'))

layout = go.Layout(
    title="Histogram Frequency Counts"
)

fig = go.Figure(data=go.Data([trace]), layout=layout)
py.iplot(fig, filename='histogram-freq-counts-larger-bins')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'python-Frequency-Counts.ipynb', 'python/frequency-counts/', 'Frequency Counts | plotly',
    'Learn how to perform frequency counts using Python.',
    title='Frequency Counts in Python. | plotly',
    name='Frequency Counts',
    language='python',
    page_type='example_index', has_thumbnail='false', display_as='statistics', order=2,
    ipynb= '~notebook_demo/111')
```

```python

```
