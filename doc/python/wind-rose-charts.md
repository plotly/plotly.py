---
description: How to graph wind rose charts in python. Wind Rose charts display wind
  speed and direction of a given location.
---
### Wind Rose Chart with Plotly Express

A [wind rose chart](https://en.wikipedia.org/wiki/Wind_rose) (also known as a polar bar chart) is a graphical tool used to visualize how wind speed and direction are typically distributed at a given location. You can use the `px.bar_polar` function from Plotly Express as below, otherwise use `go.Barpolar` as explained in the next section.

[Plotly Express](plotly-express.md) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](px-arguments.md) and produces [easy-to-style figures](styling-plotly-express.md).

```python
import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, r="frequency", theta="direction",
                   color="strength", template="plotly_dark",
                   color_discrete_sequence= px.colors.sequential.Plasma_r)
fig.show()
```

#### Basic Wind Rose Chart

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Barpolar(
    r=[77.5, 72.5, 70.0, 45.0, 22.5, 42.5, 40.0, 62.5],
    name='11-14 m/s',
    marker_color='rgb(106,81,163)'
))
fig.add_trace(go.Barpolar(
    r=[57.5, 50.0, 45.0, 35.0, 20.0, 22.5, 37.5, 55.0],
    name='8-11 m/s',
    marker_color='rgb(158,154,200)'
))
fig.add_trace(go.Barpolar(
    r=[40.0, 30.0, 30.0, 35.0, 7.5, 7.5, 32.5, 40.0],
    name='5-8 m/s',
    marker_color='rgb(203,201,226)'
))
fig.add_trace(go.Barpolar(
    r=[20.0, 7.5, 15.0, 22.5, 2.5, 2.5, 12.5, 22.5],
    name='< 5 m/s',
    marker_color='rgb(242,240,247)'
))

fig.update_traces(text=['North', 'N-E', 'East', 'S-E', 'South', 'S-W', 'West', 'N-W'])
fig.update_layout(
    title=dict(text='Wind Speed Distribution in Laurel, NE'),
    font_size=16,
    legend_font_size=16,
    polar_radialaxis_ticksuffix='%',
    polar_angularaxis_rotation=90,

)
fig.show()
```

#### Reference

See [function reference for `px.(bar_polar)`](reference/plotly-express.md#plotly.express.bar_polar) or the [full reference for `go.Barpolar`](reference/graph_objects/Barpolar.md) for more information and chart attribute options!
