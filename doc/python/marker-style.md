---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: "1.1"
      jupytext_version: 1.1.7
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
    version: 3.6.5
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

### Reference

See https://plot.ly/python/reference/ for more information and chart attribute options!
