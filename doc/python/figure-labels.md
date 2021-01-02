---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.6.0
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
    version: 3.7.6
  plotly:
    description: How to set the global font, title, legend-entries, and axis-titles
      in python.
    display_as: file_settings
    language: python
    layout: base
    name: Setting the Font, Title, Legend Entries, and Axis Titles
    order: 13
    permalink: python/figure-labels/
    redirect_from: python/font/
    thumbnail: thumbnail/figure-labels.png
---

### Automatic Labelling with Plotly Express

[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/).

When using Plotly Express, your axes and legend are automatically labelled, and it's easy to override the automation for a customized figure using the `labels` keyword argument. The title of your figure is up to you though!

Here's a figure with automatic labels and then the same figure with overridden labels. Note the fact that when overriding labels, the axes, legend title *and hover labels* reflect the specified labels automatically.

```python
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_length", y="sepal_width", color="species",
                title="Automatic Labels Based on Data Frame Column Names")
fig.show()
```

```python
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_length", y="sepal_width", color="species",
                 labels={
                     "sepal_length": "Sepal Length (cm)",
                     "sepal_width": "Sepal Width (cm)",
                     "species": "Species of Iris"
                 },
                title="Manually Specified Labels")
fig.show()
```

### Global and Local Font Specification

You can set the figure-wide font with the `layout.font` attribute, which will apply to all titles and tick labels, but this can be overridden for specific plot items like individual axes and legend titles etc. In the following figure, we set the figure-wide font to Courier New in blue, and then override this for certain parts of the figure.

```python
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_length", y="sepal_width", color="species",
                title="Playing with Fonts")
fig.update_layout(
    font_family="Courier New",
    font_color="blue",
    title_font_family="Times New Roman",
    title_font_color="red",
    legend_title_font_color="green"
)
fig.update_xaxes(title_font_family="Arial")
fig.show()
```

### Fonts and Labels in Dash

[Dash](https://plotly.com/dash/) is the best way to build analytical apps in Python using Plotly figures. To run the app below, run `pip install dash dash-daq`, click "Download" to get the code and run `python app.py`.

Get started  with [the official Dash docs](https://dash.plotly.com/installation) and **learn how to effortlessly [style](https://plotly.com/dash/design-kit/) & [deploy](https://plotly.com/dash/app-manager/) apps like this with <a class="plotly-red" href="https://plotly.com/dash/">Dash Enterprise</a>.**

```python hide_code=true
from IPython.display import IFrame
snippet_url = 'https://dash-gallery.plotly.host/python-docs-dash-snippets/'
IFrame(snippet_url + 'figure-labels', width='100%', height=630)
```

### Manual Labelling with Graph Objects

When using (graph objects)[/python/graph-objects/] rather than [Plotly Express](/python/plotly-express/), you will need to explicitly label traces and axes:

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
    xaxis_title="X Axis Title",
    yaxis_title="Y Axis Title",
    legend_title="Legend Title",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    )
)

fig.show()
```

The configuration of the legend is discussed in detail in the [Legends](/python/legend/) page.

### Align Plot Title
The following example shows how to align the plot title in [layout.title](https://plotly.com/python/reference/layout/#layout-title). `x` sets the x position with respect to `xref` from "0" (left) to "1" (right), and `y` sets the y position with respect to `yref` from "0" (bottom) to "1" (top). Moreover, you can define `xanchor` to `left`,`right`, or `center` for setting the title's horizontal alignment with respect to its x position, and/or `yanchor` to `top`, `bottom`, or `middle` for setting the title's vertical alignment with respect to its y position.

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
See https://plotly.com/python/reference/layout/ for more information!
