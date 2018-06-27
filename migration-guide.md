# Migration to Plotly 3.0.0
There are many new and great features in Plotly 3.0 including deeper Jupyter integration, deeper figure validation, improved performance, and more. To get started right away with Plotly, check out the tutorial below:

## Simple FigureWidget Example
We now have a seamless integration of Jupyter support and the Plotly objects. We've introduced a new graph object called `go.FigureWidget` that acts like a regular plotly `go.Figure` that can be displayed in Jupyter.

Simple Example: Make a Scatter Plot
```
import plotly
import plotly.graph_objs as go

f = go.FigureWidget()
f.add_scatter(x=[1, 2, 3], y=[4, 3, 5])
f
```

##


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
