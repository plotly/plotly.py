# Migration to Plotly 3.0.0
There are many new and great features in Plotly 3.0 including deeper Jupyter integration, deeper figure validation, improved performance, and more. To get started right away with Plotly, check out the tutorial below:

## Simple FigureWidget Example
We now have a seamless integration of Jupyter support and the Plotly objects. We've introduced a new graph object called `go.FigureWidget` that acts like a regular plotly `go.Figure` that can be displayed in Jupyter.

Simple Example: Make a Scatter Plot
```
import plotly
import plotly.graph_objs as go

f = go.FigureWidget()
```

## Tab Completion
Entering ``f.add_<tab>`` displays add methods for all of the supported trace types. Try it!
```
f.add_
```

Entering `f.add_scatter(<tab>)` displays the names of all of the top-level properties for the scatter trace type

Entering `f.add_scatter(<shift+tab>)` displays the signature pop-up. Expanding this pop-up reveals the method doc string which contains the descriptions of all of the top level properties. Let's finish add a scatter trace to `f`:

```
f.add_scatter(x=[1,2,3], y=[4,3,2])
f
```

## New __repr__ method
plotly figures and graph objects now include the dict-like `__repr__` method that represents the object as a string

```
f.__repr__()
```

## FigureWidget Subplot Example
Let's create a subplot then turn it into a FigureWidget to display in the notebook. Note that `append_trace` is no deprecated. Use `add_trace` or `add_traces` instead.

```
import plotly
import plotly.graph_objs as go
import plotly.tools as tls

import pandas as pd
dataset = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv')

subplot = tls.make_subplots(2, 2, print_grid=False)
f2 = go.FigureWidget(subplot)

f2.add_trace(go.Scatter(x=dataset['Age'], y=dataset['Pregnancies'], mode='markers'), 1,1)
f2.add_trace(go.Scatter(x=dataset['Age'], y=dataset['BMI'], mode='markers'), 1,2)
f2.add_trace(go.Scatter(x=dataset['Age'], y=dataset['SkinThickness'], mode='markers'), 2,1)
f2.add_trace(go.Scatter(x=dataset['Age'], y=dataset['BloodPressure'], mode='markers'), 2,2)
f2.layout.title = 'Age against variables relating to diabetes'
f2
```

## What doesn't work anymore
Run the following examples to see what is now deprecated or not valid:

- Data array properties may not be specified as scalars:
```
import plotly.graph_objs as go
go.Bar(x=1)
```

- Undocumented properties are no longer available. These include: `.to_string`, `.strip_style`, `.get_data`, `.validate` and `.to_dataframe`.

- Object arrays such as `Figure.data` and `Layout.images` are now represented as tuples of graph objects, not lists. Run the following as a sanity check:

```
type(go.Figure().data)
```
