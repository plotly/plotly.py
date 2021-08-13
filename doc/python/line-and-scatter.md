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
    description: How to make scatter plots in Python with Plotly.
    display_as: basic
    language: python
    layout: base
    name: Scatter Plots
    order: 1
    page_type: example_index
    permalink: python/line-and-scatter/
    redirect_from: python/line-and-scatter-plots-tutorial/
    thumbnail: thumbnail/line-and-scatter.jpg
---

## Scatter plots with Plotly Express

[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/).

With `px.scatter`, each data point is represented as a marker point, whose location is given by the `x` and `y` columns.

```python
# x and y given as array_like objects
import plotly.express as px
fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
fig.show()
```

```python
# x and y given as DataFrame columns
import plotly.express as px
df = px.data.iris() # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length")
fig.show()
```

#### Setting size and color with column names

Scatter plots with variable-sized circular markers are often known as [bubble charts](https://plotly.com/python/bubble-charts/). Note that `color` and `size` data are added to hover information. You can add other columns to hover data with the `hover_data` argument of `px.scatter`.

```python
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
fig.show()
```

Color can be [continuous](https://plotly.com/python/colorscales/) as follows, or [discrete/categorical](https://plotly.com/python/discrete-color/) as above.

```python
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color='petal_length')
fig.show()
```

The `symbol` argument can be mapped to a column as well. A [wide variety of symbols](https://plotly.com/python/marker-style/) are available.

```python
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", symbol="species")
fig.show()
```

## Scatter plots in Dash

[Dash](https://plotly.com/dash/) is the best way to build analytical apps in Python using Plotly figures. To run the app below, run `pip install dash`, click "Download" to get the code and run `python app.py`.

Get started  with [the official Dash docs](https://dash.plotly.com/installation) and **learn how to effortlessly [style](https://plotly.com/dash/design-kit/) & [deploy](https://plotly.com/dash/app-manager/) apps like this with <a class="plotly-red" href="https://plotly.com/dash/">Dash Enterprise</a>.**


```python hide_code=true
from IPython.display import IFrame
snippet_url = 'https://dash-gallery.plotly.host/python-docs-dash-snippets/'
IFrame(snippet_url + 'line-and-scatter', width='100%', height=630)
```

### Scatter plots and Categorical Axes

Scatters plots can be made on using any type of cartesian axis, including [linear](https://plotly.com/python/axes/), [logarithmic](https://plotly.com/python/log-plot/), [categorical](https://plotly.com/python/categorical-axes/) or [date](https://plotly.com/python/time-series/) axes.

Scatter plots where one axis is categorical are often known as [dot plots](https://plotly.com/python/dot-plots/).

```python
import plotly.express as px
df = px.data.medals_long()

fig = px.scatter(df, y="nation", x="count", color="medal", symbol="medal")
fig.update_traces(marker_size=10)
fig.show()
```

### Error Bars

Scatter plots support [error bars](https://plotly.com/python/error-bars/).

```python
import plotly.express as px
df = px.data.iris()
df["e"] = df["sepal_width"]/100
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 error_x="e", error_y="e")
fig.show()
```

### Marginal Distribution Plots

Scatter plots support [marginal distribution plots](https://plotly.com/python/marginal-plots/)

```python
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_length", y="sepal_width", marginal_x="histogram", marginal_y="rug")
fig.show()
```

### Facetting

Scatter plots support [faceting](https://plotly.com/python/facet-plots/).

```python
import plotly.express as px
df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", color="smoker", facet_col="sex", facet_row="time")
fig.show()
```

### Linear Regression and Other Trendlines

Scatter plots support [linear and non-linear trendlines](https://plotly.com/python/linear-fits/).

```python
import plotly.express as px

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", trendline="ols")
fig.show()
```

## Line plots with Plotly Express

```python
import plotly.express as px
import numpy as np

t = np.linspace(0, 2*np.pi, 100)

fig = px.line(x=t, y=np.cos(t), labels={'x':'t', 'y':'cos(t)'})
fig.show()
```

```python
import plotly.express as px
df = px.data.gapminder().query("continent == 'Oceania'")
fig = px.line(df, x='year', y='lifeExp', color='country')
fig.show()
```

The `markers` argument can be set to `True` to show markers on lines.

```python
import plotly.express as px
df = px.data.gapminder().query("continent == 'Oceania'")
fig = px.line(df, x='year', y='lifeExp', color='country', markers=True)
fig.show()
```

The `symbol` argument can be used to map a data field to the marker symbol. A [wide variety of symbols](https://plotly.com/python/marker-style/) are available.

```python
import plotly.express as px
df = px.data.gapminder().query("continent == 'Oceania'")
fig = px.line(df, x='year', y='lifeExp', color='country', symbol="country")
fig.show()
```

### Line plots on Date axes

Line plots can be made on using any type of cartesian axis, including [linear](https://plotly.com/python/axes/), [logarithmic](https://plotly.com/python/log-plot/), [categorical](https://plotly.com/python/categorical-axes/) or date axes. Line plots on date axes are often called [time-series charts](https://plotly.com/python/time-series/).

Plotly auto-sets the axis type to a date format when the corresponding data are either ISO-formatted date strings or if they're a [date pandas column](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html) or [datetime NumPy array](https://docs.scipy.org/doc/numpy/reference/arrays.datetime.html).

```python
import plotly.express as px

df = px.data.stocks()
fig = px.line(df, x='date', y="GOOG")
fig.show()
```

### Data Order in Scatter and Line Charts

Plotly line charts are implemented as [connected scatterplots](https://www.data-to-viz.com/graph/connectedscatter.html) (see below), meaning that the points are plotted and connected with lines **in the order they are provided, with no automatic reordering**. 

This makes it possible to make charts like the one below, but also means that it may be required to explicitly sort data before passing it to Plotly to avoid lines moving "backwards" across the chart.

```python
import plotly.express as px
import pandas as pd

df = pd.DataFrame(dict(
    x = [1, 3, 2, 4],
    y = [1, 2, 3, 4]
))
fig = px.line(df, x="x", y="y", title="Unsorted Input") 
fig.show()

df = df.sort_values(by="x")
fig = px.line(df, x="x", y="y", title="Sorted Input") 
fig.show()
```

### Connected Scatterplots

In a connected scatterplot, two continuous variables are plotted against each other, with a line connecting them in some meaningful order, usually a time variable. In the plot below, we show the "trajectory" of a pair of countries through a space defined by GDP per Capita and Life Expectancy. Botswana's life expectancy 

```python
import plotly.express as px

df = px.data.gapminder().query("country in ['Canada', 'Botswana']")

fig = px.line(df, x="lifeExp", y="gdpPercap", color="country", text="year")
fig.update_traces(textposition="bottom right")
fig.show()
```

## Scatter and line plots with go.Scatter

If Plotly Express does not provide a good starting point, it is possible to use [the more generic `go.Scatter` class from `plotly.graph_objects`](/python/graph-objects/). Whereas `plotly.express` has two functions `scatter` and `line`, `go.Scatter` can be used both for plotting points (makers) or lines, depending on the value of `mode`. The different options of `go.Scatter` are documented in its [reference page](https://plotly.com/python/reference/scatter/).

#### Simple Scatter Plot

```python
import plotly.graph_objects as go
import numpy as np

N = 1000
t = np.linspace(0, 10, 100)
y = np.sin(t)

fig = go.Figure(data=go.Scatter(x=t, y=y, mode='markers'))

fig.show()
```

#### Line and Scatter Plots

Use `mode` argument to choose between markers, lines, or a combination of both. For more options about line plots, see also the [line charts notebook](https://plotly.com/python/line-charts/) and the [filled area plots notebook](https://plotly.com/python/filled-area-plots/).

```python
import plotly.graph_objects as go

# Create random data with numpy
import numpy as np
np.random.seed(1)

N = 100
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N) + 5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) - 5

fig = go.Figure()

# Add traces
fig.add_trace(go.Scatter(x=random_x, y=random_y0,
                    mode='markers',
                    name='markers'))
fig.add_trace(go.Scatter(x=random_x, y=random_y1,
                    mode='lines+markers',
                    name='lines+markers'))
fig.add_trace(go.Scatter(x=random_x, y=random_y2,
                    mode='lines',
                    name='lines'))

fig.show()
```

#### Bubble Scatter Plots

In [bubble charts](https://en.wikipedia.org/wiki/Bubble_chart), a third dimension of the data is shown through the size of markers. For more examples, see the [bubble chart notebook](https://plotly.com/python/bubble-charts/)

```python
import plotly.graph_objects as go

fig = go.Figure(data=go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 11, 12, 13],
    mode='markers',
    marker=dict(size=[40, 60, 80, 100],
                color=[0, 1, 2, 3])
))

fig.show()
```

#### Style Scatter Plots

```python
import plotly.graph_objects as go
import numpy as np


t = np.linspace(0, 10, 100)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=t, y=np.sin(t),
    name='sin',
    mode='markers',
    marker_color='rgba(152, 0, 0, .8)'
))

fig.add_trace(go.Scatter(
    x=t, y=np.cos(t),
    name='cos',
    marker_color='rgba(255, 182, 193, .9)'
))

# Set options common to all traces with fig.update_traces
fig.update_traces(mode='markers', marker_line_width=2, marker_size=10)
fig.update_layout(title='Styled Scatter',
                  yaxis_zeroline=False, xaxis_zeroline=False)


fig.show()
```

#### Data Labels on Hover

```python
import plotly.graph_objects as go
import pandas as pd

data= pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv")

fig = go.Figure(data=go.Scatter(x=data['Postal'],
                                y=data['Population'],
                                mode='markers',
                                marker_color=data['Population'],
                                text=data['State'])) # hover text goes here

fig.update_layout(title='Population of USA States')
fig.show()

```

#### Scatter with a Color Dimension

```python
import plotly.graph_objects as go
import numpy as np

fig = go.Figure(data=go.Scatter(
    y = np.random.randn(500),
    mode='markers',
    marker=dict(
        size=16,
        color=np.random.randn(500), #set color equal to a variable
        colorscale='Viridis', # one of plotly colorscales
        showscale=True
    )
))

fig.show()
```

#### Large Data Sets

Now in Plotly you can implement WebGL with `Scattergl()` in place of `Scatter()` <br>
for increased speed, improved interactivity, and the ability to plot even more data!

```python
import plotly.graph_objects as go
import numpy as np

N = 100000
fig = go.Figure(data=go.Scattergl(
    x = np.random.randn(N),
    y = np.random.randn(N),
    mode='markers',
    marker=dict(
        color=np.random.randn(N),
        colorscale='Viridis',
        line_width=1
    )
))

fig.show()
```

```python
import plotly.graph_objects as go
import numpy as np

N = 100000
r = np.random.uniform(0, 1, N)
theta = np.random.uniform(0, 2*np.pi, N)

fig = go.Figure(data=go.Scattergl(
    x = r * np.cos(theta), # non-uniform distribution
    y = r * np.sin(theta), # zoom to see more points at the center
    mode='markers',
    marker=dict(
        color=np.random.randn(N),
        colorscale='Viridis',
        line_width=1
    )
))

fig.show()
```

### Reference

See [function reference for `px.scatter()`](https://plotly.com/python-api-reference/generated/plotly.express.scatter) or https://plotly.com/python/reference/scatter/ or https://plotly.com/python/reference/scattergl/ for more information and chart attribute options!
