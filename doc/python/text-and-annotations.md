---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.2
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
    description: How to add text labels and annotations to plots in python.
    display_as: file_settings
    language: python
    layout: base
    name: Text and Annotations
    order: 21
    permalink: python/text-and-annotations/
    thumbnail: thumbnail/text-and-annotations.png
---

### Text scatter plot with Plotly Express

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

### Adding Text to Data in Line and Scatter Plots

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

### Adding Hover Text to Data in Line and Scatter Plots

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[0, 1, 2],
    y=[1, 3, 2],
    mode="markers",
    hovertext=["Text A", "Text B", "Text C"]
))

fig.update_layout(title_text="Hover over the points to see the text")

fig.show()
```

### Simple Annotation

Annotations can be added to a figure using `fig.update_layout(annotations=[...])` or `fig.add_annotation`.

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

fig.update_layout(
    showlegend=False,
    annotations=[
        dict(
            x=2,
            y=5,
            xref="x",
            yref="y",
            text="dict Text",
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=-40
        )
    ]
)

fig.show()
```

### Multiple Annotations

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
            text="dict Text")
fig.add_annotation(
            x=4,
            y=4,
            text="dict Text 2")
fig.update_annotations(dict(
            xref="x",
            yref="y",
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=-40
))

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
    xaxis=dict(title_text="x"),
    yaxis=dict(title_text="y"),
    scene=dict(
        aspectratio=dict(
            x=1,
            y=1,
            z=1
        ),
        camera=dict(
            center=dict(
                x=0,
                y=0,
                z=0
            ),
            eye=dict(
                x=1.96903462608,
                y=-1.09022831971,
                z=0.405345349304
            ),
            up=dict(
                x=0,
                y=0,
                z=1
            )
        ),
        dragmode="turntable",
        xaxis=dict(
            title_text="",
            type="date"
        ),
        yaxis=dict(
            title_text="",
            type="category"
        ),
        zaxis=dict(
            title_text="",
            type="log"
        ),
        annotations=[dict(
            showarrow=False,
            x="2017-01-01",
            y="A",
            z=0,
            text="Point 1",
            xanchor="left",
            xshift=10,
            opacity=0.7
        ), dict(
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
            arrowhead=1
        ), dict(
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

### Disabling Hover Text

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, ],
    y=[10, 30, 15],
    name="first trace",
    hoverinfo="none"
))

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

### Adding Annotations with xref and yref as Paper

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3],
    y=[1, 2, 3],
    name="y",
))

fig.update_layout(
    annotations=[
        dict(
            x=0.5,
            y=-0.15,
            showarrow=False,
            text="Custom x-axis title",
            xref="paper",
            yref="paper"
        ),
        dict(
            x=-0.07,
            y=0.5,
            showarrow=False,
            text="Custom y-axis title",
            textangle=-90,
            xref="paper",
            yref="paper"
        )
    ],
    autosize=True,
    margin=dict(
        b=100
    ),
    title_text="Plot Title",
    xaxis=dict(
        autorange=False,
        range=[-0.05674507980728292, -0.0527310420933204],
        type="linear"
    ),
    yaxis=dict(
        autorange=False,
        range=[1.2876210047544652, 1.2977732997811402],
        type="linear"
    ),
    height=550,
    width=1137
)

fig.show()
```

### Customize Displayed Text with a Text Template

To show an arbitrary text in your chart you can use [texttemplate](https://plot.ly/python/reference/#pie-texttemplate), which is a template string used for rendering the information, and will override [textinfo](https://plot.ly/python/reference/#treemap-textinfo).
This template string can include `variables` in %{variable} format, `numbers` in [d3-format's syntax](https://github.com/d3/d3-3.x-api-reference/blob/master/Formatting.md#d3_forma), and `date` in [d3-time-fomrat's syntax](https://github.com/d3/d3-3.x-api-reference/blob/master/Time-Formatting.md#format).
`texttemplate` customizes the text that appears on your plot vs. [hovertemplate](https://plot.ly/python/reference/#pie-hovertemplate) that customizes the tooltip text.

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

The following example uses [textfont](https://plot.ly/python/reference/#scatterternary-textfont) to customize the added text.

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

The following example shows how to show date by setting [axis.type](https://plot.ly/python/reference/#layout-yaxis-type) in [funnel charts](https://plot.ly/python/funnel-charts/).
As you can see [textinfo](https://plot.ly/python/reference/#funnel-textinfo) and [texttemplate](https://plot.ly/python/reference/#funnel-texttemplate) have the same functionality when you want to determine 'just' the trace information on the graph.

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

See https://plot.ly/python/reference/#layout-annotations for more information and chart attribute options!
