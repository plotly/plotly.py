---
description: How to make radar charts in Python with Plotly.
---
A [Radar Chart](https://en.wikipedia.org/wiki/Radar_chart) (also known as a spider plot or star plot) displays multivariate data in the form of a two-dimensional chart of quantitative variables represented on axes originating from the center. The relative position and angle of the axes is typically uninformative. It is equivalent to a [parallel coordinates plot](parallel-coordinates-plot.md) with the axes arranged radially.

For a Radar Chart, use a [polar chart](polar-chart.md) with categorical angular variables, with `px.line_polar`, or with `go.Scatterpolar`. See [more examples of polar charts](polar-chart.md).

#### Radar Chart with Plotly Express

[Plotly Express](plotly-express.md) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](px-arguments.md) and produces [easy-to-style figures](styling-plotly-express.md).

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

See [function reference for `px.(line_polar)`](reference/plotly-express.md#plotly.express.line_polar) or the [full reference for `go.Scatterpolar`](reference/graph_objects/Scatterpolar.md) for more information and chart attribute options!
