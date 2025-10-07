---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.1
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
    version: 3.8.8
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

#### Horizontal and vertical lines in Dash

[Dash](https://plotly.com/dash/) is the best way to build analytical apps in Python using Plotly figures. To run the app below, run `pip install dash`, click "Download" to get the code and run `python app.py`.

Get started  with [the official Dash docs](https://dash.plotly.com/installation) and **learn how to effortlessly [style](https://plotly.com/dash/design-kit/) & publish apps like this with <a class="plotly-red" href="https://plotly.com/dash/">Dash Enterprise</a> or <a class="plotly-red" href="https://plotly.com/cloud/">Plotly Cloud</a>.**


```python hide_code=true
from IPython.display import IFrame
snippet_url = 'https://python-docs-dash-snippets.herokuapp.com/python-docs-dash-snippets/'
IFrame(snippet_url + 'horizontal-vertical-shapes', width='100%', height=1200)
```

<div style="font-size: 0.9em;"><div style="width: calc(100% - 30px); box-shadow: none; border: thin solid rgb(229, 229, 229);"><div style="padding: 5px;"><div><p><strong>Sign up for Dash Club</strong> → Free cheat sheets plus updates from Chris Parmer and Adam Schroeder delivered to your inbox every two months. Includes tips and tricks, community apps, and deep dives into the Dash architecture.
<u><a href="https://go.plotly.com/dash-club?utm_source=Dash+Club+2022&utm_medium=graphing_libraries&utm_content=inline">Join now</a></u>.</p></div></div></div></div>


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
#### Text Labels on Shapes

*New in 5.14*

[Text labels on shapes](/python/shapes/#addingtextlabelstoshapes), introduced in version 5.14, is now the recommended way to add text to shapes. The above examples using `add_hline`, `add_vrect`, `add_hrect`, and `add_vline` that add annotations can be rewritten to use `label`.

```python
import plotly.express as px

df = px.data.stocks(indexed=True)
fig = px.line(df)
fig.add_hline(
    y=1,
    line_dash="dot",
    label=dict(
        text="Jan 1 2018 Baseline",
        textposition="end",
        font=dict(size=20, color="blue"),
        yanchor="top",
    ),
)
fig.add_vrect(
    x0="2018-09-24",
    x1="2018-12-18",
    label=dict(
        text="Decline",
        textposition="top center",
        font=dict(size=20, family="Times New Roman"),
    ),
    fillcolor="green",
    opacity=0.25,
    line_width=0,
)
fig.show()

```

With [text labels on shapes](/python/shapes/#adding-text-labels-to-shapes), you can also add text labels to shapes other than lines and rectangles, and the labels can be added automatically to shapes drawn by the user.


### Reference

More details are available about [layout shapes](/python/shapes/) and [annotations](/python/text-and-annotations).

Reference documentation is also available for [`add_hline`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html?highlight=add_hline#plotly.graph_objects.Figure.add_hline), [`add_vline`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html?highlight=add_vline#plotly.graph_objects.Figure.add_vline), [`add_hrect`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html?highlight=add_hrect#plotly.graph_objects.Figure.add_hrect), [`add_vrect`](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html?highlight=add_vrect#plotly.graph_objects.Figure.add_vrect).
