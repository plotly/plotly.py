---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: "1.2"
      jupytext_version: 1.3.0
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
    version: 3.7.3
  plotly:
    description: How to configure and style the legend in Plotly with Python.
    display_as: file_settings
    language: python
    layout: base
    name: Legends
    order: 14
    permalink: python/legend/
    redirect_from: python/horizontal-legend/
    thumbnail: thumbnail/legends.gif
---

#### Show Legend

By default the legend is displayed on Plotly charts with multiple traces.

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[5, 4, 3, 2, 1],
))

fig.show()
```

Add `showlegend=True` to the `layout` object to display the legend on a plot with a single trace.

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
))

fig.update_layout(showlegend=True)

fig.show()
```

#### Hide Legend

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[5, 4, 3, 2, 1],
))

fig.update_layout(showlegend=False)

fig.show()
```

#### Hide Legend Entries

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
    showlegend=False
))


fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[5, 4, 3, 2, 1],
))

fig.update_layout(showlegend=True)

fig.show()
```

#### Legend Names

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
    name="Positive"
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[5, 4, 3, 2, 1],
    name="Negative"
))

fig.show()
```

#### Legend titles

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
    name="Increasing"
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[5, 4, 3, 2, 1],
    name="Decreasing"
))

fig.update_layout(legend_title='<b> Trend </b>')
fig.show()
```

#### Horizontal Legend

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[5, 4, 3, 2, 1],
))

fig.update_layout(legend_orientation="h")

fig.show()
```

#### Legend Position

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[5, 4, 3, 2, 1],
))

fig.update_layout(legend=dict(x=-.1, y=1.2))

fig.show()
```

#### Style Legend

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[5, 4, 3, 2, 1],
))

fig.update_layout(
    legend=dict(
        x=0,
        y=1,
        traceorder="normal",
        font=dict(
            family="sans-serif",
            size=12,
            color="black"
        ),
        bgcolor="LightSteelBlue",
        bordercolor="Black",
        borderwidth=2
    )
)

fig.show()
```

### Size of Legend Items

In this example [itemsizing](https://plot.ly/python/reference/#layout-legend-itemsizing) attribute determines the legend items symbols remain constant, regardless of how tiny/huge the bubbles would be in the graph.

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
    mode='markers',
    marker={'size':10}
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[5, 4, 3, 2, 1],
    mode='markers',
    marker={'size':100}
))

fig.update_layout(legend= {'itemsizing': 'constant'})

fig.show()
```

#### Grouped Legend

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3],
    y=[2, 1, 3],
    legendgroup="group",  # this can be any string, not just "group"
    name="first legend group",
    mode="markers",
    marker=dict(color="Crimson", size=10)
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3],
    y=[2, 2, 2],
    legendgroup="group",
    name="first legend group - average",
    mode="lines",
    line=dict(color="Crimson")
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3],
    y=[4, 9, 2],
    legendgroup="group2",
    name="second legend group",
    mode="markers",
    marker=dict(color="MediumPurple", size=10)
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3],
    y=[5, 5, 5],
    legendgroup="group2",
    name="second legend group - average",
    mode="lines",
    line=dict(color="MediumPurple")
))

fig.show()
```

You can also hide entries in grouped legends:

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3],
    y=[2, 1, 3],
    legendgroup="group",  # this can be any string, not just "group"
    name="first legend group",
    mode="markers",
    marker=dict(color="Crimson", size=10)
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3],
    y=[2, 2, 2],
    legendgroup="group",
    name="first legend group - average",
    mode="lines",
    line=dict(color="Crimson"),
    showlegend=False,
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3],
    y=[4, 9, 2],
    legendgroup="group2",
    name="second legend group",
    mode="markers",
    marker=dict(color="MediumPurple", size=10)
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3],
    y=[5, 5, 5],
    legendgroup="group2",
    name="second legend group - average",
    mode="lines",
    line=dict(color="MediumPurple"),
    showlegend=False,
))

fig.show()
```

### Legend items for continuous fields (2D and 3D)

Traces corresponding to 2D fields (e.g. `go.Heatmap`, `go.Histogram2d`) or 3D fields (e.g. `go.Isosurface`, `go.Volume`, `go.Cone`) can also appear in the legend. They come with legend icons corresponding to each trace type, which are colored using the same colorscale as the trace.

The example below explores a vector field using several traces. Note that you can click on legend items to hide or to select (with a double click) a specific trace. This will make the exploration of your data easier!

```python
import numpy as np
import plotly.graph_objects as go

# Define vector and scalar fields
x, y, z = np.mgrid[0:1:8j, 0:1:8j, 0:1:8j]
u =    np.sin(np.pi*x) * np.cos(np.pi*z)
v = -2*np.sin(np.pi*y) * np.cos(2*np.pi*z)
w = np.cos(np.pi*x)*np.sin(np.pi*z) + np.cos(np.pi*y)*np.sin(2*np.pi*z)
magnitude = np.sqrt(u**2 + v**2 + w**2)
mask1 = np.logical_and(y>=.4, y<=.6)
mask2 = y>.6

fig = go.Figure(go.Isosurface(
                      x=x.ravel(), y=y.ravel(), z=z.ravel(),
                      value=magnitude.ravel(),
                      isomin=1.9, isomax=1.9,
                      colorscale="BuGn",
                      name='isosurface'))


fig.add_trace(go.Cone(x=x[mask1], y=y[mask1], z=z[mask1],
                      u=u[mask1], v=v[mask1], w=w[mask1],
                      colorscale="Blues",
                      name='cones'
))
fig.add_trace(go.Streamtube(
                      x=x[mask2], y=y[mask2], z=z[mask2],
                      u=u[mask2], v=v[mask2], w=w[mask2],
                      colorscale="Reds",
                      name='streamtubes'
))
# Update all traces together
fig.update_traces(showlegend=True, showscale=False)
fig.update_layout(width=600, title_text='Exporation of a vector field using several traces')
fig.show()
```

#### Reference

See https://plot.ly/python/reference/#layout-legend for more information!
