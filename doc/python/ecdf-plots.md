---
description: How to add empirical cumulative distribution function (ECDF) plots.
---
### Overview

[Empirical cumulative distribution function plots](https://en.wikipedia.org/wiki/Empirical_distribution_function) are a way to visualize the distribution of a variable, and Plotly Express has a built-in function, `px.ecdf()` to generate such plots. [Plotly Express](plotly-express.md) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](px-arguments.md) and produces [easy-to-style figures](styling-plotly-express.md).

Alternatives to ECDF plots for visualizing distributions include [histograms](histograms.md), [violin plots](violin.md), [box plots](box-plots.md) and [strip charts](strip-charts.md).

### Simple ECDF Plots

Providing a single column to the `x` variable yields a basic ECDF plot.

```python
import plotly.express as px
df = px.data.tips()
fig = px.ecdf(df, x="total_bill")
fig.show()
```

Providing multiple columns leverage's Plotly Express' [wide-form data support](wide-form.md) to show multiple variables on the same plot.

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

In `standard` mode (the default), the right-most point is at 1 (or the total count/sum, depending on `ecdfnorm`) and the right-most point is above 0.

```python
import plotly.express as px
fig = px.ecdf(df, x=[1,2,3,4], markers=True, ecdfmode="standard",
              title="ecdfmode='standard' (Y=fraction at or below X value, this the default)")
fig.show()
```

In `reversed` mode, the right-most point is at 1 (or the total count/sum, depending on `ecdfnorm`) and the left-most point is above 0.

```python
import plotly.express as px
fig = px.ecdf(df, x=[1,2,3,4], markers=True, ecdfmode="reversed",
              title="ecdfmode='reversed' (Y=fraction at or above X value)")
fig.show()
```

In `complementary` mode, the right-most point is at 0 and no points are at 1 (or the total count/sum) per the definition of the CCDF as 1-ECDF, which has no point at 0.

```python
import plotly.express as px
fig = px.ecdf(df, x=[1,2,3,4], markers=True, ecdfmode="complementary",
              title="ecdfmode='complementary' (Y=fraction above X value)")
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

### Marginal Plots

ECDF plots also support [marginal plots](marginal-plots.md)

```python
import plotly.express as px
df = px.data.tips()
fig = px.ecdf(df, x="total_bill", color="sex", markers=True, lines=False, marginal="histogram")
fig.show()
```

```python
import plotly.express as px
df = px.data.tips()
fig = px.ecdf(df, x="total_bill", color="sex", marginal="rug")
fig.show()
```

### Facets

ECDF Plots also support [faceting](facet-plots.md)

```python
import plotly.express as px
df = px.data.tips()
fig = px.ecdf(df, x="total_bill", color="sex", facet_row="time", facet_col="day")
fig.show()
```

```python

```
