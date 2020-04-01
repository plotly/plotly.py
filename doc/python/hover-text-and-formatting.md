---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.1
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
    version: 3.6.8
  plotly:
    description: How to use hover text and formatting in Python with Plotly.
    display_as: file_settings
    language: python
    layout: base
    name: Hover Text and Formatting
    order: 22
    permalink: python/hover-text-and-formatting/
    thumbnail: thumbnail/hover-text.png
---

### Hover Labels

One of the most deceptively-power features of interactive visualization using Plotly is the ability for the user to reveal more information about a data point by moving their mouse cursort over the point and having a hover label appear. 

There are three hover modes available in Plotly. The default setting is `layout.hovermode='closest'`, wherein a single hover label appears for the point directly underneat the cursor:

```python
import plotly.express as px

df = px.data.gapminder().query("continent=='Oceania'")

fig = px.line(df, x="year", y="lifeExp", color="country", title="layout.hovermode='closest' (the default)")
fig.update_traces(mode="markers+lines")

fig.show()
```

If `layout.hovermode='x'` (or `'y'`), a single hover label appears per trace, for points at the same `x` (or `y`) value as the cursor. If multiple points in a given trace exist at the same coordinate, only one will get a hover label. In the line plot below we have forced markers to appear, to make it clearer what can be hovered over, and we have disabled the built-in Plotly Express `hovertemplate` by setting it to `None`, resulting in a more compact hover label per point:

```python
import plotly.express as px

df = px.data.gapminder().query("continent=='Oceania'")

fig = px.line(df, x="year", y="lifeExp", color="country", title="layout.hovermode='x'")
fig.update_traces(mode="markers+lines", hovertemplate=None)
fig.update_layout(hovermode="x")

fig.show()
```

If `layout.hovermode='x unified'` (or `'y unified'`), a single hover label appear, describing one point per trace, for points at the same `x` (or `y`) value as the cursor.  If multiple points in a given trace exist at the same coordinate, only one will get an entry in the hover label. In the line plot below we have forced markers to appear, to make it clearer what can be hovered over, and we have disabled the built-in Plotly Express `hovertemplate` by setting it to `None`, resulting in a more compact entry per point in the hover label:

```python
import plotly.express as px

df = px.data.gapminder().query("continent=='Oceania'")

fig = px.line(df, x="year", y="lifeExp", color="country", title="layout.hovermode='x unified'")
fig.update_traces(mode="markers+lines", hovertemplate=None)
fig.update_layout(hovermode="x unified")

fig.show()
```

### Customizing Hover Label Appearance

Hover label text and colors default to trace colors in hover modes other than `unified`, and can be globally set via the `layout.hoverlabel` attributes. Hover label appearance can also be controlled per trace in `<trace>.hoverlabel`.

```python
import plotly.express as px

df = px.data.gapminder().query("continent=='Oceania'")

fig = px.line(df, x="year", y="lifeExp", color="country", title="Custom layout.hoverlabel formatting")
fig.update_traces(mode="markers+lines")

fig.update_layout(
    hoverlabel=dict(
        bgcolor="white", 
        font_size=16, 
        font_family="Rockwell"
    )
)

fig.show()
```

### Customizing Hover text with Plotly Express

Plotly Express functions automatically add all the data being plotted (x, y, color etc) to the hover label. Many Plotly Express functions also support configurable hover text. The `hover_data` argument accepts a list of column names to be added to the hover tooltip. The `hover_name` property controls which column is displayed in bold as the tooltip title.

Here is an example that creates a scatter plot using Plotly Express with custom hover data and a custom hover name.

```python
import plotly.express as px

df_2007 = px.data.gapminder().query("year==2007")

fig = px.scatter(df_2007, x="gdpPercap", y="lifeExp", log_x=True,
                 hover_name="country", hover_data=["continent", "pop"])

fig.show()
```

### Customizing hover text with a hovertemplate

To customize the tooltip on your graph you can use [hovertemplate](https://plotly.com/python/reference/#pie-hovertemplate), which is a template string used for rendering the information that appear on hoverbox.
This template string can include `variables` in %{variable} format, `numbers` in [d3-format's syntax](https://github.com/d3/d3-3.x-api-reference/blob/master/Formatting.md#d3_forma), and `date` in [d3-time-format's syntax](https://github.com/d3/d3-3.x-api-reference/blob/master/Time-Formatting.md#format).
Hovertemplate customize the tooltip text vs. [texttemplate](https://plotly.com/python/reference/#pie-texttemplate) which customizes the text that appears on your chart. <br>
Set the horizontal alignment of the text within tooltip with [hoverlabel.align](https://plotly.com/python/reference/#layout-hoverlabel-align).

Plotly Express automatically sets the `hovertemplate`, but you can set it manually when using `graph_objects`.

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scatter(
    x = [1,2,3,4,5],
    y = [2.02825,1.63728,6.83839,4.8485,4.73463],
    hovertemplate =
    '<i>Price</i>: $%{y:.2f}'+
    '<br><b>X</b>: %{x}<br>'+
    '<b>%{text}</b>',
    text = ['Custom text {}'.format(i + 1) for i in range(5)],
    showlegend = False))

fig.add_trace(go.Scatter(
    x = [1,2,3,4,5],
    y = [3.02825,2.63728,4.83839,3.8485,1.73463],
    hovertemplate = 'Price: %{y:$.2f}<extra></extra>',
    showlegend = False))

fig.update_layout(
    hoverlabel_align = 'right',
    title = "Set hover text with hovertemplate")

fig.show()
```

```python
import plotly.graph_objects as go

fig = go.Figure(go.Pie(
    name = "",
    values = [2, 5, 3, 2.5],
    labels = ["R", "Python", "Java Script", "Matlab"],
    text = ["textA", "TextB", "TextC", "TextD"],
    hovertemplate = "%{label}: <br>Popularity: %{percent} </br> %{text}"
))

fig.show()
```

### Advanced Hover Template

The following example shows how to format hover template. [Here](https://plotly.com/python/v3/hover-text-and-formatting/#dash-example) is an example to see how to format hovertemplate in Dash.

```python
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import math

data = px.data.gapminder()
df_2007 = data[data['year']==2007]
df_2007 = df_2007.sort_values(['continent', 'country'])

bubble_size = []

for index, row in df_2007.iterrows():
    bubble_size.append(math.sqrt(row['pop']))

df_2007['size'] = bubble_size
continent_names = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
continent_data = {continent:df_2007.query("continent == '%s'" %continent)
                              for continent in continent_names}

fig = go.Figure()

for continent_name, continent in continent_data.items():
    fig.add_trace(go.Scatter(
        x=continent['gdpPercap'],
        y=continent['lifeExp'],
        name=continent_name,
        text=df_2007['continent'],
        hovertemplate=
        "<b>%{text}</b><br><br>" +
        "GDP per Capita: %{y:$,.0f}<br>" +
        "Life Expectation: %{x:.0%}<br>" +
        "Population: %{marker.size:,}" +
        "<extra></extra>",
        marker_size=continent['size'],
        ))

fig.update_traces(
    mode='markers',
    marker={'sizemode':'area',
            'sizeref':10})

fig.update_layout(
    xaxis={
        'title':'GDP per capita',
        'type':'log'},
    yaxis={'title':'Life Expectancy (years)'})

fig.show()
```

### Adding other data to the hover with customdata and a hovertemplate

`go` traces have a `customdata` argument in which you can add an array, which outer dimensions should have the same dimensions as the plotted data. You can then use `customdata` inside a `hovertemplate` to display the value of customdata.

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
np.random.seed(0)
z1, z2, z3 = np.random.random((3, 7, 7))
customdata = np.dstack((z2, z3))
fig = make_subplots(1, 2, subplot_titles=['z1', 'z2'])
fig.add_trace(go.Heatmap(
    z=z1,
    customdata=np.dstack((z2, z3)),
    hovertemplate='<b>z1:%{z:.3f}</b><br>z2:%{customdata[0]:.3f} <br>z3: %{customdata[1]:.3f} ',
    coloraxis="coloraxis1", name=''),
    1, 1)
fig.add_trace(go.Heatmap(
    z=z2,
    customdata=np.dstack((z1, z3)),
    hovertemplate='z1:%{customdata[0]:.3f} <br><b>z2:%{z:.3f}</b><br>z3: %{customdata[1]:.3f} ',
    coloraxis="coloraxis1", name=''),
    1, 2)
fig.update_layout(title_text='Hover to see the value of z1, z2 and z3 together')
fig.show()
```

### Setting the Hover Template in Mapbox Maps

```python
import plotly.graph_objects as go

token = open(".mapbox_token").read() # you need your own token

fig = go.Figure(go.Scattermapbox(
    name = "",
    mode = "markers+text+lines",
    lon = [-75, -80, -50],
    lat = [45, 20, -20],
    marker = {'size': 20, 'symbol': ["bus", "harbor", "airport"]},
    hovertemplate =
    "<b>%{marker.symbol} </b><br><br>" +
    "longitude: %{lon}<br>" +
    "latitude: %{lat}<br>" ))

fig.update_layout(
    mapbox = {
        'accesstoken': token,
        'style': "outdoors", 'zoom': 1},
    showlegend = False)

fig.show()
```

### Controlling Hover Text with `graph_objects` and `hoverinfo`

Prior to the addition of `hovertemplate`, hover text was controlled via the now-deprecated `hoverinfo` attribute.

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[2, 1, 6, 4, 4],
    hovertext=["Text A", "Text B", "Text C", "Text D", "Text E"],
    hoverinfo="text",
    marker=dict(
        color="green"
    ),
    showlegend=False
))

fig.show()
```

### Spike lines

Plotly supports "spike lines" which link a point to the axis on hover, and can be configured per axis.

```python
import plotly.express as px

df = px.data.gapminder().query("continent=='Oceania'")

fig = px.line(df, x="year", y="lifeExp", color="country", title="Spike lines active")
fig.update_traces(mode="markers+lines")

fig.update_xaxes(showspikes=True)
fig.update_yaxes(showspikes=True)

fig.show()
```

Spike lines can be styled per axis as well, and the cursor distance setting can be controlled via `layout.spikedistance`.

```python
import plotly.express as px

df = px.data.gapminder().query("continent=='Oceania'")

fig = px.line(df, x="year", y="lifeExp", color="country", title="Styled Spike Lines")
fig.update_traces(mode="markers+lines")

fig.update_xaxes(showspikes=True, spikecolor="green", spikesnap="cursor", spikemode="across")
fig.update_yaxes(showspikes=True, spikecolor="orange", spikethickness=2)
fig.update_layout(spikedistance=1000, hoverdistance=100)

fig.show()
```

#### Reference

See https://plotly.com/python/reference/ for more information and chart attribute options!
