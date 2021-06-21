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
    description: How to use hover text and formatting in Python with Plotly.
    display_as: file_settings
    language: python
    layout: base
    name: Hover Text and Formatting
    order: 23
    permalink: python/hover-text-and-formatting/
    thumbnail: thumbnail/hover-text.png
---

### Hover Labels

One of the most deceptively-powerful features of interactive visualization using Plotly is the ability for the user to reveal more information about a data point by moving their mouse cursor over the point and having a hover label appear.

There are three hover modes available in Plotly. The default setting is `layout.hovermode='closest'`, wherein a single hover label appears for the point directly underneath the cursor.

#### Hovermode `closest` (default mode)

```python
import plotly.express as px

df = px.data.gapminder().query("continent=='Oceania'")

fig = px.line(df, x="year", y="lifeExp", color="country", title="layout.hovermode='closest' (the default)")
fig.update_traces(mode="markers+lines")

fig.show()
```

#### Hovermode `x` or `y`

If `layout.hovermode='x'` (or `'y'`), a single hover label appears per trace, for points at the same `x` (or `y`) value as the cursor. If multiple points in a given trace exist at the same coordinate, only one will get a hover label. In the line plot below we have forced markers to appear, to make it clearer what can be hovered over, and we have disabled the built-in Plotly Express `hovertemplate` by setting it to `None`, resulting in a more compact hover label per point:

```python
import plotly.express as px

df = px.data.gapminder().query("continent=='Oceania'")

fig = px.line(df, x="year", y="lifeExp", color="country", title="layout.hovermode='x'")
fig.update_traces(mode="markers+lines", hovertemplate=None)
fig.update_layout(hovermode="x")

fig.show()
```

#### Unified hovermode

If `layout.hovermode='x unified'` (or `'y unified'`), a single hover label appear, describing one point per trace, for points at the same `x` (or `y`) value as the cursor.  If multiple points in a given trace exist at the same coordinate, only one will get an entry in the hover label. In the line plot below we have forced markers to appear, to make it clearer what can be hovered over, and we have disabled the built-in Plotly Express `hovertemplate` by setting it to `None`, resulting in a more compact entry per point in the hover label:

```python
import plotly.express as px

df = px.data.gapminder().query("continent=='Oceania'")

fig = px.line(df, x="year", y="lifeExp", color="country", title="layout.hovermode='x unified'")
fig.update_traces(mode="markers+lines", hovertemplate=None)
fig.update_layout(hovermode="x unified")

fig.show()
```

#### Control hovermode with Dash

[Dash](https://plotly.com/dash/) is the best way to build analytical apps in Python using Plotly figures. To run the app below, run `pip install dash`, click "Download" to get the code and run `python app.py`.

Get started  with [the official Dash docs](https://dash.plotly.com/installation) and **learn how to effortlessly [style](https://plotly.com/dash/design-kit/) & [deploy](https://plotly.com/dash/app-manager/) apps like this with <a class="plotly-red" href="https://plotly.com/dash/">Dash Enterprise</a>.**

Change the hovermode below and try hovering over the points:

```python hide_code=true
from IPython.display import IFrame
snippet_url = 'https://dash-gallery.plotly.host/python-docs-dash-snippets/'
IFrame(snippet_url + 'hover-text-and-formatting', width='100%', height=630)
```

#### Selecting a hovermode in a figure created with `plotly.graph_objects`

The hovermode is a property of the figure layout, so you can select a hovermode no matter how you created the figure, either with `plotly.express` or with `plotly.graph_objects`. Below is an example with a figure created with `plotly.graph_objects`. If you're not familiar with the structure of plotly figures, you can read [the tutorial on creating and updating plotly figures](/python/creating-and-updating-figures/).

```python
import plotly.graph_objects as go
import numpy as np
t = np.linspace(0, 2 * np.pi, 100)
fig = go.Figure()
fig.add_trace(go.Scatter(x=t, y=np.sin(t), name='sin(t)'))
fig.add_trace(go.Scatter(x=t, y=np.cos(t), name='cost(t)'))
fig.update_layout(hovermode='x unified')
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

Plotly Express functions automatically add all the data being plotted (x, y, color etc) to the hover label. Many Plotly Express functions also support configurable hover text. The `hover_data` argument accepts a list of column names to be added to the hover tooltip, or a dictionary for advanced formatting (see the next section). The `hover_name` property controls which column is displayed in bold as the tooltip title.

Here is an example that creates a scatter plot using Plotly Express with custom hover data and a custom hover name.

```python
import plotly.express as px

df_2007 = px.data.gapminder().query("year==2007")

fig = px.scatter(df_2007, x="gdpPercap", y="lifeExp", log_x=True,
                 hover_name="country", hover_data=["continent", "pop"])

fig.show()
```

### Disabling or customizing hover of columns in plotly express

`hover_data` can also be a dictionary. Its keys are existing columns of the `dataframe` argument, or new labels. For an existing column, the values can be
* `False` to remove the column from the hover data (for example, if one wishes to remove the column of the `x` argument)
* `True` to add a different column, with default formatting
* a formatting string starting with `:` for numbers [d3-format's syntax](https://github.com/d3/d3-3.x-api-reference/blob/master/Formatting.md#d3_forma), and `|` for dates in [d3-time-format's syntax](https://github.com/d3/d3-time-format), for example `:.3f`, `|%a`.

It is also possible to pass new data as values of the `hover_data` dict, either as list-like data, or inside a tuple, which first element is one of the possible values described above for existing columns, and the second element correspond to the list-like data, for example `(True, [1, 2, 3])` or `(':.1f', [1.54, 2.345])`.

These different cases are illustrated in the following example.

```python
import plotly.express as px
import numpy as np
df = px.data.iris()
fig = px.scatter(df, x='petal_length', y='sepal_length', facet_col='species', color='species',
                 hover_data={'species':False, # remove species from hover data
                             'sepal_length':':.2f', # customize hover for column of y attribute
                             'petal_width':True, # add other column, default formatting
                             'sepal_width':':.2f', # add other column, customized formatting
                             # data not in dataframe, default formatting
                             'suppl_1': np.random.random(len(df)),
                             # data not in dataframe, customized formatting
                             'suppl_2': (':.3f', np.random.random(len(df)))
                            })
fig.update_layout(height=300)
fig.show()
```

### Customizing hover text with a hovertemplate

To customize the tooltip on your graph you can use the [hovertemplate](https://plotly.com/python/reference/pie/#pie-hovertemplate) attribute of `graph_objects` tracces, which is a template string used for rendering the information that appear on hoverbox.
This template string can include `variables` in %{variable} format, `numbers` in [d3-format's syntax](https://github.com/d3/d3-3.x-api-reference/blob/master/Formatting.md#d3_format), and `date` in [d3-time-format's syntax](https://github.com/d3/d3-time-format). In the example below, the empty `<extra></extra>` tag removes the part of the hover where the trace name is usually displayed in a contrasting color. The `<extra>` tag can be used to display other parts of the hovertemplate, it is not reserved for the trace name.

Note that a hovertemplate customizes the tooltip text, while a [texttemplate](https://plotly.com/python/reference/pie/#pie-texttemplate) customizes the text that appears on your chart. <br>

Set the horizontal alignment of the text within tooltip with [hoverlabel.align](https://plotly.com/python/reference/layout/#layout-hoverlabel-align).

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

### Modifying the hovertemplate of a plotly express figure

`plotly.express` automatically sets the hovertemplate but you can modify it using the `update_traces` method of the generated figure. It helps to print the hovertemplate generated by `plotly.express` in order to be able to modify it. One can also revert to the default hover information of traces by setting the hovertemplate to `None`.

```python
import plotly.express as px

df_2007 = px.data.gapminder().query("year==2007")

fig = px.scatter(df_2007, x="gdpPercap", y="lifeExp", log_x=True, color='continent'
                )
print("plotly express hovertemplate:", fig.data[0].hovertemplate)
fig.update_traces(hovertemplate='GDP: %{x} <br>Life Expectancy: %{y}') #
fig.update_traces(hovertemplate=None, selector={'name':'Europe'}) # revert to default hover
print("user_defined hovertemplate:", fig.data[0].hovertemplate)
fig.show()
```

### Hover Templates with Mixtures of Period data

*New in v5.0*

When [displaying periodic data](https://plotly.com/python/time-series/#displaying-period-data) with mixed-sized periods (i.e. quarterly and monthly) in conjunction with `x` or `x unified` hovermodes and using `hovertemplate`, the `xhoverformat` attribute can be used to control how each period's X value is displayed, and the special `%{xother}` hover-template directive can be used to control how the X value is displayed for points that do not share the exact X coordinate with the point that is being hovered on. `%{xother}` will return an empty string when the X value is the one being hovered on, otherwise it will return `(%{x})`. The special `%{_xother}`, `%{xother_}` and `%{_xother_}` variations will display with spaces before, after or around the parentheses, respectively.

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Bar(
    x=["2020-01-01", "2020-04-01", "2020-07-01"],
    y=[1000, 1500, 1700],
    xperiod="M3",
    xperiodalignment="middle",
    xhoverformat="Q%q",
    hovertemplate="%{y}%{_xother}"
))

fig.add_trace(go.Scatter(
    x=["2020-01-01", "2020-02-01", "2020-03-01",
      "2020-04-01", "2020-05-01", "2020-06-01",
      "2020-07-01", "2020-08-01", "2020-09-01"],
    y=[1100,1050,1200,1300,1400,1700,1500,1400,1600],
    xperiod="M1",
    xperiodalignment="middle",
    hovertemplate="%{y}%{_xother}"
))

fig.update_layout(hovermode="x unified")
fig.show()
```

### Advanced Hover Template

The following example shows how to format a hover template.

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
        "GDP per Capita: %{x:$,.0f}<br>" +
        "Life Expectation: %{y:.0%}<br>" +
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
