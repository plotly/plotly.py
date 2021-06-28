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
    description: Plotly Express can be used as a Pandas .plot() backend.
    display_as: file_settings
    language: python
    layout: base
    name: Pandas Plotting Backend
    order: 32
    permalink: python/pandas-backend/
    redirect_from: python/cufflinks/
    thumbnail: thumbnail/plotly-express.png
---

### Introduction

The popular [Pandas](https://pandas.pydata.org/) data analysis and manipulation tool provides [plotting functions on its `DataFrame` and `Series` objects](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html), which have historically produced `matplotlib` plots. Since version 0.25, Pandas has provided a mechanism to use different backends, and as of version 4.8 of `plotly`, you can now use a [Plotly Express-powered](/python/plotly-express/) backend for Pandas plotting. This means you can now produce interactive plots directly from a data frame, without even needing to import Plotly.

To activate this backend, you will need to [have Plotly installed](/python/getting-started/), and then just need to set `pd.options.plotting.backend` to `"plotly"` and call `.plot()` to get a `plotly.graph_objects.Figure` object back, just like if you had called Plotly Express directly:

```python
import pandas as pd
pd.options.plotting.backend = "plotly"

df = pd.DataFrame(dict(a=[1,3,2], b=[3,2,1]))
fig = df.plot()
fig.show()
```

This functionality wraps [Plotly Express](/python/plotly-express/) and so you can use any of the [styling options available to Plotly Express methods](/python/styling-plotly-expres/). Since what you get back is a regular `Figure` object, you can use any of the update mechanisms supported by these objects to apply [templates](/python/templates/) or further customize [axes](/python/axes/), [colors](/python/colorscales/), [legends](/python/legend/), [fonts](/python/figure-labels/), [hover labels](/python/hover-text-and-formatting/) etc. [Faceting](/python/facet-plots/) is also supported.

```python
import pandas as pd
pd.options.plotting.backend = "plotly"

df = pd.DataFrame(dict(a=[1,3,2], b=[3,2,1]))
fig = df.plot(title="Pandas Backend Example", template="simple_white",
              labels=dict(index="time", value="money", variable="option"))
fig.update_yaxes(tickprefix="$")
fig.show()
```

### A Note on API Compatibility

> The Plotly plotting backend for Pandas is *not intended* to be a drop-in replacement for the default; it does not implement all or even most of the same keyword arguments, such as `subplots=True` etc.

The Plotly plotting backend for Pandas is a more convenient way to invoke certain [Plotly Express](/python/plotly-express/) functions by chaining a `.plot()` call without having to import Plotly Express directly. Plotly Express, as of version 4.8 with [wide-form data support](/python/wide-form/) in addition to its robust long-form data support, implements behaviour for the `x` and `y` keywords that are very similar to the `matplotlib` backend.

In practice, this means that the following two ways of making a chart are identical and support the same additional arguments, because they call the same underlying code:

```python
import pandas as pd
pd.options.plotting.backend = "plotly"
df = pd.DataFrame(dict(a=[1,3,2], b=[3,2,1]))

# using Plotly Express via the Pandas backend
fig1 = df.plot.bar()
fig1.show()

# using Plotly Express directly
import plotly.express as px
fig2 = px.bar(df)
fig2.show()
```

To achieve a similar effect to `subplots=True`, for example, the [Plotly Express `facet_row` and `facet_col` options](/python/facet-plots/) can be used, the same was as they work when directly calling [Plotly Express with wide-form data](/python/wide-form/):

```python
import pandas as pd
pd.options.plotting.backend = "plotly"
df = pd.DataFrame(dict(a=[1,3,2], b=[3,2,1]))

fig = df.plot.bar(facet_row="variable")
fig.show()
```

### Supported Methods

The Plotly backend supports the following `kind`s of Pandas plots: `scatter`, `line`, `area`, `bar`, `barh`, `hist` and `box`, via the call pattern `df.plot(kind='scatter')` or `df.plot.scatter()`. These delegate to the corresponding Plotly Express functions. In addition, the following are valid options to the `kind` argument of `df.plot()`: `violin`, `strip`, `funnel`, `density_heatmap`, `density_contour` and `imshow`, even though the call pattern `df.plot.violin()` is not supported for these kinds of charts, per the Pandas API.

```python
import pandas as pd
import numpy as np
pd.options.plotting.backend = "plotly"
np.random.seed(1)

df = pd.DataFrame(dict(
    a=np.random.normal(loc=1, scale=2, size=100),
    b=np.random.normal(loc=2, scale=1, size=100)
))
fig = df.plot.scatter(x="a", y="b")
fig.show()
```

```python
import pandas as pd
pd.options.plotting.backend = "plotly"

df = pd.DataFrame(dict(a=[1,3,2], b=[3,2,1]))
fig = df.plot.line()
fig.show()
```

```python
import pandas as pd
pd.options.plotting.backend = "plotly"

df = pd.DataFrame(dict(a=[1,3,2], b=[3,2,1]))
fig = df.plot.area()
fig.show()
```

```python
import pandas as pd
pd.options.plotting.backend = "plotly"

df = pd.DataFrame(dict(a=[1,3,2], b=[3,2,1]))
fig = df.plot.bar()
fig.show()
```

```python
import pandas as pd
pd.options.plotting.backend = "plotly"

df = pd.DataFrame(dict(a=[1,3,2], b=[3,2,1]))
fig = df.plot.barh()
fig.show()
```

```python
import pandas as pd
import numpy as np
pd.options.plotting.backend = "plotly"
np.random.seed(1)

df = pd.DataFrame(dict(
    a=np.random.normal(loc=1, scale=2, size=100),
    b=np.random.normal(loc=2, scale=1, size=100)
))
fig = df.plot.hist()
fig.show()
```

```python
import pandas as pd
import numpy as np
pd.options.plotting.backend = "plotly"
np.random.seed(1)

df = pd.DataFrame(dict(
    a=np.random.normal(loc=1, scale=2, size=100),
    b=np.random.normal(loc=2, scale=1, size=100)
))
fig = df.plot.box()
fig.show()
```

### `Series` and `DataFrame` functions: `hist` and `boxplot`

The Pandas plotting API also exposes `.hist()` on `DataFrame`s and `Series` objects, and `.boxplot()` on `DataFrames`, which can also be used with the Plotly backend.

```python
import pandas as pd
import numpy as np
pd.options.plotting.backend = "plotly"
np.random.seed(1)

df = pd.DataFrame(dict(
    a=np.random.normal(loc=1, scale=2, size=100),
    b=np.random.normal(loc=2, scale=1, size=100)
))
fig = df.boxplot()
fig.show()
```

### What about Cufflinks?

There also exists an independent third-party wrapper library around Plotly called [Cufflinks](https://github.com/santosjorge/cufflinks), which provides similar functionality (with an API closer to that of Pandas' default `matplotlib` backend) by adding a `.iplot()` method to Pandas dataframes, as it was developed before Pandas supported configurable backends. Issues and questions regarding Cufflinks should be [raised in the Cufflinks repository](https://github.com/santosjorge/cufflinks/issues/new).
