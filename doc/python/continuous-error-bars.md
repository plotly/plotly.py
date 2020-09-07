---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.2
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
    version: 3.7.7
  plotly:
    description: Add continuous error bands to charts in Python with Plotly.
    display_as: statistical
    language: python
    layout: base
    name: Continuous Error Bands
    order: 15
    page_type: u-guide
    permalink: python/continuous-error-bars/
    thumbnail: thumbnail/error-cont.jpg
---

Continuous error bands are a graphical representation of error or uncertainty as a shaded region around a main trace, rather than as discrete whisker-like error bars. They can be implemented in a manner similar to [filled area plots](/python/filled-area-plots/) using `scatter` traces with the `fill` attribute.

#### Filling within a single trace

In this example we show how to construct a trace that goes from low to high X values along the upper Y edge of a region, and then from high to low X values along the lower Y edge of the region. This trace is then 'self-filled' using `fill='toself'`.

```python
import plotly.graph_objs as go

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 2, 7, 4, 5, 6, 7, 8, 9, 10]
y_upper = [2, 3, 8, 5, 6, 7, 8, 9, 10, 11]
y_lower = [0, 1, 5, 3, 4, 5, 6, 7, 8, 9]


fig = go.Figure([
    go.Scatter(
        x=x,
        y=y,
        line=dict(color='rgb(0,100,80)'),
        mode='lines'
    ),
    go.Scatter(
        x=x+x[::-1], # x, then x reversed
        y=y_upper+y_lower[::-1], # upper, then lower reversed
        fill='toself',
        fillcolor='rgba(0,100,80,0.2)',
        line=dict(color='rgba(255,255,255,0)'),
        hoverinfo="skip",
        showlegend=False
    )
])
fig.show()
```

#### Filling between two traces

In this example we show how to construct the bounds of the band using two traces, with the lower trace using `fill='tonexty'` to fill an area up to the upper trace.

```python
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/wind_speed_laurel_nebraska.csv')

fig = go.Figure([
    go.Scatter(
        name='Measurement',
        x=df['Time'],
        y=df['10 Min Sampled Avg'],
        mode='lines',
        line=dict(color='rgb(31, 119, 180)'),
    ),
    go.Scatter(
        name='Upper Bound',
        x=df['Time'],
        y=df['10 Min Sampled Avg']+df['10 Min Std Dev'],
        mode='lines',
        marker=dict(color="#444"),
        line=dict(width=0),
        showlegend=False
    ),
    go.Scatter(
        name='Lower Bound',
        x=df['Time'],
        y=df['10 Min Sampled Avg']-df['10 Min Std Dev'],
        marker=dict(color="#444"),
        line=dict(width=0),
        mode='lines',
        fillcolor='rgba(68, 68, 68, 0.3)',
        fill='tonexty',
        showlegend=False
    )
])
fig.update_layout(
    yaxis_title='Wind speed (m/s)',
    title='Continuous, variable value error bars',
    hovermode="x"
)
fig.show()
```
