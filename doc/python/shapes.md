---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.2.1
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
    description: How to make SVG shapes in python. Examples of lines, circle, rectangle,
      and path.
    display_as: file_settings
    language: python
    layout: base
    name: Shapes
    order: 24
    permalink: python/shapes/
    thumbnail: thumbnail/shape.jpg
---

### Filled Area Chart

There are two ways to draw filled shapes: scatter traces and [layout.shapes](https://plot.ly/python/reference/#layout-shapes-items-shape-type) which is mostly useful for the 2d subplots, and defines the shape type to be drawn, and can be rectangle, circle, line, or path (a custom SVG path). You also can use [scatterpolar](https://plot.ly/python/polar-chart/#categorical-polar-chart), scattergeo, [scattermapbox](https://plot.ly/python/filled-area-on-mapbox/#filled-scattermapbox-trace) to draw filled shapes on any kind of subplots. To set an area to be filled with a solid color, you need to define [Scatter.fill="toself"](https://plot.ly/python/reference/#scatter-fill) that connects the endpoints of the trace into a closed shape. If `mode=line` (default value), then you need to repeat the initial point of a shape at the of the sequence to have a closed shape. 

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scatter(x=[0,1,2,0], y=[0,2,0,0], fill="toself"))
fig.show()
```

You can have more shapes either by adding [more traces](https://plot.ly/python/filled-area-plots/) or interrupting the series with `None`.

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scatter(x=[0,1,2,0,None,3,3,5,5,3], y=[0,2,0,0,None,0.5,1.5,1.5,0.5,0.5], fill="toself"))
fig.show()
```

#### Vertical and Horizontal Lines Positioned Relative to the Axes

```python
import plotly.graph_objects as go

fig = go.Figure()

# Create scatter trace of text labels
fig.add_trace(go.Scatter(
    x=[2, 3.5, 6],
    y=[1, 1.5, 1],
    text=["Vertical Line",
          "Horizontal Dashed Line",
          "Diagonal dotted Line"],
    mode="text",
))

# Set axes ranges
fig.update_xaxes(range=[0, 7])
fig.update_yaxes(range=[0, 2.5])

# Add shapes
fig.add_shape(
        # Line Vertical
        go.layout.Shape(
            type="line",
            x0=1,
            y0=0,
            x1=1,
            y1=2,
            line=dict(
                color="RoyalBlue",
                width=3
            )
))
fig.add_shape(
        # Line Horizontal
        go.layout.Shape(
            type="line",
            x0=2,
            y0=2,
            x1=5,
            y1=2,
            line=dict(
                color="LightSeaGreen",
                width=4,
                dash="dashdot",
            ),
    ))
fig.add_shape(
        # Line Diagonal
        go.layout.Shape(
            type="line",
            x0=4,
            y0=0,
            x1=6,
            y1=2,
            line=dict(
                color="MediumPurple",
                width=4,
                dash="dot",
            )
))
fig.update_shapes(dict(xref='x', yref='y'))
fig.show()
```

#### Lines Positioned Relative to the Plot & to the Axes

```python
import plotly.graph_objects as go

fig = go.Figure()

# Create scatter trace of text labels
fig.add_trace(go.Scatter(
    x=[2, 6],
    y=[1, 1],
    text=["Line positioned relative to the plot",
          "Line positioned relative to the axes"],
    mode="text",
))

# Set axes ranges
fig.update_xaxes(range=[0, 8])
fig.update_yaxes(range=[0, 2])

# Add shapes
fig.add_shape(
        # Line reference to the axes
        go.layout.Shape(
            type="line",
            xref="x",
            yref="y",
            x0=4,
            y0=0,
            x1=8,
            y1=1,
            line=dict(
                color="LightSeaGreen",
                width=3,
            ),
        ))
fig.add_shape(
        # Line reference to the plot
        go.layout.Shape(
            type="line",
            xref="paper",
            yref="paper",
            x0=0,
            y0=0,
            x1=0.5,
            y1=0.5,
            line=dict(
                color="DarkOrange",
                width=3,
            ),
        ),
)

fig.show()
```

#### Creating Tangent Lines with Shapes

```python
import plotly.graph_objects as go

import numpy as np

# Generate data
x0 = np.linspace(1, 3, 200)
y0 = x0 * np.sin(np.power(x0, 2)) + 1

# Create figure with scatter trace
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x0,
    y=y0,
))

# Set title text
fig.update_layout(
    title_text="$f(x)=x\\sin(x^2)+1\\\\ f\'(x)=\\sin(x^2)+2x^2\\cos(x^2)$"
)

# Add tangent line shapes
fig.add_shape(
        go.layout.Shape(
            type="line",
            x0=1,
            y0=2.30756,
            x1=1.75,
            y1=2.30756,
        ))
fig.add_shape(
        go.layout.Shape(
            type="line",
            x0=2.5,
            y0=3.80796,
            x1=3.05,
            y1=3.80796,
        ))
fig.add_shape(
        go.layout.Shape(
            type="line",
            x0=1.90,
            y0=-1.1827,
            x1=2.50,
            y1=-1.1827,
        ))
fig.update_shapes(dict(
    xref="x",
    yref="y",
    opacity=0.7,
    line=dict(
        color="Crimson",
        width=2.5,
        )))
fig.show()
```

#### Rectangles Positioned Relative to the Axes

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1.5, 4.5],
    y=[0.75, 0.75],
    text=["Unfilled Rectangle", "Filled Rectangle"],
    mode="text",
))

# Set axes properties
fig.update_xaxes(range=[0, 7], showgrid=False)
fig.update_yaxes(range=[0, 3.5])

# Add shapes
fig.add_shape(
        # unfilled Rectangle
        go.layout.Shape(
            type="rect",
            x0=1,
            y0=1,
            x1=2,
            y1=3,
            line=dict(
                color="RoyalBlue",
            ),
        ))
fig.add_shape(
        # filled Rectangle
        go.layout.Shape(
            type="rect",
            x0=3,
            y0=1,
            x1=6,
            y1=2,
            line=dict(
                color="RoyalBlue",
                width=2,
            ),
            fillcolor="LightSkyBlue",
        ))
fig.update_shapes(dict(xref='x', yref='y'))
fig.show()
```

#### Rectangle Positioned Relative to the Plot & to the Axes

```python
import plotly.graph_objects as go

fig = go.Figure()

# Create scatter trace of text labels
fig.add_trace(go.Scatter(
    x=[1.5, 3],
    y=[2.5, 2.5],
    text=["Rectangle reference to the plot",
          "Rectangle reference to the axes"],
    mode="text",
))

# Set axes properties
fig.update_xaxes(range=[0, 4], showgrid=False)
fig.update_yaxes(range=[0, 4])

# Add shapes
fig.add_shape(
        # Rectangle reference to the axes
        go.layout.Shape(
            type="rect",
            xref="x",
            yref="y",
            x0=2.5,
            y0=0,
            x1=3.5,
            y1=2,
            line=dict(
                color="RoyalBlue",
                width=3,
            ),
            fillcolor="LightSkyBlue",
        ))
fig.add_shape(
        # Rectangle reference to the plot
        go.layout.Shape(
            type="rect",
            xref="paper",
            yref="paper",
            x0=0.25,
            y0=0,
            x1=0.5,
            y1=0.5,
            line=dict(
                color="LightSeaGreen",
                width=3,
            ),
            fillcolor="PaleTurquoise",
        ))

fig.show()
```

#### Highlighting Time Series Regions with Rectangle Shapes

```python
import plotly.graph_objects as go

fig = go.Figure()

# Add scatter trace for line
fig.add_trace(go.Scatter(
    x=["2015-02-01", "2015-02-02", "2015-02-03", "2015-02-04", "2015-02-05",
       "2015-02-06", "2015-02-07", "2015-02-08", "2015-02-09", "2015-02-10",
       "2015-02-11", "2015-02-12", "2015-02-13", "2015-02-14", "2015-02-15",
       "2015-02-16", "2015-02-17", "2015-02-18", "2015-02-19", "2015-02-20",
       "2015-02-21", "2015-02-22", "2015-02-23", "2015-02-24", "2015-02-25",
       "2015-02-26", "2015-02-27", "2015-02-28"],
    y=[-14, -17, -8, -4, -7, -10, -12, -14, -12, -7, -11, -7, -18, -14, -14,
       -16, -13, -7, -8, -14, -8, -3, -9, -9, -4, -13, -9, -6],
    mode="lines",
    name="temperature"
))

# Add shape regions
fig.update_layout(
    shapes=[
        # 1st highlight during Feb 4 - Feb 6
        go.layout.Shape(
            type="rect",
            # x-reference is assigned to the x-values
            xref="x",
            # y-reference is assigned to the plot paper [0,1]
            yref="paper",
            x0="2015-02-04",
            y0=0,
            x1="2015-02-06",
            y1=1,
            fillcolor="LightSalmon",
            opacity=0.5,
            layer="below",
            line_width=0,
        ),
        # 2nd highlight during Feb 20 - Feb 23
        go.layout.Shape(
            type="rect",
            xref="x",
            yref="paper",
            x0="2015-02-20",
            y0=0,
            x1="2015-02-22",
            y1=1,
            fillcolor="LightSalmon",
            opacity=0.5,
            layer="below",
            line_width=0,
        )
    ]
)

fig.show()
```

#### Circles Positioned Relative to the Axes

```python
import plotly.graph_objects as go

fig = go.Figure()

# Create scatter trace of text labels
fig.add_trace(go.Scatter(
    x=[1.5, 3.5],
    y=[0.75, 2.5],
    text=["Unfilled Circle",
          "Filled Circle"],
    mode="text",
))

# Set axes properties
fig.update_xaxes(range=[0, 4.5], zeroline=False)
fig.update_yaxes(range=[0, 4.5])

# Add circles
fig.update_layout(
    shapes=[
        # unfilled circle
        go.layout.Shape(
            type="circle",
            xref="x",
            yref="y",
            x0=1,
            y0=1,
            x1=3,
            y1=3,
            line_color="LightSeaGreen",
        ),
        # filled circle
        go.layout.Shape(
            type="circle",
            xref="x",
            yref="y",
            fillcolor="PaleTurquoise",
            x0=3,
            y0=3,
            x1=4,
            y1=4,
            line_color="LightSeaGreen",
        ),
    ]
)

# Set figure size
fig.update_layout(width=800, height=800)

fig.show()
```

#### Highlighting Clusters of Scatter Points with Circle Shapes

```python
import plotly.graph_objects as go

import numpy as np
np.random.seed(1)

# Generate data
x0 = np.random.normal(2, 0.45, 300)
y0 = np.random.normal(2, 0.45, 300)

x1 = np.random.normal(6, 0.4, 200)
y1 = np.random.normal(6, 0.4, 200)

x2 = np.random.normal(4, 0.3, 200)
y2 = np.random.normal(4, 0.3, 200)

# Create figure
fig = go.Figure()

# Add scatter traces
fig.add_trace(go.Scatter(
    x=x0,
    y=y0,
    mode="markers",
))

fig.add_trace(go.Scatter(
    x=x1,
    y=y1,
    mode="markers"
))

fig.add_trace(go.Scatter(
    x=x2,
    y=y2,
    mode="markers"
))

fig.add_trace(go.Scatter(
    x=x1,
    y=y0,
    mode="markers"
))

# Add shapes
fig.update_layout(
    shapes=[
        go.layout.Shape(
            type="circle",
            xref="x",
            yref="y",
            x0=min(x0),
            y0=min(y0),
            x1=max(x0),
            y1=max(y0),
            opacity=0.2,
            fillcolor="blue",
            line_color="blue",
        ),
        go.layout.Shape(
            type="circle",
            xref="x",
            yref="y",
            x0=min(x1),
            y0=min(y1),
            x1=max(x1),
            y1=max(y1),
            opacity=0.2,
            fillcolor="orange",
            line_color="orange",
        ),
        go.layout.Shape(
            type="circle",
            xref="x",
            yref="y",
            x0=min(x2),
            y0=min(y2),
            x1=max(x2),
            y1=max(y2),
            opacity=0.2,
            fillcolor="green",
            line_color="green",
        ),
        go.layout.Shape(
            type="circle",
            xref="x",
            yref="y",
            x0=min(x1),
            y0=min(y0),
            x1=max(x1),
            y1=max(y0),
            opacity=0.2,
            fillcolor="red",
            line_color="red",
        ),
    ],
)

# Hide legend
fig.update_layout(showlegend=False)

fig.show()
```

#### Venn Diagram with Circle Shapes

```python
import plotly.graph_objects as go

fig = go.Figure()

# Create scatter trace of text labels
fig.add_trace(go.Scatter(
    x=[1, 1.75, 2.5],
    y=[1, 1, 1],
    text=["$A$", "$A+B$", "$B$"],
    mode="text",
    textfont=dict(
        color="black",
        size=18,
        family="Arail",
    )
))

# Update axes properties
fig.update_xaxes(
    showticklabels=False,
    showgrid=False,
    zeroline=False,
)

fig.update_yaxes(
    showticklabels=False,
    showgrid=False,
    zeroline=False,
)

# Add circles
fig.add_shape(
        go.layout.Shape(
            type="circle",
            fillcolor="blue",
            x0=0,
            y0=0,
            x1=2,
            y1=2,
            line_color="blue"
        ))
fig.add_shape(
        go.layout.Shape(
            type="circle",
            fillcolor="gray",
            x0=1.5,
            y0=0,
            x1=3.5,
            y1=2,
            line_color="gray"
        ))
fig.update_shapes(dict(
    opacity=0.3,
    xref="x",
    yref="y",
    layer="below"
))
# Update figure dimensions
fig.update_layout(
    margin=dict(
        l=20,
        r=20,
        b=100
    ),
    height=600,
    width=800,
    plot_bgcolor="white"
)

fig.show()
```

#### SVG Paths

```python
import plotly.graph_objects as go

fig = go.Figure()

# Create scatter trace of text labels
fig.add_trace(go.Scatter(
    x=[2, 1, 8, 8],
    y=[0.25, 9, 2, 6],
    text=["Filled Triangle",
          "Filled Polygon",
          "Quadratic Bezier Curves",
          "Cubic Bezier Curves"],
    mode="text",
))

# Update axes properties
fig.update_xaxes(
    range=[0, 9],
    zeroline=False,
)

fig.update_yaxes(
    range=[0, 11],
    zeroline=False,
)

# Add shapes
fig.update_layout(
    shapes=[
        # Quadratic Bezier Curves
        go.layout.Shape(
            type="path",
            path="M 4,4 Q 6,0 8,4",
            line_color="RoyalBlue",
        ),
        # Cubic Bezier Curves
        go.layout.Shape(
            type="path",
            path="M 1,4 C 2,8 6,4 8,8",
            line_color="MediumPurple",
        ),
        # filled Triangle
        go.layout.Shape(
            type="path",
            path=" M 1 1 L 1 3 L 4 1 Z",
            fillcolor="LightPink",
            line_color="Crimson",
        ),
        # filled Polygon
        go.layout.Shape(
            type="path",
            path=" M 3,7 L2,8 L2,9 L3,10, L4,10 L5,9 L5,8 L4,7 Z",
            fillcolor="PaleTurquoise",
            line_color="LightSeaGreen",
        ),
    ]
)

fig.show()
```

### Reference
See https://plot.ly/python/reference/#layout-shapes for more information and chart attribute options!
