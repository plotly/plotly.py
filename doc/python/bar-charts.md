---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.1
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
    version: 3.10.11
  plotly:
    description: How to make Bar Charts in Python with Plotly.
    display_as: basic
    language: python
    layout: base
    name: Bar Charts
    order: 3
    page_type: example_index
    permalink: python/bar-charts/
    thumbnail: thumbnail/bar.jpg
---

### Bar chart with Plotly Express

[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/).

With `px.bar`, **each row of the DataFrame is represented as a rectangular mark**. To aggregate multiple data points into the same rectangular mark, please refer to the [histogram documentation](/python/histograms).

In the example below, there is only a single row of data per year, so a single bar is displayed per year.

```python
import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, x='year', y='pop')
fig.show()
```


#### Bar charts with Long Format Data

Long-form data has one row per observation, and one column per variable. This is suitable for storing and displaying multivariate data i.e. with dimension greater than 2. This format is sometimes called "tidy".

To learn more about how to provide a specific form of column-oriented data to 2D-Cartesian Plotly Express functions such as `px.bar`, see the [Plotly Express Wide-Form Support in Python
documentation](https://plotly.com/python/wide-form/).

For  detailed column-input-format documentation, see the [Plotly Express Arguments documentation](https://plotly.com/python/px-arguments/).

```python
import plotly.express as px

long_df = px.data.medals_long()

fig = px.bar(long_df, x="nation", y="count", color="medal", title="Long-Form Input")
fig.show()
```

```python
long_df
```

#### Bar charts with Wide Format Data
Wide-form data has one row per value of one of the first variable, and one column per value of the second variable. This is suitable for storing and displaying 2-dimensional data.

```python
import plotly.express as px

wide_df = px.data.medals_wide()

fig = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input")
fig.show()
```

```python
wide_df
```

### Bar charts in Dash

[Dash](https://plotly.com/dash/) is the best way to build analytical apps in Python using Plotly figures. To run the app below, run `pip install dash`, click "Download" to get the code and run `python app.py`.

Get started  with [the official Dash docs](https://dash.plotly.com/installation) and **learn how to effortlessly [style](https://plotly.com/dash/design-kit/) & [deploy](https://plotly.com/dash/app-manager/) apps like this with <a class="plotly-red" href="https://plotly.com/dash/">Dash Enterprise</a>.**


```python hide_code=true
from IPython.display import IFrame
snippet_url = 'https://python-docs-dash-snippets.herokuapp.com/python-docs-dash-snippets/'
IFrame(snippet_url + 'bar-charts', width='100%', height=1200)
```

<div style="font-size: 0.9em;"><div style="width: calc(100% - 30px); box-shadow: none; border: thin solid rgb(229, 229, 229);"><div style="padding: 5px;"><div><p><strong>Sign up for Dash Club</strong> → Free cheat sheets plus updates from Chris Parmer and Adam Schroeder delivered to your inbox every two months. Includes tips and tricks, community apps, and deep dives into the Dash architecture.
<u><a href="https://go.plotly.com/dash-club?utm_source=Dash+Club+2022&utm_medium=graphing_libraries&utm_content=inline">Join now</a></u>.</p></div></div></div></div>


### Colored Bars

The bar plot can be customized using keyword arguments, for example to use [continuous color](https://plotly.com/python/colorscales/), as below, or [discrete color](/python/discrete-color/), as above.

```python
import plotly.express as px

df = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(df, x='year', y='pop',
             hover_data=['lifeExp', 'gdpPercap'], color='lifeExp',
             labels={'pop':'population of Canada'}, height=400)
fig.show()
```

```python
import plotly.express as px

df = px.data.gapminder().query("continent == 'Oceania'")
fig = px.bar(df, x='year', y='pop',
             hover_data=['lifeExp', 'gdpPercap'], color='country',
             labels={'pop':'population of Canada'}, height=400)
fig.show()
```

### Stacked vs Grouped Bars

When several rows share the same value of `x` (here Female or Male), the rectangles are stacked on top of one another by default.

```python
import plotly.express as px
df = px.data.tips()
fig = px.bar(df, x="sex", y="total_bill", color='time')
fig.show()
```

The default stacked bar chart behavior can be changed to grouped (also known as clustered) using the `barmode` argument:

```python
import plotly.express as px
df = px.data.tips()
fig = px.bar(df, x="sex", y="total_bill",
             color='smoker', barmode='group',
             height=400)
fig.show()
```

### Aggregating into Single Colored Bars

As noted above `px.bar()` will result in **one rectangle drawn per row of input**. This can sometimes result in a striped look as in the examples above. To combine these rectangles into one per color per position, you can use `px.histogram()`, which has [its own detailed documentation page](/python/histogram).

> `px.bar` and `px.histogram` are designed  to be nearly interchangeable in their call signatures, so as to be able to switch between aggregated and disaggregated bar representations.

```python
import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, x="sex", y="total_bill",
             color='smoker', barmode='group',
             height=400)
fig.show()
```

`px.histogram()` will aggregate `y` values by summing them by default, but the `histfunc` argument can be used to set this to `avg` to create what is sometimes called a "barplot" which summarizes the central tendency of a dataset, rather than visually representing the totality of the dataset.

> Warning: when using `histfunc`s other than `"sum"` or `"count"` it can be very misleading to use a `barmode` other than `"group"`, as stacked bars in effect represent the sum of the bar heights, and summing averages is rarely a reasonable thing to visualize.

```python
import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, x="sex", y="total_bill",
             color='smoker', barmode='group',
             histfunc='avg',
             height=400)
fig.show()
```

### Bar Charts with Text

*New in v5.5*

You can add text to bars using the `text_auto` argument. Setting it to `True` will display the values on the bars, and setting it to a `d3-format` formatting string will control the output format.

```python
import plotly.express as px
df = px.data.medals_long()

fig = px.bar(df, x="medal", y="count", color="nation", text_auto=True)
fig.show()
```

The `text` argument can be used to display arbitrary text on the bars:

```python
import plotly.express as px
df = px.data.medals_long()

fig = px.bar(df, x="medal", y="count", color="nation", text="nation")
fig.show()
```

By default, Plotly will scale and rotate text labels to maximize the number of visible labels, which can result in a variety of text angles and sizes and positions in the same figure. The `textfont`, `textposition` and `textangle` trace attributes can be used to control these.

Here is an example of the default behavior:

```python
import plotly.express as px

df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
fig = px.bar(df, y='pop', x='country', text_auto='.2s',
            title="Default: various text sizes, positions and angles")
fig.show()
```

Here is the same data with less variation in text formatting. Note that `textfont_size` will set the *maximum* size. The `layout.uniformtext` attribute can be used to guarantee that all text labels are the same size. See the [documentation on text and annotations](/python/text-and-annotations/) for details.

The `cliponaxis` attribute is set to `False` in the example below to ensure that the outside text on the tallest bar is allowed to render outside of the plotting area.

```python
import plotly.express as px

df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
fig = px.bar(df, y='pop', x='country', text_auto='.2s',
            title="Controlled text sizes, positions and angles")
fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
fig.show()
```

### Pattern Fills

*New in v5.0*


Bar charts afford the use of [patterns (also known as hatching or texture)](/python/pattern-hatching-texture/) in addition to color:

```python
import plotly.express as px
df = px.data.medals_long()

fig = px.bar(df, x="medal", y="count", color="nation",
             pattern_shape="nation", pattern_shape_sequence=[".", "x", "+"])
fig.show()
```

### Facetted subplots

Use the keyword arguments `facet_row` (resp. `facet_col`) to create facetted subplots, where different rows (resp. columns) correspond to different values of the dataframe column specified in `facet_row`.

```python
import plotly.express as px
df = px.data.tips()
fig = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group",
             facet_row="time", facet_col="day",
             category_orders={"day": ["Thur", "Fri", "Sat", "Sun"],
                              "time": ["Lunch", "Dinner"]})
fig.show()
```

#### Basic Bar Charts with plotly.graph_objects

If Plotly Express does not provide a good starting point, it is also possible to use [the more generic `go.Bar` class from `plotly.graph_objects`](/python/graph-objects/).

```python
import plotly.graph_objects as go
animals=['giraffes', 'orangutans', 'monkeys']

fig = go.Figure([go.Bar(x=animals, y=[20, 14, 23])])
fig.show()
```

#### Grouped Bar Chart

Customize the figure using `fig.update`.

```python
import plotly.graph_objects as go
animals=['giraffes', 'orangutans', 'monkeys']

fig = go.Figure(data=[
    go.Bar(name='SF Zoo', x=animals, y=[20, 14, 23]),
    go.Bar(name='LA Zoo', x=animals, y=[12, 18, 29])
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.show()
```

### Stacked Bar Chart

```python
import plotly.graph_objects as go
animals=['giraffes', 'orangutans', 'monkeys']

fig = go.Figure(data=[
    go.Bar(name='SF Zoo', x=animals, y=[20, 14, 23]),
    go.Bar(name='LA Zoo', x=animals, y=[12, 18, 29])
])
# Change the bar mode
fig.update_layout(barmode='stack')
fig.show()
```

### Stacked Bar Chart From Aggregating a DataFrame

Stacked bar charts are a powerful way to present results summarizing categories generated using the Pandas aggregate commands. `pandas.DataFrame.agg` produces a wide data set format incompatible with `px.bar`. Transposing and updating the indexes to achieve `px.bar` compatibility is a somewhat involved option. Here is one straightforward alternative, which presents the aggregated data as a stacked bar using plotly.graph_objects.

```python
from plotly import graph_objects as go
import pandas as pd

# Get one year of gapminder data
url = 'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv'
df = pd.read_csv(url)
df = df[df['year']==2007]
df["gdp"]=df["pop"]*df['gdpPercap']


# Build the summary of interest
df_summarized = df.groupby("continent", observed=True).agg("sum").reset_index()

df_summarized["percent of world population"]=100*df_summarized["pop"]/df_summarized["pop"].sum()
df_summarized["percent of world GDP"]=100*df_summarized["gdp"]/df_summarized["gdp"].sum()


df = df_summarized[["continent",
"percent of world population",
"percent of world GDP",
]]

# We now have a wide data frame, but it's in the opposite orientation from the one that px is designed to deal with.
# Transposing it and rebuilding the indexes is an option, but iterating through the DF using graph objects is more succinct.

fig=go.Figure()
for category in df_summarized["continent"].values:
    fig.add_trace(go.Bar(
            x=df.columns[1:],
            # We need to get a pandas series that contains just the values to graph;
            # We do so by selecting the right row, selecting the right columns
            # and then transposing and using iloc to convert to a series
            # Here, we assume that the bar element category variable is in column 0
            y=list(df.loc[df["continent"]==category][list(df.columns[1:])].transpose().iloc[:,0]),
            name=str(category)


        )
)
fig.update_layout(barmode="stack")

fig.show()
```


### Bar Chart with Hover Text

```python
import plotly.graph_objects as go

x = ['Product A', 'Product B', 'Product C']
y = [20, 14, 23]

# Use the hovertext kw argument for hover text
fig = go.Figure(data=[go.Bar(x=x, y=y,
            hovertext=['27% market share', '24% market share', '19% market share'])])
# Customize aspect
fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)
fig.update_layout(title_text='January 2013 Sales Report')
fig.show()
```

### Bar Chart with Direct Labels

```python
import plotly.graph_objects as go

x = ['Product A', 'Product B', 'Product C']
y = [20, 14, 23]

# Use textposition='auto' for direct text
fig = go.Figure(data=[go.Bar(
            x=x, y=y,
            text=y,
            textposition='auto',
        )])

fig.show()
```

### Controlling text fontsize with uniformtext

If you want all the text labels to have the same size, you can use the `uniformtext` layout parameter. The `minsize` attribute sets the font size, and the `mode` attribute sets what happens for labels which cannot fit with the desired fontsize: either `hide` them or `show` them with overflow. In the example below we also force the text to be outside of bars with `textposition`.

```python
import plotly.express as px

df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
fig = px.bar(df, y='pop', x='country', text='pop')
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.show()
```

### Rotated Bar Chart Labels

```python
import plotly.graph_objects as go

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

fig = go.Figure()
fig.add_trace(go.Bar(
    x=months,
    y=[20, 14, 25, 16, 18, 22, 19, 15, 12, 16, 14, 17],
    name='Primary Product',
    marker_color='indianred'
))
fig.add_trace(go.Bar(
    x=months,
    y=[19, 14, 22, 14, 16, 19, 15, 14, 10, 12, 12, 16],
    name='Secondary Product',
    marker_color='lightsalmon'
))

# Here we modify the tickangle of the xaxis, resulting in rotated labels.
fig.update_layout(barmode='group', xaxis_tickangle=-45)
fig.show()
```

### Customizing Individual Bar Colors

```python
import plotly.graph_objects as go

colors = ['lightslategray',] * 5
colors[1] = 'crimson'

fig = go.Figure(data=[go.Bar(
    x=['Feature A', 'Feature B', 'Feature C',
       'Feature D', 'Feature E'],
    y=[20, 14, 23, 25, 22],
    marker_color=colors # marker color can be a single color value or an iterable
)])
fig.update_layout(title_text='Least Used Feature')
```

### Customizing Individual Bar Widths

```python
import plotly.graph_objects as go

fig = go.Figure(data=[go.Bar(
    x=[1, 2, 3, 5.5, 10],
    y=[10, 8, 6, 4, 2],
    width=[0.8, 0.8, 0.8, 3.5, 4] # customize width here
)])

fig.show()
```

Bar charts with custom widths can be used to make mekko charts (also known as marimekko charts, mosaic plots, or variwide charts).

```python
import plotly.graph_objects as go
import numpy as np

labels = ["apples","oranges","pears","bananas"]
widths = np.array([10,20,20,50])

data = {
    "South": [50,80,60,70],
    "North": [50,20,40,30]
}

fig = go.Figure()
for key in data:
    fig.add_trace(go.Bar(
        name=key,
        y=data[key],
        x=np.cumsum(widths)-widths,
        width=widths,
        offset=0,
        customdata=np.transpose([labels, widths*data[key]]),
        texttemplate="%{y} x %{width} =<br>%{customdata[1]}",
        textposition="inside",
        textangle=0,
        textfont_color="white",
        hovertemplate="<br>".join([
            "label: %{customdata[0]}",
            "width: %{width}",
            "height: %{y}",
            "area: %{customdata[1]}",
        ])
    ))

fig.update_xaxes(
    tickvals=np.cumsum(widths)-widths/2,
    ticktext= ["%s<br>%d" % (l, w) for l, w in zip(labels, widths)]
)

fig.update_xaxes(range=[0,100])
fig.update_yaxes(range=[0,100])

fig.update_layout(
    title_text="Marimekko Chart",
    barmode="stack",
    uniformtext=dict(mode="hide", minsize=10),
)
```

### Customizing Individual Bar Base

```python
import plotly.graph_objects as go

years = ['2016','2017','2018']

fig = go.Figure()
fig.add_trace(go.Bar(x=years, y=[500, 600, 700],
                base=[-500,-600,-700],
                marker_color='crimson',
                name='expenses'))
fig.add_trace(go.Bar(x=years, y=[300, 400, 700],
                base=0,
                marker_color='lightslategrey',
                name='revenue'
                ))

fig.show()
```

### Rounded Bars

*New in 5.19*

You can round the corners on all bar traces in a figure by setting `barcornerradius` on the figure's layout. `barcornerradius` can be a number of pixels or a percentage of the bar width (using a string ending in %, for example "20%").

In this example, we set all bars to have a radius of 15 pixels.

```python
import plotly.graph_objects as go
from plotly import data

df = data.medals_wide()

fig = go.Figure(
    data=[
        go.Bar(x=df.nation, y=df.gold, name="Gold"),
        go.Bar(x=df.nation, y=df.silver, name="Silver"),
        go.Bar(x=df.nation, y=df.bronze, name="Bronze"),
    ],
    layout=dict(
        barcornerradius=15,
    ),
)

fig.show()
```

When you don't want all bar traces in a figure to have the same rounded corners, you can instead configure rounded corners on each trace using `marker.cornerradius`. In this example, which uses subplots, the first trace has a corner radius of 30 pixels, the second trace has a bar corner radius of 30% of the bar width, and the third trace has no rounded corners set.

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly import data

df = data.medals_wide()

fig = make_subplots(rows=1, cols=3, shared_yaxes=True)

fig.add_trace(
    go.Bar(x=df.nation, y=df.gold, name="Gold", marker=dict(cornerradius=30)), 1, 1
)
fig.add_trace(
    go.Bar(x=df.nation, y=df.silver, name="Silver", marker=dict(cornerradius="30%")),
    1,
    2,
)

fig.add_trace(
    go.Bar(x=df.nation, y=df.bronze, name="Bronze"),
    1,
    3,
)


fig.show()
```

### Colored and Styled Bar Chart

In this example several parameters of the layout as customized, hence it is convenient to use directly the `go.Layout(...)` constructor instead of calling `fig.update`.

```python
import plotly.graph_objects as go

years = [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
         2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012]

fig = go.Figure()
fig.add_trace(go.Bar(x=years,
                y=[219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                   350, 430, 474, 526, 488, 537, 500, 439],
                name='Rest of world',
                marker_color='rgb(55, 83, 109)'
                ))
fig.add_trace(go.Bar(x=years,
                y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                   299, 340, 403, 549, 499],
                name='China',
                marker_color='rgb(26, 118, 255)'
                ))

fig.update_layout(
    title='US Export of Plastic Scrap',
    xaxis_tickfont_size=14,
    yaxis=dict(
        title=dict(
            text="USD (millions)",
            font=dict(
                size=16
            )
        ),
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
fig.show()
```

### Bar Chart with Relative Barmode

With "relative" barmode, the bars are stacked on top of one another, with negative values
below the axis, positive values above.

```python
import plotly.graph_objects as go
x = [1, 2, 3, 4]

fig = go.Figure()
fig.add_trace(go.Bar(x=x, y=[1, 4, 9, 16]))
fig.add_trace(go.Bar(x=x, y=[6, -8, -4.5, 8]))
fig.add_trace(go.Bar(x=x, y=[-15, -3, 4.5, -8]))
fig.add_trace(go.Bar(x=x, y=[-1, 3, -3, -4]))

fig.update_layout(barmode='relative', title_text='Relative Barmode')
fig.show()
```

### Bar Chart with Sorted or Ordered Categories

Set `categoryorder` to `"category ascending"` or `"category descending"` for the alphanumerical order of the category names or `"total ascending"` or `"total descending"` for numerical order of values. [categoryorder](https://plotly.com/python/reference/layout/xaxis/#layout-xaxis-categoryorder) for more information. Note that sorting the bars by a particular trace isn't possible right now - it's only possible to sort by the total values. Of course, you can always sort your data _before_ plotting it if you need more customization.

This example orders the bar chart alphabetically with `categoryorder: 'category ascending'`

```python
import plotly.graph_objects as go

x=['b', 'a', 'c', 'd']
fig = go.Figure(go.Bar(x=x, y=[2,5,1,9], name='Montreal'))
fig.add_trace(go.Bar(x=x, y=[1, 4, 9, 16], name='Ottawa'))
fig.add_trace(go.Bar(x=x, y=[6, 8, 4.5, 8], name='Toronto'))

fig.update_layout(barmode='stack', xaxis={'categoryorder':'category ascending'})
fig.show()
```

This example shows how to customise sort ordering by defining `categoryorder` to "array" to derive the ordering from the attribute `categoryarray`.

```python
import plotly.graph_objects as go

x=['b', 'a', 'c', 'd']
fig = go.Figure(go.Bar(x=x, y=[2,5,1,9], name='Montreal'))
fig.add_trace(go.Bar(x=x, y=[1, 4, 9, 16], name='Ottawa'))
fig.add_trace(go.Bar(x=x, y=[6, 8, 4.5, 8], name='Toronto'))

fig.update_layout(barmode='stack', xaxis={'categoryorder':'array', 'categoryarray':['d','a','c','b']})
fig.show()
```

This example orders the bar chart by descending value with `categoryorder: 'total descending'`

```python
import plotly.graph_objects as go

x=['b', 'a', 'c', 'd']
fig = go.Figure(go.Bar(x=x, y=[2,5,1,9], name='Montreal'))
fig.add_trace(go.Bar(x=x, y=[1, 4, 9, 16], name='Ottawa'))
fig.add_trace(go.Bar(x=x, y=[6, 8, 4.5, 8], name='Toronto'))

fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
fig.show()
```

### Horizontal Bar Charts

See examples of horizontal bar charts [here](https://plotly.com/python/horizontal-bar-charts/).

### Bar Charts With Multicategory Axis Type

If your traces have arrays for `x` or `y`, then the axis type is automatically inferred to be `multicategory`.

```python
import plotly.graph_objects as go
x = [
    ["BB+", "BB+", "BB+", "BB", "BB", "BB"],
    [16, 17, 18, 16, 17, 18,]
]
fig = go.Figure()
fig.add_bar(x=x,y=[1,2,3,4,5,6])
fig.add_bar(x=x,y=[6,5,4,3,2,1])
fig.update_layout(barmode="relative")
fig.show()
```




### Reference

See [function reference for `px.bar()`](https://plotly.com/python-api-reference/generated/plotly.express.bar) or https://plotly.com/python/reference/bar/ for more information and chart attribute options!
