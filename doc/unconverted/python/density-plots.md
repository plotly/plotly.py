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
    description: How to make a 2d density plot in python. Examples of density plots
      with kernel density estimations, custom color-scales, and smoothing.
    display_as: statistical
    language: python
    layout: base
    name: 2d Density Plots
    order: 7
    page_type: u-guide
    permalink: python/density-plots/
    thumbnail: thumbnail/density.gif
---

<!-- #region {"deletable": true, "editable": true} -->
#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by dowloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!
<!-- #endregion -->

<!-- #region {"deletable": true, "editable": true} -->
#### Version Check
Note: 2D Density Plots are available in version <b>2.0.0+</b><br>
Run  `pip install plotly --upgrade` to update your Plotly version
<!-- #endregion -->

```python deletable=true editable=true
import plotly
plotly.__version__
```

<!-- #region {"deletable": true, "editable": true} -->
#### 2D Histogram Contour Plot with Histogram Subplots
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import plotly.figure_factory as ff

import numpy as np

t = np.linspace(-1, 1.2, 2000)
x = (t**3) + (0.3 * np.random.randn(2000))
y = (t**6) + (0.3 * np.random.randn(2000))

colorscale = ['#7A4579', '#D56073', 'rgb(236,158,105)', (1, 1, 0.2), (0.98,0.98,0.98)]

fig = ff.create_2d_density(
    x, y, colorscale=colorscale,
    hist_color='rgb(255, 237, 222)', point_size=3
)

py.iplot(fig, filename='histogram_subplots')
```

<!-- #region {"deletable": true, "editable": true} -->
#### 2D Histogram Contour Plot with Slider Control
<!-- #endregion -->

<!-- #region {"deletable": true, "editable": true} -->
https://jsfiddle.net/plotlygraphs/y9sdy76h/4/embedded/result,js,html/
<!-- #endregion -->

<!-- #region {"deletable": true, "editable": true} -->
Add slider controls to 2d-density-plot plots with the <a href="https://github.com/plotly/postMessage-API" target="_blank">postMessage API</a>.

See the <a href="https://jsfiddle.net/plotlygraphs/y9sdy76h/4/" target="_blank">code on JSFiddle</a>.

Watch <a href="https://raw.githubusercontent.com/plotly/documentation/gh-pages/all_static/images/flight_conflicts.gif" target="_blank">the 5 second video</a> of how it works:
<!-- #endregion -->

<!-- #region {"deletable": true, "editable": true} -->
![IPython terminal](https://raw.githubusercontent.com/plotly/documentation/gh-pages/all_static/images/flight_conflicts.gif)
<!-- #endregion -->

<!-- #region {"deletable": true, "editable": true} -->
#### Reference
<!-- #endregion -->

```python deletable=true editable=true
help(ff.create_2d_density)
```

```python deletable=true editable=true
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'density-plots.ipynb', 'python/density-plots/', 'Python 2d Density Plots | plotly',
    'How to make a 2d density plot in python. Examples of density plots with kernel density estimations, custom color-scales, and smoothing.',
    title='Python 2d Density Plots | plotly',
    name='2d Density Plots',
    thumbnail='thumbnail/density.gif', language='python',
    has_thumbnail='true', display_as='statistical', order=7,
    ipynb= '~notebook_demo/25')
```

```python deletable=true editable=true

```
