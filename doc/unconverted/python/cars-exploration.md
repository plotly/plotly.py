---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  plotly:
    description: Use Plotly FigureWidget with hover callbacks and slider widgets
    display_as: chart_events
    language: python
    layout: base
    name: Car Exploration with Hover Events
    order: 26
    permalink: python/cars-exploration/
    thumbnail: thumbnail/figurewidget-cars.gif
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


# Cars dataset exploration with plotly.py version 3.0


## Load cars dataset

```python
import pandas as pd
import numpy as np
import plotly.graph_objs as go

cars_df = pd.read_csv('data/cars/cars.csv',
                      usecols=['City mpg',
                               'Fuel Type',
                               'Horsepower',
                               'Model Year',
                               'Torque', 'Hybrid', 'ID'])
cars_df.sample(5)
```

```python
cars_df.shape
```

## Load images of cars

```python
import os

image_data = {}
for img_filename in os.listdir('data/cars/images'):
    model_year = img_filename.split('.')[0]
    with open(f"data/cars/images/{img_filename}", "rb") as f:
        b = f.read()
        image_data[model_year] = b
```

```python
from ipywidgets import Image
Image(value=image_data['2012_Chevrolet_Camaro_Coupe'])
```

## Construct plotly.py Figure Widget
Torqe vs. MPG Scatter Trace

```python
import plotly.graph_objs as go
```

```python
fig = go.FigureWidget(
    data=[
        dict(
            type='scattergl',
            x=cars_df['Torque'],
            y=cars_df['City mpg'],
            mode='markers',
        )
    ],
)
```

### Display Figure
Before online or offline `iplot`. Still supported, but not needed with `FigureWidget`

```python
fig
```

### Label Figure
Use property assignment syntax to:


Set `fig.layout.title` to `'Torque and Fuel Efficience'`

```python
fig.layout.title = 'Torque and Fuel Efficience'
```

Check default font size

```python
fig.layout.titlefont.size
```

Increase the title font size

```python
fig.layout.titlefont.size = 22
```

Set `fig.layout.titlefont.family` to `'Rockwell'`

```python
fig.layout.titlefont.family = 'Rockwell'
```

### Create New View for Figure
If working in JupyterLab, right-click on blue bar to the left of the figure and select "Create New View for Output". Drag view to the right half of the screen.


### Label Axes


Set the `fig.layout.xaxis.title` property to `'Torque (foot-pounds)'`

```python
fig.layout.xaxis.title = 'Torque (foot-pounds)'
```

Set the `fig.layout.yaxis.title` property to `'City MPG'`

```python
fig.layout.yaxis.title = 'City MPG'
```

### Notice Quantization
Zoom in and notice that the dataset is quantized


### Apply Jitter

```python
scatter = fig.data[0]
scatter
```

```python
N = len(cars_df)
scatter.x = scatter.x + np.random.rand(N) * 10
scatter.y = scatter.y + np.random.rand(N) * 1
```

Zoom level did not reset! Plot is updated in-place. Not recreated each time a property changes


### Address Overplotting


Lower marker opacity

```python
scatter.marker.opacity = 0.2
```

Decrease marker size

```python
scatter.marker.size = 4
```

### Aside on validation


What if I though opacity ranged from 0 to 255?

```python
# scatter.marker.opacity = 50
```

What if I forgot the name of an enumeration value?

```python
# fig.layout.hovermode = 'nearest' # Set to 'closest'
fig.layout.hovermode = 'closest'
```

What if I don't know how to spell 'fuchsia'?

```python
scatter.marker.color = 'fuchsia' # Set to 'fuchsia'
```

Restore default marker color

```python
scatter.marker.color = None
```

### Add density contour


Add smoothed density contour trace (`histogram2dcontour`) based on `scatter.x` and `y=scatter.y` values.

```python
contour = fig.add_histogram2dcontour(
    x=scatter.x, y=scatter.y)
```

Set contour colorscale

```python
contour.colorscale = 'Hot'
```

Reverse the colorscale

```python
contour.reversescale = True
```

Disable tooltips for contour

```python
contour.hoverinfo = 'skip'
```

Tweak marker size and opacity

```python
scatter.marker.opacity = .1
scatter.marker.size = 3
```

### Create marker configuration widget


Define function that inputs `opacity` and `size` and updates the figure.

```python
def set_opacity(opacity, size):
    scatter.marker.opacity = opacity
    scatter.marker.size = size
```

Use `ipywidgets.interactive` to generate control panel for function.

```python
from ipywidgets import interactive
opacity_slider = interactive(set_opacity,
                             opacity=(0.0, 1.0, 0.01),
                             size=(1, 10, 0.25))
opacity_slider
```

Adjust the width of the slider widgets

```python
opacity_slider.children[0].layout.width = '400px'
opacity_slider.children[1].layout.width = '400px'
```

Try zooming and then adjusting the marker params


### Looking at outliers


#### Tooltips
Use `'ID'` column as tooltip for scatter

```python
scatter.text = cars_df['ID']
scatter.hoverinfo = 'text'
```

#### All properties


Create an HTML widget to display the hover properties

```python
from ipywidgets import HTML
details = HTML()
details
```

Register callback function to be executed on hover events. It will update the HTML widget using the pandas `to_html` method.

```python
def hover_fn(trace, points, state):
    ind = points.point_inds[0]
    details.value = cars_df.iloc[ind].to_frame().to_html()

scatter.on_hover(hover_fn)
```

#### Vehicle image


Create an `ipywidgets.Image` widget to display images

```python
from ipywidgets import Image, Layout
image_widget = Image(
    value=image_data['2012_Chevrolet_Camaro_Coupe'],
    layout=Layout(height='252px', width='400px')
)
image_widget
```

Update hover function to update the image widget along with the HTML widget

```python
def hover_fn(trace, points, state):

    ind = points.point_inds[0]

    # Update details HTML widget
    details.value = cars_df.iloc[ind].to_frame().to_html()

    # Update image widget
    model_year = cars_df['Model Year'][ind].replace(' ', '_')
    image_widget.value = image_data[model_year]

scatter.on_hover(hover_fn)
```

## Bringing it all together


Create simple dashboard using `HBox` and `VBox` containers

```python
from ipywidgets import HBox, VBox
VBox([fig,
      opacity_slider,
      HBox([image_widget, details])])
```

<img src='https://raw.githubusercontent.com/michaelbabyn/plot_data/master/cars_exploration.gif'>


#### Reference


See [these Jupyter notebooks](https://github.com/jonmmease/plotly_ipywidget_notebooks) for even more FigureWidget examples.

```python
help(go.FigureWidget)
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade

import publisher
publisher.publish(
    'cars-exploration.ipynb', 'python/cars-exploration/', 'Car Exploration with go.FigureWidget, Case Study',
    'Use Plotly FigureWidget with hover callbacks and slider widgets',
    title = 'Car Exploration with Hover Events',
    name = 'Car Exploration with Hover Events',
    has_thumbnail='true', thumbnail='thumbnail/zoom.jpg',
    language='python', page_type='example_index',
    display_as='chart_events', order=26,
    ipynb= '~notebook_demo/242')
```

```python

```
