---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: "1.1"
      jupytext_version: 1.1.1
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
    description: Arguments accepted by Plotly Express functions
    display_as: file_settings
    language: python
    layout: base
    name: Plotly Express Arguments
    order: 18
    page_type: u-guide
    permalink: python/px-arguments/
    thumbnail: thumbnail/plotly-express.png
---

### Tidy Data

[Plotly Express](/python/plotly-express) operates on "tidy" or "long" data rather than "wide" data. You may pass data in either as a Pandas `DataFrame` objects or as individual array-like objects which `px` will assemble into a data frame internally, such as lists, `numpy` arrays or Pandas `Series` objects.

What follows is a very short example of the difference between wide and tidy/long data, and the excellent [Tidy Data in Python blog post](https://www.jeannicholashould.com/tidy-data-in-python.html) contains much more information about the tidy approach to structuring data.

```python
import pandas as pd
print("This is 'wide' data, unsuitable as-is for Plotly Express:")
wide_df = pd.DataFrame(dict(Month=["Jan", "Feb", "Mar"], London=[1,2,3], Paris=[3,1,2]))
wide_df
```

```python
import pandas as pd
print("This is the same data in 'long' format, ready for Plotly Express:")
wide_df = pd.DataFrame(dict(Month=["Jan", "Feb", "Mar"], London=[1,2,3], Paris=[3,1,2]))
tidy_df = wide_df.melt(id_vars="Month")
```

```python
import plotly.express as px
import pandas as pd

wide_df = pd.DataFrame(dict(Month=["Jan", "Feb", "Mar"], London=[1,2,3], Paris=[3,1,2]))
tidy_df = wide_df.melt(id_vars="Month")

fig = px.bar(tidy_df, x="Month", y="value", color="variable", barmode="group")
fig.show()
```

### pandas DataFrame input data

`px` functions supports natively pandas DataFrame. Arguments can either be passed as dataframe columns, or as column names if the `data_frame` argument is provided.

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

### Columns not in the data_frame argument

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

### Using array-like arguments: NumPy arrays, lists...

`px` arguments can also be array-like objects such as lists, NumPy arrays.

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
