---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.7
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.6.5
  plotly:
    description: How to use aggregates in Python with Plotly.
    display_as: transforms
    language: python
    layout: base
    name: Aggregations
    order: 3
    page_type: example_index
    permalink: python/aggregations/
    thumbnail: thumbnail/aggregations.jpg
---

#### Introduction

Aggregates are a type of transform that can be applied to values in a given expression. Available aggregations are:

Function | Description
------------- | -------------
`count` | Returns the quantity of items for each group.
`sum` | Returns the summation of all numeric values.
`avg` | Returns the average of all numeric values.
`median` | Returns the median of all numeric values.
`mode` | Returns the mode of all numeric values.
`rms` | Returns the rms of all numeric values.
`stddev` | Returns the standard deviation of all numeric values.
`min` | Returns the minimum numeric value for each group.
`max` | Returns the maximum numeric value for each group.
`first` | Returns the first numeric value for each group.
`last` | Returns the last numeric value for each group.


#### Basic Example

```python
import plotly.io as pio

subject = ['Moe','Larry','Curly','Moe','Larry','Curly','Moe','Larry','Curly','Moe','Larry','Curly']
score = [1,6,2,8,2,9,4,5,1,5,2,8]

data = [dict(
  type = 'scatter',
  x = subject,
  y = score,
  mode = 'markers',
  transforms = [dict(
    type = 'aggregate',
    groups = subject,
    aggregations = [dict(
        target = 'y', func = 'sum', enabled = True),
    ]
  )]
)]

fig_dict = dict(data=data)

pio.show(fig_dict, validate=False)
```

#### Aggregate Functions

```python
import plotly.io as pio

subject = ['Moe','Larry','Curly','Moe','Larry','Curly','Moe','Larry','Curly','Moe','Larry','Curly']
score = [1,6,2,8,2,9,4,5,1,5,2,8]

aggs = ["count","sum","avg","median","mode","rms","stddev","min","max","first","last"]

agg = []
agg_func = []
for i in range(0, len(aggs)):
    agg = dict(
        args=['transforms[0].aggregations[0].func', aggs[i]],
        label=aggs[i],
        method='restyle'
    )
    agg_func.append(agg)


data = [dict(
  type = 'scatter',
  x = subject,
  y = score,
  mode = 'markers',
  transforms = [dict(
    type = 'aggregate',
    groups = subject,
    aggregations = [dict(
        target = 'y', func = 'sum', enabled = True)
    ]
  )]
)]

layout = dict(
  title = '<b>Plotly Aggregations</b><br>use dropdown to change aggregation',
  xaxis = dict(title = 'Subject'),
  yaxis = dict(title = 'Score', range = [0,22]),
  updatemenus = [dict(
        x = 0.85,
        y = 1.15,
        xref = 'paper',
        yref = 'paper',
        yanchor = 'top',
        active = 1,
        showactive = False,
        buttons = agg_func
  )]
)

fig_dict = dict(data=data, layout=layout)

pio.show(fig_dict, validate=False)
```

#### Histogram Binning

```python
import plotly.io as pio

import pandas as pd

df = pd.read_csv("https://plot.ly/~public.health/17.csv")

data = [dict(
  x = df['date'],
  autobinx = False,
  autobiny = True,
  marker = dict(color = 'rgb(68, 68, 68)'),
  name = 'date',
  type = 'histogram',
  xbins = dict(
    end = '2016-12-31 12:00',
    size = 'M1',
    start = '1983-12-31 12:00'
  )
)]

layout = dict(
  paper_bgcolor = 'rgb(240, 240, 240)',
  plot_bgcolor = 'rgb(240, 240, 240)',
  title = '<b>Shooting Incidents</b>',
  xaxis = dict(
    title = '',
    type = 'date'
  ),
  yaxis = dict(
    title = 'Shootings Incidents',
    type = 'linear'
  ),
  updatemenus = [dict(
        x = 0.1,
        y = 1.15,
        xref = 'paper',
        yref = 'paper',
        yanchor = 'top',
        active = 1,
        showactive = True,
        buttons = [
        dict(
            args = ['xbins.size', 'D1'],
            label = 'Day',
            method = 'restyle',
        ), dict(
            args = ['xbins.size', 'M1'],
            label = 'Month',
            method = 'restyle',
        ), dict(
            args = ['xbins.size', 'M3'],
            label = 'Quater',
            method = 'restyle',
        ), dict(
            args = ['xbins.size', 'M6'],
            label = 'Half Year',
            method = 'restyle',
        ), dict(
            args = ['xbins.size', 'M12'],
            label = 'Year',
            method = 'restyle',
        )]
  )]
)

fig_dict = dict(data=data, layout=layout)

pio.show(fig_dict, validate=False)
```

#### Mapping with Aggregates

```python
import plotly.io as pio

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/bcdunbar/datasets/master/worldhappiness.csv")

aggs = ["count","sum","avg","median","mode","rms","stddev","min","max","first","last"]

agg = []
agg_func = []
for i in range(0, len(aggs)):
    agg = dict(
        args=['transforms[0].aggregations[0].func', aggs[i]],
        label=aggs[i],
        method='restyle'
    )
    agg_func.append(agg)

data = [dict(
  type = 'choropleth',
  locationmode = 'country names',
  locations = df['Country'],
  z = df['HappinessScore'],
  autocolorscale = False,
  colorscale = 'Portland',
  reversescale = True,
  transforms = [dict(
    type = 'aggregate',
    groups = df['Country'],
    aggregations = [dict(
        target = 'z', func = 'sum', enabled = True)
    ]
  )]
)]

layout = dict(
  title = '<b>Plotly Aggregations</b><br>use dropdown to change aggregation',
  xaxis = dict(title = 'Subject'),
  yaxis = dict(title = 'Score', range = [0,22]),
  height = 600,
  width = 900,
  updatemenus = [dict(
        x = 0.85,
        y = 1.15,
        xref = 'paper',
        yref = 'paper',
        yanchor = 'top',
        active = 1,
        showactive = False,
        buttons = agg_func
  )]
)

fig_dict = dict(data=data, layout=layout)

pio.show(fig_dict, validate=False)
```

#### Reference
See https://plot.ly/python/reference/ for more information and chart attribute options!
