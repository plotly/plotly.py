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
    order: 33
    page_type: u-guide
    permalink: python/wide-form/
    thumbnail: thumbnail/plotly-express.png
---

### Column-oriented, Matrix or Geographic Data

Plotly Express provides functions to visualize a variety of types of data. Most functions such as `px.bar` or `px.scatter` expect to operate on column-oriented data of the type you might store in a Pandas `DataFrame` (in either "long" or "wide" format, see below). [`px.imshow` operates on matrix-like data](/python/imshow/) you might store in a `numpy` or `xarray` array and functions like [`px.choropleth` and `px.choropleth_mapbox` can operate on geographic data](/python/maps/) of the kind you might store in a GeoPandas `GeoDataFrame`. This page details how to provide a specific form of column-oriented data to 2D-Cartesian Plotly Express functions, but you can also check out our [detailed column-input-format documentation](/python/px-arguments/).

### Long-, Wide-, and Mixed-Form Data

*Until version 4.8, Plotly Express only operated on long-form (previously called "tidy") data, but now accepts wide-form and mixed-form data as well.*

There are three common conventions for storing column-oriented data, usually in a data frame with column names:

* **long-form data** is suitable for storing multivariate data (i.e. dimensions greater than 2), with one row per observation, and one column per variable.
* **wide-form data** is suitable for storing 2-dimensional data, with one row per value of one of the first variable, and one column per value of the second variable.
* **mixed-form data** is a hybrid of long-form and wide-form data, with one row per value of one variable, and some columns representing values of another, and some columns representing more variables

All Plotly Express functions can operate on long-form data, and the following 2D-Cartesian functions can operate on wide-form data as well:: `px.scatter`, `px.line`, `px.area`, `px.bar`, `px.histogram`, `px.violin`, `px.box`, `px.strip`, `px.funnel`, `px.density_heatmap` and `px.density_contour`.

By way of example here is the same data, represented in long-form first, and then in wide-form:

```python
import plotly.express as px
long_df = px.data.short_track_long()
long_df
```

```python
import plotly.express as px
wide_df = px.data.short_track_wide()
wide_df
```

Plotly Express can produce the same plot from either form:

```python
import plotly.express as px
long_df = px.data.short_track_long()

fig = px.bar(long_df, x="nation", y="count", color="medal", title="Long-Form Input")
fig.show()
```

```python
import plotly.express as px
wide_df = px.data.short_track_wide()

fig = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input")
fig.show()
```

### Labeling axes, legends and hover text

You might notice that y-axis and legend labels are slightly different for the second plot: they are "value" and "variable", respectively, and this is also reflected in the hoverlabel text. This is because Plotly Express performed an [internal Pandas `melt()` operation](https://pandas.pydata.org/docs/reference/api/pandas.melt.html) to convert the wide-form data into long-form for plotting, and used the Pandas convention for assign column names to the intermediate long-form data. Note that the labels "medal" and "count" do not appear in the wide-form data frame, so in this case, you must supply these yourself, (or see below regarding using a data frame with named row- and column-indexes). You can [rename these labels with the `labels` argument](/python/styling-plotly-express/):

```python
import plotly.express as px
wide_df = px.data.short_track_wide()

fig = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input, relabelled",
            labels={"value": "count", "variable": "medal"})
fig.show()
```

Plotly Express figures created using wide-form data can be [styled just like any other Plotly Express figure](/python/styling-plotly-express/):

```python
import plotly.express as px
wide_df = px.data.short_track_wide()

fig = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"], 
             title="Wide-Form Input, styled",
             labels={"value": "Medal Count", "variable": "Medal", "nation": "Olympic Nation"},
             color_discrete_map={"gold":"gold", "silver": "silver", "bronze": "#c96"},
             template="simple_white"
            )
fig.update_layout(font_family="Rockwell", showlegend=False)
fig.show()
```

### Data Frames with Named Indexes

Pandas `DataFrames` support not only column names and "row names" via the value of `index`, but the indexes themselves can be named. Here is how to assign one column of the wide sample data frame above as the index, and to name the column index. The result "indexed" sample data frame can also be obtained by calling `px.data.short_track_wide(indexed=True)`

```python
import plotly.express as px
wide_df = px.data.short_track_wide()
wide_df = wide_df.set_index("nation")
wide_df.columns.name = "medals"
wide_df
```

When working with a data frame like the one above, you can pass the index references directly as arguments, to benefit from automatic labelling for everything except the y axis label, which will default to "values", but this can be overridden with the `labels` argument as above:

```python
import plotly.express as px
wide_df = px.data.short_track_wide(indexed=True)

fig = px.bar(wide_df, x=wide_df.index, y=wide_df.columns)
fig.show()
```

If you transpose `x` and `y`, thereby assigning the columns to `x`, the orientation will be switched to horizontal:

```python
import plotly.express as px
wide_df = px.data.short_track_wide(indexed=True)

fig = px.bar(wide_df, x=wide_df.columns, y=wide_df.index)
fig.show()
```

### Wide-Form Defaults

For bar, scatter, line and area charts, this pattern of assigning `x=df.index` and `y=df.columns` is so common that if you provide neither `x` nor `y` this is the default behaviour

```python
import plotly.express as px
wide_df = px.data.short_track_wide(indexed=True)

fig = px.bar(wide_df)
fig.show()

fig = px.area(wide_df)
fig.show()

fig = px.line(wide_df)
fig.show()

fig = px.scatter(wide_df)
fig.show()
```

### Orientation Control When Using Defaults

If you specify neither `x` nor `y`, you can specify whether the Y or X xaxis is assigned to the index with `orientation`.

```python
import plotly.express as px
wide_df = px.data.short_track_wide(indexed=True)

fig = px.bar(wide_df, orientation="h")
fig.show()
```

### Assigning Columns to Non-Color Arguments


In the examples above, the columns of the wide data frame are always assigned to the `color` argument, but this is not a hard constraint. The columns can be assigned to any Plotly Express argument, for example to accomplish faceting, and `color` can be reassigned to any other value. When plotting with a data frame without named indexes, you can reassign the inferred column named `"variable"` and `"value"` to any argument:

```python
import plotly.express as px
wide_df = px.data.short_track_wide(indexed=False)

fig = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"], facet_col="variable", color="nation")
fig.show()
```

If using a data frame's named indexes, either explicitly or relying on the defaults, the index references or names must be used:

```python
import plotly.express as px
wide_df = px.data.short_track_wide(indexed=True)

fig = px.bar(wide_df, facet_col="medal", color=wide_df.index)
fig.show()
```

### Mixed-Form Data

In some cases, a data frame is neither clearly long-form nor wide-form, and we can call this "mixed-form". For example, in the data frame below, if it contained only the `experiment` columns, the data could be described as wide-form, and if it contained only `gender` and `group` it could be described as long-form, but it contains both:

```python
import plotly.express as px
mixed_df = px.data.experiment(indexed=True)
mixed_df.head()
```

We can visualize just the wide-form portion of the data frame easily with a [violin chart](/python/violin/). As a special note, we'll assign the index, which is the participant ID, to the hover_data, so that hovering over outlier points will identify their row.

```python
import plotly.express as px
mixed_df = px.data.experiment(indexed=True)

fig = px.violin(mixed_df, y=["experiment_1", "experiment_2", "experiment_3"], hover_data=[mixed_df.index])
fig.show()
```




We can also leverage the long-form portion of the data frame, for example to color by `gender` and facet by `group`:

```python
import plotly.express as px
mixed_df = px.data.experiment(indexed=True)

fig = px.violin(mixed_df, y=["experiment_1", "experiment_2", "experiment_3"], 
                color="gender", facet_col="group", hover_data=[mixed_df.index])
fig.show()
```

And of course, we can reassign `variable` to another argument as well, in this case we'll assign it to `x` and facet by the wide variable, and we'll switch to a [box plot](/python/box-plots/) for variety.

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

```python

```
