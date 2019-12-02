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
    description: Legacy polar charts in python.
    display_as: legacy_charts
    language: python
    layout: base
    name: Polar Charts [Legacy]
    order: 1
    page_type: u-guide
    permalink: python/legacy-polar-chart/
    thumbnail: thumbnail/polar-scatter.jpg
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Legacy Plot


These polar charts are legacy and will likely be deprecated in [Plotly 2.0](https://github.com/plotly/plotly.js/issues/420). Please see the new `scatterpolar` and `scatterpolargl` [trace types](https://plot.ly/python/polar-chart/) for latest and greatest in Plotly polar coordinates.


#### Basic Polar Chart

```python
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('polar_dataset.csv')

trace1 = go.Scatter(
    r=df['x1'],
    t=df['y'],
    mode='lines',
    name='go.Figure8',
    marker=dict(
        color='none',
        line=dict(
            color='peru'
        )
    )
)
trace2 = go.Scatter(
    r=df['x2'],
    t=df['y'],
    mode='lines',
    name='Cardioid',
    marker=dict(
        color='none',
        line=dict(
            color='darkviolet'
        )
    )
)
trace3 = go.Scatter(
    r=df['x3'],
    t=df['y'],
    mode='lines',
    name='Hypercardioid',
    marker=dict(
        color='none',
        line=dict(
            color='deepskyblue'
        )
    )
)
trace4 = go.Scatter(
    r=df['x4'],
    t=df['y'],
    mode='lines',
    name='Subcardioid',
    marker=dict(
        color='none',
        line=dict(
            color='orangered'
        )
    )
)
trace5 = go.Scatter(
    r=df['x5'],
    t=df['y'],
    mode='lines',
    name='Supercardioid',
    marker=dict(
        color='none',
        line=dict(
            color='green'
        )
    )
)
data = [trace1, trace2, trace3, trace4, trace5]
layout = go.Layout(
    title='Mic Patterns',
    font=dict(
        family='Arial, sans-serif;',
        size=12,
        color='#000'
    ),
    orientation=-90
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='polar-line')
```

#### Polar Scatter Chart

```python
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

trace1 = go.Scatter(
    r = np.random.uniform(1,6,size=62),
    t = np.random.uniform(30,5,size=62),
    mode='markers',
    name='Trial 1',
    marker=dict(
        color='rgb(27,158,119)',
        size=110,
        line=dict(
            color='white'
        ),
        opacity=0.7
    )
)
trace2 = go.Scatter(
    r=np.random.uniform(3,8,size=62),
    t=np.random.uniform(-14,-76,size=62),
    mode='markers',
    name='Trial 2',
    marker=dict(
        color='rgb(217,95,2)',
        size=110,
        line=dict(
            color='white'
        ),
        opacity=0.7
    )
)
trace3 = go.Scatter(
    r=np.random.uniform(1,7,size=62),
    t=np.random.uniform(131,111,size=62),
    mode='markers',
    name='Trial 3',
    marker=dict(
        color='rgb(117,112,179)',
        size=110,
        line=dict(
            color='white'
        ),
        opacity=0.7
    )
)
trace4 = go.Scatter(
    r=np.random.uniform(1,9,size=62),
    t=np.random.uniform(-140,-177,size=62),
    mode='markers',
    name='Trial 4',
    marker=dict(
        color='rgb(231,41,138)',
        size=110,
        line=dict(
            color='white'
        ),
        opacity=0.7
    )
)
trace5 = go.Scatter(
    r=np.random.uniform(1,3,size=62),
    t=np.random.uniform(-100,-163,size=62),
    mode='markers',
    name='Trial 5',
    marker=dict(
        color='rgb(102,166,30)',
        size=110,
        line=dict(
            color='white'
        ),
        opacity=0.7
    )
)
trace6 = go.Scatter(
    r=np.random.uniform(0,5,size=62),
    t=np.random.uniform(66,47,size=62),
    mode='markers',
    name='Trial 6',
    marker=dict(
        color='rgb(230,171,2)',
        size=110,
        line=dict(
            color='white'
        ),
        opacity=0.7
    )
)
data = [trace1, trace2, trace3, trace4, trace5, trace6]
layout = go.Layout(
    title='Hobbs-Pearson Trials',
    font=dict(
        size=15
    ),
    plot_bgcolor='rgb(223, 223, 223)',
    angularaxis=dict(
        tickcolor='rgb(253,253,253)'
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)
```

#### Wind Rose Chart

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Area(
    r=[77.5, 72.5, 70.0, 45.0, 22.5, 42.5, 40.0, 62.5],
    t=['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
    name='11-14 m/s',
    marker=dict(
        color='rgb(106,81,163)'
    )
)
trace2 = go.Area(
    r=[57.49999999999999, 50.0, 45.0, 35.0, 20.0, 22.5, 37.5, 55.00000000000001],
    t=['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
    name='8-11 m/s',
    marker=dict(
        color='rgb(158,154,200)'
    )
)
trace3 = go.Area(
    r=[40.0, 30.0, 30.0, 35.0, 7.5, 7.5, 32.5, 40.0],
    t=['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
    name='5-8 m/s',
    marker=dict(
        color='rgb(203,201,226)'
    )
)
trace4 = go.Area(
    r=[20.0, 7.5, 15.0, 22.5, 2.5, 2.5, 12.5, 22.5],
    t=['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'],
    name='< 5 m/s',
    marker=dict(
        color='rgb(242,240,247)'
    )
)
data = [trace1, trace2, trace3, trace4]
layout = go.Layout(
    title='Wind Speed Distribution in Laurel, NE',
    font=dict(
        size=16
    ),
    legend=dict(
        font=dict(
            size=16
        )
    ),
    radialaxis=dict(
        ticksuffix='%'
    ),
    orientation=270
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='polar-area-chart')
```

#### Reference

See https://plot.ly/python/reference/#area for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'polar.ipynb', 'python/legacy-polar-chart/', 'Polar Charts [Legacy]',
    'Legacy polar charts in python.',
    title = 'Python Polar Charts | plotly',
    has_thumbnail='true', thumbnail='thumbnail/polar-scatter.jpg',
    language='python',
    display_as='legacy_charts', order=1,
    ipynb= '~notebook_demo/37')
```

```python

```
