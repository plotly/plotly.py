---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.4
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
    version: 3.11.10
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

Plotly Express (`px`) is the high-level interface to Plotly and provides functions for generating charts. `px` functions support data provided in a number of different formats (long, wide, and mixed) and as different types of objects, including pandas and Polars dataframes.

## Data for the Examples

The examples on this page use datasets available in the `data` package in `px`. `px.data` contains functions that when called return a dataset as a dataframe. Some of the datasets included in `px.data` are:

- `carshare` - Each row represents the availability of car-sharing services near the centroid of a zone in Montreal over a month-long period.
- `election` - Each row represents voting results for an electoral district in the 2013 Montreal mayoral election.
- `iris` - Each row represents a flower.

To access the `iris` dataset, we call its function and assign it to a variable:

```python
import plotly.express as px

df = px.data.iris()
df.head()
```

By default `px.data` functions return a pandas `DataFrame` object, but you can specify an alternative dataframe type using `return_type`. `pandas`, `polars`, `pyarrow`, `modin`, and `cuDF` are supported return types.

```python
df = px.data.iris(return_type='polars')
df.head()
```

## Long, Wide, and Mixed-Form Data

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

You might notice that y-axis and legend labels are slightly different for the second plot: they are "value" and "variable", respectively, and this is also reflected in the hoverlabel text. Note that the labels "medal" and "count" do not appear in the wide-form data frame, so in this case, you must supply these yourself, or [you can use a data frame with named row- and column-indexes](/python/wide-form/). You can [rename these labels with the `labels` argument](/python/styling-plotly-express/):

```python
import plotly.express as px
wide_df = px.data.medals_wide()

fig = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input, relabelled",
            labels={"value": "count", "variable": "medal"})
fig.show()
```

Many more examples of wide-form and messy data input can be found in our [detailed wide-form support documentation](/python/wide-form/).


## Dataframe Input

The first argument of every `px` function is `data_frame`. If you provide a dataframe as a `px` function's first argument, you can then specify column names as strings from the dataframe as other arguments.

### Supported DataFrame Types

`px` functions natively support pandas, Polars, and PyArrow dataframes. `px` uses [Narwhals](https://narwhals-dev.github.io/narwhals/) to provide this native dataframe support. Other types of dataframes that are currently supported by Narwhals, for example cuDF and Modin, may also work with `px`.

You can also pass dataframes that are not natively supported, but which support the [dataframe interchange protocol](https://data-apis.org/dataframe-protocol/latest/).

PySpark dataframes are also supported and are converted to pandas dataframes internally by Plotly Express.

#### Additional Dependencies Required

- Plotly Express requires NumPy. You can install it with `pip install numpy` if it's not installed by the dataframe library you are using.
- To use [trendlines](/python/linear-fits/), you'll also need to have pandas installed.
- To use PySpark dataframes, you'll need to have pandas installed. To use dataframes that support the dataframe interchange protocol, you'll need to have PyArrow installed.

### Example: Using a Pandas DataFrame with `px.bar`

Here, we create a pandas `DataFrame`, pass it to `px.bar` as its first argument, and then use the `"sepal_length"` column for the x-axis and the `"sepal_width"` for the y-axis.

```python
import plotly.express as px

df = px.data.iris()

fig = px.scatter(df, x='sepal_length', y='sepal_width', color='species', size='petal_length')
fig.show()
```

### Example: Polars DataFrame with `px.bar`

`px` provides native support for dataframe types other than pandas, including Polars:

```python
import plotly.express as px

df = px.data.iris(return_type='polars')

fig = px.scatter(df, x='sepal_length', y='sepal_width', color='species', size='petal_length')
fig.show()
```

### Using the Index of a Dataframe

If the dataframe you are using has an index, it is also possible to use that index as an argument. In the following example, the index is used for the hover data.

```python
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x=df.sepal_length, y=df.sepal_width, size=df.petal_length,
                 hover_data=[df.index])
fig.show()
```

### Using Columns from Multiple Dataframes

You can also use columns from multiple dataframes in one `px` function, as long as all the dataframe columns you use have the same length. In this example, we pass `df1` as the `data_frame` argument to `px.bar` and then us a column from `df2` for the `y` argument.

```python
import plotly.express as px
import pandas as pd

df1 = pd.DataFrame(dict(time=[10, 20, 30], sales=[10, 8, 30]))
df2 = pd.DataFrame(dict(market=[4, 2, 5]))
fig = px.bar(df1, x="time", y=df2.market, color="sales")
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

```python
## Other Input Data
```

### Input Data as array-like columns: NumPy arrays, lists...

`px` arguments can also be array-like objects such as lists, NumPy arrays, in both long-form or wide-form (for certain functions).

```python
import plotly.express as px

# List arguments
fig = px.line(x=[1, 2, 3, 4], y=[3, 5, 4, 8])
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

The `data_frame` argument can also accept a `dict` or `array` in addition to DataFrame objects. Using a dictionary can be a convenient way to pass column names used in axis titles, legend entries and hovers without creating a dataframe.

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

To pass a `dict` or an array (such as a NumPy `ndarray`) to the `data_frame` parameter, you'll need to have pandas installed, because `plotly.express` internally converts the `dict` or array to a pandas DataFrame.

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

It is possible to mix dataframe columns, NumPy arrays and lists as arguments. Remember that the only column names to be used correspond to columns in the `data_frame` argument, use `labels` to override names displayed in axis titles, legend entries or hovers.

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
