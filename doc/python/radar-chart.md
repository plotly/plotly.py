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
    version: 3.6.7
  plotly:
    description: How to make radar charts in Python with Plotly.
    display_as: scientific
    language: python
    layout: base
    name: Radar Charts
    order: 18
    page_type: u-guide
    permalink: python/radar-chart/
    thumbnail: thumbnail/radar.gif
---

A [Radar Chart](https://en.wikipedia.org/wiki/Radar_chart) (also known as a spider plot or star plot) displays multivariate data in the form of a two-dimensional chart of quantitative variables represented on axes originating from the center. The relative position and angle of the axes is typically uninformative.  It is equivalent to a [parallel coordinates plot](/python/parallel-coordinates-plot/) with the axes arranged radially.

For a Radar Chart, use a [polar chart](/python/polar-chart/) with categorical angular variables, with `px.line_polar` for data available as a tidy pandas DataFrame, or with `go.Scatterpolar` in the general case. See more examples of [polar charts here](/python/polar-chart/).

#### Radar Chart with Plotly Express

[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on "tidy" data](/python/px-arguments/).

Use `line_close=True` for closed lines.

```python
import plotly.express as px
import pandas as pd
df = pd.DataFrame(dict(
    r=[1, 5, 2, 2, 3],
    theta=['processing cost','mechanical properties','chemical stability',
           'thermal stability', 'device integration']))
fig = px.line_polar(df, r='r', theta='theta', line_close=True)
fig.show()
```

For a filled line in a Radar Chart, update the figure created with `px.line_polar` with `fig.update_traces`.

```python
import plotly.express as px
import pandas as pd
df = pd.DataFrame(dict(
    r=[1, 5, 2, 2, 3],
    theta=['processing cost','mechanical properties','chemical stability',
           'thermal stability', 'device integration']))
fig = px.line_polar(df, r='r', theta='theta', line_close=True)
fig.update_traces(fill='toself')
fig.show()
```

### Basic Radar Chart with go.Scatterpolar


```python
import plotly.graph_objects as go

fig = go.Figure(data=go.Scatterpolar(
  r=[1, 5, 2, 2, 3],
  theta=['processing cost','mechanical properties','chemical stability', 'thermal stability',
           'device integration'],
  fill='toself'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True
    ),
  ),
  showlegend=False
)

fig.show()
```

#### Multiple Trace Radar Chart

```python
import plotly.graph_objects as go

categories = ['processing cost','mechanical properties','chemical stability',
              'thermal stability', 'device integration']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=[1, 5, 2, 2, 3],
      theta=categories,
      fill='toself',
      name='Product A'
))
fig.add_trace(go.Scatterpolar(
      r=[4, 3, 2.5, 1, 2],
      theta=categories,
      fill='toself',
      name='Product B'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 5]
    )),
  showlegend=False
)

fig.show()
```

#### Reference
See https://plot.ly/python/reference/#scatterpolar for more information and chart attribute options!
