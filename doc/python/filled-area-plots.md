---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: "1.1"
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
    description: How to make filled area plots in Python with Plotly.
    display_as: basic
    language: python
    layout: base
    name: Filled Area Plots
    order: 8
    page_type: u-guide
    permalink: python/filled-area-plots/
    thumbnail: thumbnail/area.jpg
---

This example shows how to fill the area enclosed by traces.

## Filled area plot with plotly.express

[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on "tidy" data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/).

`px.area` creates a stacked area plot. Each filled area corresponds to one value of the column given by the `line_group` parameter.

```python
import plotly.express as px
df = px.data.gapminder()
fig = px.area(df, x="year", y="pop", color="continent",
	      line_group="country")
fig.show()
```

### Filled area chart with plotly.graph_objects

#### Basic Overlaid Area Chart

```python
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[0, 2, 3, 5], fill='tozeroy')) # fill down to xaxis
fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[3, 5, 1, 7], fill='tonexty')) # fill to trace0 y

fig.show()
```

#### Overlaid Area Chart Without Boundary Lines

```python
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[0, 2, 3, 5], fill='tozeroy',
                    mode='none' # override default markers+lines
                    ))
fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[3, 5, 1, 7], fill='tonexty',
                    mode= 'none'))

fig.show()
```

#### Interior Filling for Area Chart

```python
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[3, 4, 8, 3],
    fill=None,
    mode='lines',
    line_color='indigo',
    ))
fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4],
    y=[1, 6, 2, 6],
    fill='tonexty', # fill area between trace0 and trace1
    mode='lines', line_color='indigo'))

fig.show()
```

#### Stacked Area Chart

The `stackgroup` parameter is used to add the `y` values of the different traces in the same group. Traces in the same group fill up to the next trace of the group.

```python
import plotly.graph_objects as go

x=['Winter', 'Spring', 'Summer', 'Fall']

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x, y=[40, 60, 40, 10],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='rgb(131, 90, 241)'),
    stackgroup='one' # define stack group
))
fig.add_trace(go.Scatter(
    x=x, y=[20, 10, 10, 60],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='rgb(111, 231, 219)'),
    stackgroup='one'
))
fig.add_trace(go.Scatter(
    x=x, y=[40, 30, 50, 30],
    hoverinfo='x+y',
    mode='lines',
    line=dict(width=0.5, color='rgb(184, 247, 212)'),
    stackgroup='one'
))

fig.update_layout(yaxis_range=(0, 100))
fig.show()
```

### Stacked Area Chart with Normalized Values

```python
import plotly.graph_objects as go

x=['Winter', 'Spring', 'Summer', 'Fall']
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x, y=[40, 20, 30, 40],
    mode='lines',
    line=dict(width=0.5, color='rgb(184, 247, 212)'),
    stackgroup='one',
    groupnorm='percent' # sets the normalization for the sum of the stackgroup
))
fig.add_trace(go.Scatter(
    x=x, y=[50, 70, 40, 60],
    mode='lines',
    line=dict(width=0.5, color='rgb(111, 231, 219)'),
    stackgroup='one'
))
fig.add_trace(go.Scatter(
    x=x, y=[70, 80, 60, 70],
    mode='lines',
    line=dict(width=0.5, color='rgb(127, 166, 238)'),
    stackgroup='one'
))
fig.add_trace(go.Scatter(
    x=x, y=[100, 100, 100, 100],
    mode='lines',
    line=dict(width=0.5, color='rgb(131, 90, 241)'),
    stackgroup='one'
))

fig.update_layout(
    showlegend=True,
    xaxis_type='category',
    yaxis=dict(
        type='linear',
        range=[1, 100],
        ticksuffix='%'))

fig.show()
```

#### Select Hover Points

```python
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(x=[0,0.5,1,1.5,2], y=[0,1,2,1,0],
                    fill='toself', fillcolor='darkviolet',
                    hoveron = 'points+fills', # select where hover is active
                    line_color='darkviolet',
                    text="Points + Fills",
                    hoverinfo = 'text+x+y'))

fig.add_trace(go.Scatter(x=[3,3.5,4,4.5,5], y=[0,1,2,1,0],
                    fill='toself', fillcolor = 'violet',
                    hoveron='points',
                    line_color='violet',
                    text="Points only",
                    hoverinfo='text+x+y'))

fig.update_layout(
    title = "hover on <i>points</i> or <i>fill</i>",
    xaxis_range = [0,5.2],
    yaxis_range = [0,3]
)

fig.show()
```

#### Reference

See https://plot.ly/python/reference/#scatter-line
and https://plot.ly/python/reference/#scatter-fill
for more information and attribute options!
