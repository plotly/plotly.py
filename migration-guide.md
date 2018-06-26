# Migration to Plotly 3.0.0
There are many new and great features in Plotly 3.0 including deeper Jupyter integration, deeper figure validation, improved performance, and more. To get started right away with Plotly, check out the [tutorial](#getting-started) below.

## 3.0.0rc9 [08-06-2018]
### Added
- Jupyter integration - run `help(go.FigureWidget)` for more information
- update traces interactively
- Traces can be added and updated interactively by simply assigning to properties
- The full Traces and Layout API is generated from the plotly schema to provide a great experience for interactive use in the notebook
- Support for setting array properties as numpy arrays. When numpy arrays are used, ipywidgets binary serialization protocol is used to avoid converting these to JSON strings.
- Context manager API for animation. Run `help(go.Figure().batch_animate)` for the full doc string.
- Programmatic export of figures to static SVG images (and PNG and PDF with cairosvg installed).

### Removed
- Removed `.to_string`, `.strip_style`, `.get_data`, `.validate` and `.to_dataframe` methods from `plotly.graph_objs` objects. For example run `dir(plotly.graph_objs.Scatter)` to get all the (magic) methods of the Scatter class.


### Changed
- Improved data validation covering the full API with clear, informative error messages. This means that incorrect properties and/or values now always raise a `ValueError` with a description of the error, the invalid property, and the avaialble properties on the level that it was placed in the graph object. Eg. `go.Scatter(foo=123)` raises a validation error. See https://plot.ly/python/reference/ for a reference to all valid properties and values in the Python API.

- graph objects are not `dict`s anymore. Running a cell of a graph object prints out a dict-style representation of the object:

Eg. `plotly.graph_objs.Scatter()` prints

```
Scatter(**{
    'type': 'scatter'
})
```

- plotly objects now have a `.to_plotly_json` method that converts the object to a dict:

Eg. `go.Scatter().to_plotly_json()` returns `{'type': 'scatter'}`



### Deprecated
- all graph objects must now be written using their full path. For example if one wants to customize the marker param in a scatter object, write `plotly.graph_objs.scatter.Marker` instead of `plotly.graph_objs.Marker`. If the marker object lives in a `plotly.graph_objs.Scatter()` object then a deprecated message will appear. Similarly

```
import plotly.graph_objs as go
go.Scatter(
    x=[0],
    y=[0],
    marker=go.Marker(
        color='rgb(255,45,15)'
    )
)
```

produces a deprecation warning but

```
import plotly.graph_objs as go
go.Scatter(
    x=[0],
    y=[0],
    marker=go.scatter.Marker(
        color='rgb(255,45,15)'
    )
)
```

does not.

- `go.Data()` is deprecated. Use a list or array `[]` instead.


# Getting Started
## Installation
To install and enable with Jupyter or Jupyter lab, run:
```
pip install plotly==3.0.0rc9
pip install "notebook>=5.3" "ipywidgets>=7.2"  # only necessary for Jupyter Notebook environments
```

If you're using older versions of `notebook` or `ipywidgets` you may need to manually activate the widget extensions (this should not be needed for `notebook>=5.3` and `ipywidgets>=7.2`)

```
jupyter nbextension enable --py widgetsnbextension --sys-prefix
jupyter nbextension enable --py plotlywidget --sys-prefix
```

In addition, to add JupyterLab support run the following commands

```
pip install jupyterlab
jupyter labextension install @jupyter-widgets/jupyterlab-manager # install the Jupyter widgets extension
jupyter labextension install plotlywidget
```

## Simple Example
We now have a seamless integration of Jupyter support and the Plotly objects. We've introduced a new graph object called `go.FigureWidget` that acts like a regualar plotly `go.Figure` that can be displayed in Jupyter.

Simple Example: Make a Scatter Plot
```
import plotly
import plotly.graph_objs as go

f = go.FigureWidget()
f.add_scatter(x=[1, 2, 3], y=[4, 3, 5])
f
```


## Overview
```
# ipyplotly
from plotly.graph_objs import FigureWidget
from plotly.callbacks import Points, InputDeviceState

# pandas
import pandas as pd

# numpy
import numpy as np

# scikit learn
from sklearn import datasets

# ipywidgets
from ipywidgets import HBox, VBox, Button

# functools
from functools import partial

# Load iris dataset
iris_data = datasets.load_iris()
feature_names = [name.replace(' (cm)', '').replace(' ', '_') for name in iris_data.feature_names]
iris_df = pd.DataFrame(iris_data.data, columns=feature_names)
iris_class = iris_data.target + 1
iris_df.head()
```

#### Create and display an empty FigureWidget
A FigureWidget behaves almost identically to a Figure but it is also an ipywidget that can be displayed directly in the notebook without calling `iplot`
```
f1 = FigureWidget()
f1
```

#### Tab completion
Entering ``f1.add_<tab>`` displays add methods for all of the supported trace types
```
# f1.add_
```

Entering ``f1.add_scatter(<tab>)`` displays the names of all of the top-level properties for the scatter trace type

Entering ``f1.add_scatter(<shift+tab>)`` displays the signature pop-up. Expanding this pop-up reveals the method doc string which contains the descriptions of all of the top level properties

```
# f1.add_scatter(
```

#### Add scatter trace
```
scatt1 = f1.add_scatter(x=iris_df.sepal_length, y=iris_df.petal_width)
```

```
# That's not what we wanted, change the mode to 'markers'
scatt1.mode = 'markers'
# Set size to 8
scatt1.marker.size = 8
# Color markers by iris class
scatt1.marker.color = iris_class

# Change colorscale
scatt1.marker.cmin = 0.5
scatt1.marker.cmax = 3.5
scatt1.marker.colorscale = [[0, 'red'], [0.33, 'red'],
                            [0.33, 'green'], [0.67, 'green'],
                            [0.67, 'blue'], [1.0, 'blue']]

scatt1.marker.showscale = True

# Fix up colorscale ticks
scatt1.marker.colorbar.ticks = 'outside'
scatt1.marker.colorbar.tickvals = [1, 2, 3]
scatt1.marker.colorbar.ticktext = iris_data.target_names.tolist()

# Set colorscale title
scatt1.marker.colorbar.title = 'Species'
scatt1.marker.colorbar.titlefont.size = 16
scatt1.marker.colorbar.titlefont.family = 'Rockwell'

# Add axis labels
f1.layout.xaxis.title = 'sepal_length'
f1.layout.yaxis.title = 'petal_width'

# Hover info
scatt1.text = iris_data.target_names[iris_data.target]
scatt1.hoverinfo = 'text+x+y'
f1.layout.hovermode = 'closest'
```

#### Animate marker size change
```
# Set marker size based on petal_length
with f1.batch_animate(duration=1000):
    scatt1.marker.size = np.sqrt(iris_df.petal_length.values * 50)

# Restore constant marker size
with f1.batch_animate(duration=1000):
    scatt1.marker.size = 8
```

#### Set drag mode property callback
Make points more transparent when `dragmode` is `zoom`
```
def set_opacity(marker, layout, dragmode):
    if dragmode == 'zoom':
        marker.opacity = 0.5
    else:
        marker.opacity = 1.0
f1.layout.on_change(partial(set_opacity, scatt1.marker), 'dragmode')
```

#### Configure colorscale for brushing
```
scatt1.marker.colorbar = None
scatt1.marker.colorscale = [[0, 'lightgray'], [0.5, 'lightgray'], [0.5, 'red'], [1, 'red']]
scatt1.marker.cmin = -0.5
scatt1.marker.cmax = 1.5
scatt1.marker.colorbar.ticks = 'outside'
scatt1.marker.colorbar.tickvals = [0, 1]
scatt1.marker.colorbar.ticktext = ['unselected', 'selected']

# Reset colors to zeros (unselected)
scatt1.marker.color = np.zeros(iris_class.size)
selected = np.zeros(iris_class.size)
```

#### Configure brushing callback
```
# Assigning these variables here is not required. But doing so tricks Jupyter into
# providing property tab completion on the parameters to the brush function below
trace, points, state = scatt1, Points(), InputDeviceState()

def brush(trace, points, state):
    inds = np.array(points.point_inds)
    if inds.size:
        selected[inds] = 1
        trace.marker.color = selected

scatt1.on_selected(brush)
```

Now box or lasso select points on the figure and see them turn red

```
# Reset brush
selected = np.zeros(iris_class.size)
scatt1.marker.color = selected
```

#### Create second plot with different features
```
f2 = FigureWidget(data=[{'type': 'scatter',
                         'x': iris_df.petal_length,
                         'y': iris_df.sepal_width,
                         'mode': 'markers'}])
f2
```

```
# Set axis titles
f2.layout.xaxis.title = 'petal_length'
f2.layout.yaxis.title = 'sepal_width'

# Grab trace reference
scatt2 = f2.data[0]

# Set marker styles / colorbars to match between figures
scatt2.marker = scatt1.marker

# Configure brush on both plots to update both plots
def brush(trace, points, state):
    inds = np.array(points.point_inds)
    if inds.size:
        selected = scatt1.marker.color.copy()
        selected[inds] = 1
        scatt1.marker.color = selected
        scatt2.marker.color = selected    

scatt1.on_selected(brush)
scatt2.on_selected(brush)

f2.layout.on_change(partial(set_opacity, scatt2.marker), 'dragmode')

# Reset brush
def reset_brush(btn):
    selected = np.zeros(iris_class.size)
    scatt1.marker.color = selected
    scatt2.marker.color = selected

# Create reset button
button = Button(description="clear")
button.on_click(reset_brush)

# Hide colorbar for figure 1
scatt1.marker.showscale = False

# Set dragmode to lasso for both plots
f1.layout.dragmode = 'lasso'
f2.layout.dragmode = 'lasso'

# Display two figures and the reset button
f1.layout.width = 500
f2.layout.width = 500

VBox([HBox([f1, f2]), button])
```

#### Save figure 2 to a svg image in the exports directory
`f2.save_image('exports/f2.svg')`
