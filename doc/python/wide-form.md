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
    description: Plotly Express' 2D-Cartesian functions accept data in long-, wide-,
      and mixed-form.
    display_as: file_settings
    language: python
    layout: base
    name: Plotly Express Wide-Form Support
    order: 34
    page_type: u-guide
    permalink: python/wide-form/
    thumbnail: thumbnail/plotly-express.png
---

### Plotly Express works with Column-oriented, Matrix or Geographic Data

Plotly Express provides functions to visualize a variety of types of data. Most functions such as `px.bar` or `px.scatter` expect to operate on column-oriented data of the type you might store in a Pandas `DataFrame` (in either "long" or "wide" format, see below). [`px.imshow` operates on matrix-like data](/python/imshow/) you might store in a `numpy` or `xarray` array and functions like [`px.choropleth` and `px.choropleth_mapbox` can operate on geographic data](/python/maps/) of the kind you might store in a GeoPandas `GeoDataFrame`. This page details how to provide a specific form of column-oriented data to 2D-Cartesian Plotly Express functions, but you can also check out our [detailed column-input-format documentation](/python/px-arguments/).

### Plotly Express works with Long-, Wide-, and Mixed-Form Data

*Until version 4.8, Plotly Express only operated on long-form (previously called "tidy") data, but now accepts wide-form and mixed-form data as well.*

There are three common conventions for storing column-oriented data, usually in a data frame with column names:

* **long-form data** has one row per observation, and one column per variable. This is suitable for storing and displaying multivariate data i.e. with dimension greater than 2. This format is sometimes called "tidy".
* **wide-form data** has one row per value of one of the first variable, and one column per value of the second variable. This is suitable for storing and displaying 2-dimensional data.
* **mixed-form data** is a hybrid of long-form and wide-form data, with one row per value of one variable, and some columns representing values of another, and some columns representing more variables.

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

Plotly Express can produce **the same plot from either form**. For the long-form input, `x` and `y` are set to the respective column names.

```python
import plotly.express as px
long_df = px.data.medals_long()

fig = px.bar(long_df, x="nation", y="count", color="medal", title="Long-Form Input")
fig.show()
```

For the wide-form input, we **pass in a list of column-names `y`**, which is enough to trigger the wide-form processing mode. Wide-form mode is also the default if neither `x` nor `y` are specified, see section at bottom regarding Wide-Form Defaults.

```python
import plotly.express as px
wide_df = px.data.medals_wide()

fig = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input")
fig.show()
```

### Labeling axes, legends and hover text

You might notice that y-axis and legend labels are slightly different for the second plot: they are "value" and "variable", respectively, and this is also reflected in the hoverlabel text. This is because Plotly Express performed an [internal Pandas `melt()` operation](https://pandas.pydata.org/docs/reference/api/pandas.melt.html) to convert the wide-form data into long-form for plotting, and used the Pandas convention for assign column names to the intermediate long-form data. Note that the labels "medal" and "count" do not appear in the wide-form data frame, so in this case, you must supply these yourself, (or see below regarding using a data frame with named row- and column-indexes). You can [rename these labels with the `labels` argument](/python/styling-plotly-express/):

```python
import plotly.express as px
wide_df = px.data.medals_wide()

fig = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input, relabelled",
            labels={"value": "count", "variable": "medal"})
fig.show()
```

Plotly Express figures created using wide-form data can be [styled just like any other Plotly Express figure](/python/styling-plotly-express/):

```python
import plotly.express as px
wide_df = px.data.medals_wide()

fig = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"],
             title="Wide-Form Input, styled",
             labels={"value": "Medal Count", "variable": "Medal", "nation": "Olympic Nation"},
             color_discrete_map={"gold": "gold", "silver": "silver", "bronze": "#c96"},
             template="simple_white"
            )
fig.update_layout(font_family="Rockwell", showlegend=False)
fig.show()
```

### Data Frames with Named Indexes

Pandas `DataFrames` support not only column names and "row names" via the value of `index`, but the indexes themselves can be named. Here is how to assign one column of the wide sample data frame above as the index, and to name the column index. The result "indexed" sample data frame can also be obtained by calling `px.data.medals_wide(indexed=True)`

```python
import plotly.express as px
wide_df = px.data.medals_wide()
wide_df = wide_df.set_index("nation")
wide_df.columns.name = "medals"
wide_df
```

When working with a data frame like the one above, you can pass the index references directly as arguments, to benefit from automatic labelling for everything except the y axis label, which will default to "values", but this can be overridden with the `labels` argument as above:

```python
import plotly.express as px
wide_df = px.data.medals_wide(indexed=True)

fig = px.bar(wide_df, x=wide_df.index, y=wide_df.columns)
fig.show()
```

If you transpose `x` and `y`, thereby assigning the columns to `x`, the orientation will be switched to horizontal:

```python
import plotly.express as px
wide_df = px.data.medals_wide(indexed=True)

fig = px.bar(wide_df, x=wide_df.columns, y=wide_df.index)
fig.show()
```

### Assigning Inferred Columns to Non-Default Arguments


In the examples above, the columns of the wide data frame are assigned by default as an "inferred" column named `variable` to the `color` argument (see section below for documentation of the default behaviours), but this is not a hard constraint. The `variable` column can be assigned to any Plotly Express argument, for example to accomplish faceting, and `color` can be reassigned to any other value. More generally, when plotting with a data frame without named indexes, you can reassign the inferred column named `variable` and `value` to any argument:

```python
import plotly.express as px
wide_df = px.data.medals_wide(indexed=False)

fig = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"], facet_col="variable", color="nation")
fig.show()
```

You can also prevent `color` from getting assigned if you're mapping `variable` to some other argument:

```python
import plotly.express as px
wide_df = px.data.medals_wide(indexed=False)

fig = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"], facet_col="variable", color=px.NO_COLOR)
fig.show()
```

If using a data frame's named indexes, either explicitly or relying on the defaults, the row-index references (i.e. `df.index`) or column-index names (i.e. the value of `df.columns.name`) must be used:

```python
import plotly.express as px
wide_df = px.data.medals_wide(indexed=True)

fig = px.bar(wide_df, facet_col="medal", color=wide_df.index)
fig.show()
```

### Mixed-Form Data

In some cases, a data frame is neither clearly long-form nor wide-form, and we can call this "mixed-form". For example, in the data frame below, if it contained only the `experiment` columns, the data could be described as wide-form, and if it contained only `gender` and `group` it could be described as long-form, but it contains both, so it is best described as mixed-form data:

```python
import plotly.express as px
mixed_df = px.data.experiment(indexed=True)
mixed_df.head()
```

We can visualize just the wide-form portion of the data frame easily with a [violin chart](/python/violin/). As a special note, we'll assign the index, which is the participant ID, to the `hover_data`, so that hovering over outlier points will identify their row.

```python
import plotly.express as px
mixed_df = px.data.experiment(indexed=True)

fig = px.violin(mixed_df, y=["experiment_1", "experiment_2", "experiment_3"], hover_data=[mixed_df.index])
fig.show()
```




We are not limited to visualizing only the wide-form portion of the data, however. We can also leverage the long-form portion of the data frame, for example to color by participant `gender` and facet by participant `group`, all without having to manipulate the data frame:

```python
import plotly.express as px
mixed_df = px.data.experiment(indexed=True)

fig = px.violin(mixed_df, y=["experiment_1", "experiment_2", "experiment_3"],
                color="gender", facet_col="group", hover_data=[mixed_df.index])
fig.show()
```

In the plots above, the column names provided to `y` are internally mapped to long-form column called `variable`, as is apparent in the x-axis labels. We can reassign `variable` to another argument as well, in this case we'll assign it to `facet_col` and reassign `group` to the `x` axis. We'll switch to a [box plot](/python/box-plots/) for variety.

```python
import plotly.express as px
mixed_df = px.data.experiment(indexed=True)

fig = px.box(mixed_df, x="group", y=["experiment_1", "experiment_2", "experiment_3"],
                color="gender", facet_col="variable", hover_data=[mixed_df.index])
fig.show()
```

One interesting thing about a mixed-form data frame like this is that it remains easy to plot, say, one experiment against another, which would require some preliminary data wrangling if this was represented as a pure long-form dataset:

```python
import plotly.express as px
mixed_df = px.data.experiment(indexed=True)

fig = px.scatter(mixed_df, x="experiment_1", y="experiment_2",
                color="group", facet_col="gender", hover_data=[mixed_df.index])
fig.show()
```

In fact, we can even visualize the results of every experiment against every other, using a [scatterplot matrix](/python/splom/):

```python
import plotly.express as px
mixed_df = px.data.experiment(indexed=True)

fig = px.scatter_matrix(mixed_df, dimensions=["experiment_1", "experiment_2", "experiment_3"], color="gender")
fig.show()
```

### Wide-Form Defaults

For bar, scatter, line and area charts, the pattern of assigning `x=df.index`, `y=df.columns`, `color="variable"` is so common that if you provide neither `x` nor `y` this is the default behaviour. An exception is made for bar charts when the values are not continuous variables, in which case the default is similar to histograms, with `x=df.columns`, `color="variable"` and `y=<constant 1, labeled "count">`.

For violin and box plots, the default is to assign `x=variable`, `y=df.columns` and for histograms the default is `x=df.columns`, `color="variable"`

These defaults are also filled in if you specify only `y` (`x` for histograms) as a list-of-columns. See below for orientation control.

```python
import plotly.express as px
wide_df = px.data.medals_wide(indexed=True)

fig = px.bar(wide_df)
fig.show()

fig = px.area(wide_df)
fig.show()

fig = px.line(wide_df)
fig.show()

fig = px.scatter(wide_df)
fig.show()
```

```python
import plotly.express as px

mixed_df = px.data.experiment(indexed=True)
wide_df = mixed_df[["experiment_1", "experiment_2", "experiment_3"]]

fig = px.histogram(wide_df)
fig.show()

fig = px.violin(wide_df)
fig.show()

fig = px.box(wide_df)
fig.show()
```

### Orientation Control When Using Defaults

If you specify neither `x` nor `y`, you can swap the default behaviour of `x` and `y` by setting `orientation="h"`.

If you specify only `x` as a list-of-columns (`y` in the case of histograms), then the defaults are filled in as if `orientation="h"`

```python
import plotly.express as px
wide_df = px.data.medals_wide(indexed=True)

fig = px.bar(wide_df, orientation="h")
fig.show()

fig = px.area(wide_df, x=wide_df.columns)
fig.show()

mixed_df = px.data.experiment(indexed=True)
wide_df = mixed_df[["experiment_1", "experiment_2", "experiment_3"]]

fig = px.histogram(wide_df, orientation="h")
fig.show()

fig = px.violin(wide_df, orientation="h")
fig.show()

fig = px.box(wide_df, orientation="h")
fig.show()
```