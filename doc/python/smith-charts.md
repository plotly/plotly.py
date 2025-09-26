---
description: How to make Smith Charts with plotly.
---
*New in v5.4*

A [Smith Chart](https://en.wikipedia.org/wiki/Smith_chart) is a specialized chart for visualizing [complex numbers](https://en.wikipedia.org/wiki/Complex_number): numbers with both a real and imaginary part.


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
See [https://plotly.com/python/reference/scattersmith/](reference/graph_objects/Scattersmith.md) and [https://plotly.com/python/reference/layout/smith/](reference/graph_objects/Layout.md#plotly.graph_objects.Layout.smith) for more information and chart attribute options!

```python

```
