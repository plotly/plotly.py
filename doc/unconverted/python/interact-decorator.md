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
    description: Use the Interact decorator with go.FigureWidget
    display_as: chart_events
    language: python
    layout: base
    name: Use Interact decorator with FigureWidget
    order: 4
    permalink: python/interact-decorator/
    thumbnail: thumbnail/figurewidget-interact.gif
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Interact
Here is a simple example of using the `interact` decorator from ipywidgets to create a simple set of widgets to control the parameters of a plot.

```python
import plotly.graph_objs as go

import numpy as np
from ipywidgets import interact
```

First we'll create an empty figure, and add an empty scatter trace to it.

```python
fig = go.FigureWidget()
scatt = fig.add_scatter()
fig
```

<img src='https://raw.githubusercontent.com/michaelbabyn/plot_data/master/empty_fw.png'>


Then, write an update function that inputs the frequency factor (`a`) and phase factor (`b`) and sets the `x` and `y` properties of the scatter trace.  This function is decorated with the `interact` decorator from the `ipywidgets` package. The decorator parameters are used to specify the ranges of parameters that we want to sweep over. See http://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html for more details.

```python
xs=np.linspace(0, 6, 100)

@interact(a=(1.0, 4.0, 0.01), b=(0, 10.0, 0.01), color=['red', 'green', 'blue'])
def update(a=3.6, b=4.3, color='blue'):
    with fig.batch_update():
        scatt.x=xs
        scatt.y=np.sin(a*xs-b)
        scatt.line.color=color
```

<img src='https://raw.githubusercontent.com/michaelbabyn/plot_data/master/interact_figurewidget.gif'>


#### Reference


See [these Jupyter notebooks](https://github.com/jonmmease/plotly_ipywidget_notebooks) for even more FigureWidget examples.

```python
help(go.FigureWidget)
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade

import publisher
publisher.publish(
    'Interact.ipynb', 'python/interact-decorator/', 'Use the Interact decorator with go.FigureWidget',
    'Use the Interact decorator with go.FigureWidget',
    title = 'Use Interact decorator with FigureWidget',
    name = 'Use Interact decorator with FigureWidget',
    has_thumbnail='true', thumbnail='thumbnail/zoom.jpg',
    language='python', page_type='example_index',
    display_as='chart_events', order=4,
    ipynb= '~notebook_demo/254')
```

```python

```
