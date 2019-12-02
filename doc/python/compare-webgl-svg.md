---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.7
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
    version: 3.6.5
  plotly:
    description: Comparing WebGL with Scattergl() to SVG with Scatter() in Python
      with Plotly.
    has_thumbnail: false
    language: python
    layout: base
    name: Comparing WebGL vs SVG
    page_type: example_index
    permalink: python/compare-webgl-svg/
    thumbnail: /images/static-image
---

### Comparing Scatter Plots with 75,000 Random Points


Now in Ploty you can implement WebGL with `Scattergl()` in place of `Scatter()` <br>
for increased speed, improved interactivity, and the ability to plot even more data!


### WebGL

```python
import plotly.graph_objects as go

import numpy as np
np.random.seed(1)

N = 75000

fig = go.Figure()
fig.add_trace(
    go.Scattergl(
        x = np.random.randn(N),
        y = np.random.randn(N),
        mode = 'markers',
        marker = dict(
            line = dict(
                width = 1,
                color = 'DarkSlateGrey')
        )
    )
)

fig.update_layout(title_text = 'WebGL')

fig.show()
```

### SVG

```python
import plotly.graph_objects as go

import numpy as np

N = 75000

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x = np.random.randn(N),
        y = np.random.randn(N),
        mode = 'markers',
        marker = dict(
            line = dict(
                width = 1,
                color = 'DarkSlateGrey')
        )
    )
)

fig.update_layout(title_text = 'SVG')

fig.show()
```

### References


For more information see <br>
`Scattergl()` : https://plot.ly/python/reference/#scattergl <br>
`Scatter()` : https://plot.ly/python/reference/#scatter
