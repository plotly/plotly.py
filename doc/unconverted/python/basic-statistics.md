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
    description: Learn how to perform basic statistical operations using Python.
    display_as: statistics
    has_thumbnail: false
    language: python
    layout: base
    name: Basic Statistics
    order: 1
    page_type: example_index
    permalink: python/basic-statistics/
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

#### Import Data


Let us import a dataset to perform our statistics. We will be looking at the consumption of alcohol by country in 2010.

```python
data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2010_alcohol_consumption_by_country.csv')
df = data[0:10]

table = FF.create_table(df)
py.iplot(table, filename='alcohol-data-sample')
```

#### Mean and Variance


Two of the most basic statistical operations are the `mean` $\mu$ and `standard deviation` $\sigma$ of a one-dimension array of data, that is, a sequence of numeric values. The `mean` of a set of numbers $x_1, ..., x_N$ is defined as:

$$\begin{align*}
\mu = \sum_{i=1}^N{x_i}
\end{align*}
$$

The mean is used colloquially as the _average_ of a set of values. The standard deviation on the other hand is a statistical metric that describes the spread of the data, or how far the values are from the mean. The `standard deviation` of a set of data is defined as:

$$\begin{align*}
\sigma = \sqrt{\frac{1}{N-1}\sum_{i=1}^{N}{(x_i-\mu)^2}}
\end{align*}
$$

```python
mean = np.mean(data['alcohol'])
st_dev = np.std(data['alcohol'])

print("The mean is %r") %(mean)
print("The standard deviation is %r") %(st_dev)
```

#### Secondary Statistics


We can also compute other statistics such as the `median`, `maximum` and `minimum` of the data

```python
median = np.median(data['alcohol'])
maximum = np.max(data['alcohol'])
minimum = np.min(data['alcohol'])

print("The median is %r") %(median)
print("The maximum is %r") %(maximum)
print("The minimum is %r") %(minimum)
```

#### Visualize the Statistics


We can visualize these statistics by producing a Plotly box or Violin chart.

```python
y = data['alcohol'].values.tolist()

fig = FF.create_violin(y, title='Violin Plot', colors='#604d9e')
py.iplot(fig, filename='alcohol-violin-visual')
```

```python
y = data['alcohol'].values.tolist()

trace = go.Box(
    y=y,
    name = 'Box Plot',
    boxpoints='all',
    jitter=0.3,
    marker = dict(
        color = 'rgb(214,12,140)',
    ),
)

layout = go.Layout(
    width=500,
    yaxis=dict(
        title='Alcohol Consumption by Country',
        zeroline=False
    ),
)

data = [trace]
fig= go.Figure(data=data, layout=layout)
py.iplot(fig, filename='alcohol-box-plot')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'python-Basic-Statistics.ipynb', 'python/basic-statistics/', 'Basic Statistics | plotly',
    'Learn how to perform basic statistical operations using Python.',
    title='Basic Statistics in Python. | plotly',
    name='Basic Statistics',
    language='python',
    page_type='example_index', has_thumbnail='false', display_as='statistics', order=1,
    ipynb= '~notebook_demo/109')
```

```python

```
