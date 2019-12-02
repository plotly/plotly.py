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
    description: Learn how to plot statistical data with various charts using Python.
    display_as: statistics
    has_thumbnail: false
    language: python
    layout: base
    name: Statistics Charts
    order: 5
    page_type: example_index
    permalink: python/statistics-charts/
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


For this example we will use some real data of wind speeds sampled every 10 minutes.

```python
wind_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/wind_speed_laurel_nebraska.csv')
df = wind_data[0:10]

table = FF.create_table(df)
py.iplot(table, filename='wind-data-sample')
```

#### Histogram


We will be producing a `histogram` with the "10 Min Std Dev" column of our data. For more info on the histogram charts, you can checkout the [documentation page](https://plot.ly/python/histograms/).

```python
data = [
    go.Histogram(
        x=wind_data['10 Min Std Dev'],
        histnorm='probability'
    )
]
py.iplot(data, filename='wind-data-histogram')
```

#### Box Plots


We will be producing a `box plot` with the "10 Min Std Dev" column of our data again. For more info on the histogram charts, you can checkout the [documentation page](https://plot.ly/python/box-plots/).

```python
data = [
    go.Box(
        y=wind_data['10 Min Std Dev'],
    )
]

py.iplot(data, filename='wind-data-box-plot')
```

#### Scatterplot Matrix


We will be producing a `scatterplot matrix` with all the columns of our data. For more info on the histogram charts, you can checkout the [documentation page](https://plot.ly/python/scatterplot-matrix/).

```python
fig = FF.create_scatterplotmatrix(wind_data,
                                  height=1000,
                                  width=1000,
                                  title='Wind Data - Scatterplot Matrix')
py.iplot(fig, filename='wind-data-scatterplot-matrix')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'python-Statistics-Charts.ipynb', 'python/statistics-charts/', 'Statistics Charts | plotly',
    'Learn how to plot statistical data with various charts using Python.',
    title='Statistics Charts in Python. | plotly',
    name='Statistics Charts',
    language='python',
    page_type='example_index', has_thumbnail='false', display_as='statistics', order=5,
    ipynb= '~notebook_demo/116')
```

```python

```
