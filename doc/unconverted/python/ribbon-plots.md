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
    description: How to make ribbon plots in Python.
    display_as: 3d_charts
    language: python
    layout: base
    name: Ribbon Plots
    order: 4
    permalink: python/ribbon-plots/
    thumbnail: thumbnail/ribbon-plot.jpg
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Basic Ribbon Plot

```python
import plotly.plotly as py
import plotly.graph_objs as go

import urllib
import numpy as np

url = "https://raw.githubusercontent.com/plotly/datasets/master/spectral.csv"
f = urllib.urlopen(url)
spectra=np.loadtxt(f, delimiter=',')

traces = []
y_raw = spectra[:, 0] # wavelength
sample_size = spectra.shape[1]-1
for i in range(1, sample_size):
    z_raw = spectra[:, i]
    x = []
    y = []
    z = []
    ci = int(255/sample_size*i) # ci = "color index"
    for j in range(0, len(z_raw)):
        z.append([z_raw[j], z_raw[j]])
        y.append([y_raw[j], y_raw[j]])
        x.append([i*2, i*2+1])
    traces.append(dict(
        z=z,
        x=x,
        y=y,
        colorscale=[ [i, 'rgb(%d,%d,255)'%(ci, ci)] for i in np.arange(0,1.1,0.1) ],
        showscale=False,
        type='surface',
    ))

fig = { 'data':traces, 'layout':{'title':'Ribbon Plot'} }
py.iplot(fig, filename='ribbon-plot-python')
```

#### Reference
See https://plot.ly/python/reference/#surface for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade

import publisher
publisher.publish(
    'ribbon.ipynb', 'python/ribbon-plots/', 'Python Ribbon Plots | plotly',
    'How to make ribbon plots in Python. ',
    title = 'Python Ribbon Plots | plotly',
    name = 'Ribbon Plots',
    has_thumbnail='true', thumbnail='thumbnail/ribbon-plot.jpg',
    language='python', page_type='example_index',
    display_as='3d_charts', order=4,
    ipynb= '~notebook_demo/64')
```

```python

```
