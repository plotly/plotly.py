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
    description: Implement WebGL for increased speed, improved interactivity, and
      the ability to plot even more data!
    display_as: basic
    language: python
    layout: base
    name: WebGL vs SVG
    order: 15
    permalink: python/webgl-vs-svg/
    thumbnail: thumbnail/webgl.jpg
---

Here we show that it is possible to represent millions of points with WebGL.
For larger datasets, or for a clearer visualization of the density of points,
it is also possible to use [datashader](/python/datashader/).

#### Compare WebGL and SVG
Checkout [this notebook](https://plot.ly/python/compare-webgl-svg) to compare WebGL and SVG scatter plots with 75,000 random data points

#### WebGL with Plotly Express

The `rendermode` argument to supported Plotly Express functions can be used to enable WebGL rendering.

Here is an example that creates a 100,000 point scatter plot using Plotly Express with WebGL rendering enabled.

```python
import plotly.express as px

import pandas as pd
import numpy as np
np.random.seed(1)

N = 100000

df = pd.DataFrame(dict(x=np.random.randn(N),
                       y=np.random.randn(N)))

fig = px.scatter(df, x="x", y="y", render_mode='webgl')

fig.update_traces(marker_line=dict(width=1, color='DarkSlateGray'))

fig.show()
```

#### WebGL with 100,000 points

The `Scattergl` trace type can be used to create a WebGL enabled scatter plot.

```python
import plotly.graph_objects as go

import numpy as np

N = 100000

# Create figure
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

fig.show()
```

#### WebGL with 1 Million Points

```python
import plotly.graph_objects as go

import numpy as np

N = 1000000

# Create figure
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

fig.show()
```

#### WebGL with many traces

```python
import plotly.graph_objects as go

import numpy as np

fig = go.Figure()

trace_num = 10
point_num = 5000
for i in range(trace_num):
    fig.add_trace(
        go.Scattergl(
                x = np.linspace(0, 1, point_num),
                y = np.random.randn(point_num)+(i*5)
        )
    )

fig.update_layout(showlegend=False)

fig.show()
```

### Reference

See https://plot.ly/python/reference/#scattergl for more information and chart attribute options!
