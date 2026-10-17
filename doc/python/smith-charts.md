---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.4
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
    version: 3.8.11
  plotly:
    description: How to make Smith Charts with plotly.
    display_as: scientific
    language: python
    layout: base
    name: Smith Charts
    order: 20
    page_type: u-guide
    permalink: python/smith-charts/
    thumbnail: thumbnail/contourcarpet.jpg
---

*New in v5.4*

A [Smith Chart](https://en.wikipedia.org/wiki/Smith_chart) is a specialized chart for visualizing [complex numbers](https://en.wikipedia.org/wiki/Complex_number): numbers with both a real and imaginary part.


### Smith Charts with Plotly Express

[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/). With `px.scatter_smith`, each row of the DataFrame is represented as a marker on the Smith chart, with `real` and `imag` giving the real and imaginary parts of its normalized impedance.

```python
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    "real": [0.2, 0.5, 1.0, 2.0, 0.2, 0.5, 1.0, 2.0],
    "imag": [0.5, 1.0, 0.5, -1.0, -0.5, -1.0, 2.0, 0.0],
    "antenna": ["A", "A", "A", "A", "B", "B", "B", "B"],
})

fig = px.scatter_smith(df, real="real", imag="imag", color="antenna")
fig.show()
```

### Smith Charts with Plotly Graph Objects

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scattersmith(imag=[0.5, 1, 2, 3], real=[0.5, 1, 2, 3]))
fig.show()
```

### Smith Chart Subplots and Styling

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scattersmith(
    imag=[1],
    real=[1],
    marker_symbol='x',
    marker_size=30,
    marker_color="green",
    subplot="smith1"
))

fig.add_trace(go.Scattersmith(
    imag=[1],
    real=[1],
    marker_symbol='x',
    marker_size=30,
    marker_color="pink",
    subplot="smith2"
))

fig.update_layout(
    smith=dict(
        realaxis_gridcolor='red',
        imaginaryaxis_gridcolor='blue',
        domain=dict(x=[0,0.45])
    ),
    smith2=dict(
        realaxis_gridcolor='blue',
        imaginaryaxis_gridcolor='red',
        domain=dict(x=[0.55,1])
    )
)

fig.update_smiths(bgcolor="lightgrey")

fig.show()
```

#### Reference
See https://plotly.com/python/reference/scattersmith/ and https://plotly.com/python/reference/layout/smith/ for more information and chart attribute options!

```python

```
