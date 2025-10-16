---
description: How to add images to charts as background images or logos.
---

### Add a Background Image

In this page we explain how to add static, non-interactive images as background, logo or annotation images to a figure. For exploring image data in interactive charts, see the [tutorial on displaying image data](imshow.md).

A background image can be added to the layout of a figure with
`fig.add_layout_image` or by setting the `images` parameter of `go.Layout`. The
`source` attribute of a `go.layout.Image` can be the URL of an image, or a PIL
Image object (`from PIL import Image; img = Image.open('filename.png')`).

```python
import plotly.graph_objects as go

# Create figure
fig = go.Figure()

# Add trace
fig.add_trace(
    go.Scatter(x=[0, 0.5, 1, 2, 2.2], y=[1.23, 2.5, 0.42, 3, 1])
)

# Add images
fig.add_layout_image(
        dict(
            source="https://images.plot.ly/language-icons/api-home/python-logo.png",
            xref="x",
            yref="y",
            x=0,
            y=3,
            sizex=2,
            sizey=2,
            sizing="stretch",
            opacity=0.5,
            layer="below")
)

# Set templates
fig.update_layout(template="plotly_white")

fig.show()
```

### Add a Logo
See more examples of [adding logos to charts](https://plotly.com/python/logos/)!

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=["-35.3", "-15.9", "-15.8", "-15.6", "-11.1",
           "-9.6", "-9.2", "-3.5", "-1.9", "-0.9",
           "1.0", "1.4", "1.7", "2.0", "2.8", "6.2",
           "8.1", "8.5", "8.5", "8.6", "11.4", "12.5",
           "13.3", "13.7", "14.4", "17.5", "17.7",
           "18.9", "25.1", "28.9", "41.4"],
        y=["Designers, musicians, artists, etc.",
           "Secretaries and administrative assistants",
           "Waiters and servers", "Archivists, curators, and librarians",
           "Sales and related", "Childcare workers, home car workers, etc.",
           "Food preparation occupations", "Janitors, maids, etc.",
           "Healthcare technicians, assistants. and aides",
           "Counselors, social and religious workers",
           "Physical, life and social scientists", "Construction",
           "Factory assembly workers", "Machinists, repairmen, etc.",
           "Media and communications workers", "Teachers",
           "Mechanics, repairmen, etc.", "Financial analysts and advisers",
           "Farming, fishing and forestry workers",
           "Truck drivers, heavy equipment operator, etc.", "Accountants and auditors",
           "Human resources, management analysts, etc.", "Managers",
           "Lawyers and judges", "Engineers, architects and surveyors",
           "Nurses", "Legal support workers",
           "Computer programmers and system admin.", "Police officers and firefighters",
           "Chief executives", "Doctors, dentists and surgeons"],
        marker=go.bar.Marker(
            color="rgb(253, 240, 54)",
            line=dict(color="rgb(0, 0, 0)",
                      width=2)
        ),
        orientation="h",
    )
)

# Add image
fig.add_layout_image(
    dict(
        source="https://raw.githubusercontent.com/cldougl/plot_images/add_r_img/vox.png",
        xref="paper", yref="paper",
        x=1, y=1.05,
        sizex=0.2, sizey=0.2,
        xanchor="right", yanchor="bottom"
    )
)

# update layout properties
fig.update_layout(
    autosize=False,
    height=800,
    width=700,
    bargap=0.15,
    bargroupgap=0.1,
    barmode="stack",
    hovermode="x",
    margin=dict(r=20, l=300, b=75, t=125),
    title=("Moving Up, Moving Down<br>" +
           "<i>Percentile change in income between childhood and adulthood</i>"),
)

fig.show()
```

### Label Spectroscopy Data by Adding Multiple Images

```python
import plotly.graph_objects as go

import numpy as np
np.random.seed(1)
from scipy.signal import savgol_filter

# Simulate spectroscopy data
def simulated_absorption(mu, sigma, intensity):
    data = [np.random.normal(mu[i], sigma[i], intensity[i]) for i in range(len(mu))]
    hists = [np.histogram(d, 1000, range=(200, 500), density=True) for d in data]
    ys = [y for y, x in hists]
    s = savgol_filter(np.max(ys, axis=0), 41, 3)
    return hists[0][1], s

mus = [[290, 240, 260], [330, 350]]
sigmas = [[4, 6, 10], [5, 4]]
intensities = [[100000, 300000, 700000], [40000, 20000]]
simulated_absorptions = [simulated_absorption(m, s, i) for m, s, i in
                         zip(mus, sigmas, intensities)]

# Create figure
fig = go.Figure()

# Create traces from data
names = ["Benzene", "Naphthalene"]
for (x, y), n in zip(simulated_absorptions, names):
    fig.add_trace(go.Scatter(x=x, y=y, name=n))

# Add images
fig.add_layout_image(
    dict(
        source="https://raw.githubusercontent.com/michaelbabyn/plot_data/master/benzene.png",
        x=0.75,
        y=0.65,
    ))
fig.add_layout_image(dict(
        source="https://raw.githubusercontent.com/michaelbabyn/plot_data/master/naphthalene.png",
        x=0.9,
        y=0.3,
        )
)
fig.update_layout_images(dict(
        xref="paper",
        yref="paper",
        sizex=0.3,
        sizey=0.3,
        xanchor="right",
        yanchor="bottom"
))

# Add annotations
fig.update_layout(
    annotations=[
        dict(
            x=93.0 / 300,
            y=0.07 / 0.1,
            xref="paper",
            yref="paper",
            showarrow=True,
            arrowhead=0,
            opacity=0.5,
            ax=250,
            ay=-40,
        ),
        dict(
            x=156.0 / 300,
            y=0.04 / 0.1,
            xref="paper",
            yref="paper",
            showarrow=True,
            arrowhead=0,
            opacity=0.5,
            ax=140,
            ay=-10,
        )
    ]
)

# Configure axes
fig.update_xaxes(title_text="Wavelength")
fig.update_yaxes(title_text="Absorption", hoverformat=".3f")

# Configure other layout properties
fig.update_layout(
    title_text="Absorption Frequencies of Benzene and Naphthalene",
    height=500,
    width=900,
    template="plotly_white"
)

fig.show()
```

### Zoom on Static Images

```python
import plotly.graph_objects as go

# Create figure
fig = go.Figure()

# Constants
img_width = 1600
img_height = 900
scale_factor = 0.5

# Add invisible scatter trace.
# This trace is added to help the autoresize logic work.
fig.add_trace(
    go.Scatter(
        x=[0, img_width * scale_factor],
        y=[0, img_height * scale_factor],
        mode="markers",
        marker_opacity=0
    )
)

# Configure axes
fig.update_xaxes(
    visible=False,
    range=[0, img_width * scale_factor]
)

fig.update_yaxes(
    visible=False,
    range=[0, img_height * scale_factor],
    # the scaleanchor attribute ensures that the aspect ratio stays constant
    scaleanchor="x"
)

# Add image
fig.add_layout_image(
    dict(
        x=0,
        sizex=img_width * scale_factor,
        y=img_height * scale_factor,
        sizey=img_height * scale_factor,
        xref="x",
        yref="y",
        opacity=1.0,
        layer="below",
        sizing="stretch",
        source="https://raw.githubusercontent.com/michaelbabyn/plot_data/master/bridge.jpg")
)

# Configure other layout
fig.update_layout(
    width=img_width * scale_factor,
    height=img_height * scale_factor,
    margin={"l": 0, "r": 0, "t": 0, "b": 0},
)

# Disable the autosize on double click because it adds unwanted margins around the image
# More detail: https://plotly.com/python/configuration-options/
fig.show(config={'doubleClick': 'reset'})
```

## Annotating layout image with shapes

_introduced in plotly 4.7_

It can be useful to add shapes to a layout image, for highlighting an object, drawing bounding boxes as part of a machine learning training set, or identifying seeds for a segmentation algorithm.

In order to enable shape drawing, you need to
- define a dragmode corresponding to a drawing tool (`'drawline'`,`'drawopenpath'`, `'drawclosedpath'`, `'drawcircle'`, or `'drawrect'`)
- add [modebar buttons](configuration-options.md#add-optional-shapedrawing-buttons-to-modebar) corresponding to the drawing tools you wish to use.

The style of new shapes is specified by the `newshape` layout attribute. Shapes can be selected and modified after they have been drawn. More details and examples are given in the [tutorial on shapes](shapes.md#drawing-shapes-on-cartesian-plots).

Drawing or modifying a shape triggers a `relayout` event, which [can be captured by a callback inside a Dash application](https://dash.plotly.com/interactive-graphing).

```python
import plotly.graph_objects as go
fig = go.Figure()
# Add image
img_width = 1600
img_height = 900
scale_factor = 0.5
fig.add_layout_image(
        x=0,
        sizex=img_width,
        y=0,
        sizey=img_height,
        xref="x",
        yref="y",
        opacity=1.0,
        layer="below",
        source="https://raw.githubusercontent.com/michaelbabyn/plot_data/master/bridge.jpg"
)
fig.update_xaxes(showgrid=False, range=(0, img_width))
fig.update_yaxes(showgrid=False, scaleanchor='x', range=(img_height, 0))
# Line shape added programatically
fig.add_shape(
    type='line', xref='x', yref='y',
    x0=650, x1=1080, y0=380, y1=180, line_color='cyan'
)
# Set dragmode and newshape properties; add modebar buttons
fig.update_layout(
    dragmode='drawrect',
    newshape=dict(line_color='cyan'),
    title_text='Drag to add annotations - use modebar to change drawing tool'
)
fig.show(config={'modeBarButtonsToAdd':['drawline',
                                        'drawopenpath',
                                        'drawclosedpath',
                                        'drawcircle',
                                        'drawrect',
                                        'eraseshape'
                                       ]})
```


## Images Placed Relative to Axes

Using `xref='x domain'` or `yref='y domain'`, images can be placed relative to
axes. As an example, the following shows how to put an image in the top corner
of a subplot (try panning and zooming the resulting figure):

```python
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_length", y="sepal_width", facet_col="species")
# sources of images
sources = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Iris_setosa_var._setosa_%282595031014%29.jpg/360px-Iris_setosa_var._setosa_%282595031014%29.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Iris_versicolor_quebec_1.jpg/320px-Iris_versicolor_quebec_1.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Iris_virginica_2.jpg/480px-Iris_virginica_2.jpg",
]
# add images
for col, src in enumerate(sources):
    fig.add_layout_image(
        row=1,
        col=col + 1,
        source=src,
        xref="x domain",
        yref="y domain",
        x=1,
        y=1,
        xanchor="right",
        yanchor="top",
        sizex=0.2,
        sizey=0.2,
    )

fig.show()
```

### Reference
See [https://plotly.com/python/reference/layout/images/](reference/graph_objects/Layout.md#plotly.graph_objects.Layout.images) for more information and chart attribute options!
