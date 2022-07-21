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
    order: 26
    permalink: python/selections/
    thumbnail: thumbnail/make_selection.jpg
---

## Adding Selections

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

## Selections with Time Series

Selections are also supported on time series figures. Here, we add a rectangular selection with a region between the dates `2019-01-01"` and `"2019-10-01"` on the x axis and between `1` and `1.15` on the y axis.


```python
import plotly.express as px

df = px.data.stocks()
fig = px.line(df, x='date', y="GOOG")
fig.add_selection(x0="2019-01-01", y0=1, x1="2019-10-01", y1=1.17)
fig.show()
```

## More on Selections

For more on selections, see the [selections section of the `dcc.Graph` page](https://dash.plotly.com/dash-core-components/graph#selections) in the Dash docs.
