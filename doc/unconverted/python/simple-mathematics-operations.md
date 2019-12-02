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
    description: Learn how to perform simple mathematical operations on dataframes
      such as scaling, adding, and subtracting
    display_as: mathematics
    has_thumbnail: false
    language: python
    layout: base
    name: Simple Mathematics Operations
    order: 1
    page_type: example_index
    permalink: python/simple-mathematics-operations/
    thumbnail: /images/static-image
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
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

#### Import Data
Let us import a timeseries dataset to perform mathematical operations on:

```python
data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/timeseries.csv')

table = FF.create_table(data)
py.iplot(table, filename='timeseries-data-table')
```

#### Scale a Dataset
You can modify a dataset by scaling each number by a constant.

```python
x = data['Date']
y = data['A']
y2 = [2.*k for k in y]

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
    x=x,
    y=y2,
    mode='markers',
    name='Scaled by 2',
    marker=dict(
        size=12,
        symbol='x'
    )
)

trace_data = [trace1, trace2]
py.iplot(trace_data, filename='scale-a-dataset')
```

#### Subtract Two Columns

```python
trace1 = go.Scatter(
    x=data['Date'],
    y=data['A'],
    mode='markers',
    name='Column A',
    marker=dict(
        size=12
    )
)

trace2 = go.Scatter(
    x=data['Date'],
    y=data['D'],
    mode='markers',
    name='Column D',
    marker=dict(
        size=12
    )
)

trace3 = go.Scatter(
    x=data['Date'],
    y=data['D'] - data['A'],
    mode='markers',
    name='Column D - Column A',
    marker=dict(
        size=12,
        symbol='square-open'
    )
)

trace_data1 = [trace1, trace2, trace3]
py.iplot(trace_data1, filename='subtract-two-dataframe-columns')
```

#### Modify DataFrame Entries
Use arithmetic operations including addition, subtraction, multiplication and division to change the values in a DataFrame column:

```python
dataframe = pd.DataFrame([[1, 2],
                          [3, 4],
                          [5, 6],
                          [7, 8]],
                         columns=['A', 'B'])

table = FF.create_table(dataframe)
py.iplot(table, filename='math-operations-dataframe')
```

```python
dataframe['A'][0] = 120
dataframe['B'][3] = -2*dataframe['B'][3]

table = FF.create_table(dataframe)
py.iplot(table, filename='math-operations-dataframe-changed')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'python_Simple_Mathematics_Operations.ipynb', 'python/simple-mathematics-operations/', 'Simple Mathematics Operations | plotly',
    'Learn how to perform simple mathematical operations on dataframes such as scaling, adding, and subtracting',
    title='Simple Mathematics Operations in Python. | plotly',
    name='Simple Mathematics Operations',
    language='python',
    page_type='example_index', has_thumbnail='false', display_as='mathematics', order=1,
    ipynb= '~notebook_demo/99')
```

```python

```
