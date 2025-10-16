---
description: How to add LaTeX to python graphs.
---

### LaTeX Typesetting

Figure titles, axis labels and annotations all accept LaTeX directives for rendering mathematical formulas and notation, when the entire label is surrounded by dollar signs `$...$`. This rendering is handled by the [MathJax library](https://www.npmjs.com/package/mathjax?activeTab=versions), which must be loaded in the environment where figures are being rendered. MathJax is included by default in Jupyter-like environments. When embedding Plotly figures in other contexts it may be required to ensure that MathJax is separately loaded, for example via a `<script>` tag pointing to a content-delivery network (CDN). Versions 2 and 3 are supported.

```python
import plotly.express as px

fig = px.line(x=[1, 2, 3, 4], y=[1, 4, 9, 16], title=r'$\alpha_{1c} = 352 \pm 11 \text{ km s}^{-1}$')
fig.update_layout(
    xaxis_title=r'$\sqrt{(n_\text{c}(t|{T_\text{early}}))}$',
    yaxis_title=r'$d, r \text{ (solar radius)}$'
)
fig.show()
```

```python
import plotly.graph_objs as go

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4],
    y=[1, 4, 9, 16],
    name=r'$\alpha_{1c} = 352 \pm 11 \text{ km s}^{-1}$'
))
fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4],
    y=[0.5, 2, 4.5, 8],
    name=r'$\beta_{1c} = 25 \pm 11 \text{ km s}^{-1}$'
))
fig.update_layout(
    xaxis_title=r'$\sqrt{(n_\text{c}(t|{T_\text{early}}))}$',
    yaxis_title=r'$d, r \text{ (solar radius)}$'
)
fig.show()
```
