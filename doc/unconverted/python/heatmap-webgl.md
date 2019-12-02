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
    description: How to make webGL based heatmaps in Python with Plotly.
    display_as: scientific
    language: python
    layout: base
    name: WebGL Heatmaps
    order: 4
    page_type: u-guide
    permalink: python/heatmap-webgl/
    thumbnail: thumbnail/heatmap-webgl.jpg
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!
#### Version Check
Plotly's python package is updated frequently. Run pip install plotly --upgrade to use the latest version.

```python
import plotly
plotly.__version__
```

#### Imports

```python
import plotly.plotly as py

import requests
from PIL import Image
from io import BytesIO
```

### Create a HeatmapGL from an Image
Process the image for generating heatmap:

```python
image_url = 'https://images.plot.ly/plotly-documentation/images/heatmap-galaxy.jpg'

response = requests.get(image_url)
img = Image.open(BytesIO(response.content))
img
```

```python
arr = np.array(img)
z_data = []

for i in range(500):
    k = []
    for j in range(500):
        k.append(sum(arr[i][j]))
    z_data.append(k)
```

Create the WebGL Heatmap

```python
trace = dict(type='heatmapgl', z=z_data, colorscale='Picnic')
data = [trace]

layout = dict(width=700, height=700)
fig = dict(data=data, layout=layout)
py.iplot(fig, filename='basic heatmapgl')
```

#### Reference
See https://plot.ly/python/reference/#heatmapgl for more information and chart attribute options!


```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/csshref="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

import publisher
publisher.publish(
    'heatmap-webgl.ipynb', 'python/heatmap-webgl/', 'WebGL based Heatmaps | plotly',
    'How to make webGL based heatmaps in Python with Plotly.',
    title = 'Python Heatmaps WebGL | plotly',
    name = 'WebGL Heatmaps',
    has_thumbnail='true', thumbnail='thumbnail/heatmap-webgl.jpg',
    language='python',
    display_as='scientific', order=4,
    ipynb= '~notebook_demo/34')
```

```python

```
