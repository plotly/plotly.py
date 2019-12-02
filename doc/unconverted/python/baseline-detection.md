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
    description: Learn how to detect baselines on data in Python.
    display_as: peak-analysis
    has_thumbnail: false
    language: python
    layout: base
    name: Baseline Detection
    order: 1
    page_type: example_index
    permalink: python/baseline-detection/
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
import plotly.figure_factory as ff

import numpy as np
import pandas as pd
import scipy
import peakutils
```

#### Import Data
For our baseline detection example, we will import some data on milk production by month:

```python
milk_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/monthly-milk-production-pounds.csv')
time_series = milk_data['Monthly milk production (pounds per cow)']
time_series = np.asarray(time_series)

df = milk_data[0:15]

table = ff.create_table(df)
py.iplot(table, filename='milk-production-dataframe')
```

#### Plot with Baseline

```python
# calculate baseline y values
baseline_values = peakutils.baseline(time_series)

trace = go.Scatter(
    x=[j for j in range(len(time_series))],
    y=time_series,
    mode='lines',
    marker=dict(
        color='#B292EA',
    ),
    name='Original Plot'
)

trace2 = go.Scatter(
    x=[j for j in range(len(time_series))],
    y=baseline_values,
    mode='markers',
    marker=dict(
        size=3,
        color='#EB55BF',
        symbol='circle-open'
    ),
    name='Baseline'
)

data = [trace, trace2]
py.iplot(data, filename='milk-production-plot-with-baseline')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'python-Baseline-Detection.ipynb', 'python/baseline-detection/', 'Baseline Detection | plotly',
    'Learn how to detect baselines on data in Python.',
    title='Baseline Detection in Python | plotly',
    name='Baseline Detection',
    language='python',
    page_type='example_index', has_thumbnail='false', display_as='peak-analysis', order=1,
    ipynb= '~notebook_demo/117')
```

```python

```
