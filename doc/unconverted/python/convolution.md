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
    description: Learn how to perform convolution between two signals in Python.
    display_as: signal-analysis
    has_thumbnail: false
    language: python
    layout: base
    name: Convolution
    order: 4
    page_type: example_index
    permalink: python/convolution/
    thumbnail: /images/static-image
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Imports
The tutorial below imports [NumPy](http://www.numpy.org/), [Pandas](https://plot.ly/pandas/intro-to-pandas-tutorial/), [SciPy](https://www.scipy.org/) and [Plotly](https://plot.ly/python/getting-started/).

```python
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff

import numpy as np
import pandas as pd
import scipy

from scipy import signal
```

#### Import Data
Let us import some stock data to apply convolution on.

```python
stock_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/stockdata.csv')
df = stock_data[0:15]

table = ff.create_table(df)
py.iplot(table, filename='stockdata-peak-fitting')
```

<!-- #region -->
#### Convolve Two Signals
`Convolution` is a type of transform that takes two functions `f` and `g` and produces another function via an integration. In particular, the convolution $(f*g)(t)$ is defined as:

$$
\begin{align*}
\int_{-\infty}^{\infty} {f(\tau)g(t - \tau)d\tau}
\end{align*}
$$


We can use convolution in the discrete case between two n-dimensional arrays.
<!-- #endregion -->

```python
sample = range(15)
saw = signal.sawtooth(t=sample)

data_sample = list(stock_data['SBUX'][0:100])
data_sample2 = list(stock_data['AAPL'][0:100])
x = list(range(len(data_sample)))
y_convolve = signal.convolve(saw, data_sample2)
x_convolve = list(range(len(y_convolve)))

trace1 = go.Scatter(
    x = x,
    y = data_sample,
    mode = 'lines',
    name = 'SBUX'
)

trace2 = go.Scatter(
    x = x,
    y = data_sample2,
    mode = 'lines',
    name = 'AAPL'
)

trace3 = go.Scatter(
    x = x_convolve,
    y = y_convolve,
    mode = 'lines',
    name = 'Convolution'
)

data = [trace1, trace2, trace3]
py.iplot(data, filename='convolution-of-two-signals')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'python-Convolution.ipynb', 'python/convolution/', 'Convolution | plotly',
    'Learn how to perform convolution between two signals in Python.',
    title='Convolution in Python | plotly',
    name='Convolution',
    language='python',
    page_type='example_index', has_thumbnail='false', display_as='signal-analysis', order=4)
```

```python

```
