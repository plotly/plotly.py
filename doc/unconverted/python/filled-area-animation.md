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
    description: How to make an animated filled-area plot with apple stock data in
      Python.
    display_as: animations
    language: python
    layout: base
    name: Filled-Area Animation
    order: 3
    page_type: example_index
    permalink: python/filled-area-animation/
    thumbnail: thumbnail/apple_stock_animation.gif
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Version Check
Note: Animations are available in version 1.12.10+
Run `pip install plotly --upgrade` to update your Plotly version.

```python
import plotly
plotly.__version__
```

#### Import Data
Let us import some apple stock data for this animation.

```python
import plotly.plotly as py
from plotly.grid_objs import Grid, Column
from plotly.tools import FigureFactory as FF

import time
from datetime import datetime
import numpy as np
import pandas as pd

appl = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
appl.columns = [col.replace('AAPL.', '') for col in appl.columns]
apple_data_matrix = appl.head(10).round(2)

table = FF.create_table(apple_data_matrix)
py.iplot(table, filename='apple_data_table')
```

#### Make the Grid

```python
def to_unix_time(dt):
    epoch =  datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000

appl_price = list(appl['Adjusted'])
my_columns = []
for k in range(len(appl.Date) - 1):
    my_columns.append(Column(list(appl.Date)[:k + 1], 'x{}'.format(k + 1)))
    my_columns.append(Column(appl_price[:k + 1], 'y{}'.format(k + 1)))
grid = Grid(my_columns)
py.grid_ops.upload(grid, 'AAPL-daily-stock-price' + str(time.time()), auto_open=False)
```

#### Make the Figure

```python
data=[dict(type='scatter',
           xsrc=grid.get_column_reference('x1'),
           ysrc= grid.get_column_reference('y1'),
           name='AAPL',
           mode='lines',
           line=dict(color= 'rgb(114, 186, 59)'),
           fill='tozeroy',
           fillcolor='rgba(114, 186, 59, 0.5)')]

axis=dict(ticklen=4,
          mirror=True,
          zeroline=False,
          showline=True,
          autorange=False,
          showgrid=False)

layout = dict(title='AAPL Daily Stock Price',
              font=dict(family='Balto'),
              showlegend=False,
              autosize=False,
              width=800,
              height=400,
              xaxis=dict(axis, **{'nticks':12, 'tickangle':-45,
                                  'range': [to_unix_time(datetime(2015, 2, 17)),
                                            to_unix_time(datetime(2016, 11, 30))]}),
              yaxis=dict(axis, **{'title': '$', 'range':[0,170]}),
              updatemenus=[dict(type='buttons',
                                showactive=False,
                                y=1,
                                x=1.1,
                                xanchor='right',
                                yanchor='top',
                                pad=dict(t=0, r=10),
                                buttons=[dict(label='Play',
                                              method='animate',
                                              args=[None, dict(frame=dict(duration=50, redraw=False),
                                                               transition=dict(duration=0),
                                                               fromcurrent=True,
                                                               mode='immediate')])])])

frames=[{'data':[{'xsrc': grid.get_column_reference('x{}'.format(k + 1)),
                  'ysrc': grid.get_column_reference('y{}'.format(k + 1))}],
         'traces': [0]
        } for k in range(len(appl.Date) - 1)]

fig=dict(data=data, layout=layout, frames=frames)
py.icreate_animations(fig, 'AAPL-stockprice' + str(time.time()))
```

#### Reference
For additional information on filled area plots in Plotly see: https://plot.ly/python/filled-area-plots/.
For more documentation on creating animations with Plotly, see https://plot.ly/python/#animations.

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

!pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'filled-area-animation.ipynb', 'python/filled-area-animation/', 'Filled-Area Animation | plotly',
    'How to make an animated filled-area plot with apple stock data in Python.',
    title='Filled-Area Animation | plotly',
    name='Filled-Area Animation',
    language='python',
    page_type='example_index', has_thumbnail='true', thumbnail='thumbnail/apple_stock_animation.gif',
    display_as='animations', ipynb= '~notebook_demo/128', order=3)
```

```python

```
