---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.6
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
    version: 3.10.10
  plotly:
    description: How to make SVG shapes in python. Examples of lines, circle, rectangle,
      and path.
    display_as: file_settings
    language: python
    layout: base
    name: Shapes
    order: 25
    permalink: python/shapes/
    thumbnail: thumbnail/shape.jpg
---

### Adding Lines and Polygons to Figures

As a general rule, there are two ways to add shapes (lines or polygons) to figures:
1. Trace types in the `scatter` family (e.g. `scatter`, `scatter3d`, `scattergeo` etc) can be drawn with `mode="lines"` and optionally support a `fill="self"` attribute, and so can be used to draw open or closed shapes on figures.
2. Standalone lines, ellipses and rectangles can be added to figures using `fig.add_shape()`, and they can be positioned absolutely within the figure, or they can be positioned relative to the axes of 2d cartesian subplots i.e. in data coordinates.

*Note:* there are [special methods `add_hline`, `add_vline`, `add_hrect` and `add_vrect` for the common cases of wanting to draw horizontal or vertical lines or rectangles](/python/horizontal-vertical-shapes/) that are fixed to data coordinates in one axis and absolutely positioned in another.

The differences between these two approaches are that:
* Traces can optionally support hover labels and can appear in legends.
* Shapes can be positioned absolutely or relative to data coordinates in 2d cartesian subplots only.
* Traces cannot be positioned absolutely but can be positioned relative to date coordinates in any subplot type.
* Traces also support [optional text](/python/text-and-annotations/), although there is a [textual equivalent to shapes in text annotations](/python/text-and-annotations/).



### Shape-drawing with Scatter traces

There are two ways to draw filled shapes: scatter traces and [layout.shapes](https://plotly.com/python/reference/layout/shapes/#layout-shapes-items-shape-type) which is mostly useful for the 2d subplots, and defines the shape type to be drawn, and can be rectangle, circle, line, or path (a custom SVG path). You also can use [scatterpolar](https://plotly.com/python/polar-chart/#categorical-polar-chart), scattergeo, [scattermapbox](https://plotly.com/python/filled-area-on-mapbox/#filled-scattermapbox-trace) to draw filled shapes on any kind of subplots. To set an area to be filled with a solid color, you need to define [Scatter.fill="toself"](https://plotly.com/python/reference/scatter/#scatter-fill) that connects the endpoints of the trace into a closed shape. If `mode=line` (default value), then you need to repeat the initial point of a shape at the end of the sequence to have a closed shape.

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scatter(x=[0,1,2,0], y=[0,2,0,0], fill="toself"))
fig.show()
```

You can have more shapes either by adding [more traces](https://plotly.com/python/filled-area-plots/) or interrupting the series with `None`.

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scatter(x=[0,1,2,0,None,3,3,5,5,3], y=[0,2,0,0,None,0.5,1.5,1.5,0.5,0.5], fill="toself"))
fig.show()
```

#### Shapes in Dash

[Dash](https://plotly.com/dash/) is the best way to build analytical apps in Python using Plotly figures. To run the app below, run `pip install dash`, click "Download" to get the code and run `python app.py`.

Get started  with [the official Dash docs](https://dash.plotly.com/installation) and **learn how to effortlessly [style](https://plotly.com/dash/design-kit/) & [deploy](https://plotly.com/dash/app-manager/) apps like this with <a class="plotly-red" href="https://plotly.com/dash/">Dash Enterprise</a>.**


```python hide_code=true
from IPython.display import IFrame
snippet_url = 'https://python-docs-dash-snippets.herokuapp.com/python-docs-dash-snippets/'
IFrame(snippet_url + 'shapes', width='100%', height=1200)
```

<div style="font-size: 0.9em;"><div style="width: calc(100% - 30px); box-shadow: none; border: thin solid rgb(229, 229, 229);"><div style="padding: 5px;"><div><p><strong>Sign up for Dash Club</strong> → Free cheat sheets plus updates from Chris Parmer and Adam Schroeder delivered to your inbox every two months. Includes tips and tricks, community apps, and deep dives into the Dash architecture.
<u><a href="https://go.plotly.com/dash-club?utm_source=Dash+Club+2022&utm_medium=graphing_libraries&utm_content=inline">Join now</a></u>.</p></div></div></div></div>


#### Vertical and Horizontal Lines Positioned Relative to the Axis Data

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
fig.add_shape(type="line",
    x0=1, y0=0, x1=1, y1=2,
    line=dict(color="RoyalBlue",width=3)
)
fig.add_shape(type="line",
    x0=2, y0=2, x1=5, y1=2,
    line=dict(
        color="LightSeaGreen",
        width=4,
        dash="dashdot",
    )
)
fig.add_shape(type="line",
    x0=4, y0=0, x1=6, y1=2,
    line=dict(
        color="MediumPurple",
        width=4,
        dash="dot",
    )
)
fig.update_shapes(dict(xref='x', yref='y'))
fig.show()
```

#### Lines Positioned Relative to the Plot & to the Axis Data

```python
import plotly.graph_objects as go

fig = go.Figure()

# Create scatter trace of text labels
fig.add_trace(go.Scatter(
    x=[2, 6], y=[1, 1],
    text=["Line positioned relative to the plot",
          "Line positioned relative to the axes"],
    mode="text",
))

# Set axes ranges
fig.update_xaxes(range=[0, 8])
fig.update_yaxes(range=[0, 2])

fig.add_shape(type="line",
    xref="x", yref="y",
    x0=4, y0=0, x1=8, y1=1,
    line=dict(
        color="LightSeaGreen",
        width=3,
    ),
)
fig.add_shape(type="line",
    xref="paper", yref="paper",
    x0=0, y0=0, x1=0.5,
    y1=0.5,
    line=dict(
        color="DarkOrange",
        width=3,
    ),
)

fig.show()
```

#### Rectangles Positioned Relative to the Axis Data

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
fig.add_shape(type="rect",
    x0=1, y0=1, x1=2, y1=3,
    line=dict(color="RoyalBlue"),
)
fig.add_shape(type="rect",
    x0=3, y0=1, x1=6, y1=2,
    line=dict(
        color="RoyalBlue",
        width=2,
    ),
    fillcolor="LightSkyBlue",
)
fig.update_shapes(dict(xref='x', yref='y'))
fig.show()
```

#### Rectangle Positioned Relative to the Plot & to the Axis Data

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
fig.update_xaxes(range=[0, 4])
fig.update_yaxes(range=[0, 4])

# Add shapes
fig.add_shape(type="rect",
    xref="x", yref="y",
    x0=2.5, y0=0,
    x1=3.5, y1=2,
    line=dict(
        color="RoyalBlue",
        width=3,
    ),
    fillcolor="LightSkyBlue",
)
fig.add_shape(type="rect",
    xref="paper", yref="paper",
    x0=0.25, y0=0,
    x1=0.5, y1=0.5,
    line=dict(
        color="LightSeaGreen",
        width=3,
    ),
    fillcolor="PaleTurquoise",
)

fig.show()
```

#### A Rectangle Placed Relative to the Axis Position and Length

A shape can be placed relative to an axis's position on the plot by adding the
string `' domain'` to the axis reference in the `xref` or `yref` attributes for
shapes.
The following code places a rectangle that starts at 60% and ends at 70% along
the x-axis, starting from the left, and starts at 80% and ends at 90% along the
y-axis, starting from the bottom.

```python
import plotly.graph_objects as go
import plotly.express as px

df = px.data.wind()
fig = px.scatter(df, y="frequency")

fig.update_layout(xaxis=dict(domain=[0, 0.5]), yaxis=dict(domain=[0.25, 0.75]))

# Add a shape whose x and y coordinates refer to the domains of the x and y axes
fig.add_shape(type="rect",
    xref="x domain", yref="y domain",
    x0=0.6, x1=0.7, y0=0.8, y1=0.9,
)

fig.show()
```

#### Highlighting Time Series Regions with Rectangle Shapes

*Note:* there are [special methods `add_hline`, `add_vline`, `add_hrect` and `add_vrect` for the common cases of wanting to draw horizontal or vertical lines or rectangles](/python/horizontal-vertical-shapes/) that are fixed to data coordinates in one axis and absolutely positioned in another.


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
fig.add_vrect(
    x0="2015-02-04", x1="2015-02-06",
    fillcolor="LightSalmon", opacity=0.5,
    layer="below", line_width=0,
),

fig.add_vrect(
    x0="2015-02-20", x1="2015-02-22",
    fillcolor="LightSalmon", opacity=0.5,
    layer="below", line_width=0,
)

fig.show()
```

#### Circles Positioned Relative to the Axis Data

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
fig.add_shape(type="circle",
    xref="x", yref="y",
    x0=1, y0=1, x1=3, y1=3,
    line_color="LightSeaGreen",
)
fig.add_shape(type="circle",
    xref="x", yref="y",
    fillcolor="PaleTurquoise",
    x0=3, y0=3, x1=4, y1=4,
    line_color="LightSeaGreen",
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

# Create figure
fig = go.Figure()

# Add scatter traces
fig.add_trace(go.Scatter(x=x0, y=y0, mode="markers"))
fig.add_trace(go.Scatter(x=x1, y=y1, mode="markers"))

# Add shapes
fig.add_shape(type="circle",
    xref="x", yref="y",
    x0=min(x0), y0=min(y0),
    x1=max(x0), y1=max(y0),
    opacity=0.2,
    fillcolor="blue",
    line_color="blue",
)

fig.add_shape(type="circle",
    xref="x", yref="y",
    x0=min(x1), y0=min(y1),
    x1=max(x1), y1=max(y1),
    opacity=0.2,
    fillcolor="orange",
    line_color="orange",
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
fig.add_shape(type="circle",
    line_color="blue", fillcolor="blue",
    x0=0, y0=0, x1=2, y1=2
)
fig.add_shape(type="circle",
    line_color="gray", fillcolor="gray",
    x0=1.5, y0=0, x1=3.5, y1=2
)
fig.update_shapes(opacity=0.3, xref="x", yref="y")

fig.update_layout(
    margin=dict(l=20, r=20, b=100),
    height=600, width=800,
    plot_bgcolor="white"
)

fig.show()
```

#### Adding Shapes to Subplots
Here we use the different axes (`x1`, `x2`) created by `make_subplots` as reference in order to draw shapes in figure subplots.

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create Subplots
fig = make_subplots(rows=2, cols=2)

fig.add_trace(go.Scatter(x=[2, 6], y=[1,1]), row=1, col=1)
fig.add_trace(go.Bar(x=[1,2,3], y=[4,5,6]), row=1, col=2)
fig.add_trace(go.Scatter(x=[10,20], y=[40,50]), row=2, col=1)
fig.add_trace(go.Bar(x=[11,13,15], y=[8,11,20]), row=2, col=2)

# Add shapes
fig.update_layout(
    shapes=[
        dict(type="line", xref="x", yref="y",
            x0=3, y0=0.5, x1=5, y1=0.8, line_width=3),
        dict(type="rect", xref="x2", yref='y2',
             x0=4, y0=2, x1=5, y1=6),
        dict(type="rect", xref="x3", yref="y3",
             x0=10, y0=20, x1=15, y1=30),
        dict(type="circle", xref="x4", yref="y4",
             x0=5, y0=12, x1=10, y1=18)])
fig.show()
```

#### Adding the Same Shapes to Multiple Subplots
The same shape can be added to multiple facets by using the `'all'`
keyword in the `row` and `col` arguments. For example
```python
import plotly.express as px

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", facet_row="smoker", facet_col="sex")
# Adds a rectangle to all facets
fig.add_shape(
    dict(type="rect", x0=25, x1=35, y0=4, y1=6, line_color="purple"),
    row="all",
    col="all",
)
# Adds a line to all the rows of the second column
fig.add_shape(
    dict(type="line", x0=20, x1=25, y0=5, y1=6, line_color="yellow"), row="all", col=2
)

# Adds a circle to all the columns of the first row
fig.add_shape(
    dict(type="circle", x0=10, y0=2, x1=20, y1=7), row=1, col="all", line_color="green"
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
        dict(
            type="path",
            path="M 4,4 Q 6,0 8,4",
            line_color="RoyalBlue",
        ),
        # Cubic Bezier Curves
        dict(
            type="path",
            path="M 1,4 C 2,8 6,4 8,8",
            line_color="MediumPurple",
        ),
        # filled Triangle
        dict(
            type="path",
            path=" M 1 1 L 1 3 L 4 1 Z",
            fillcolor="LightPink",
            line_color="Crimson",
        ),
        # filled Polygon
        dict(
            type="path",
            path=" M 3,7 L2,8 L2,9 L3,10, L4,10 L5,9 L5,8 L4,7 Z",
            fillcolor="PaleTurquoise",
            line_color="LightSeaGreen",
        ),
    ]
)

fig.show()
```

### Drawing shapes with a Mouse on Cartesian plots

_introduced in plotly 4.7_

You can create layout shapes programmatically, but you can also draw shapes manually by setting the `dragmode` to one of the shape-drawing modes: `'drawline'`,`'drawopenpath'`, `'drawclosedpath'`, `'drawcircle'`, or `'drawrect'`. If you need to switch between different shape-drawing or other dragmodes (panning, selecting, etc.), [modebar buttons can be added](/python/configuration-options#add-optional-shapedrawing-buttons-to-modebar) in the `config` to select the dragmode. If you switch to a different dragmode such as pan or zoom, you will need to select the drawing tool in the modebar to go back to shape drawing.

This shape-drawing feature is particularly interesting for annotating graphs, in particular [image traces](/python/imshow) or [layout images](/python/images).

Once you have drawn shapes, you can select and modify an existing shape by clicking on its boundary (note the arrow pointer). Its fillcolor turns to pink to highlight the activated shape and then you can
- drag and resize it for lines, rectangles and circles/ellipses
- drag and move individual vertices for closed paths
- move individual vertices for open paths.

An activated shape is deleted by clicking on the `eraseshape` button.

Drawing or modifying a shape triggers a `relayout` event, which [can be captured by a callback inside a Dash application](https://dash.plotly.com/interactive-graphing).

```python
import plotly.graph_objects as go
fig = go.Figure()
text="Click and drag here <br> to draw a rectangle <br><br> or select another shape <br>in the modebar"
fig.add_annotation(
            x=0.5,
            y=0.5,
            text=text,
            xref="paper",
            yref="paper",
            showarrow=False,
            font_size=20
)
# shape defined programatically
fig.add_shape(editable=True,
              x0=-1, x1=0, y0=2, y1=3,
              xref='x', yref='y')
# define dragmode and add modebar buttons
fig.update_layout(dragmode='drawrect')
fig.show(config={'modeBarButtonsToAdd':['drawline',
                                        'drawopenpath',
                                        'drawclosedpath',
                                        'drawcircle',
                                        'drawrect',
                                        'eraseshape'
                                       ]})
```

### Style of user-drawn shapes

The layout `newshape` attribute controls the visual appearance of new shapes drawn by the user. `newshape` attributes have the same names as layout shapes.

_Note on shape opacity_: having a new shape's opacity > 0.5 makes it possible to activate a shape by clicking inside the shape (for opacity <= 0.5 you have to click on the border of the shape), but you cannot start a new shape within an existing shape (which is possible for an opacity <= 0.5).

```python
import plotly.graph_objects as go
fig = go.Figure()
text="Click and drag<br> to draw a rectangle <br><br> or select another shape <br>in the modebar"
fig.add_annotation(
            x=0.5,
            y=0.5,
            text=text,
            xref="paper",
            yref="paper",
            showarrow=False,
            font_size=20
)
# shape defined programatically
fig.add_shape(line_color='yellow',
              fillcolor='turquoise',
              opacity=0.4,
              editable=True,
              x0=0, x1=1, y0=2, y1=3,
              xref='x', yref='y'
)
fig.update_layout(dragmode='drawrect',
                  # style of new shapes
                  newshape=dict(line_color='yellow',
                                fillcolor='turquoise',
                                opacity=0.5))
fig.show(config={'modeBarButtonsToAdd':['drawline',
                                        'drawopenpath',
                                        'drawclosedpath',
                                        'drawcircle',
                                        'drawrect',
                                        'eraseshape'
                                       ]})
```

### Adding Text Labels to Shapes

*New in 5.14*

Add a text `label` to a shape by adding a `label` property to a shape with `text`. In this example, we add a `rect` and `line` shape and add a text label to both.

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_shape(
    type="rect", 
    fillcolor='turquoise', 
    x0=1, 
    y0=1, 
    x1=2, 
    y1=3, 
    label=dict(text="Text in rectangle")
)
fig.add_shape(
    type="line",
    x0=3,
    y0=0.5,
    x1=5,
    y1=0.8,
    line_width=3,
    label=dict(text="Text above line")
)

fig.show()

```

#### Styling Text Labels

Use the `font` property to configure the `color`, `size`, and `family` of the label font. 
In this example, we change the label color of the first rectangle to "DarkOrange", set the size of the text above the line to 20, and change the font family and set the font size on the second rectangle. 

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_shape(
    type="rect",
    fillcolor='MediumSlateBlue',
    x0=1,
    y0=1,
    x1=2,
    y1=3,
    label=dict(text="Text in rectangle", font=dict(color="DarkOrange")),
)
fig.add_shape(
    type="line",
    x0=3,
    y0=0.5,
    x1=5,
    y1=0.8,
    line_width=3,
    label=dict(text="Text above line", font=dict(size=20)),
)
fig.add_shape(
    type="rect",
    fillcolor='Lavender',
    x0=2.5,
    y0=2.5,
    x1=5,
    y1=3.5,
    label=dict(
        text="Text in rectangle 2", font=dict(family="Courier New, monospace", size=20)
    ),
)

fig.show()

```

#### Setting Label Position

Set a label's position relative to the shape by setting `textposition`. The default position for lines is `middle`. The default position for other shapes is `middle center`.


```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_shape(
    type="rect",
    fillcolor='Lavender',
    x0=0,
    y0=0,
    x1=1.5,
    y1=1.5,
    label=dict(text="Text at middle center"),
)

fig.add_shape(
    type="rect",
    fillcolor='Lavender',
    x0=3,
    y0=0,
    x1=4.5,
    y1=1.5,
    label=dict(text="Text at top left", textposition="top left"),
)


fig.add_shape(
    type="line",
    line_color="MediumSlateBlue",    
    x0=3,
    y0=2,
    x1=5,
    y1=3,
    line_width=3,
    label=dict(text="Text at start", textposition="start"),
)


fig.add_shape(
    type="line",
    line_color="MediumSlateBlue",
    x0=0,
    y0=2,
    x1=2,
    y1=3,
    line_width=3,
    label=dict(text="Text at middle"),
)

fig.show()

```

#### Setting Label Angle

Use `textangle` to rotate a label by setting a value between -180 and 180. The default angle for a label on a line is the angle of the line. The default angle for a label on other shapes is 0. In this example, in the first shape, the label is at 45 degrees, and in the second, the label is at -45 degrees.

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_shape(
    type="rect",
    fillcolor='LightGreen',
    x0=0,
    y0=0,
    x1=2,
    y1=2,
    label=dict(text="Text at 45", textangle=45),
)

fig.add_shape(
    type="rect",
    fillcolor='Gold',
    x0=3,
    y0=0,
    x1=5,
    y1=2,
    label=dict(text="Text at -45", textangle=-45),
)

fig.show()

```

#### Setting Label Padding

`padding` adds padding between the label and shape. This example shows one line with padding of 30px and another with the default padding, which is 3px.

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_shape(
    type="line",
    line_color="RoyalBlue",
    x0=3,
    y0=0,
    x1=5,
    y1=3,
    line_width=3,
    label=dict(text="Label padding of 30px", padding=30),
)

fig.add_shape(
    type="line",
    line_color="RoyalBlue",
    x0=0,
    y0=0,
    x1=2,
    y1=3,
    line_width=3,
    label=dict(text="Default label padding of 3px"),
)

fig.show()
```

#### Setting Label Anchors

`xanchor` sets a label's horizontal positional anchor and `yanchor` sets its vertical position anchor. 
Use `xanchor` to bind the `textposition` to the "left", "center" or "right" of the label text and `yanchor` to bind `textposition` to the "top", "middle" or "bottom" of the label text.

In this example, `yanchor`is set to "top", instead of the default of "bottom" for lines, meaning the text displays below the line. 


```python
import plotly.express as px

df = px.data.stocks(indexed=True)
fig = px.line(df)

fig.add_shape(
    type="rect",
    x0="2018-09-24",
    y0=0,
    x1="2018-12-18",
    y1=3,
    line_width=0,
    label=dict(text="Decline", textposition="top center", font=dict(size=20)),
    fillcolor="green",
    opacity=0.25,
)

fig.add_shape(
    type="line",
    x0=min(df.index),
    y0=1,
    x1=max(df.index),
    y1=1,
    line_width=3,
    line_dash="dot",
    label=dict(
        text="Jan 1 2018 Baseline",
        textposition="end",
        font=dict(size=20, color="blue"),
        yanchor="top",
    ),
)

fig.show()
```

#### Variables in Shape Label Text

*New in 5.15*

Use `texttemplate` to add text with variables to shapes. You have access to raw variables (`x0`, `x1`, `y0`, `y1`), which use raw data values from the shape definition, and the following calculated variables:

- `xcenter`: (x0 + x1) / 2
- `ycenter`: (y0 + y1) / 2
- `dx`: x1 - x0
- `dy`: y1 - y0
- `width`: abs(x1 - x0)
- `height`: abs(y1 - y0)
- `length` (for lines only): sqrt(dx^2 + dy^2)
- `slope`: (y1 - y0) / (x1 - x0)

`texttemplate` supports d3 number and date formatting.

Add a variable with "%{variable}". This example adds the raw variables `x0` and `y0` to a rectangle and shows the calculated variables `height`, `slope`, `length`, and `width` on three other shapes. 

```python
import plotly.graph_objects as go

fig = go.Figure()


fig.add_shape(
    type="rect",
    fillcolor="MediumSlateBlue",
    x0=-0.5,
    y0=-0.5,
    x1=1,
    y1=1,
    label=dict(
        texttemplate="x0 is %{x0:.3f}, y0 is %{y0:.3f}", font=dict(color="DarkOrange")
    ),
)

fig.add_shape(
    type="rect",
    fillcolor="LightGreen",
    x0=1,
    y0=1.75,
    x1=2.25,
    y1=3,
    label=dict(texttemplate="Height: %{height:.3f}", font=dict(color="DarkOrange")),
)
fig.add_shape(
    type="line",
    x0=3,
    y0=0.5,
    x1=5,
    y1=1.5,
    line_width=3,
    label=dict(
        texttemplate="Slope of %{slope:.3f} and length of %{length:.3f}",
        font=dict(size=20),
    ),
)
fig.add_shape(
    type="rect",
    fillcolor="Lavender",
    x0=2.5,
    y0=2.5,
    x1=5,
    y1=3.5,
    label=dict(
        texttemplate="Width: %{width:.3f}",
        font=dict(family="Courier New, monospace", size=20),
    ),
)

fig.show()

```

#### Variables in Shape Label Text for New Shapes

*New in 5.15*

You can also use `texttemplate` to add text with variables to new shapes drawn on the graph.

In this example, we enable drawing lines on the figure by adding `drawline` to `modeBarButtonsToAdd` in `config`. We then define a `texttemplate` for shapes that shows the calculated variable `dy`. Select **Draw line** in the modebar to try it out.

```python
import plotly.graph_objects as go
from plotly import data

df = data.stocks()

fig = go.Figure(
    data=go.Scatter(
        x=df.date,
        y=df.GOOG,
    ),
    layout=go.Layout(
        yaxis=dict(title="Price in USD"),
        newshape=dict(
            label=dict(texttemplate="Change: %{dy:.2f}")
        ),
        title="Google Share Price 2018/2019",
    ),
)


fig.show(
    config={
        "modeBarButtonsToAdd": [
            "drawline",
        ]
    }
)
```

### Reference
See https://plotly.com/python/reference/layout/shapes/ for more information and chart attribute options!
