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
    description: How to cluster points in 3d with alpha shapes in plotly and Python
    display_as: 3d_charts
    language: python
    layout: base
    name: 3d Clustering
    order: 14
    permalink: python/3d-point-clustering/
    thumbnail: thumbnail/3d-clusters.jpg
---

<!-- #region {"deletable": true, "editable": true} -->
#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!
<!-- #endregion -->

<!-- #region {"deletable": true, "editable": true} -->
#### 3D Clustering with Alpha Shapes
<!-- #endregion -->

```python deletable=true editable=true
import plotly.plotly as py
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/alpha_shape.csv')
df.head()

scatter = dict(
    mode = "markers",
    name = "y",
    type = "scatter3d",
    x = df['x'], y = df['y'], z = df['z'],
    marker = dict( size=2, color="rgb(23, 190, 207)" )
)
clusters = dict(
    alphahull = 7,
    name = "y",
    opacity = 0.1,
    type = "mesh3d",
    x = df['x'], y = df['y'], z = df['z']
)
layout = dict(
    title = '3d point clustering',
    scene = dict(
        xaxis = dict( zeroline=False ),
        yaxis = dict( zeroline=False ),
        zaxis = dict( zeroline=False ),
    )
)
fig = dict( data=[scatter, clusters], layout=layout )
# Use py.iplot() for IPython notebook
py.iplot(fig, filename='3d point clustering')
```

<!-- #region {"deletable": true, "editable": true} -->
#### Reference
<!-- #endregion -->

<!-- #region {"deletable": true, "editable": true} -->
See https://plot.ly/python/reference/#mesh3d for more information regarding subplots!
<!-- #endregion -->

```python deletable=true editable=true
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade

import publisher
publisher.publish(
    '3d-clusters.ipynb', 'python/3d-point-clustering/', 'Python 3D Clustering | plotly',
    'How to cluster points in 3d with alpha shapes in plotly and Python',
    title= '3D Point Clustering in Python | plotly',
    name = '3d Clustering',
    has_thumbnail='true', thumbnail='thumbnail/3d-clusters.jpg',
    language='python',
    display_as='3d_charts', order=14,
    ipynb= '~notebook_demo/74')
```

```python deletable=true editable=true

```
