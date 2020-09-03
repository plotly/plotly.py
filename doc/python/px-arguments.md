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
    description: Input data arguments accepted by Plotly Express functions
    display_as: file_settings
    language: python
    layout: base
    name: Plotly Express Arguments
    order: 19
    page_type: u-guide
    permalink: python/px-arguments/
    thumbnail: thumbnail/plotly-express.png
---

### Plotly Express works with Column-oriented, Matrix or Geographic Data

[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/).

Plotly Express provides functions to visualize a variety of types of data. Most functions such as `px.bar` or `px.scatter` expect to operate on column-oriented data of the type you might store in a Pandas `DataFrame` (in either "long" or "wide" format, see below). [`px.imshow` operates on matrix-like data](/python/imshow/) you might store in a `numpy` or `xarray` array and functions like [`px.choropleth` and `px.choropleth_mapbox` can operate on geographic data](/python/maps/) of the kind you might store in a GeoPandas `GeoDataFrame`. This page details how to provide column-oriented data to most Plotly Express functions.



### Plotly Express works with  Long-, Wide-, and Mixed-Form Data

*Until version 4.8, Plotly Express only operated on long-form (previously called "tidy") data, but [now accepts wide-form and mixed-form data](/python/wide-form/) as well.*

There are three common conventions for storing column-oriented data, usually in a data frame with column names:

* **long-form data** has one row per observation, and one column per variable. This is suitable for storing and displaying multivariate data i.e. with dimension greater than 2. This format is sometimes called "tidy".
* **wide-form data** has one row per value of one of the first variable, and one column per value of the second variable. This is suitable for storing and displaying 2-dimensional data.
* **mixed-form data** is a hybrid of long-form and wide-form data, with one row per value of one variable, and some columns representing values of another, and some columns representing more variables. See the [wide-form documentation](/python/wide-form/) for examples of how to use Plotly Express to visualize this kind of data.

Every Plotly Express function can operate on long-form data (other than `px.imshow` which operates only on wide-form input), and in addition, the following 2D-Cartesian functions can operate on wide-form and mixed-form data: `px.scatter`, `px.line`, `px.area`, `px.bar`, `px.histogram`, `px.violin`, `px.box`, `px.strip`, `px.funnel`, `px.density_heatmap` and `px.density_contour`.

By way of example here is the same data, represented in long-form first, and then in wide-form:

```python
import plotly.express as px
long_df = px.data.medals_long()
long_df
```

```python
import plotly.express as px
wide_df = px.data.medals_wide()
wide_df
```

Plotly Express can produce the same plot from either form:

```python
import plotly.express as px
long_df = px.data.medals_long()

fig = px.bar(long_df, x="nation", y="count", color="medal", title="Long-Form Input")
fig.show()
```

```python
import plotly.express as px
wide_df = px.data.medals_wide()

fig = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input")
fig.show()
```

You might notice that y-axis and legend labels are slightly different for the second plot: they are "value" and "variable", respectively, and this is also reflected in the hoverlabel text. This is because Plotly Express performed an [internal Pandas `melt()` operation](https://pandas.pydata.org/docs/reference/api/pandas.melt.html) to convert the wide-form data into long-form for plotting, and used the Pandas convention for assign column names to the intermediate long-form data. Note that the labels "medal" and "count" do not appear in the wide-form data frame, so in this case, you must supply these yourself, or [you can use a data frame with named row- and column-indexes](/python/wide-form/). You can [rename these labels with the `labels` argument](/python/styling-plotly-express/):

```python
import plotly.express as px
wide_df = px.data.medals_wide()

fig = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input, relabelled",
            labels={"value": "count", "variable": "medal"})
fig.show()
```

Many more examples of wide-form and messy data input can be found in our [detailed wide-form support documentation](/python/wide-form/).


### Input Data as Pandas `DataFrame`s

As shown above, `px` functions supports natively pandas DataFrame. Arguments can either be passed as dataframe columns, or as column names if the `data_frame` argument is provided.

#### Passing columns as arguments

```python
import plotly.express as px
df = px.data.iris()
# Use directly Columns as argument. You can use tab completion for this!
fig = px.scatter(df, x=df.sepal_length, y=df.sepal_width, color=df.species, size=df.petal_length)
fig.show()
```

#### Passing name strings as arguments

```python
import plotly.express as px
df = px.data.iris()
# Use column names instead. This is the same chart as above.
fig = px.scatter(df, x='sepal_length', y='sepal_width', color='species', size='petal_length')
fig.show()
```

#### Using the index of a DataFrame

In addition to columns, it is also possible to pass the index of a DataFrame as argument. In the example below the index is displayed in the hover data.

```python
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x=df.sepal_length, y=df.sepal_width, size=df.petal_length,
                 hover_data=[df.index])
fig.show()
```

### Columns not in the `data_frame` argument

In the addition to columns from the `data_frame` argument, one may also pass columns from a different DataFrame, _as long as all columns have the same length_. It is also possible to pass columns without passing the `data_frame` argument.

However, column names are used only if they correspond to columns in the `data_frame` argument, in other cases, the name of the keyword argument is used. As explained below, the `labels` argument can be used to set names.

```python
import plotly.express as px
import pandas as pd
df1 = pd.DataFrame(dict(time=[10, 20, 30], sales=[10, 8, 30]))
df2 = pd.DataFrame(dict(market=[4, 2, 5]))
fig = px.bar(df1, x=df1.time, y=df2.market, color=df1.sales)
fig.show()
```

### Using labels to pass names

The `labels` argument can be used to override the names used for axis titles, legend entries and hovers.

```python
import plotly.express as px
import pandas as pd

df = px.data.gapminder()
gdp = df['pop'] * df['gdpPercap']
fig = px.bar(df, x='year', y=gdp, color='continent', labels={'y':'gdp'},
             hover_data=['country'],
             title='Evolution of world GDP')
fig.show()
```

### Input Data as array-like columns: NumPy arrays, lists...

`px` arguments can also be array-like objects such as lists, NumPy arrays, in both long-form or wide-form (for certain functions).

```python
import plotly.express as px

# List arguments
fig = px.line(x=[1, 2, 3, 4], y=[3, 5, 4, 8])
fig.show()
```

```python
import numpy as np
import plotly.express as px

t = np.linspace(0, 10, 100)
# NumPy arrays arguments
fig = px.scatter(x=t, y=np.sin(t), labels={'x':'t', 'y':'sin(t)'}) # override keyword names with labels
fig.show()
```

List arguments can also be passed in as a list of lists, which triggers [wide-form data processing](/python/wide-form/), with the downside that the resulting traces will need to be manually renamed via `fig.data[<n>].name = "name"`.

```python
import plotly.express as px

# List arguments in wide form
series1 = [3, 5, 4, 8]
series2 = [5, 4, 8, 3]
fig = px.line(x=[1, 2, 3, 4], y=[series1, series2])
fig.show()
```

### Passing dictionaries or array-likes as the data_frame argument

The column-based argument `data_frame` can also be passed with a `dict` or `array`. Using a dictionary can be a convenient way to pass column names used in axis titles, legend entries and hovers without creating a pandas DataFrame.

```python
import plotly.express as px
import numpy as np
N = 10000
np.random.seed(0)
fig = px.density_contour(dict(effect_size=5 + np.random.randn(N),
                              waiting_time=np.random.poisson(size=N)),
                         x="effect_size", y="waiting_time")
fig.show()
```

#### Integer column names

When the `data_frame` argument is a NumPy array, column names are integer corresponding to the columns of the array. In this case, keyword names are used in axis, legend and hovers. This is also the case for a pandas DataFrame with integer column names. Use the `labels` argument to override these names.

```python
import numpy as np
import plotly.express as px

ar = np.arange(100).reshape((10, 10))
fig = px.scatter(ar, x=2, y=6, size=1, color=5)
fig.show()
```

### Mixing dataframes and other types

It is possible to mix DataFrame columns, NumPy arrays and lists as arguments. Remember that the only column names to be used correspond to columns in the `data_frame` argument, use `labels` to override names displayed in axis titles, legend entries or hovers.

```python
import plotly.express as px
import numpy as np
import pandas as pd

df = px.data.gapminder()
gdp = np.log(df['pop'] * df['gdpPercap'])  # NumPy array
fig = px.bar(df, x='year', y=gdp, color='continent', labels={'y':'log gdp'},
             hover_data=['country'],
             title='Evolution of world GDP')
fig.show()
```