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
    description: How to add marginal distribution plots.
    display_as: statistical
    language: python
    layout: base
    name: Marginal Distribution Plots
    order: 13
    page_type: u-guide
    permalink: python/marginal-plots/
    thumbnail: thumbnail/figure-labels.png
---

### Overview

Marginal distribution plots are small subplots above or to the right of a main plot, which show the distribution of data along only one dimension. Marginal distribution plot capabilities are built into various Plotly Express functions such as `scatter` and `histogram`. [Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/).

### Scatter Plot Marginals

The `marginal_x` and `marginal_y` arguments accept one of `"histogram"`, `"rug"`, `"box"`, or `"violin"` (see also how to create [histograms](/python/histograms/), [box plots](/python/box-plots/) and [violin plots](/python/violin-plots/) as the main figure). 

Marginal plots are linked to the main plot: try zooming or panning on the main plot.

Marginal plots also support hover, including per-point hover as with the rug-plot on the right: try hovering over the points on the right marginal plot.

```python
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_length", y="sepal_width", marginal_x="histogram", marginal_y="rug")
fig.show()
```

```python
import plotly.express as px
df = px.data.iris()
fig = px.density_heatmap(df, x="sepal_length", y="sepal_width", marginal_x="box", marginal_y="violin")
fig.show()
```

### Marginal Plots and Color

Marginal plots respect the `color` argument as well, and are linked to the respective legend elements. Try clicking on the legend items.

```python
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_length", y="sepal_width", color="species", 
                 marginal_x="box", marginal_y="violin",
                  title="Click on the legend items!")
fig.show()
```

### Marginal Plots on Histograms

[Histograms](/python/histograms/) are often used to show the distribution of a variable, and they also support marginal plots in Plotly Express, with the `marginal` argument:

```python
import plotly.express as px
df = px.data.iris()
fig = px.histogram(df, x="sepal_length", color="species", marginal="box")
fig.show()
```

Try hovering over the rug plot points to identify individual country values in the histogram below:

```python
import plotly.express as px
df = px.data.gapminder().query("year == 2007")
fig = px.histogram(df, x="lifeExp", color="continent", marginal="rug", hover_name="country",
                  title="Hover over the rug plot!")
fig.show()
```

### Marginal Plots and Facets

Marginal plots can be used in conjunction with [Plotly Express facets](/python/facet-plots/) so long as they go along different directions: 

```python
import plotly.express as px
df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", color="sex", facet_col="day",
                  marginal_x="box")
fig.show()
```

```python
import plotly.express as px
df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", color="sex", facet_row="time",
                  marginal_y="box")
fig.show()
```

```python
import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, x="total_bill", y="tip", color="sex", facet_col="day",
                  marginal="box")
fig.show()
```
