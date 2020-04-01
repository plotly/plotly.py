---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.1
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
    description: How to plot date and time in python.
    display_as: financial
    language: python
    layout: base
    name: Time Series and Date Axes
    order: 1
    page_type: example_index
    permalink: python/time-series/
    thumbnail: thumbnail/time-series.jpg
---

### Time Series using Axes of type `date`

Time series can be represented using either `plotly.express` functions (`px.line`, `px.scatter`, `px.bar` etc) or `plotly.graph_objects` charts objects (`go.Scatter`, `go.Bar` etc). For more examples of such charts, see the documentation of [line and scatter plots](https://plotly.com/python/line-and-scatter/) or [bar charts](/python/bar-charts/).

For financial applications, Plotly can also be used to create [Candlestick charts](/python/candlestick-charts/) and [OHLC charts](/python/ohlc-charts/), which default to date axes.

Plotly auto-sets the axis type to a date format when the corresponding data are either ISO-formatted date strings or if they're a [date pandas column](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html) or [datetime NumPy array](https://docs.scipy.org/doc/numpy/reference/arrays.datetime.html).

```python
# Using plotly.express
import plotly.express as px

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = px.line(df, x='Date', y='AAPL.High')
fig.show()
```

```python
# Using graph_objects
import plotly.graph_objects as go

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = go.Figure([go.Scatter(x=df['Date'], y=df['AAPL.High'])])
fig.show()
```

### Time Series Plot with Custom Date Range

The data range can be set manually using either `datetime.datetime` objects, or date strings.

```python
# Using plotly.express
import plotly.express as px

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = px.line(df, x='Date', y='AAPL.High', range_x=['2016-07-01','2016-12-31'])
fig.show()
```

```python
# Using graph_objects

import plotly.graph_objects as go
import datetime

x = [datetime.datetime(year=2013, month=10, day=4),
     datetime.datetime(year=2013, month=11, day=5),
     datetime.datetime(year=2013, month=12, day=6)]

fig = go.Figure(data=[go.Scatter(x=x, y=[1, 3, 6])])
# Use datetime objects to set xaxis range
fig.update_layout(xaxis_range=[datetime.datetime(2013, 10, 17),
                               datetime.datetime(2013, 11, 20)])
fig.show()
```

```python
import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = px.line(df, x='Date', y='AAPL.High')

# Use date string to set xaxis range
fig.update_layout(xaxis_range=['2016-07-01','2016-12-31'],
                  title_text="Manually Set Date Range")
fig.show()
```

### Time Series With Range Slider

A range slider is a small subplot-like area below a plot which allows users to pan and zoom the X-axis while maintaining an overview of the chart. Check out the reference for more options: https://plotly.com/python/reference/#layout-xaxis-rangeslider

```python
import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = px.line(df, x='Date', y='AAPL.High', title='Time Series with Rangeslider')

fig.update_xaxes(rangeslider_visible=True)
fig.show()
```

### Time Series with Range Selector Buttons

Range selector buttons are special controls that work well with time series and range sliders, and allow users to easily set the range of the x-axis. Check out the reference for more options: https://plotly.com/python/reference/#layout-xaxis-rangeselector

```python
import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = px.line(df, x='Date', y='AAPL.High', title='Time Series with Range Slider and Selectors')

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
fig.show()
```

### Customizing Tick Label Formatting by Zoom Level

The `tickformatstops` attribute can be used to customize the formatting of tick labels depending on the zoom level. Try zooming in to the chart below and see how the tick label formatting changes. Check out the reference for more options: https://plotly.com/python/reference/#layout-xaxis-tickformatstops

```python
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = go.Figure(go.Scatter(
    x = df['Date'],
    y = df['mavg']
))

fig.update_xaxes(
    rangeslider_visible=True,
    tickformatstops = [
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

### Hiding Weekends and Holidays

The `rangebreaks` attribute available on x- and y-axes of type `date` can be used to hide certain time-periods. In the example below, we show two plots: one in default mode to show gaps in the data, and one where we hide weekends and holidays to show an uninterrupted trading history. Note the smaller gaps between the grid lines for December 21 and January 4, where holidays were removed. Check out the reference for more options: https://plotly.com/python/reference/#layout-xaxis-rangebreaks

```python
import plotly.express as px
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = px.scatter(df, x='Date', y='AAPL.High', range_x=['2015-12-01', '2016-01-15'],
                 title="Default Display with Gaps")
fig.show()
```

```python
import plotly.express as px
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = px.scatter(df, x='Date', y='AAPL.High', range_x=['2015-12-01', '2016-01-15'],
                 title="Hide Gaps with rangebreaks")
fig.update_xaxes(
    rangebreaks=[
        dict(bounds=["sat", "mon"]), #hide weekends
        dict(values=["2015-12-25", "2016-01-01"]) #hide Christmas and New Year's
    ]
)
fig.show()
```
