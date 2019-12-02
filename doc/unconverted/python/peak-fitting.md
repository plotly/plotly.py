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
    description: Learn how to fit to peaks in Python
    display_as: peak-analysis
    has_thumbnail: false
    language: python
    layout: base
    name: Peak Fitting
    order: 5
    page_type: example_index
    permalink: python/peak-fitting/
    thumbnail: /images/static-image
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Imports
The tutorial below imports [NumPy](http://www.numpy.org/), [Pandas](https://plot.ly/pandas/intro-to-pandas-tutorial/), [SciPy](https://www.scipy.org/) and [PeakUtils](http://pythonhosted.org/PeakUtils/).

```python
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

import numpy as np
import pandas as pd
import scipy
import peakutils

from scipy import signal
```

#### Import Data
Let us import some stock data for our fitting:

```python
stock_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/stockdata.csv')
df = stock_data[0:15]

table = FF.create_table(df)
py.iplot(table, filename='stockdata-peak-fitting')
```

#### Original Plot
Let us plot the `SBUX` column of the data and highlight a section we will fit to:

```python
left_endpt=1857
right_endpt=1940

original_trace = go.Scatter(
    x = [j for j in range(len(stock_data['SBUX']))],
    y = stock_data['SBUX'][0:left_endpt].tolist() + [None for k in range(right_endpt - left_endpt)] +
        stock_data['SBUX'][right_endpt + 1:len(stock_data['SBUX'])].tolist(),
    mode = 'lines',
    name = 'Full Data',
    marker = dict(color = 'rgb(160,200,250)')
)

highlighted_trace = go.Scatter(
    x = [j for j in range(left_endpt, right_endpt)],
    y = stock_data['SBUX'][left_endpt:right_endpt],
    mode = 'lines',
    name = 'Highlighted Section',
    marker = dict(color = 'rgb(0,56,210)')
)

data = [original_trace, highlighted_trace,]
py.iplot(data, filename='stock-data-SBUX')
```

#### Peak Detection
Before we are able to apply `Peak Fitting` we need to detect the peaks in this waveform to properly specify a peak to fit to.

```python
x = [j for j in range(len(stock_data))][left_endpt:right_endpt]
y = stock_data['SBUX'][left_endpt:right_endpt]
y = y.tolist()

cb = np.array(y)
indices = peakutils.indexes(cb, thres=0.75, min_dist=0.1)

trace = go.Scatter(
    x=x,
    y=y,
    mode='lines',
    marker=dict(
        color='rgb(0,56,210)'
    ),
    name='Highlighted Plot'
)

trace2 = go.Scatter(
    x=indices + left_endpt,
    y=[y[j] for j in indices],
    mode='markers',
    marker=dict(
        size=8,
        color='rgb(255,0,0)',
        symbol='cross'
    ),
    name='Detected Peaks'
)

data = [trace, trace2]
py.iplot(data, filename='stock-data-with-peaks')
```

#### Peak Fitting
Since we have detected all the local maximum points on the data, we can now isolate a few peaks and superimpose a fitted gaussian over one.

```python
def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

first_index = indices[6]
left_gauss_bound = 1894
right_gauss_bound = 1910

x_values_1 = np.asarray(x[left_gauss_bound-left_endpt:right_gauss_bound-left_endpt])
y_values_1 = np.asarray(y[left_gauss_bound-left_endpt:right_gauss_bound-left_endpt])

gaussian_params_1 = peakutils.gaussian_fit(x_values_1, y_values_1, center_only=False)
gaussian_y_1 = [gaussian(x_dummy, gaussian_params_1[1], 1.5) for x_dummy in x_values_1]

trace = go.Scatter(
    x=x,
    y=y,
    mode='lines',
    marker=dict(
        color='rgb(0,56,210)'
    ),
    name='Highlighted Plot'
)

trace2 = go.Scatter(
    x=indices + left_endpt,
    y=[y[j] for j in indices],
    mode='markers',
    marker=dict(
        size=8,
        color='rgb(255,0,0)',
        symbol='cross'
    ),
    name='Detected Peaks'
)

trace3 = go.Scatter(
    #x=x_values_1,
    x=[item_x + 1.5 for item_x in x_values_1],
    y=[item_y + 38.2 for item_y in gaussian_y_1],
    mode='lines',
    marker=dict(
        size=2,
        color='rgb(200,0,250)',
    ),
    name='Gaussian Fit'
)

data = [trace, trace2, trace3]
py.iplot(data, filename='stock-data-with-peaks-and-fit')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'python-Peak-Fitting.ipynb', 'python/peak-fitting/', 'Peak Fitting | plotly',
    'Learn how to fit to peaks in Python',
    title='Peak Fitting in Python | plotly',
    name='Peak Fitting',
    language='python',
    page_type='example_index', has_thumbnail='false', display_as='peak-analysis', order=5,
    ipynb= '~notebook_demo/119')
```

```python

```
