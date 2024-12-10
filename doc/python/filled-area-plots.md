---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.1
  kernelspec:
    display_name: Python 3 (ipykernel)
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
    version: 3.10.11
  plotly:
    description: How to make filled area plots in Python with Plotly.
    display_as: basic
    language: python
    layout: base
    name: Filled Area Plots
    order: 7
    page_type: u-guide
    permalink: python/filled-area-plots/
    thumbnail: thumbnail/area.jpg
---

This example shows how to fill the area enclosed by traces.

## Filled area plot with plotly.express

[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/).

`px.area` creates a stacked area plot. Each filled area corresponds to one value of the column given by the `line_group` parameter.

```python
import plotly.express as px
df = px.data.gapminder()
fig = px.area(df, x="year", y="pop", color="continent", line_group="country")
fig.show()
```

## Filled area plot in Dash

[Dash](https://plotly.com/dash/) is the best way to build analytical apps in Python using Plotly figures. To run the app below, run `pip install dash`, click "Download" to get the code and run `python app.py`.

Get started  with [the official Dash docs](https://dash.plotly.com/installation) and **learn how to effortlessly [style](https://plotly.com/dash/design-kit/) & [deploy](https://plotly.com/dash/app-manager/) apps like this with <a class="plotly-red" href="https://plotly.com/dash/">Dash Enterprise</a>.**


```python hide_code=true
from IPython.display import IFrame
snippet_url = 'https://python-docs-dash-snippets.herokuapp.com/python-docs-dash-snippets/'
IFrame(snippet_url + 'filled-area-plots', width='100%', height=1200)
```

<div style="font-size: 0.9em;"><div style="width: calc(100% - 30px); box-shadow: none; border: thin solid rgb(229, 229, 229);"><div style="padding: 5px;"><div><p><strong>Sign up for Dash Club</strong> → Free cheat sheets plus updates from Chris Parmer and Adam Schroeder delivered to your inbox every two months. Includes tips and tricks, community apps, and deep dives into the Dash architecture.
<u><a href="https://go.plotly.com/dash-club?utm_source=Dash+Club+2022&utm_medium=graphing_libraries&utm_content=inline">Join now</a></u>.</p></div></div></div></div>


### Pattern Fills

*New in v5.7*

Area charts afford the use of [patterns (also known as hatching or texture)](/python/pattern-hatching-texture/) in addition to color:

```python
import plotly.express as px
df = px.data.medals_long()

fig = px.area(df, x="medal", y="count", color="nation",
             pattern_shape="nation", pattern_shape_sequence=[".", "x", "+"])
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
                    mode='none' # override default markers+lines
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
    fill='tonexty', # fill area between trace0 and trace1
    mode='lines', line_color='indigo'))

fig.show()
```

#### Gradient Fill

*New in 5.20*

Scatter traces with a fill support a `fillgradient`, which is a `dict` of options that defines the gradient. Use `fillgradient.colorscale` to define the [colorscale](https://plotly.com/python/colorscales) for the gradient and choose a `type` to define the orientation of the gradient (`'horizontal'`, `'vertical'` or `'radial'`). 

In the following example, we've defined a `horizontal` `fillgradient` with a colorscale of three colors. 

```python
import plotly.graph_objects as go

fig = go.Figure(
    [
        go.Scatter(
            x=[1, 2, 3, 4],
            y=[3, 4, 8, 3],
            fill=None,
            mode="lines",
            line_color="darkblue",
        ),
        go.Scatter(
            x=[1, 2, 3, 4],
            y=[1, 6, 2, 6],
            fill="tonexty",
            mode="lines",
            line_color="darkblue",
            fillgradient=dict(
                type="horizontal",
                colorscale=[(0.0, "darkblue"), (0.5, "royalblue"), (1.0, "cyan")],
            ),
        ),
    ]
)

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

See https://plotly.com/python/reference/scatter/#scatter-line
and https://plotly.com/python/reference/scatter/#scatter-fill
for more information and attribute options!
