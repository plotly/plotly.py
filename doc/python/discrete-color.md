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
    description: How to use and configure discrete color sequences, also known as
      categorical or qualitative color scales.
    display_as: file_settings
    has_thumbnail: true
    ipynb: ~notebook_demo/187
    language: python
    layout: base
    name: Discrete Colors
    order: 28
    permalink: python/discrete-color/
    thumbnail: thumbnail/heatmap_colorscale.jpg
    v4upgrade: true
---

### Discrete vs Continuous Color

In the same way as the X or Y position of a mark in cartesian coordinates can be used to represent continuous values (i.e. amounts or moments in time) or categories (i.e. labels), color can be used to represent continuous or discrete data. This page is about using color to represent **categorical** data using discrete colors, but Plotly can also [represent continuous values with color](/python/colorscales/).

### Discrete Color Concepts

This document explains the following discrete-color-related concepts:

- **color sequences** are lists of colors to be mapped onto discrete data values. No interpolation occurs when using color sequences, unlike with [continuous color scales](/python/colorscales/), and each color is used as-is. Color sequence defaults depend on the `layout.colorway` attribute of the active [template](/python/templates/), and can be explicitly specified using the `color_discrete_sequence` argument for many [Plotly Express](/python/plotly-express/) functions.
- **legends** are visible representations of the mapping between colors and data values. Legend markers also change shape when used with various kinds of traces, such as symbols or lines for scatter-like traces. [Legends are configurable](/python/legend/) under the `layout.legend` attribute. Legends are the discrete equivalent of [continous color bars](/python/colorscales/)

### Discrete Color with Plotly Express

Most Plotly Express functions accept a `color` argument which automatically assigns data values to discrete colors **if the data is non-numeric**. If the data is numeric, the color will automatically be considered [continuous](/python/colorscales/). This means that numeric strings must be parsed to be used for continuous color, and conversely, numbers used as category codes must be converted to strings.

For example, in the `tips` dataset, the `smoker` column contains strings:

```python
import plotly.express as px
df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", color="smoker",
                 title="String 'smoker' values mean discrete colors")

fig.show()
```

The `size` column, however, contains numbers:

```python
import plotly.express as px
df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", color="size",
                 title="Numeric 'size' values mean continous color")

fig.show()
```

Converting this column to strings is very straightforward, but note that the ordering in the legend is not sequential by default (see below for how to control discrete order):

```python
import plotly.express as px
df = px.data.tips()
df["size"] = df["size"].astype(str)
fig = px.scatter(df, x="total_bill", y="tip", color="size",
                 title="String 'size' values mean discrete colors")

fig.show()
```

Converting a string column to a numeric one is also quite straightforward:

```python
import plotly.express as px
df = px.data.tips()
df["size"] = df["size"].astype(str) #convert to string
df["size"] = df["size"].astype(float) #convert back to numeric

fig = px.scatter(df, x="total_bill", y="tip", color="size",
                 title="Numeric 'size' values mean continous color")

fig.show()
```

### Color Sequences in Plotly Express

By default, Plotly Express will use the color sequence from the active [template](/python/templates/)'s `layout.colorway` attribute, and the default active template is `plotly` which uses the `plotly` color sequence. You can choose any of the following built-in qualitative color sequences from the `px.colors.qualitative` module, however, or define your own.

```python
import plotly.express as px

fig = px.colors.qualitative.swatches()
fig.show()
```

Color sequences in the `px.colors.qualitative` module are stored as lists of CSS colors:

```python
import plotly.express as px

print(px.colors.qualitative.Plotly)
```

Here is an example that creates a scatter plot using Plotly Express, with points colored using the built-in qualitative `G10` color sequence.

```python
import plotly.express as px
df = px.data.gapminder()
fig = px.line(df, y="lifeExp", x="year", color="continent", line_group="country",
              line_shape="spline", render_mode="svg",
             color_discrete_sequence=px.colors.qualitative.G10,
             title="Built-in G10 color sequence")

fig.show()
```

### Explicitly Constructing a Color Sequence

The Plotly Express `color_discrete_sequence` argument accepts explicitly-constructed color sequences as well, as lists of CSS colors:

```python
import plotly.express as px
df = px.data.gapminder().query("year == 2007")
fig = px.bar(df, y="continent", x="pop", color="continent", orientation="h", hover_name="country",
             color_discrete_sequence=["red", "green", "blue", "goldenrod", "magenta"],
             title="Explicit color sequence"
            )

fig.show()
```

**_Warning_**: If your color sequence is has fewer colors than the number of unique values in the column you are mapping to `color`, the colors will cycle through and repeat, possibly leading to ambiguity:

```python
import plotly.express as px
df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", color="day",
             color_discrete_sequence=["red", "blue"],
             title="<b>Ambiguous!</b> Explicit color sequence cycling because it is too short"
            )

fig.show()
```

### Directly Mapping Colors to Data Values

The example above assigned colors to data values on a first-come-first-served basis, but you can directly map colors to data values if this is important to your application with `color_discrete_map`. Note that this does not change the order in which values appear in the figure or legend, as can be controlled below:

```python
import plotly.express as px
df = px.data.gapminder().query("year == 2007")
fig = px.bar(df, y="continent", x="pop", color="continent", orientation="h", hover_name="country",
             color_discrete_map={
                "Europe": "red",
                "Asia": "green",
                "Americas": "blue",
                "Oceania": "goldenrod",
                "Africa": "magenta"},
             title="Explicit color mapping")

fig.show()
```

### Controlling Discrete Color Order

Plotly Express lets you specify an ordering over categorical variables with `category_orders`, which will apply to colors and legends as well as symbols, [axes](/python/axes/) and [facets](/python/facet-plots/). This can be used with either `color_discrete_sequence` or `color_discrete_map`.

```python
import plotly.express as px
df = px.data.gapminder().query("year == 2007")
fig = px.bar(df, y="continent", x="pop", color="continent", orientation="h", hover_name="country",
             color_discrete_sequence=["red", "green", "blue", "goldenrod", "magenta"],
             category_orders={"continent": ["Oceania", "Europe", "Asia", "Africa", "Americas"]},
             title="Explicit color sequence with explicit ordering"
            )

fig.show()
```

```python
import plotly.express as px
df = px.data.gapminder().query("year == 2007")
fig = px.bar(df, y="continent", x="pop", color="continent", orientation="h", hover_name="country",
             color_discrete_map={
                "Europe": "red",
                "Asia": "green",
                "Americas": "blue",
                "Oceania": "goldenrod",
                "Africa": "magenta"},
             category_orders={"continent": ["Oceania", "Europe", "Asia", "Africa", "Americas"]},
             title="Explicit color mapping with explicit ordering"
            )

fig.show()
```

### Using Sequential Scales as Discrete Sequences

In most cases, discrete/qualitative/categorical data values have no meaningful natural ordering, such as in the continents example used above. In some cases, however, there is a meaningful order, and in this case it can be helpful and appealing to use part of a continuous scale as a discrete sequence, as in the following [wind rose chart](/python/wind-rose-charts/):

```python
import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, r="frequency", theta="direction", color="strength",
                   color_discrete_sequence= px.colors.sequential.Plasma_r,
                   title="Part of a continuous color scale used as a discrete sequence"
                  )
fig.show()
```

This works because just like in `px.colors.qualitative`, all [built-in continuous color scales](/python/builtin-colorscales/) are stored as lists of CSS colors:

```python
import plotly.express as px

print(px.colors.sequential.Plasma)
```
