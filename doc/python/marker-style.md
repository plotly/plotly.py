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
    version: 3.7.0
  plotly:
    description: How to style markers in Python with Plotly.
    display_as: file_settings
    language: python
    layout: base
    name: Styling Markers
    order: 19
    permalink: python/marker-style/
    thumbnail: thumbnail/marker-style.gif
---

### Add Marker Border

In order to make markers look more distinct, you can add a border to the markers. This can be achieved by adding the line property to the marker object.

Here is an example of adding a marker border to a faceted scatter plot created using Plotly Express.

```python
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

fig.update_traces(marker=dict(size=12,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
fig.show()
```

Here is an example that creates an empty graph object figure, and then adds two scatter traces with a marker border.

```python
import plotly.graph_objects as go

# Generate example data
import numpy as np
np.random.seed(1)

x = np.random.uniform(low=3, high=6, size=(500,))
y = np.random.uniform(low=3, high=6, size=(500,))

# Build figure
fig = go.Figure()

# Add scatter trace with medium sized markers
fig.add_trace(
    go.Scatter(
        mode='markers',
        x=x,
        y=y,
        marker=dict(
            color='LightSkyBlue',
            size=20,
            line=dict(
                color='MediumPurple',
                width=2
            )
        ),
        showlegend=False
    )
)

# Add trace with large marker
fig.add_trace(
    go.Scatter(
        mode='markers',
        x=[2],
        y=[4.5],
        marker=dict(
            color='LightSkyBlue',
            size=120,
            line=dict(
                color='MediumPurple',
                width=12
            )
        ),
        showlegend=False
    )
)

fig.show()
```

Fully opaque, the default setting, is useful for non-overlapping markers. When many points overlap it can be hard to observe density.

### Opacity

Setting opacity outside the marker will set the opacity of the trace. Thus, it will allow greater visbility of additional traces but like fully opaque it is hard to distinguish density.

```python
import plotly.graph_objects as go

# Generate example data
import numpy as np

x = np.random.uniform(low=3, high=6, size=(500,))
y = np.random.uniform(low=3, high=4.5, size=(500,))
x2 = np.random.uniform(low=3, high=6, size=(500,))
y2 = np.random.uniform(low=4.5, high=6, size=(500,))

# Build figure
fig = go.Figure()

# Add first scatter trace with medium sized markers
fig.add_trace(
    go.Scatter(
        mode='markers',
        x=x,
        y=y,
        opacity=0.5,
        marker=dict(
            color='LightSkyBlue',
            size=20,
            line=dict(
                color='MediumPurple',
                width=2
            )
        ),
        name='Opacity 0.5'
    )
)

# Add second scatter trace with medium sized markers
# and opacity 1.0
fig.add_trace(
    go.Scatter(
        mode='markers',
        x=x2,
        y=y2,
        marker=dict(
            color='LightSkyBlue',
            size=20,
            line=dict(
                color='MediumPurple',
                width=2
            )
        ),
        name='Opacity 1.0'
    )
)

# Add trace with large markers
fig.add_trace(
    go.Scatter(
        mode='markers',
        x=[2, 2],
        y=[4.25, 4.75],
        opacity=0.5,
        marker=dict(
            color='LightSkyBlue',
            size=80,
            line=dict(
                color='MediumPurple',
                width=8
            )
        ),
        showlegend=False
    )
)

fig.show()

```

### Marker Opacity

To maximise visibility of density, it is recommended to set the opacity inside the marker `marker:{opacity:0.5}`. If mulitple traces exist with high density, consider using marker opacity in conjunction with trace opacity.

```python
import plotly.graph_objects as go

# Generate example data
import numpy as np

x = np.random.uniform(low=3, high=6, size=(500,))
y = np.random.uniform(low=3, high=6, size=(500,))

# Build figure
fig = go.Figure()

# Add scatter trace with medium sized markers
fig.add_trace(
    go.Scatter(
        mode='markers',
        x=x,
        y=y,
        marker=dict(
            color='LightSkyBlue',
            size=20,
            opacity=0.5,
            line=dict(
                color='MediumPurple',
                width=2
            )
        ),
        showlegend=False
    )
)


# Add trace with large markers
fig.add_trace(
    go.Scatter(
        mode='markers',
        x=[2, 2],
        y=[4.25, 4.75],
        marker=dict(
            color='LightSkyBlue',
            size=80,
            opacity=0.5,
            line=dict(
                color='MediumPurple',
                width=8
            )
        ),
        showlegend=False
    )
)

fig.show()

```

### Color Opacity

To maximise visibility of each point, set the color as an `rgba` string that includes an alpha value of 0.5.

This example sets the marker color to `'rgba(135, 206, 250, 0.5)'`. The rgb values of 135, 206, and 250 are from the definition of the `LightSkyBlue` named CSS color that is is used in the previous examples (See https://www.color-hex.com/color/87cefa). The marker line will remain opaque.

```python
import plotly.graph_objects as go

# Generate example data
import numpy as np

x = np.random.uniform(low=3, high=6, size=(500,))
y = np.random.uniform(low=3, high=6, size=(500,))


# Build figure
fig = go.Figure()

# Add scatter trace with medium sized markers
fig.add_trace(
    go.Scatter(
        mode='markers',
        x=x,
        y=y,
        marker=dict(
            color='rgba(135, 206, 250, 0.5)',
            size=20,
            line=dict(
                color='MediumPurple',
                width=2
            )
        ),
        showlegend=False
    )
)


# Add trace with large markers
fig.add_trace(
    go.Scatter(
        mode='markers',
        x=[2, 2],
        y=[4.25, 4.75],
        marker=dict(
            color='rgba(135, 206, 250, 0.5)',
            size=80,
            line=dict(
                color='MediumPurple',
                width=8
            )
        ),
        showlegend=False
    )
)

fig.show()

```

### Custom Marker Symbols

The `marker_symbol` attribute allows you to choose from a wide array of symbols to represent markers in your figures.

The basic symbols are: `circle`, `square`, `diamond`, `cross`, `x`, `triangle`, `pentagon`, `hexagram`, `star`, `diamond`, `hourglass`, `bowtie`, `asterisk`, `hash`, `y`, and `line`. 

Each basic symbol is also represented by a number. Adding 100 to that number is equivalent to appending the suffix "-open" to a symbol name. Adding 200 is equivalent to appending "-dot" to a symbol name. Adding 300 is equivalent to appending "-open-dot" or "dot-open" to a symbol name.

In the following figures, hover over a symbol to see its name or number. Set the `marker_symbol` attribute equal to that name or number to change the marker symbol in your figure.

#### Basic Symbols

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.update_layout(title="Basic Symbols")

fig.update_xaxes(showticklabels=False)
fig.update_yaxes(showticklabels=False)

for index in range(27):
    fig.add_trace(go.Scatter(x=[(index % 6)], y=[index // 6],  name="",
                             marker_symbol=index, marker_color='black', 
                             marker_size=10, showlegend=False, mode="markers+text",
                             textposition="middle right", text=f'<b>{index}</b>',
                             hovertemplate=f'<b>Symbol Number: {index}</b>'))

fig.show()    
```

#### All Symbols

```python
import plotly.graph_objects as go

symbols = [0, 'circle', 100, 'circle-open', 200, 'circle-dot', 300,
            'circle-open-dot', 1, 'square', 101, 'square-open', 201,
            'square-dot', 301, 'square-open-dot', 2, 'diamond', 102,
            'diamond-open', 202, 'diamond-dot', 302,
            'diamond-open-dot', 3, 'cross', 103, 'cross-open', 203,
            'cross-dot', 303, 'cross-open-dot', 4, 'x', 104, 'x-open',
            204, 'x-dot', 304, 'x-open-dot', 5, 'triangle-up', 105,
            'triangle-up-open', 205, 'triangle-up-dot', 305,
            'triangle-up-open-dot', 6, 'triangle-down', 106,
            'triangle-down-open', 206, 'triangle-down-dot', 306,
            'triangle-down-open-dot', 7, 'triangle-left', 107,
            'triangle-left-open', 207, 'triangle-left-dot', 307,
            'triangle-left-open-dot', 8, 'triangle-right', 108,
            'triangle-right-open', 208, 'triangle-right-dot', 308,
            'triangle-right-open-dot', 9, 'triangle-ne', 109,
            'triangle-ne-open', 209, 'triangle-ne-dot', 309,
            'triangle-ne-open-dot', 10, 'triangle-se', 110,
            'triangle-se-open', 210, 'triangle-se-dot', 310,
            'triangle-se-open-dot', 11, 'triangle-sw', 111,
            'triangle-sw-open', 211, 'triangle-sw-dot', 311,
            'triangle-sw-open-dot', 12, 'triangle-nw', 112,
            'triangle-nw-open', 212, 'triangle-nw-dot', 312,
            'triangle-nw-open-dot', 13, 'pentagon', 113,
            'pentagon-open', 213, 'pentagon-dot', 313,
            'pentagon-open-dot', 14, 'hexagon', 114, 'hexagon-open',
            214, 'hexagon-dot', 314, 'hexagon-open-dot', 15,
            'hexagon2', 115, 'hexagon2-open', 215, 'hexagon2-dot',
            315, 'hexagon2-open-dot', 16, 'octagon', 116,
            'octagon-open', 216, 'octagon-dot', 316,
            'octagon-open-dot', 17, 'star', 117, 'star-open', 217,
            'star-dot', 317, 'star-open-dot', 18, 'hexagram', 118,
            'hexagram-open', 218, 'hexagram-dot', 318,
            'hexagram-open-dot', 19, 'star-triangle-up', 119,
            'star-triangle-up-open', 219, 'star-triangle-up-dot', 319,
            'star-triangle-up-open-dot', 20, 'star-triangle-down',
            120, 'star-triangle-down-open', 220,
            'star-triangle-down-dot', 320,
            'star-triangle-down-open-dot', 21, 'star-square', 121,
            'star-square-open', 221, 'star-square-dot', 321,
            'star-square-open-dot', 22, 'star-diamond', 122,
            'star-diamond-open', 222, 'star-diamond-dot', 322,
            'star-diamond-open-dot', 23, 'diamond-tall', 123,
            'diamond-tall-open', 223, 'diamond-tall-dot', 323,
            'diamond-tall-open-dot', 24, 'diamond-wide', 124,
            'diamond-wide-open', 224, 'diamond-wide-dot', 324,
            'diamond-wide-open-dot', 25, 'hourglass', 125,
            'hourglass-open', 26, 'bowtie', 126, 'bowtie-open', 27,
            'circle-cross', 127, 'circle-cross-open', 28, 'circle-x',
            128, 'circle-x-open', 29, 'square-cross', 129,
            'square-cross-open', 30, 'square-x', 130, 'square-x-open',
            31, 'diamond-cross', 131, 'diamond-cross-open', 32,
            'diamond-x', 132, 'diamond-x-open', 33, 'cross-thin', 133,
            'cross-thin-open', 34, 'x-thin', 134, 'x-thin-open', 35,
            'asterisk', 135, 'asterisk-open', 36, 'hash', 136,
            'hash-open', 236, 'hash-dot', 336, 'hash-open-dot', 37,
            'y-up', 137, 'y-up-open', 38, 'y-down', 138,
            'y-down-open', 39, 'y-left', 139, 'y-left-open', 40,
            'y-right', 140, 'y-right-open', 41, 'line-ew', 141,
            'line-ew-open', 42, 'line-ns', 142, 'line-ns-open', 43,
            'line-ne', 143, 'line-ne-open', 44, 'line-nw', 144,
            'line-nw-open']

fig = go.Figure()

fig.update_layout(title="Custom Marker Symbols", height=800)

fig.update_xaxes(showticklabels=False)
fig.update_yaxes(showticklabels=False)

for index, symbol in enumerate(symbols[::2]): 
    fig.add_trace(go.Scatter(x=[(index % 16)], y=[(index // 16)], 
                                 marker_symbol=symbol, marker_color=index,
                                 marker_size=20, showlegend=False, mode="markers+text",
                                 name='',
                                 hovertemplate=f'<b>Symbol Name: {symbols[2*index + 1]}</b><br><b>Symbol Number: {symbols[2*index]}</b>',
                                 textfont_size=8
                                ))
  
fig.show()
```


### Reference

See https://plot.ly/python/reference/ for more information and chart attribute options!
