---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.2.1
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
    description: How to set the global font, title, legend-entries, and axis-titles
      in python.
    display_as: file_settings
    language: python
    layout: base
    name: Setting the Font, Title, Legend Entries, and Axis Titles
    order: 12
    permalink: python/figure-labels/
    redirect_from: python/font/
    thumbnail: thumbnail/figure-labels.png
---

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    name="Name of Trace 1"       # this sets its legend entry
))


fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[1, 0, 3, 2, 5, 4, 7, 6, 8],
    name="Name of Trace 2"
))

fig.update_layout(
    title="Plot Title",
    xaxis_title="x Axis Title",
    yaxis_title="y Axis Title",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
)

fig.show()
```

The configuration of the legend is discussed in detail in the [Legends](/python/legend/) page.

### Align Plot Title
The following example shows how to align the plot title in [layout.title](https://plot.ly/python/reference/#layout-title). `x` sets the x position with respect to `xref` from "0" (left) to "1" (right), and `y` sets the y position with respect to `yref` from "0" (bottom) to "1" (top). Moreover, you can define `xanchor` to `left`,`right`, or `center` for setting the title's horizontal alignment with respect to its x position, and/or `yanchor` to `top`, `bottom`, or `middle` for setting the title's vertical alignment with respect to its y position.

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scatter(
    y=[3, 1, 4],
    x=["Mon", "Tue", "Wed"]))

fig.update_layout(
    title={
        'text': "Plot Title",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'})

fig.show()
```

#### Reference
See https://plot.ly/python/reference/#layout for more information!
