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
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.6.8
  plotly:
    description: How to format axes ticks in Python with Plotly.
    display_as: file_settings
    language: python
    layout: base
    name: Formatting Ticks
    order: 11
    permalink: python/tick-formatting/
    thumbnail: thumbnail/tick-formatting.gif
---

#### Tickmode - Linear


If `"linear"`, the placement of the ticks is determined by a starting position `tick0` and a tick step `dtick`

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scatter(
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    y = [28.8, 28.5, 37, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9]
))

fig.update_layout(
    xaxis = dict(
        tickmode = 'linear',
        tick0 = 0.5,
        dtick = 0.75
    )
)

fig.show()
```

#### Tickmode - Array


If `"array"`, the placement of the ticks is set via `tickvals` and the tick text is `ticktext`.

```python
import plotly.graph_objects as go

go.Figure(go.Scatter(
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    y = [28.8, 28.5, 37, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9]
))

fig.update_layout(
    xaxis = dict(
        tickmode = 'array',
        tickvals = [1, 3, 5, 7, 9, 11],
        ticktext = ['One', 'Three', 'Five', 'Seven', 'Nine', 'Eleven']
    )
)

fig.show()
```

#### Using Tickformat Attribute


For more formatting types, see: https://github.com/d3/d3-format/blob/master/README.md#locale_format

```python
import plotly.graph_objects as go

go.Figure(go.Scatter(
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    y = [28.8, 28.5, 37, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9]
))

fig.update_layout(yaxis_tickformat = '%')

fig.show()
```

#### Using Tickformat Atttribute - Date/Time


For more date/time formatting types, see: https://github.com/d3/d3-time-format/blob/master/README.md

```python
import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = go.Figure(go.Scatter(
    x = df['Date'],
    y = df['AAPL.High'],
))

fig.update_layout(
    title = 'Time Series with Custom Date-Time Format',
    xaxis_tickformat = '%d %B (%a)<br>%Y'
)

fig.show()
```

#### Using Exponentformat Attribute

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scatter(
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    y = [68000, 52000, 60000, 20000, 95000, 40000, 60000, 79000, 74000, 42000, 20000, 90000]
))

fig.update_layout(
    yaxis = dict(
        showexponent = 'all',
        exponentformat = 'e'
    )
)

fig.show()
```

#### Tickformatstops to customize for different zoom levels

```python
import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = go.Figure(go.Scatter(
    x = df['Date'],
    y = df['mavg']
))

fig.update_layout(
    xaxis_tickformatstops = [
        dict(dtickrange=[None, 1000], value="%H:%M:%S.%L ms"),
        dict(dtickrange=[1000, 60000], value="%H:%M:%S s"),
        dict(dtickrange=[60000, 3600000], value="%H:%M m"),
        dict(dtickrange=[3600000, 86400000], value="%H:%M h"),
        dict(dtickrange=[86400000, 604800000], value="%e. %b d"),
        dict(dtickrange=[604800000, "M1"], value="%e. %b w"),
        dict(dtickrange=["M1", "M12"], value="%b '%y M"),
        dict(dtickrange=["M12", None], value="%Y Y")
    ]
)

fig.show()
```

#### Placing ticks and gridlines between categories

```python
import plotly.graph_objects as go

fig = go.Figure(go.Bar(
    x = ["apples", "oranges", "pears"],
    y = [1, 2, 3]
))

fig.update_xaxes(
    showgrid=True,
    ticks="outside",
    tickson="boundaries",
    ticklen=20
)

fig.show()
```

#### Reference
See https://plot.ly/python/reference/#layout-xaxis for more information and chart attribute options!

