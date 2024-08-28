---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.3
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
    version: 3.10.14
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

### Set Automargin on the Plot Title

*New in 5.14*

Set `automargin=True` to allow the title to push the figure margins. With `yref` set to `paper`, `automargin=True`  expands the margins to make the title visible, but doesn't push outside the container. With `yref` set to `container`, `automargin=True` expands the margins, but the title doesn't overlap with the plot area, tick labels, and axis titles. 


```python
import plotly.express as px

df = px.data.gapminder().query("continent == 'Oceania'")
fig = px.line(df, x="year", y="gdpPercap", color="country")

fig.update_layout(
    title=dict(text="GDP-per-capita", font=dict(size=50), automargin=True, yref='paper')
)

fig.show()
```

### Fonts and Labels in Dash

[Dash](https://plotly.com/dash/) is the best way to build analytical apps in Python using Plotly figures. To run the app below, run `pip install dash dash-daq`, click "Download" to get the code and run `python app.py`.

Get started  with [the official Dash docs](https://dash.plotly.com/installation) and **learn how to effortlessly [style](https://plotly.com/dash/design-kit/) & [deploy](https://plotly.com/dash/app-manager/) apps like this with <a class="plotly-red" href="https://plotly.com/dash/">Dash Enterprise</a>.**

```python hide_code=true
from IPython.display import IFrame
snippet_url = 'https://python-docs-dash-snippets.herokuapp.com/python-docs-dash-snippets/'
IFrame(snippet_url + 'figure-labels', width='100%', height=1200)
```

<div style="font-size: 0.9em;"><div style="width: calc(100% - 30px); box-shadow: none; border: thin solid rgb(229, 229, 229);"><div style="padding: 5px;"><div><p><strong>Sign up for Dash Club</strong> → Free cheat sheets plus updates from Chris Parmer and Adam Schroeder delivered to your inbox every two months. Includes tips and tricks, community apps, and deep dives into the Dash architecture.
<u><a href="https://go.plotly.com/dash-club?utm_source=Dash+Club+2022&utm_medium=graphing_libraries&utm_content=inline">Join now</a></u>.</p></div></div></div></div>


### Manual Labelling with Graph Objects

When using [graph objects](/python/graph-objects/) rather than [Plotly Express](/python/plotly-express/), you will need to explicitly label traces and axes:

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

### Configuring Font Variant, Style, and  Weight

*New in 5.22*

You can configure a `variant`, `style`, and `weight` on `layout.font`. Here, we set the font variant to `small-caps`.

```python
import plotly.graph_objects as go
from plotly import data

df = data.iris()

setosa_df = df[df["species"] == "setosa"]
versicolor_df = df[df["species"] == "versicolor"]
virginica_df = df[df["species"] == "virginica"]

fig = go.Figure(
    data=[
        go.Scatter(
            x=setosa_df["sepal_width"],
            y=setosa_df["sepal_length"],
            mode="markers",
            name="setosa",
        ),
        go.Scatter(
            x=versicolor_df["sepal_width"],
            y=versicolor_df["sepal_length"],
            mode="markers",
            name="versicolor",
        ),
        go.Scatter(
            x=virginica_df["sepal_width"],
            y=virginica_df["sepal_length"],
            mode="markers",
            name="virginica",
        ),
    ],
    layout=go.Layout(
        title="Plot Title",
        xaxis=dict(title="X Axis Title"),
        yaxis=dict(title="Y Axis Title"),
        legend=dict(title="Legend Title"),
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple",
            variant="small-caps",
        )
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

### Adding a Plot Subtitle

*New in 5.23*

Add a subtitle to a plot with `layout.title.subtitle`. In the following example, we set the subtitle's `text`, and configure the `font` `color` and `size`. By default, if you don't set a font size for the subtitle, it will be `0.7` of the `title` font size.

```python
import plotly.graph_objects as go
from plotly import data

df = data.gapminder().query("continent == 'Europe' and (year == 1952 or year == 2002)")

df_pivot = df.pivot(index="country", columns="year", values="lifeExp")

fig = go.Figure(
    [
        go.Bar(
            x=df_pivot.index, y=df_pivot[1952], name="1952", marker_color="IndianRed"
        ),
        go.Bar(
            x=df_pivot.index, y=df_pivot[2002], name="2002", marker_color="LightSalmon"
        ),
    ],
    layout=dict(
        title=dict(
            text="Life Expectancy",
            subtitle=dict(
                text="Life expectancy by European country in 1952 and in 2002",
                font=dict(color="gray", size=13),
            ),
        )
    ),
)


fig.show()

```

#### Reference
See https://plotly.com/python/reference/layout/ for more information!
