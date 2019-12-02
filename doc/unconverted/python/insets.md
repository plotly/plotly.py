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
    description: How to make an inset graph in python.
    display_as: multiple_axes
    language: python
    layout: base
    name: Inset Plots
    order: 3
    page_type: example_index
    permalink: python/insets/
    thumbnail: thumbnail/insets.jpg
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


### Simple Inset Graph

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[1, 2, 3],
    y=[4, 3, 2]
)
trace2 = go.Scatter(
    x=[20, 30, 40],
    y=[30, 40, 50],
    xaxis='x2',
    yaxis='y2'
)
data = [trace1, trace2]
layout = go.Layout(
    xaxis2=dict(
        domain=[0.6, 0.95],
        anchor='y2'
    ),
    yaxis2=dict(
        domain=[0.6, 0.95],
        anchor='x2'
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='simple-inset')

```

### Reference


See https://plot.ly/python/reference/#layout-scene for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

!pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'inset.ipynb', 'python/insets/', 'Inset Plots | plotly',
    'How to make an inset graph in python.',
    title = 'Inset Plots | plotly',
    name = 'Inset Plots',
    has_thumbnail='true', thumbnail='thumbnail/insets.jpg',
    language='python', page_type='example_index',
    display_as='multiple_axes', order=3)
```

```python

```
