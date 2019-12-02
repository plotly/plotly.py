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
    description: Learn how to perform discrete frequency analysis using Python.
    display_as: statistics
    has_thumbnail: false
    language: python
    layout: base
    name: Discrete Frequency
    order: 3
    page_type: example_index
    permalink: python/discrete-frequency/
    thumbnail: /images/static-image
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by dowloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Imports
The tutorial below imports [Numpy](http://www.numpy.org/), [Pandas](https://plot.ly/pandas/intro-to-pandas-tutorial/), and [SciPy](https://www.scipy.org/).

```python
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

import numpy as np
import pandas as pd
import scipy
```

#### Import Data


We will import a dataset to perform our discrete frequency analysis on. We will look at the consumption of alcohol by country in 2010.

```python
data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2010_alcohol_consumption_by_country.csv')
df = data[0:10]

table = FF.create_table(df)
py.iplot(table, filename='alcohol-data-sample')
```

#### Probability Distribution


We can produce a histogram plot of the data with the y-axis representing the probability distribution of the data.

```python
x = data['alcohol'].values.tolist()

trace = go.Histogram(x=x, histnorm='probability',
                     xbins=dict(start=np.min(x),
                                size=0.25,
                                end=np.max(x)),
                     marker=dict(color='rgb(25, 25, 100)'))

layout = go.Layout(
    title="Histogram with Probability Distribution"
)

fig = go.Figure(data=go.Data([trace]), layout=layout)
py.iplot(fig, filename='histogram-prob-dist')
```

#### Frequency Counts

```python
trace = go.Histogram(x=x,
                     xbins=dict(start=np.min(x),
                                size=0.25,
                                end=np.max(x)),
                     marker=dict(color='rgb(25, 25, 100)'))

layout = go.Layout(
    title="Histogram with Frequency Count"
)

fig = go.Figure(data=go.Data([trace]), layout=layout)
py.iplot(fig, filename='histogram-discrete-freq-count')
```

#### Percentage

```python
trace = go.Histogram(x=x, histnorm='percent',
                     xbins=dict(start=np.min(x),
                                size=0.25,
                                end=np.max(x)),
                     marker=dict(color='rgb(50, 50, 125)'))

layout = go.Layout(
    title="Histogram with Frequency Count"
)

fig = go.Figure(data=go.Data([trace]), layout=layout)
py.iplot(fig, filename='histogram-percentage')
```

#### Cumulative Density Function


We can also take the cumulatve sum of our dataset and then plot the cumulative density function, or `CDF`, as a scatter plot

```python
cumsum = np.cumsum(x)

trace = go.Scatter(x=[i for i in range(len(cumsum))], y=10*cumsum/np.linalg.norm(cumsum),
                     marker=dict(color='rgb(150, 25, 120)'))
layout = go.Layout(
    title="Cumulative Distribution Function"
)

fig = go.Figure(data=go.Data([trace]), layout=layout)
py.iplot(fig, filename='cdf-dataset')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'python-Discrete-Frequency.ipynb', 'python/discrete-frequency/', 'Discrete Frequency | plotly',
    'Learn how to perform discrete frequency analysis using Python.',
    title='Discrete Frequency in Python. | plotly',
    name='Discrete Frequency',
    language='python',
    page_type='example_index', has_thumbnail='false', display_as='statistics', order=3,
    ipynb= '~notebook_demo/110')
```

```python

```
