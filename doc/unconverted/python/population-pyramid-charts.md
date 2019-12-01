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
    display_name: Python 3
    language: python
    name: python3
  plotly:
    description: How to make Population Pyramid Charts in Python with Plotly.
    display_as: basic
    language: python
    layout: base
    name: Population Pyramid Charts
    order: 5.01
    page_type: u-guide
    permalink: python/population-pyramid-charts/
    thumbnail: thumbnail/pyramid.jpg
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Basic Population Pyramid Chart
If you're starting with binned data, use a `go.Bar` trace.

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

women_bins = np.array([-600, -623, -653, -650, -670, -578, -541, -411, -322, -230])
men_bins = np.array([600, 623, 653, 650, 670, 578, 541, 360, 312, 170])

y = list(range(0, 100, 10))

layout = go.Layout(yaxis=go.layout.YAxis(title='Age'),
                   xaxis=go.layout.XAxis(
                       range=[-1200, 1200],
                       tickvals=[-1000, -700, -300, 0, 300, 700, 1000],
                       ticktext=[1000, 700, 300, 0, 300, 700, 1000],
                       title='Number'),
                   barmode='overlay',
                   bargap=0.1)

data = [go.Bar(y=y,
               x=men_bins,
               orientation='h',
               name='Men',
               hoverinfo='x',
               marker=dict(color='powderblue')
               ),
        go.Bar(y=y,
               x=women_bins,
               orientation='h',
               name='Women',
               text=-1 * women_bins.astype('int'),
               hoverinfo='text',
               marker=dict(color='seagreen')
               )]

py.iplot(dict(data=data, layout=layout), filename='EXAMPLES/bar_pyramid')
```

#### Stacked Population Pyramid

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

women_bins = np.array([-600, -623, -653, -650, -670, -578, -541, -411, -322, -230])
men_bins = np.array([600, 623, 653, 650, 670, 578, 541, 360, 312, 170])
women_with_dogs_bins = np.array([-0, -3, -308, -281, -245, -231, -212, -132, -74, -76])
men_with_dogs_bins = np.array([0, 1, 300, 273, 256, 211, 201, 170, 145, 43])

y = list(range(0, 100, 10))

layout = go.Layout(yaxis=go.layout.YAxis(title='Age'),
                   xaxis=go.layout.XAxis(
                       range=[-1200, 1200],
                       tickvals=[-1000, -700, -300, 0, 300, 700, 1000],
                       ticktext=[1000, 700, 300, 0, 300, 700, 1000],
                       title='Number'),
                   barmode='overlay',
                   bargap=0.1)

data = [go.Bar(y=y,
               x=men_bins,
               orientation='h',
               name='Men',
               hoverinfo='x',
               marker=dict(color='powderblue')
               ),
        go.Bar(y=y,
               x=women_bins,
               orientation='h',
               name='Women',
               text=-1 * women_bins.astype('int'),
               hoverinfo='text',
               marker=dict(color='seagreen')
               ),
        go.Bar(y=y,
               x=men_with_dogs_bins,
               orientation='h',
               hoverinfo='x',
               showlegend=False,
               opacity=0.5,
               marker=dict(color='teal')
               ),
        go.Bar(y=y,
               x=women_with_dogs_bins,
               orientation='h',
               text=-1 * women_bins.astype('int'),
               hoverinfo='text',
               showlegend=False,
               opacity=0.5,
               marker=dict(color='darkgreen')
               )]

py.iplot(dict(data=data, layout=layout), filename='EXAMPLES/stacked_bar_pyramid')
```

#### Population Pyramid with Binning
If you want to quickly create a Population Pyramid from raw data, try `go.Histogram`.

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

layout = go.Layout(barmode='overlay',
                   yaxis=go.layout.YAxis(range=[0, 90], title='Age'),
                   xaxis=go.layout.XAxis(
                       tickvals=[-150, -100, -50, 0, 50, 100, 150],
                       ticktext=[150, 100, 50, 0, 50, 100, 150],
                       title='Number'))

data = [go.Histogram(
    y=np.random.exponential(50, 1000),
    orientation='h',
    name='Men',
    marker=dict(color='plum'),
    hoverinfo='skip'
),
    go.Histogram(
        y=np.random.exponential(55, 1000),
        orientation='h',
        name='Women',
        marker=dict(color='purple'),
        hoverinfo='skip',
        x=-1 * np.ones(1000),
        histfunc="sum"
    )
]

py.iplot(dict(data=data, layout=layout), filename='EXAMPLES/histogram_pyramid')
```

### More Bar and Histogram Examples
See more examples of [horizontal bar charts](https://plot.ly/python/horizontal-bar-charts/), [bar charts](https://plot.ly/python/bar-charts/) and [histograms](https://plot.ly/python/histograms/).


### Reference
See https://plot.ly/python/reference/#bar and https://plot.ly/python/reference/#histogram for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'pyramid-charts.ipynb', 'python/population-pyramid-charts/', 'Python Population Pyramid Charts | Plotly',
    'How to make Population Pyramid Charts in Python with Plotly.',
    title = 'Population Pyramid Charts | Plotly',
    name = 'Population Pyramid Charts',
    thumbnail='thumbnail/pyramid.jpg', language='python',
    has_thumbnail='true', display_as='basic', order=5.01,
    ipynb= '~notebook_demo/221')
```

```python

```
