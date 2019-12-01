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
    description: How to use multiple transforms (filter, group by, and aggregates)
      in Python with Plotly.
    display_as: transforms
    language: python
    layout: base
    name: Multiple Transforms
    order: 4
    page_type: example_index
    permalink: python/multiple-transforms/
    thumbnail: thumbnail/multiple-transforms.jpg
---

#### Filter and Group By

```python
import plotly.io as pio

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")

colors = ['blue', 'orange', 'green', 'red', 'purple']

opt = []
opts = []
for i in range(0, len(colors)):
    opt = dict(
        target = df['continent'][[i]].unique(), value = dict(marker = dict(color = colors[i]))
    )
    opts.append(opt)

data = [dict(
  type = 'scatter',
  mode = 'markers',
  x = df['lifeExp'],
  y = df['gdpPercap'],
  text = df['continent'],
  hoverinfo = 'text',
  opacity = 0.8,
  marker = dict(
      size = df['pop'],
      sizemode = 'area',
      sizeref = 200000
  ),
  transforms = [
      dict(
        type = 'filter',
        target = df['year'],
        orientation = '=',
        value = 2007
      ),
      dict(
        type = 'groupby',
        groups = df['continent'],
        styles = opts
    )]
)]

layout = dict(
    yaxis = dict(
        type = 'log'
    )
)

fig_dict = dict(data=data, layout=layout)
pio.show(fig_dict, validate=False)
```

#### Filter and Aggregate

```python
import plotly.io as pio
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")

data = [dict(
  type = 'scatter',
  mode = 'markers',
  x = df['lifeExp'],
  y = df['gdpPercap'],
  text = df['continent'],
  hoverinfo = 'text',
  opacity = 0.8,
  marker = dict(
      size = df['pop'],
      sizemode = 'area',
      sizeref = 200000
  ),
  transforms = [
      dict(
        type = 'filter',
        target = df['year'],
        orientation = '=',
        value = 2007
      ),
      dict(
        type = 'aggregate',
        groups = df['continent'],
        aggregations = [
            dict(target = 'x', func = 'avg'),
            dict(target = 'y', func = 'avg'),
            dict(target = 'marker.size', func = 'sum')
        ]
      )]
)]

layout = dict(
    yaxis = dict(
        type = 'log'
    )
)


fig_dict = dict(data=data, layout=layout)

pio.show(fig_dict, validate=False)
```

#### All Transforms

```python
import plotly.io as pio

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")

colors = ['blue', 'orange', 'green', 'red', 'purple']

opt = []
opts = []
for i in range(0, len(colors)):
    opt = dict(
        target = df['continent'][[i]].unique(), value = dict(marker = dict(color = colors[i]))
    )
    opts.append(opt)

data = [dict(
  type = 'scatter',
  mode = 'markers',
  x = df['lifeExp'],
  y = df['gdpPercap'],
  text = df['continent'],
  hoverinfo = 'text',
  opacity = 0.8,
  marker = dict(
      size = df['pop'],
      sizemode = 'area',
      sizeref = 200000
  ),
  transforms = [
      dict(
        type = 'filter',
        target = df['year'],
        orientation = '=',
        value = 2007
      ),
      dict(
        type = 'groupby',
        groups = df['continent'],
        styles = opts
      ),
      dict(
        type = 'aggregate',
        groups = df['continent'],
        aggregations = [
            dict(target = 'x', func = 'avg'),
            dict(target = 'y', func = 'avg'),
            dict(target = 'marker.size', func = 'sum')
        ]
      )]
)]

layout = dict(
    title = '<b>Gapminder</b><br>2007 Average GDP Per Cap & Life Exp. by Continent',
    yaxis = dict(
        type = 'log'
    )
)

fig_dict = dict(data=data, layout=layout)
pio.show(fig_dict, validate=False)
```

#### Reference
See https://plot.ly/python/reference/ for more information and chart attribute options!
