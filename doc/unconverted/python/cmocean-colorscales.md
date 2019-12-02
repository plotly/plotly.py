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
    description: How to make Cmocean Colorscales in Python with Plotly.
    display_as: advanced_opt
    language: python
    layout: base
    name: Cmocean Colorscales
    order: 22
    page_type: example_index
    permalink: python/cmocean-colorscales/
    thumbnail: thumbnail/colorbars.jpg
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


### cmocean
[cmocean](https://github.com/matplotlib/cmocean) is a package containing colormaps for commonly-used oceanographic variables. Below we provide a function to convert a cmocean colormap to a Plotly colorscale. Check out all of the cmocean colormaps below!


### Imports

```python
import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools

import cmocean

import numpy as np
import os
```

### Defining Colormaps

```python
import cmocean

def cmocean_to_plotly(cmap, pl_entries):
    h = 1.0/(pl_entries-1)
    pl_colorscale = []

    for k in range(pl_entries):
        C = map(np.uint8, np.array(cmap(k*h)[:3])*255)
        pl_colorscale.append([k*h, 'rgb'+str((C[0], C[1], C[2]))])

    return pl_colorscale
```

The examples data can be downloaded from [here.](https://github.com/plotly/documentation/blob/source-design-merge/_posts/python/style/cmocean/examples)

```python
# Plotting the colorscale.

example_dir = os.path.join(os.path.dirname('__file__'), "examples")
hist2d = np.loadtxt(os.path.join(example_dir, "hist2d.txt"))
st_helens = np.loadtxt(os.path.join(example_dir,
                                        "st-helens_before-modified.txt.gz")).T
dx = dy = 0.05
y, x = np.mgrid[-5 : 5 + dy : dy, -5 : 10 + dx : dx]
z = np.sin(x)**10 + np.cos(10 + y*x) + np.cos(x) + 0.2*y + 0.1*x

elem_len = [len(hist2d), len(st_helens), len(z)]
max_len = max(elem_len)

def colorscale_plot(colorscale, title):
    trace1 = go.Heatmap(z=hist2d, colorscale=colorscale, showscale=False)
    trace2 = go.Heatmap(z=st_helens, colorscale=colorscale, y0=-5, x0=-5)
    trace3 = go.Heatmap(z=z,colorscale=colorscale, showscale=False)

    fig = tools.make_subplots(rows=1, cols=3, print_grid=False)
    fig.append_trace(trace1, 1, 1)
    fig.append_trace(trace2, 1, 2)
    fig.append_trace(trace3, 1, 3)

    fig['layout'].update(title=title)
    fig['layout']['xaxis2'].update(range=[0, 450])
    fig['layout']['yaxis2'].update(range=[0, 270])

    return fig
```

### Thermal

```python
thermal = cmocean_to_plotly(cmocean.cm.thermal, max_len)
py.iplot(colorscale_plot(colorscale=thermal, title='Thermal'))
```

### Haline

```python
haline = cmocean_to_plotly(cmocean.cm.haline, max_len)
py.iplot(colorscale_plot(colorscale=haline, title='Haline'))
```

### Solar

```python
solar = cmocean_to_plotly(cmocean.cm.solar, max_len)
py.iplot(colorscale_plot(colorscale=solar, title='Solar'))
```

### Ice

```python
ice = cmocean_to_plotly(cmocean.cm.ice, max_len)
py.iplot(colorscale_plot(colorscale=ice, title='Ice'))
```

### Gray

```python
gray = cmocean_to_plotly(cmocean.cm.gray, max_len)
py.iplot(colorscale_plot(colorscale=gray, title='Gray'))
```

### Oxy

```python
oxy = cmocean_to_plotly(cmocean.cm.oxy, max_len)
py.iplot(colorscale_plot(colorscale=oxy, title='Oxy'))
```

### Deep

```python
deep = cmocean_to_plotly(cmocean.cm.deep, max_len)
py.iplot(colorscale_plot(colorscale=deep, title='Deep'))
```

### Dense

```python
dense = cmocean_to_plotly(cmocean.cm.dense, max_len)
py.iplot(colorscale_plot(colorscale=dense, title='Dense'))
```

### Algae

```python
algae = cmocean_to_plotly(cmocean.cm.algae, max_len)
py.iplot(colorscale_plot(colorscale=algae, title='Algae'))
```

### Matter

```python
matter = cmocean_to_plotly(cmocean.cm.matter, max_len)
py.iplot(colorscale_plot(colorscale=matter, title='Matter'))
```

### Turbid

```python
turbid = cmocean_to_plotly(cmocean.cm.turbid, max_len)
py.iplot(colorscale_plot(colorscale=turbid, title='Turbid'))
```

### Speed

```python
speed = cmocean_to_plotly(cmocean.cm.speed, max_len)
py.iplot(colorscale_plot(colorscale=speed, title='Speed'))
```

### Amp

```python
amp = cmocean_to_plotly(cmocean.cm.amp, max_len)
py.iplot(colorscale_plot(colorscale=amp, title='Amp'))
```

### Tempo

```python
tempo = cmocean_to_plotly(cmocean.cm.tempo, max_len)
py.iplot(colorscale_plot(colorscale=tempo, title='Tempo'))
```

### Phase

```python
phase = cmocean_to_plotly(cmocean.cm.phase, max_len)
py.iplot(colorscale_plot(colorscale=phase, title='Phase'))
```

### Balance

```python
balance = cmocean_to_plotly(cmocean.cm.balance, max_len)
py.iplot(colorscale_plot(colorscale=balance, title='Balance'))
```

### Delta

```python
delta = cmocean_to_plotly(cmocean.cm.delta, max_len)
py.iplot(colorscale_plot(colorscale=delta, title='Delta'))
```

### Curl

```python
curl = cmocean_to_plotly(cmocean.cm.curl, max_len)
py.iplot(colorscale_plot(colorscale=curl, title='Curl'))
```

### Reference
Learn more about Plotly colorscales here: [https://plot.ly/python/colorscales/](https://plot.ly/python/colorscales/)


### Acknowledgment
Special thanks to [Kristen Thyng](https://github.com/kthyng) for the statistics of colormaps.

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'cmocean.ipynb', 'python/cmocean-colorscales/', 'Cmocean Colorscales | plotly',
    'How to make Cmocean Colorscales in Python with Plotly.',
    title = 'Cmocean Colorscales | plotly',
    name = 'Cmocean Colorscales',
    has_thumbnail='true', thumbnail='thumbnail/colorbars.jpg',
    language='python', page_type='example_index',
    display_as='style_opt', order=22,
    ipynb= '~notebook_demo/52')
```

```python

```
