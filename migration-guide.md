# Migration to Plotly 3.0.0

Plotly 3 introduces huge enhancements to the `plotly.py` visualization library from tab completion for properties in the Jupyter to a tighter validation detection to catch unknown figure errors, plotly 3 provides better workflow for Plotly users.


# Added
[asd](#foo)


# What's Added?
- Traces can be added and updated interactively by simply assigning to properties

- The full Traces and Layout API is generated from the plotly schema to provide a great experience for interactive use in the notebook

- Data validation covering the full API with clear, informative error messages



- Jupyter friendly docstrings on constructor params and properties

- Support for setting array properties as numpy arrays. When numpy arrays are used, ipywidgets binary serialization protocol is used to avoid converting these to JSON strings.

- Context manager API for animation

- Programmatic export of figures to static SVG images (and PNG and PDF with cairosvg installed).


```
# Load iris dataset
iris_data = datasets.load_iris()
feature_names = [name.replace(' (cm)', '').replace(' ', '_') for name in iris_data.feature_names]
iris_df = pd.DataFrame(iris_data.data, columns=feature_names)
iris_class = iris_data.target + 1
iris_df.head()
```

|  | sepal_length |	sepal_width	| petal_length	| petal_width|
| --- | --- | --- | --- |
| 0	| 5.1	|	3.5	|	1.4	|	0.2 |
| 1	| 4.9	|	3.0	|	1.4	|	0.2 |
| 2	| 4.7	|	3.2	|	1.3	|	0.2 |
| 3	| 4.6	| 3.1	|	1.5	|	0.2 |
| 4	| 5.0	| 3.6	|	1.4	|	0.2 |


## Create and display an empty FigureWidget
A FigureWidget behaves almost identically to a Figure but it is also an ipywidget that can be displayed directly in the notebook without calling `iplot`

```
f1 = FigureWidget()
f1
```

## Tab completion
Entering ``f1.add_<tab>`` displays add methods for all of the supported trace types

Entering ``f1.add_scatter(<tab>)`` displays the names of all of the top-level properties for the scatter trace type

Entering ``f1.add_scatter(<shift+tab>)`` displays the signature pop-up. Expanding this pop-up reveals the method doc string which contains the descriptions of all of the top level properties

```
# f1.add_
# f1.add_scatter
```

## Add scatter trace
```
scatt1 = f1.add_scatter(x=iris_df.sepal_length, y=iris_df.petal_width)
```

change the params
```
# Set marker
scatt1.mode = 'markers'
scatt1.marker.size = 8
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

f1
```


## What have we Changed?
- go.Figure() is not a dict
- widgets in jupyter

```
import plotly.graph_objs as go
scatter = go.Scatter()
```


# What have we Removed?
We have removed the following methods from the `plotly.graph_objs` plotly objects:
- `.to_string`
- `.strip_style`
- `.get_data`
- `.validate`
- `.to_dataframe`

# What is Depreciated?

- Plotly Objects form a tree hierarchy. For instance we have `go.Scatter` and the nested attribute `Marker` lives under scatter at `go.Scatter.Marker`. Now params that live a few nodes down the tree under a plotly class must be referenced in the full path.

Example:
```
fig = go.Figure(
    data=[
        go.Scatter(
            go.Scatter.Marker(
                symbol=0,
            ),
            x=[1,2,3],
            y=[1,2,3],
        )
    ]
)
```

`go.Data` is depreciated:

Instead of

```
go.Data([])
```

drop the go.Data and use a `list` instead:

```
[]
```

# foo
