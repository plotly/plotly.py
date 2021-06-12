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
    description: How to add LaTeX to python graphs.
    display_as: advanced_opt
    language: python
    layout: base
    name: LaTeX
    order: 5
    page_type: example_index
    permalink: python/LaTeX/
    thumbnail: thumbnail/latex.jpg
---

#### LaTeX Typesetting

Figure titles, axis labels and annotations all accept LaTeX directives for rendering mathematical formulas and notation, when the entire label is surrounded by dollar signs `$...$`. This rendering is handled by the [MathJax library](https://www.mathjax.org/) (version 2.7.5), which must be loaded in the environment where figures are being rendered. MathJax is included by default in Jupyter-like environments, but when embedding Plotly figures in other contexts it may be required to ensure that MathJax is separately loaded, for example via a `<script>` tag pointing to a content-delivery network (CDN).

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
