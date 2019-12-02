---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  plotly:
    description: How to add LaTeX to python graphs.
    display_as: advanced_opt
    language: python
    layout: base
    name: LaTeX
    order: 3
    page_type: u-guide
    permalink: python/LaTeX/
    thumbnail: thumbnail/latex.jpg
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Version Check
Plotly's python package is updated frequently. Run `pip install plotly --upgrade` to use the latest version.

```python
import plotly
plotly.__version__
```

#### LaTeX Typesetting

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[1, 4, 9, 16],
    name=r'$\alpha_{1c} = 352 \pm 11 \text{ km s}^{-1}$'
)
trace2 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[0.5, 2, 4.5, 8],
    name=r'$\beta_{1c} = 25 \pm 11 \text{ km s}^{-1}$'
)
data = [trace1, trace2]
layout = go.Layout(
    xaxis=dict(
        title=r'$\sqrt{(n_\text{c}(t|{T_\text{early}}))}$'
    ),
    yaxis=dict(
        title=r'$d, r \text{ (solar radius)}$'
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='latex')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'latex-typesetting.ipynb', 'python/LaTeX/', 'LaTeX',
    'How to add LaTeX to python graphs.',
    title = 'Python LaTeX | Examples | Plotly',
    has_thumbnail='true', thumbnail='thumbnail/latex.jpg',
    language='python',
    display_as='style_opt', order=3, ipynb='~notebook_demo/268')
```

```python

```
