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
    display_name: Python 2
    language: python
    name: python2
  plotly:
    description: How to add webGL based text labels and annotations to plots in python
    display_as: advanced_opt
    has_thumbnail: false
    language: python
    layout: base
    name: WebGL Text and Annotations
    order: 2
    page_type: example_index
    permalink: python/webgl-text-and-annotations/
    thumbnail: thumbnail/webgl-text-and-annotations.jpg
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!!


### Heatmap with Annotations

```python
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.figure_factory import create_annotated_heatmap

n=250

y = [[i]*n for i in range(12)]
y = [item for sublist in y for item in sublist]

trace = dict(type='heatmap', z=np.random.randint(1, 10,(12, n)), colorscale = 'Viridis')
data=[trace]

# Here's the key part - Scattergl text!

data.append({'type': 'scattergl',
                    'mode': 'text',
                    'x': list(range(n))*12,
                    'y': y,
                    'text': np.random.choice(list('ATGC'), 12*250),
                    'textfont': {
                        'size': 20
                    }})

steps = [{'args': ['xaxis', {'range': [-0.5 + e, 30.5 + e]}], 'method': 'relayout'} for e in range(n-30)]

sliders = [dict(
    active = 0,
    steps = steps
)]

layout = dict(sliders=sliders)
layout['xaxis'] = {'range': [-0.5, 30.5]}

fig = dict(data=data, layout=layout)

py.iplot(fig, validate=False)
```

### Reference


See https://plot.ly/python/reference/#scattergl for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'webgl-text-and-annotations.ipynb', 'python/webgl-text-and-annotations/', 'WebGL Text and Annotations',
    'How to add webGL based text labels and annotations to plots in python',
    title = 'WebGL Text and Annotations | plotly',
    name = 'WebGL Text and Annotations',
    has_thumbnail='false', thumbnail='thumbnail/webgl-text-and-annotations.jpg',
    language='python',
    page_type='example_index', display_as='style_opt', order=2,
    ipynb= '~notebook_demo/219', uses_plotly_offline=False)
```

```python

```
