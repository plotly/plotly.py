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
    description: Create a exponential fit / regression in Python and add a line of
      best fit to your chart.
    display_as: statistics
    language: python
    layout: base
    name: Exponential Fit
    order: 11
    page_type: example_index
    permalink: python/exponential-fits/
    thumbnail: thumbnail/exponential_fit.jpg
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Version Check
Note: exponential fits are available in version <b>1.9.2+</b><br>
Run  `pip install plotly --upgrade` to update your Plotly version

```python
import plotly
plotly.__version__
```

### Exponential Fit

```python
# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
import plotly.graph_objs as go

# Scientific libraries
import numpy as np
from scipy.optimize import curve_fit


x = np.array([399.75, 989.25, 1578.75, 2168.25, 2757.75, 3347.25, 3936.75, 4526.25, 5115.75, 5705.25])
y = np.array([109,62,39,13,10,4,2,0,1,2])

def exponenial_func(x, a, b, c):
    return a*np.exp(-b*x)+c


popt, pcov = curve_fit(exponenial_func, x, y, p0=(1, 1e-6, 1))

xx = np.linspace(300, 6000, 1000)
yy = exponenial_func(xx, *popt)

# Creating the dataset, and generating the plot
trace1 = go.Scatter(
                  x=x,
                  y=y,
                  mode='markers',
                  marker=go.Marker(color='rgb(255, 127, 14)'),
                  name='Data'
                  )

trace2 = go.Scatter(
                  x=xx,
                  y=yy,
                  mode='lines',
                  marker=go.Marker(color='rgb(31, 119, 180)'),
                  name='Fit'
                  )

annotation = go.Annotation(
                  x=2000,
                  y=100,
                  text='$\textbf{Fit}: 163.56e^{-0.00097x} - 1.16$',
                  showarrow=False
                  )
layout = go.Layout(
                title='Exponential Fit in Python',
                plot_bgcolor='rgb(229, 229, 229)',
                  xaxis=go.XAxis(zerolinecolor='rgb(255,255,255)', gridcolor='rgb(255,255,255)'),
                  yaxis=go.YAxis(zerolinecolor='rgb(255,255,255)', gridcolor='rgb(255,255,255)'),
                  annotations=[annotation]
                )

data = [trace1, trace2]
fig = go.Figure(data=data, layout=layout)

py.plot(fig, filename='Exponential-Fit-in-python')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'Exponential-fits.ipynb', 'python/exponential-fits/', 'Exponential Fit',
    'Create a exponential fit / regression in Python and add a line of best fit to your chart.',
    title = 'Exponential Fit',
    name = 'Exponential Fit',
    has_thumbnail='true', thumbnail='thumbnail/exponential_fit.jpg',
    language='python', page_type='example_index',
    display_as='statistics', order=11,
    ipynb= '~notebook_demo/135')
```

```python

```
