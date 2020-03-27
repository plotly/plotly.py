---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: "1.2"
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
    description:
      Cufflinks is a third-party wrapper library around Plotly, inspired by the Pandas .plot() API.
    display_as: file_settings
    language: python
    layout: base
    name: Cufflinks
    order: 31
    permalink: python/cufflinks/
    thumbnail: thumbnail/plotly-express.png
---

### Introduction

[Cufflinks](https://github.com/santosjorge/cufflinks) is a third-party wrapper library around Plotly, maintained by [Santos Jorge](https://github.com/santosjorge).

When you import cufflinks, all [Pandas](https://pandas.pydata.org/) data frames and series objects have a new method attached to them called `.iplot()` which has a similar API to Pandas' built-in `.plot()` method.

By passing the `asFigure=True` argument to `.iplot()`, Cufflinks works similarly to [Plotly Express](/python/plotly-express/), by returning [customizable `go.Figure` objects](/python/styling-plotly-express/) which are compatible with [Dash](https://dash.plot.ly)'s [`dcc.Graph` component](https://dash.plotly.com/dash-core-components/graph). Cufflinks also adds a `.figure()` method which has the same signature as `.iplot()` except that it has `asFigure=True` set as the default.

This page shows some high-level examples of how to use Cufflinks, and more examples and documentation are available in the [Cufflinks Github repository](https://github.com/santosjorge/cufflinks).

> Issues and questions regarding Cufflinks should be [raised in the Cufflinks repository](https://github.com/santosjorge/cufflinks/issues/new).

```python
import cufflinks as cf
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(1000, 2), columns=['A', 'B']).cumsum()
fig = df.iplot(asFigure=True, xTitle="The X Axis",
                    yTitle="The Y Axis", title="The Figure Title")
fig.show()
```

Cufflinks has a `datagen` module for generating demo data.

```python
import cufflinks as cf

df = cf.datagen.lines()
fig = df.iplot(asFigure=True)
fig.show()
df.head()
```

### Scatter Plots

```python
import cufflinks as cf
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(1000, 2), columns=['A', 'B']).cumsum()
fig = df.iplot(asFigure=True, x='A', y='B', mode='markers')
fig.show()
```

### Bar Charts

```python
import cufflinks as cf
import pandas as pd
df = pd.DataFrame(np.random.rand(10, 4), columns=['A', 'B', 'C', 'D'])
fig = df.iplot(asFigure=True, kind="bar")
fig.show()
```

### Histograms

```python
import cufflinks as cf
import pandas as pd
df = pd.DataFrame({'a': np.random.randn(1000) + 1,
                   'b': np.random.randn(1000),
                   'c': np.random.randn(1000) - 1})

fig = df.iplot(asFigure=True, kind="histogram")
fig.show()
```

### Box Plots

```python
import cufflinks as cf
import pandas as pd
df = pd.DataFrame({'a': np.random.randn(1000) + 1,
                   'b': np.random.randn(1000),
                   'c': np.random.randn(1000) - 1})

fig = df.iplot(asFigure=True, kind="box")
fig.show()
```

### Subplots

```python
import cufflinks as cf

df=cf.datagen.lines(4)
fig = df.iplot(asFigure=True, subplots=True, shape=(4,1), shared_xaxes=True, fill=True)
fig.show()
```

```python
import cufflinks as cf

df=cf.datagen.lines(4)
fig = df.iplot(asFigure=True, subplots=True, subplot_titles=True, legend=False)
fig.show()
```

### Line and Box Annotations

```python
import cufflinks as cf

df=cf.datagen.lines(4)
fig = df.iplot(asFigure=True, hline=[2,4], vline=['2015-02-10'])
fig.show()
```

```python
import cufflinks as cf

df=cf.datagen.lines(4)
fig = df.iplot(asFigure=True, hspan=[(-1,1),(2,5)])
fig.show()
```

```python
import cufflinks as cf

df=cf.datagen.lines(4)
fig = df.iplot(asFigure=True,
               vspan={'x0':'2015-02-15','x1':'2015-03-15',
                      'color':'rgba(30,30,30,0.3)','fill':True,'opacity':.4})
fig.show()
```

### More Examples

More documentation and examples for Cufflinks can be found in its [Github repository](https://github.com/santosjorge/cufflinks).
