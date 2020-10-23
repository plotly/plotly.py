---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.0
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
    version: 3.7.3
  plotly:
    description: How to add annotated horizontal and vertical lines in Python.
    display_as: file_settings
    language: python
    layout: base
    name: Horizontal and Vertical Lines and Rectangles
    order: 37
    permalink: python/horizontal-vertical-shapes/
    thumbnail: thumbnail/shape.jpg
---

### Horizontal and Vertical Lines and Rectangles (Autoshapes)

*introduced in plotly 4.12*

Horizontal and vertical lines and rectangles (autoshapes) that span an entire
plot can be added via the `add_hline`, `add_vline`, `add_hrect`, and `add_vrect`
methods of `plotly.graph_objects.Figure`. Shapes added with these methods are
added as [layout shapes](/python/shapes) (as shown when doing `print(fig)`, for
example). These shapes are fixed to the endpoints of one axis, regardless of the
range of the plot, and fixed to data coordinates on the other axis. The
following shows some possibilities, try panning and zooming the resulting figure
to see how the shapes stick to some axes:


```python
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_length", y="sepal_width")

# Add a vertical line that spans the entire y axis
# intersecting the x axis at x=5
fig.add_vline(x=5, line_color="red")
# Add a horizontal line that spans the entire x axis
# intersecting the y axis at y=3
fig.add_hline(y=3, line_color="blue")
# Add a vertical rectangle that spans the entire y axis
# intersecting the x axis at 5.5 and 6.5
fig.add_vrect(x0=5.5, x1=6.5, line_color="purple")
# Add a horizontal rectangle that spans the entire x axis
# intersecting the y axis at 2.5 and 4
fig.add_hrect(y0=2.5, y1=4, line_color="orange")
# (try panning and zooming the plot)
fig.show()
```

#### Adding Autoshapes to Multiple Facets / Subplots

The same line or box can be added to multiple facets by using the `'all'`
keyword in the `row` and `col` arguments like with `Figure.add_shape`. For
example
```python
import plotly.express as px

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", facet_row="smoker", facet_col="sex")
# Adds a vertical line to all facets
fig.add_vline(x=30, row="all", col="all", line_color="purple")
# Adds a horizontal line to all the rows of the second column
fig.add_hline(y=6, row="all", col=2, line_color="yellow")
# Adds a vertical rectangle to all the columns of the first row
fig.add_vrect(x0=20, x1=40, row=1, col="all", line_color="green")
fig.show()
```
The default `row` and `col` values are `"all"` so
`fig.add_vline(x=30, line_color="purple")` is equivalent
to `fig.add_vline(x=30, row="all", col="all", line_color="purple")` in the above
example.

#### Adding Text Annotations to Autoshapes

Text [annotations](/python/text-and-annotations) can be added to an autoshape
using the `annotation` keyword. Using the above example:
```python
import plotly.express as px
import plotly.graph_objects as go

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", facet_row="smoker", facet_col="sex")
# Add annotations anchored to the top right corner of the resulting lines
fig.add_vline(x=30, line_color="purple", annotation=go.layout.Annotation(text="A"))
# Another way to add annotations when we are only interested in specifying text
fig.add_hline(y=6, row="all", col=2, line_color="yellow", annotation_text="B")
# Specify the position of the resulting annotations
fig.add_vrect(
    x0=20,
    x1=40,
    row=1,
    col="all",
    line_color="green",
    annotation_text="C",
    annotation_position="bottom inside left",
)
fig.show()
```
Call `help` on any of the autoshape functions in the Python interpreter to learn
more (e.g., `help(fig.add_vline)`).
