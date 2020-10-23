---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.2
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
    version: 3.7.7
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

### Horizontal and Vertical Lines and Rectangles

*introduced in plotly 4.12*

Horizontal and vertical lines and rectangles that span an entire
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
fig = px.scatter(df, x="petal_length", y="petal_width")
fig.add_hline(y=0.9)
fig.add_vrect(x0=0.9, x1=2)
fig.show()
```

These shapes can be styled by passing the same arguments as are accepted by `add_shape`:

```python
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="petal_length", y="petal_width")
fig.add_vline(x=2.5, line_width=3, line_dash="dash", line_color="green")
fig.add_hrect(y0=0.9, y1=2.6, line_width=0, fillcolor="red", opacity=0.2)
fig.show()
```

#### Adding Text Annotations

[Text annotations](/python/text-and-annotations) can optionally be added to an autoshape
using the `annotation_text` keyword argument, and positioned using the `annotation_position` argument:

```python
import plotly.express as px

df = px.data.stocks(indexed=True)
fig = px.line(df)
fig.add_hline(y=1, line_dash="dot",
              annotation_text="Jan 1, 2018 baseline", 
              annotation_position="bottom right")
fig.add_vrect(x0="2018-09-24", x1="2018-12-18", 
              annotation_text="decline", annotation_position="top left",
              fillcolor="green", opacity=0.25, line_width=0)
fig.show()
```

Extra formatting of the annotation can be done using magic-underscores prefixed by `annotation_` or by passing a `dict` or `go.layout.Annotation` instance to the `annotation` argument:

```python
import plotly.express as px

df = px.data.stocks(indexed=True)
fig = px.line(df)
fig.add_hline(y=1, line_dash="dot",
              annotation_text="Jan 1, 2018 baseline", 
              annotation_position="bottom right",
              annotation_font_size=20,
              annotation_font_color="blue"
             )
fig.add_vrect(x0="2018-09-24", x1="2018-12-18", 
              annotation_text="decline", annotation_position="top left",
              annotation=dict(font_size=20, font_family="Times New Roman"),
              fillcolor="green", opacity=0.25, line_width=0)
fig.show()
```

#### Adding to Multiple Facets / Subplots

The same line or box can be added to multiple [subplots](/python/subplots/) or [facets](/python/facet-plots/) by setting the `row` and/or `col` to `"all"`. The default `row` and `col` values are `"all"`.
```python
import plotly.express as px

df = px.data.stocks(indexed=True)
fig = px.line(df, facet_col="company", facet_col_wrap=2)
fig.add_hline(y=1, line_dash="dot", row=3, col="all",
              annotation_text="Jan 1, 2018 baseline", 
              annotation_position="bottom right")
fig.add_vrect(x0="2018-09-24", x1="2018-12-18", row="all", col=1,
              annotation_text="decline", annotation_position="top left",
              fillcolor="green", opacity=0.25, line_width=0)
fig.show()
```
### Reference

More details are available about [layout shapes](/python/shapes/) and [annotations](/python/text-and-annotations). 

Reference documentation is also available for [`add_hline`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html?highlight=add_hline#plotly.graph_objects.Figure.add_hline), [`add_vline`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html?highlight=add_vline#plotly.graph_objects.Figure.add_vline), [`add_hrect`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html?highlight=add_hrect#plotly.graph_objects.Figure.add_hrect), [`add_vrect`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html?highlight=add_vrect#plotly.graph_objects.Figure.add_vrect).
