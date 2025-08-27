---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.17.2
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
    version: 3.9.0
  plotly:
    description: How to use patterns (also known as hatching or texture) with bar
      charts.
    display_as: basic
    language: python
    layout: base
    name: Patterns, Hatching, Texture
    order: 18
    page_type: u-guide
    permalink: python/pattern-hatching-texture/
    thumbnail: thumbnail/pattern.png
---

*New in 5.0, with support for pie, sunburst, icicle, funnelarea, and treemap charts in 5.15*

[Bar charts](/python/bar-charts/), [histograms](/python/histograms/), [polar bar charts](/python/wind-rose-charts/), [area charts](/python/filled-area-plots/), [pie charts](/python/pie-charts), [sunburst charts](/python/sunburst-charts), [funnelarea charts](/python/funnel-charts), [icicle charts](/python/icicle-charts/), and [treemap charts](/python/treemaps), have large markers or areas which support not only a fill color, but also an optional **pattern** (also known as "hatching" or "texture"). This can be used for a variety of reasons:

* to double-encode variables (i.e. using both color and pattern) to improve accessibility for visually-impaired end-users
* to encode an additional variable beyond just using color
* to make charts that are easier to print in black and white


### Patterned Charts with Plotly Express

the `px.bar()`, `px.histogram()`, `px.bar_polar()` and `px.area()` functions support the `pattern_shape` argument. In the chart below, we double-encode `nation` using color and pattern:

```python
import plotly.express as px
df = px.data.medals_long()

fig = px.bar(df, x="medal", y="count", color="nation", pattern_shape="nation")
fig.show()
```

```python
import plotly.express as px
df = px.data.medals_long()

fig = px.area(df, x="medal", y="count", color="nation", pattern_shape="nation")
fig.show()
```

In the chart below we use `px.histogram()` instead of `px.bar()` to aggregate multiple values together, and encode one variable (sex) using both color and x-position and another (smoker) using patterns:

```python
import plotly.express as px

df = px.data.tips()
fig = px.histogram(df, x="sex", y="total_bill", color="sex", pattern_shape="smoker")
fig.show()
```

### Controlling Pattern Assignment

In the charts above, the first value of the variable assigned `pattern_shape` gets the empty pattern, but this (and indeed every pattern-to-variable assignment) can be controlled using `pattern_shape_sequence` and `pattern_shape_map`, analogously to the way [discrete colors](/python/discrete-color/) can be mapped using Plotly Express.

Here we use `pattern_shape_sequence` to replace the defaults and include a pattern-shape for the first variable:

```python
import plotly.express as px
df = px.data.medals_long()

fig = px.bar(df, x="medal", y="count", color="nation",
             pattern_shape="nation", pattern_shape_sequence=[".", "x", "+"])
fig.show()
```

Here we use `pattern_shape_map` to explictly assign a shape to each value of `nation`, regardless of order:

```python
import plotly.express as px
df = px.data.medals_long()

fig = px.bar(df, x="medal", y="count", color="nation",
             pattern_shape="nation", pattern_shape_map={
             "China": ".", "Canada": "/", "South Korea": "+"
             })
fig.show()
```

### Black on White Patterns for Print

When creating figures meant to be printed on black and white printers, it is better to *replace* the fill-color with the pattern, rather than to overlay it. This can be controlled with the `<trace>.marker.pattern.fillmode` attribute, which defaults to `"overlay"` but can be set to `"replace"` instead. Changing this attribute, and using a simpler default template and color scheme gives the following output:

```python
import plotly.express as px
df = px.data.medals_long()

fig = px.bar(df, x="medal", y="count", color="nation",
             pattern_shape="nation", pattern_shape_sequence=[".", "x", "+"],
             template="simple_white"
            )
fig.update_traces(
    marker=dict(color="black", line_color="black", pattern_fillmode="replace")
)
fig.show()
```

Of course, this setting can be used without making the figure monochrome as well:

```python
import plotly.express as px
df = px.data.medals_long()

fig = px.bar(df, x="medal", y="count", color="nation",
             pattern_shape="nation", pattern_shape_sequence=[".", "x", "+"],
            )
fig.update_traces(
    marker=dict(line_color="grey", pattern_fillmode="replace")
)
fig.show()
```

### Patterns using Graph Objects

If Plotly Express does not provide a good starting point, it is also possible to use [the more generic `go.Bar` class from `plotly.graph_objects`](/python/graph-objects/).

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Bar(x=["a","b"], y=[1,2], marker_pattern_shape="."))
fig.add_trace(go.Bar(x=["a","b"], y=[3,1], marker_pattern_shape="x"))
fig.add_trace(go.Bar(x=["a","b"], y=[2,3], marker_pattern_shape="+"))

fig.show()
```

### Patterns Using SVG Paths

*New in 6.3*

You can make custom patterns for graphs by using an SVG path. Set `marker.pattern.path` to the SVG path to use:

```python
import plotly.graph_objects as go
import plotly.data

df = plotly.data.gapminder().query("year == 2007 and continent == 'Europe'").copy()
df['gdp'] = df['gdpPercap'] * df['pop']
df = df.sort_values('gdp', ascending=False).head(4)

fig = go.Figure(
    data=[go.Bar(
        x=df['country'],
        y=df['gdp'],
        marker=dict(
            color=["lightsteelblue", "mistyrose", "palegreen", "thistle"],
            pattern=dict(
                path=[
                    "M0,0H4V4H0Z",
                    "M0,0H6V6Z",
                    "M0,0V4H4Z",
                    "M0,0C0,2,4,2,4,4C4,6,0,6,0,8H2C2,6,6,6,6,4C6,2,2,2,2,0Z"
                ],
                fgcolor=["midnightblue", "crimson", "seagreen", "indigo"],
                bgcolor=["mintcream", "lavenderblush", "azure", "honeydew"],
                size=20,
                solidity=0.7
            )
        ),
        name="GDP (2007)"
    )],
    layout=dict(
        title="Top 4 European Countries by GDP (Gapminder 2007) with Custom SVG Path Patterns",
        xaxis_title="Country",
        yaxis_title="GDP (USD)",
        yaxis_tickformat="$.2s",
        width=800,
        height=500,
        bargap=0.3
    )
)

fig.show()
```

#### Reference

See https://plotly.com/python/reference/bar/ for more information and chart attribute options!
