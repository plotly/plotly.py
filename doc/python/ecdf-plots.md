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
    description: How to add empirical cumulative distribution function (ECDF) plots.
    display_as: statistical
    language: python
    layout: base
    name: Empirical Cumulative Distribution Plots
    order: 16
    page_type: u-guide
    permalink: python/ecdf-plots/
    thumbnail: thumbnail/figure-labels.png
---

### Overview

[Empirical cumulative distribution function plots](https://en.wikipedia.org/wiki/Empirical_distribution_function) are a way to visualize the distribution of a variabl, and Plotly Express has a built-in function, `px.ecdf()` to generate such plots. [Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/).

### Simple ECDF Plots

Providing a single column to the `x` variable yields a basic ECDF plot.

```python
import plotly.express as px
df = px.data.tips()
fig = px.ecdf(df, x="total_bill")
fig.show()
```

Providing multiple columns leverage's Plotly Express' [wide-form data support](https://plotly.com/python/wide-form/) to show multiple variables on the same plot.

```python
import plotly.express as px
df = px.data.tips()
fig = px.ecdf(df, x=["total_bill", "tip"])
fig.show()
```

It is also possible to map another variable to the color dimension of a plot.

```python
import plotly.express as px
df = px.data.tips()
fig = px.ecdf(df, x="total_bill", color="sex")
fig.show()
```

### Configuring the Y axis

By default, the Y axis shows probability, but it is also possible to show raw counts by setting the `ecdfnorm` argument to `None` or to show percentages by setting it to `percent`.

```python
import plotly.express as px
df = px.data.tips()
fig = px.ecdf(df, x="total_bill", color="sex", ecdfnorm=None)
fig.show()
```

If a `y` value is provided, the Y axis is set to the sum of `y` rather than counts.

```python
import plotly.express as px
df = px.data.tips()
fig = px.ecdf(df, x="total_bill", y="tip", color="sex", ecdfnorm=None)
fig.show()
```

### Reversed and Complementary CDF plots

By default, the Y value represents the fraction of the data that is *at or below* the value on on the X axis. Setting `ecdfmode` to `"reversed"` reverses this, with the Y axis representing the fraction of the data *at or above* the X value. Setting `ecdfmode` to `"complementary"` plots `1-ECDF`, meaning that the Y values represent the fraction of the data *above* the X value.

```python
import plotly.express as px
fig = px.ecdf(df, x=[1,2,3,4], markers=True, ecdfmode="standard",
              title="ecdfmode='standard' (at or below X value, the default)")
fig.show()
```

```python
import plotly.express as px
fig = px.ecdf(df, x=[1,2,3,4], markers=True, ecdfmode="reversed",
              title="ecdfmode='reversed' (at or above X value)")
fig.show()
```

```python
import plotly.express as px
fig = px.ecdf(df, x=[1,2,3,4], markers=True, ecdfmode="complementary",
              title="ecdfmode='complementary' (above X value)")
fig.show()
```

### Orientation

By default, plots are oriented vertically (i.e. the variable is on the X axis and counted/summed upwards), but this can be overridden with the `orientation` argument.

```python
import plotly.express as px
df = px.data.tips()
fig = px.ecdf(df, x="total_bill", y="tip", color="sex", ecdfnorm=None, orientation="h")
fig.show()
```

### Markers and/or Lines

ECDF Plots can be configured to show lines and/or markers.

```python
import plotly.express as px
df = px.data.tips()
fig = px.ecdf(df, x="total_bill", color="sex", markers=True)
fig.show()
```

```python
import plotly.express as px
df = px.data.tips()
fig = px.ecdf(df, x="total_bill", color="sex", markers=True, lines=False)
fig.show()
```

```python

```
