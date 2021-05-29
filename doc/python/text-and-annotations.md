---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.6.0
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
    version: 3.7.6
  plotly:
    description: How to add text labels and annotations to plots in python.
    display_as: file_settings
    language: python
    layout: base
    name: Text and Annotations
    order: 22
    permalink: python/text-and-annotations/
    thumbnail: thumbnail/text-and-annotations.png
---

### Adding Text to Figures

As a general rule, there are two ways to add text labels to figures:
1. Certain trace types, notably in the `scatter` family (e.g. `scatter`, `scatter3d`, `scattergeo` etc), support a `text` attribute, and can be displayed with or without markers.
2. Standalone text annotations can be added to figures using `fig.add_annotation()`, with or without arrows, and they can be positioned absolutely within the figure, or they can be positioned relative to the axes of 2d or 3d cartesian subplots i.e. in data coordinates.

The differences between these two approaches are that:
* Traces can optionally support hover labels and can appear in legends.
* Text annotations can be positioned absolutely or relative to data coordinates in 2d/3d cartesian subplots only.
* Traces cannot be positioned absolutely but can be positioned relative to data coordinates in any subplot type.
* Traces also be used to [draw shapes](/python/shapes/), although there is a [shape equivalent to text annotations](/python/shapes/).


### Text on scatter plots with Plotly Express

Here is an example that creates a scatter plot with text labels using Plotly Express.

```python
import plotly.express as px

df = px.data.gapminder().query("year==2007 and continent=='Americas'")

fig = px.scatter(df, x="gdpPercap", y="lifeExp", text="country", log_x=True, size_max=60)

fig.update_traces(textposition='top center')

fig.update_layout(
    height=800,
    title_text='GDP and Life Expectancy (Americas, 2007)'
)

fig.show()
```

### Text on scatter plots with Graph Objects

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[0, 1, 2],
    y=[1, 1, 1],
    mode="lines+markers+text",
    name="Lines, Markers and Text",
    text=["Text A", "Text B", "Text C"],
    textposition="top center"
))

fig.add_trace(go.Scatter(
    x=[0, 1, 2],
    y=[2, 2, 2],
    mode="markers+text",
    name="Markers and Text",
    text=["Text D", "Text E", "Text F"],
    textposition="bottom center"
))

fig.add_trace(go.Scatter(
    x=[0, 1, 2],
    y=[3, 3, 3],
    mode="lines+text",
    name="Lines and Text",
    text=["Text G", "Text H", "Text I"],
    textposition="bottom center"
))

fig.show()
```

### Text positioning in Dash

[Dash](https://plotly.com/dash/) is the best way to build analytical apps in Python using Plotly figures. To run the app below, run `pip install dash`, click "Download" to get the code and run `python app.py`.

Get started  with [the official Dash docs](https://dash.plotly.com/installation) and **learn how to effortlessly [style](https://plotly.com/dash/design-kit/) & [deploy](https://plotly.com/dash/app-manager/) apps like this with <a class="plotly-red" href="https://plotly.com/dash/">Dash Enterprise</a>.**


```python hide_code=true
from IPython.display import IFrame
snippet_url = 'https://dash-gallery.plotly.host/python-docs-dash-snippets/'
IFrame(snippet_url + 'text-and-annotations', width='100%', height=630)
```

### Controlling text fontsize with uniformtext

For the [pie](/python/pie-charts), [bar](/python/bar-charts), [sunburst](/python/sunburst-charts) and [treemap](/python/treemap-charts) traces, it is possible to force all the text labels to have the same size thanks to the `uniformtext` layout parameter. The `minsize` attribute sets the font size, and the `mode` attribute sets what happens for labels which cannot fit with the desired fontsize: either `hide` them or `show` them with overflow.

```python
import plotly.express as px

df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
fig = px.bar(df, y='pop', x='country', text='pop')
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.show()
```

```python
import plotly.express as px

df = px.data.gapminder().query("continent == 'Asia' and year == 2007")
fig = px.pie(df, values='pop', names='country')
fig.update_traces(textposition='inside')
fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
fig.show()
```

### Controlling text fontsize with textfont

The `textfont_size` parameter of the the [pie](/python/pie-charts), [bar](/python/bar-charts), [sunburst](/python/sunburst-charts) and [treemap](/python/treemap-charts) traces can be used to set the **maximum font size** used in the chart. Note that the `textfont` parameter sets the `insidetextfont` and `outsidetextfont` parameter, which can also be set independently.

```python
import plotly.express as px

df = px.data.gapminder().query("continent == 'Asia' and year == 2007")
fig = px.pie(df, values='pop', names='country')
fig.update_traces(textposition='inside', textfont_size=14)
fig.show()
```

### Text Annotations

Annotations can be added to a figure using `fig.add_annotation()`.

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 3, 2, 4, 3, 4, 6, 5]
))


fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 4, 5, 1, 2, 2, 3, 4, 2]
))

fig.add_annotation(x=2, y=5,
            text="Text annotation with arrow",
            showarrow=True,
            arrowhead=1)
fig.add_annotation(x=4, y=4,
            text="Text annotation without arrow",
            showarrow=False,
            yshift=10)

fig.update_layout(showlegend=False)

fig.show()
```

### 3D Annotations

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=["2017-01-01", "2017-02-10", "2017-03-20"],
    y=["A", "B", "C"],
    z=[1, 1000, 100000],
    name="z",
))

fig.update_layout(
    scene=dict(
        xaxis=dict(type="date"),
        yaxis=dict(type="category"),
        zaxis=dict(type="log"),
        annotations=[
        dict(
            showarrow=False,
            x="2017-01-01",
            y="A",
            z=0,
            text="Point 1",
            xanchor="left",
            xshift=10,
            opacity=0.7),
        dict(
            x="2017-02-10",
            y="B",
            z=4,
            text="Point 2",
            textangle=0,
            ax=0,
            ay=-75,
            font=dict(
                color="black",
                size=12
            ),
            arrowcolor="black",
            arrowsize=3,
            arrowwidth=1,
            arrowhead=1),
        dict(
            x="2017-03-20",
            y="C",
            z=5,
            ax=50,
            ay=0,
            text="Point 3",
            arrowhead=1,
            xanchor="left",
            yanchor="bottom"
        )]
    ),
)

fig.show()
```

### Custom Text Color and Styling

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[0, 1, 2],
    y=[1, 1, 1],
    mode="lines+markers+text",
    name="Lines, Markers and Text",
    text=["Text A", "Text B", "Text C"],
    textposition="top right",
    textfont=dict(
        family="sans serif",
        size=18,
        color="crimson"
    )
))

fig.add_trace(go.Scatter(
    x=[0, 1, 2],
    y=[2, 2, 2],
    mode="lines+markers+text",
    name="Lines and Text",
    text=["Text G", "Text H", "Text I"],
    textposition="bottom center",
    textfont=dict(
        family="sans serif",
        size=18,
        color="LightSeaGreen"
    )
))

fig.update_layout(showlegend=False)

fig.show()
```

### Styling and Coloring Annotations

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 3, 2, 4, 3, 4, 6, 5]
))

fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 4, 5, 1, 2, 2, 3, 4, 2]
))

fig.add_annotation(
        x=2,
        y=5,
        xref="x",
        yref="y",
        text="max=5",
        showarrow=True,
        font=dict(
            family="Courier New, monospace",
            size=16,
            color="#ffffff"
            ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#636363",
        ax=20,
        ay=-30,
        bordercolor="#c7c7c7",
        borderwidth=2,
        borderpad=4,
        bgcolor="#ff7f0e",
        opacity=0.8
        )

fig.update_layout(showlegend=False)
fig.show()
```

### Text Font as an Array - Styling Each Text Element

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scattergeo(
    lat=[45.5, 43.4, 49.13, 51.1, 53.34, 45.24, 44.64, 48.25, 49.89, 50.45],
    lon=[-73.57, -79.24, -123.06, -114.1, -113.28, -75.43, -63.57, -123.21, -97.13,
         -104.6],
    marker={
        "color": ["MidnightBlue", "IndianRed", "MediumPurple", "Orange", "Crimson",
                  "LightSeaGreen", "RoyalBlue", "LightSalmon", "DarkOrange", "MediumSlateBlue"],
        "line": {
            "width": 1
        },
        "size": 10
    },
    mode="markers+text",
    name="",
    text=["Montreal", "Toronto", "Vancouver", "Calgary", "Edmonton", "Ottawa",
          "Halifax",
          "Victoria", "Winnepeg", "Regina"],
    textfont={
        "color": ["MidnightBlue", "IndianRed", "MediumPurple", "Gold", "Crimson",
                  "LightSeaGreen",
                  "RoyalBlue", "LightSalmon", "DarkOrange", "MediumSlateBlue"],
        "family": ["Arial, sans-serif", "Balto, sans-serif", "Courier New, monospace",
                   "Droid Sans, sans-serif", "Droid Serif, serif",
                   "Droid Sans Mono, sans-serif",
                   "Gravitas One, cursive", "Old Standard TT, serif",
                   "Open Sans, sans-serif",
                   "PT Sans Narrow, sans-serif", "Raleway, sans-serif",
                   "Times New Roman, Times, serif"],
        "size": [22, 21, 20, 19, 18, 17, 16, 15, 14, 13]
    },
    textposition=["top center", "middle left", "top center", "bottom center",
                  "top right",
                  "middle left", "bottom right", "bottom left", "top right",
                  "top right"]
))

fig.update_layout(
    title_text="Canadian cities",
    geo=dict(
        lataxis=dict(range=[40, 70]),
        lonaxis=dict(range=[-130, -55]),
        scope="north america"
    )
)

fig.show()
```

### Positioning Text Annotations Absolutely

By default, text annotations have `xref` and `yref` set to `"x"` and `"y"`, respectively, meaning that their x/y coordinates are with respect to the axes of the plot. This means that panning the plot will cause the annotations to move. Setting `xref` and/or `yref` to `"paper"` will cause the `x` and `y` attributes to be interpreted in [paper coordinates](/python/figure-structure/#positioning-with-paper-container-coordinates-or-axis-domain-coordinates).

Try panning or zooming in the following figure:

```python
import plotly.express as px

fig = px.scatter(x=[1, 2, 3], y=[1, 2, 3], title="Try panning or zooming!")

fig.add_annotation(text="Absolutely-positioned annotation",
                  xref="paper", yref="paper",
                  x=0.3, y=0.3, showarrow=False)

fig.show()
```

### Adding Annotations Referenced to an Axis

To place annotations relative to the length or height of an axis, the string
`' domain'` can be added after the axis reference in the `xref` or `yref` fields.
For example:

```python
import plotly.express as px
import plotly.graph_objects as go

df = px.data.wind()
fig = px.scatter(df, y="frequency")

# Set a custom domain to see how the ' domain' string changes the behaviour
fig.update_layout(xaxis=dict(domain=[0, 0.5]), yaxis=dict(domain=[0.25, 0.75]))

fig.add_annotation(
    xref="x domain",
    yref="y domain",
    # The arrow head will be 25% along the x axis, starting from the left
    x=0.25,
    # The arrow head will be 40% along the y axis, starting from the bottom
    y=0.4,
    text="An annotation referencing the axes",
    arrowhead=2,
)

fig.show()
```

### Specifying the Text's Position Absolutely

The text coordinates / dimensions of the arrow can be specified absolutely, as
long as they use exactly the same coordinate system as the arrowhead. For
example:

```python
import plotly.express as px
import plotly.graph_objects as go

df = px.data.wind()
fig = px.scatter(df, y="frequency")

fig.update_layout(xaxis=dict(domain=[0, 0.5]), yaxis=dict(domain=[0.25, 0.75]))
fig.add_annotation(
    xref="x domain",
    yref="y",
    x=0.75,
    y=1,
    text="An annotation whose text and arrowhead reference the axes and the data",
    # If axref is exactly the same as xref, then the text's position is
    # absolute and specified in the same coordinates as xref.
    axref="x domain",
    # The same is the case for yref and ayref, but here the coordinates are data
    # coordinates
    ayref="y",
    ax=0.5,
    ay=2,
    arrowhead=2,
)

fig.show()
```

### Customize Displayed Text with a Text Template

To show an arbitrary text in your chart you can use [texttemplate](https://plotly.com/python/reference/pie/#pie-texttemplate), which is a template string used for rendering the information, and will override [textinfo](https://plotly.com/python/reference/treemap/#treemap-textinfo).
This template string can include `variables` in %{variable} format, `numbers` in [d3-format's syntax](https://github.com/d3/d3-3.x-api-reference/blob/master/Formatting.md#d3_forma), and `date` in [d3-time-format's syntax](https://github.com/d3/d3-time-format).
`texttemplate` customizes the text that appears on your plot vs. [hovertemplate](https://plotly.com/python/reference/pie/#pie-hovertemplate) that customizes the tooltip text.

```python
import plotly.graph_objects as go

fig = go.Figure(go.Pie(
    values = [40000000, 20000000, 30000000, 10000000],
    labels = ["Wages", "Operating expenses", "Cost of sales", "Insurance"],
    texttemplate = "%{label}: %{value:$,s} <br>(%{percent})",
    textposition = "inside"))

fig.show()
```

### Customize Text Template

The following example uses [textfont](https://plotly.com/python/reference/scatterternary/#scatterternary-textfont) to customize the added text.

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scatterternary(
    a = [3, 2, 5],
    b = [2, 5, 2],
    c = [5, 2, 2],
    mode = "markers+text",
    text = ["A", "B", "C"],
    texttemplate = "%{text}<br>(%{a:.2f}, %{b:.2f}, %{c:.2f})",
    textposition = "bottom center",
    textfont = {'family': "Times", 'size': [18, 21, 20], 'color': ["IndianRed", "MediumPurple", "DarkOrange"]}
))

fig.show()
```

### Set Date in Text Template

The following example shows how to show date by setting [axis.type](https://plotly.com/python/reference/layout/yaxis/#layout-yaxis-type) in [funnel charts](https://plotly.com/python/funnel-charts/).
As you can see [textinfo](https://plotly.com/python/reference/funnel/#funnel-textinfo) and [texttemplate](https://plotly.com/python/reference/funnel/#funnel-texttemplate) have the same functionality when you want to determine 'just' the trace information on the graph.

```python
from plotly import graph_objects as go

fig = go.Figure()

fig.add_trace(go.Funnel(
    name = 'Montreal',
    orientation = "h",
    y = ["2018-01-01", "2018-07-01", "2019-01-01", "2020-01-01"],
    x = [100, 60, 40, 20],
    textposition = "inside",
    texttemplate = "%{y| %a. %_d %b %Y}"))

fig.add_trace(go.Funnel(
    name = 'Vancouver',
    orientation = "h",
    y = ["2018-01-01", "2018-07-01", "2019-01-01", "2020-01-01"],
    x = [90, 70, 50, 10],
    textposition = "inside",
    textinfo = "label"))

fig.update_layout(yaxis = {'type': 'date'})

fig.show()
```

#### Reference

See https://plotly.com/python/reference/layout/annotations/ for more information and chart attribute options!
