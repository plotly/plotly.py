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
    description: Learn how to normalize data by fitting to intervals on the real line
      and dividing by a constant
    display_as: mathematics
    has_thumbnail: false
    language: python
    layout: base
    name: Normalization
    order: 2
    page_type: example_index
    permalink: python/normalization/
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
import plotly.tools as tools
from plotly.tools import FigureFactory as FF

import numpy as np
import pandas as pd
import scipy
```

#### Import Data


To properly visualize our data and normalization, let us import a dataset of Apple Stock prices in 2014:

```python
apple_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')
df = apple_data[0:10]

table = FF.create_table(df)
py.iplot(table, filename='apple-data-sample')
```

#### Normalize by a Constant
Normalize a dataset by dividing each data point by a constant, such as the standard deviation of the data.

```python
data = apple_data['AAPL_y']

data_norm_by_std = [number/scipy.std(data) for number in data]

trace1 = go.Histogram(
    x=data,
    opacity=0.75,
    name='data'
)

trace2 = go.Histogram(
    x=data_norm_by_std,
    opacity=0.75,
    name='normalized by std = ' + str(scipy.std(data)),
)

fig = tools.make_subplots(rows=2, cols=1)

fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 2, 1)

fig['layout'].update(height=600, width=800, title='Normalize by a Constant')
py.iplot(fig, filename='apple-data-normalize-constant')
```

#### Normalize to [0, 1]
Normalize a dataset by dividing each data point by the norm of the dataset.

```python
data_norm_to_0_1 = [number/scipy.linalg.norm(data) for number in data]

trace1 = go.Histogram(
    x=data,
    opacity=0.75,
    name='data',
)

trace2 = go.Histogram(
    x=data_norm_to_0_1,
    opacity=0.75,
    name='normalized to [0,1]',
)

fig = tools.make_subplots(rows=2, cols=1)

fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 2, 1)

fig['layout'].update(height=600, width=800, title='Normalize to [0,1]')
py.iplot(fig, filename='apple-data-normalize-0-1')
```

#### Normalizing to any Interval
Normalize a dataset to an interval [a, b] where a, b are real numbers.

```python
a = 10
b = 50
data_norm_to_a_b = [(number - a)/(b - a) for number in data]

trace1 = go.Histogram(
    x=data,
    opacity=0.75,
    name='data',
)

trace2 = go.Histogram(
    x=data_norm_to_a_b,
    opacity=0.75,
    name='normalized to [10,50]',
)

fig = tools.make_subplots(rows=2, cols=1)

fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 2, 1)

fig['layout'].update(height=600, width=800, title='Normalize to [10,50]')
py.iplot(fig, filename='apple-data-normalize-a-b')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'python_Normalization.ipynb', 'python/normalization/', 'Normalization | plotly',
    'Learn how to normalize data by fitting to intervals on the real line and dividing by a constant',
    title='Normalization in Python. | plotly',
    name='Normalization',
    language='python',
    page_type='example_index', has_thumbnail='false', display_as='mathematics', order=2,
    ipynb= '~notebook_demo/103')
```

```python

```
