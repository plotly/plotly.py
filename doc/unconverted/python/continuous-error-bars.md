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
    description: Add continuous error bars to charts in Python with Plotly.
    display_as: statistical
    language: python
    layout: base
    name: Continuous Error Bars
    order: 2
    page_type: u-guide
    permalink: python/continuous-error-bars/
    thumbnail: thumbnail/error-cont.jpg
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Version Check
Plotly's Python API is updated frequently. Run `pip install plotly --upgrade` to update your version.

```python
import plotly
plotly.__version__
```

#### Basic Continuous Error Bars


```python
import plotly.plotly as py
import plotly.graph_objs as go

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x_rev = x[::-1]

# Line 1
y1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1_upper = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y1_lower = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y1_lower = y1_lower[::-1]

# Line 2
y2 = [5, 2.5, 5, 7.5, 5, 2.5, 7.5, 4.5, 5.5, 5]
y2_upper = [5.5, 3, 5.5, 8, 6, 3, 8, 5, 6, 5.5]
y2_lower = [4.5, 2, 4.4, 7, 4, 2, 7, 4, 5, 4.75]
y2_lower = y2_lower[::-1]

# Line 3
y3 = [10, 8, 6, 4, 2, 0, 2, 4, 2, 0]
y3_upper = [11, 9, 7, 5, 3, 1, 3, 5, 3, 1]
y3_lower = [9, 7, 5, 3, 1, -.5, 1, 3, 1, -1]
y3_lower = y3_lower[::-1]

trace1 = go.Scatter(
    x=x+x_rev,
    y=y1_upper+y1_lower,
    fill='tozerox',
    fillcolor='rgba(0,100,80,0.2)',
    line=dict(color='rgba(255,255,255,0)'),
    showlegend=False,
    name='Fair',
)
trace2 = go.Scatter(
    x=x+x_rev,
    y=y2_upper+y2_lower,
    fill='tozerox',
    fillcolor='rgba(0,176,246,0.2)',
    line=dict(color='rgba(255,255,255,0)'),
    name='Premium',
    showlegend=False,
)
trace3 = go.Scatter(
    x=x+x_rev,
    y=y3_upper+y3_lower,
    fill='tozerox',
    fillcolor='rgba(231,107,243,0.2)',
    line=dict(color='rgba(255,255,255,0)'),
    showlegend=False,
    name='Ideal',
)
trace4 = go.Scatter(
    x=x,
    y=y1,
    line=dict(color='rgb(0,100,80)'),
    mode='lines',
    name='Fair',
)
trace5 = go.Scatter(
    x=x,
    y=y2,
    line=dict(color='rgb(0,176,246)'),
    mode='lines',
    name='Premium',
)
trace6 = go.Scatter(
    x=x,
    y=y3,
    line=dict(color='rgb(231,107,243)'),
    mode='lines',
    name='Ideal',
)

data = [trace1, trace2, trace3, trace4, trace5, trace6]

layout = go.Layout(
    paper_bgcolor='rgb(255,255,255)',
    plot_bgcolor='rgb(229,229,229)',
    xaxis=dict(
        gridcolor='rgb(255,255,255)',
        range=[1,10],
        showgrid=True,
        showline=False,
        showticklabels=True,
        tickcolor='rgb(127,127,127)',
        ticks='outside',
        zeroline=False
    ),
    yaxis=dict(
        gridcolor='rgb(255,255,255)',
        showgrid=True,
        showline=False,
        showticklabels=True,
        tickcolor='rgb(127,127,127)',
        ticks='outside',
        zeroline=False
    ),
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename= 'shaded_lines')
```

#### Asymmetric Error Bars with a Constant Offset

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/wind_speed_laurel_nebraska.csv')

upper_bound = go.Scatter(
    name='Upper Bound',
    x=df['Time'],
    y=df['10 Min Sampled Avg']+df['10 Min Std Dev'],
    mode='lines',
    marker=dict(color="#444"),
    line=dict(width=0),
    fillcolor='rgba(68, 68, 68, 0.3)',
    fill='tonexty')

trace = go.Scatter(
    name='Measurement',
    x=df['Time'],
    y=df['10 Min Sampled Avg'],
    mode='lines',
    line=dict(color='rgb(31, 119, 180)'),
    fillcolor='rgba(68, 68, 68, 0.3)',
    fill='tonexty')

lower_bound = go.Scatter(
    name='Lower Bound',
    x=df['Time'],
    y=df['10 Min Sampled Avg']-df['10 Min Std Dev'],
    marker=dict(color="#444"),
    line=dict(width=0),
    mode='lines')

# Trace order can be important
# with continuous error bars
data = [lower_bound, trace, upper_bound]

layout = go.Layout(
    yaxis=dict(title='Wind speed (m/s)'),
    title='Continuous, variable value error bars.<br>Notice the hover text!',
    showlegend = False)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='pandas-continuous-error-bars')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

#! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'cont-error-bars.ipynb', 'python/continuous-error-bars/', 'Continuous Error Bars',
    'Add continuous error bars to charts in Python with Plotly.',
    title = 'Continuous Error Bars | plotly',
    name = 'Continuous Error Bars',
    thumbnail='thumbnail/error-cont.jpg', language='python',
    has_thumbnail='true', display_as='statistical', order=2,
    ipynb='~notebook_demo/19')
```

```python

```
