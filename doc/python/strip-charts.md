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
    description: Strip charts are like 1-dimensional jittered scatter plots.
    display_as: statistical
    language: python
    layout: base
    name: Strip Charts
    order: 14
    page_type: u-guide
    permalink: python/strip-charts/
    thumbnail: thumbnail/figure-labels.png
---

### Strip Charts with Plotly Express

[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/).

The `px.strip()` function will make strip charts using underlying `box` traces with the box hidden.

See also [box plots](/python/box-plots/) and [violin plots](/python/violin/).

```python
import plotly.express as px

df = px.data.tips()
fig = px.strip(df, x="total_bill", y="day")
fig.show()
```

Strip charts support [faceting](/python/facet-plots/) and [discrete color](/python/discrete-color/):

```python
import plotly.express as px

df = px.data.tips()
fig = px.strip(df, x="total_bill", y="time", color="sex", facet_col="day")
fig.show()
```

#### Reference

See [function reference for `px.strip()`](https://plotly.com/python-api-reference/generated/plotly.express.strip) for more information and chart attribute options!
