---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.7
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
    version: 3.9.0
  plotly:
    description: How to use selections in Python. Examples of adding and styling selections.
    display_as: file_settings
    language: python
    layout: base
    name: Selections
    order: 38
    permalink: python/selections/
    thumbnail: thumbnail/ml_apps.png
---

## Adding Selections to Cartesian Subplots

*New in 5.10*

You can add persistent selections to a rendered figure using the **Box Select** and **Lasso Select** tools in the mode bar.
To add multiple selections, select **Shift** when making new selections.
To clear a selection, double-click it. On a subplot you can clear all selections by double-clicking any unselected area of the subplot.



You can also add selections to a figure that displays when it renders using `fig.add_selection`.
Here, we add a rectangular selection with a region between `3.0` and `6.5` on the x axis and between `3.5` and `5.5` on the y axis.


```python
import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.add_selection(x0=3.0, y0=6.5, x1=3.5, y1=5.5)

fig.show()
```

## Selections Using a Custom SVG


In the above example, we added a rectangular selection. You can also render a custom SVG for a selection by defining a `path` that can include single or multiple polygons. Here, we create a selection with a single polygon path "M2,6.5L4,7.5L4,6Z".

Please note that multiple polygons e.g. "M0,0L0,10L10,10,L10,0Z M2,2L2,8L8,8,L8,2Z" could be used to subtract certain regions from the selection.

```python
import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.add_selection(path="M2,6.5L4,7.5L4,6Z")

fig.show()
```

## Styling Selections


In the above example, we added a selection to the figure that is displayed when the figure renders.
`fig.add_selection` accepts additional properties that you can use to style the selection. Here, we add a `color`, `width`, and specify the `dash` type for the selection.


```python
import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.add_selection(
    x0=2.5, y0=6.5, x1=3.5, y1=5.5,
    line=dict(
        color="Crimson",
        width=2,
        dash="dash",
    ))

fig.show()

```

## Styling New Selections

You can style new selections made on the figure by setting properties on `newselection`.
Try making a new selection on the figure to try it out.

```python
import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length")

fig.update_layout(dragmode='select',
                  newselection=dict(line=dict(color='blue')))

fig.show()
```

## Fill Color for Active Selections

You can style the active selection with `activeselection`. In this example, we set active selections (when created or clicked) to appear with a `fillcolor` of `yellow`.

```python
import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.add_selection(x0=3.0, y0=6.5, x1=3.5, y1=5.5)

fig.update_layout(dragmode='select',
                  activeselection=dict(fillcolor='yellow'))

fig.show()
```

## Selections with Time Series

Selections are also supported on time series figures. Here, we add a rectangular selection with a region between the dates `2019-01-01"` and `"2019-10-01"` on the x axis and between `0.95` and `1.15` on the y axis.


```python
import plotly.express as px

df = px.data.stocks()
fig = px.line(df, x='date', y="GOOG", markers=True)
fig.add_selection(x0="2019-01-01", y0=0.95, x1="2019-10-01", y1=1.15)
fig.show()
```

## Referencing Selections on Multiple Cartesian Subplots


You can add selections to multiple Cartesian subplots by specifying `xref` and/or `yref`. Here, we add one selection on the plot with axis ids `x` and `y2` and two selections to the the plot with axis ids `x` and `y`.

```python
import plotly.graph_objects as go

import numpy as np

np.random.seed(0)
t = np.linspace(-1, 1.2, 2000)
x = (t**3) + (0.3 * np.random.randn(2000))
y = (t**6) + (0.3 * np.random.randn(2000))

fig = go.Figure()
fig.add_trace(go.Histogram2dContour(
        x = x,
        y = y,
        colorscale = 'Blues',
        reversescale = True,
        xaxis = 'x',
        yaxis = 'y'
    ))
fig.add_trace(go.Scatter(
        x = x,
        y = y,
        xaxis = 'x',
        yaxis = 'y',
        mode = 'markers',
        marker = dict(
            color = 'rgba(0,0,0,0.3)',
            size = 3
        )
    ))
fig.add_trace(go.Histogram(
        y = y,
        xaxis = 'x2',
        marker = dict(
            color = 'rgba(0,0,0,1)'
        )
    ))
fig.add_trace(go.Histogram(
        x = x,
        yaxis = 'y2',
        marker = dict(
            color = 'rgba(0,0,0,1)'
        )
    ))

fig.update_layout(
    autosize = False,
    xaxis = dict(
        zeroline = False,
        domain = [0,0.85],
        showgrid = False
    ),
    yaxis = dict(
        zeroline = False,
        domain = [0,0.85],
        showgrid = False
    ),
    xaxis2 = dict(
        zeroline = False,
        domain = [0.85,1],
        showgrid = False
    ),
    yaxis2 = dict(
        zeroline = False,
        domain = [0.85,1],
        showgrid = False
    ),
    height = 600,
    width = 600,
    bargap = 0,
    hovermode = 'closest',
    showlegend = False,
    selections = [
        dict(
            x0 = 0.5,
            x1 = -0.5,
            xref = "x",
            y0 = 190,
            y1= 0,
            yref = "y2",
            line = dict(
                color="yellow"
            )
        ),
        dict(
            x0 = -0.2,
            x1 = -1.5,
            xref = "x",
            y0 = 2,
            y1= -1,
            yref = "y",
            line = dict(
                color="yellow"
            )
        ),
        dict(
            path= "M0.75,2.39L0.98,3.38L1.46,3.68L1.80,3.35L2.01,2.51L1.67,1.15L1.18,0.50L0.65,0.66L0.54,0.83L0.49,1.56Z",
            xref= 'x',
            yref = 'y',
            line = dict(
                color='yellow'
            )
        )
    ]
)


fig.show()
```

## Referencing Selections on a Scatterplot Matrix


You can add selections to a scatterplot matrix  by specifying `xref` and/or `yref`. Here, we add one selection on the plot with axis ids `x2` and `y2` and another on the plot with ids `x3` and `y`.

```python
import plotly.express as px

df = px.data.iris()

fig = px.scatter_matrix(df,
    dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"],
    color="species")

fig.update_layout(
    xaxis = {"matches": "y"},
    xaxis2 = {"matches": "y2"},
    xaxis3 = {"matches": "y3"},
    xaxis4 = {"matches": "y4"},
    height = 900,
    width = 750,
    dragmode = 'select',
    selections = [
        dict(
            x0 = 3,
            x1 = 4,
            xref = "x2",
            y0 = 8,
            y1= 6,
            yref = "y"
        ),
        dict(
            x0 = 5,
            x1 = 1,
            xref = "x3",
            y0 = 5,
            y1= 4,
            yref = "y",
        )
    ]
)

fig.show()
```

