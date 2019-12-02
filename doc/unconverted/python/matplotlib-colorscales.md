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
    description: How to make Matplotlib Colorscales in Python with Plotly.
    display_as: advanced_opt
    language: python
    layout: base
    name: Matplotlib Colorscales
    order: 8
    page_type: example_index
    permalink: python/matplotlib-colorscales/
    thumbnail: thumbnail/colorbars.jpg
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!



### Formatting the Colormap


Parula Colormap can be downloaded from [here](https://github.com/BIDS/colormap/blob/master/parula.py)

```python
import parula as par
import matplotlib
from matplotlib import cm
import numpy as np

magma_cmap = matplotlib.cm.get_cmap('magma')
viridis_cmap = matplotlib.cm.get_cmap('viridis')
parula_cmap = par.parula_map

viridis_rgb = []
magma_rgb = []
parula_rgb = []
norm = matplotlib.colors.Normalize(vmin=0, vmax=255)

for i in range(0, 255):
       k = matplotlib.colors.colorConverter.to_rgb(magma_cmap(norm(i)))
       magma_rgb.append(k)

for i in range(0, 255):
       k = matplotlib.colors.colorConverter.to_rgb(viridis_cmap(norm(i)))
       viridis_rgb.append(k)

for i in range(0, 255):
       k = matplotlib.colors.colorConverter.to_rgb(parula_cmap(norm(i)))
       parula_rgb.append(k)

def matplotlib_to_plotly(cmap, pl_entries):
    h = 1.0/(pl_entries-1)
    pl_colorscale = []

    for k in range(pl_entries):
        C = map(np.uint8, np.array(cmap(k*h)[:3])*255)
        pl_colorscale.append([k*h, 'rgb'+str((C[0], C[1], C[2]))])

    return pl_colorscale

magma = matplotlib_to_plotly(magma_cmap, 255)
viridis = matplotlib_to_plotly(viridis_cmap, 255)
parula = matplotlib_to_plotly(parula_cmap, 255)
```

### Colorscales  for Heatmaps

```python
import plotly.plotly as py
import numpy as np
import os
import plotly.graph_objs as go
from plotly import tools

def heatmap_plot(colorscale, title):
    example_dir = os.path.join(os.path.dirname('__file__'), "examples")

    hist2d = np.loadtxt(os.path.join(example_dir, "hist2d.txt"))
    trace1 = go.Heatmap(z=hist2d, colorscale=colorscale, showscale=False)

    st_helens = np.loadtxt(os.path.join(example_dir,
                                        "st-helens_before-modified.txt.gz")).T
    trace2 = go.Heatmap(z=st_helens, colorscale=colorscale, y0=-5, x0=-5)

    dx = dy = 0.05
    y, x = np.mgrid[-5 : 5 + dy : dy, -5 : 10 + dx : dx]
    z = np.sin(x)**10 + np.cos(10 + y*x) + np.cos(x) + 0.2*y + 0.1*x
    trace3 = go.Heatmap(z=z, colorscale=colorscale, showscale=False)

    fig = tools.make_subplots(rows=1, cols=3, print_grid=False)
    fig.append_trace(trace1, 1, 1)
    fig.append_trace(trace2, 1, 2)
    fig.append_trace(trace3, 1, 3)
    fig['layout'].update(title=title)
    fig['layout']['xaxis2'].update(range=[0, 450])
    fig['layout']['yaxis2'].update(range=[0, 270])

    return fig
```

```python
py.iplot(heatmap_plot(colorscale=magma, title='MAGMA'))
```

```python
py.iplot(heatmap_plot(colorscale=viridis, title='VIRIDIS'))
```

```python
py.iplot(heatmap_plot(colorscale=parula, title='PARULA'))
```

### Colorscales for Trisurf Plots

```python
import plotly.plotly as py
from plotly.tools import FigureFactory as FF
import plotly.graph_objs as go
import numpy as np
from scipy.spatial import Delaunay

u = np.linspace(0, 2*np.pi, 24)
v = np.linspace(-1, 1, 8)
u,v = np.meshgrid(u, v)
u = u.flatten()
v = v.flatten()

tp = 1 + 0.5*v*np.cos(u/2.)
x = tp*np.cos(u)
y = tp*np.sin(u)
z = 0.5*v*np.sin(u/2.)

points2D = np.vstack([u, v]).T
tri = Delaunay(points2D)
simplices = tri.simplices

trace1 = FF.create_trisurf(x=x, y=y, z=z,
                           simplices=simplices, colormap=magma_rgb, plot_edges=False,
                           title='Magma Colorscale for Trisurf Plot')
py.iplot(trace1)

```

```python
trace2 = FF.create_trisurf(x=x, y=y, z=z,
                           simplices=simplices, colormap=viridis_rgb, plot_edges=False,
                           title='Viridis Colorscale for Trisurf Plot')
py.iplot(trace2)

```

```python
trace3 = FF.create_trisurf(x=x, y=y, z=z,
                          simplices=simplices, colormap=parula_rgb, plot_edges=False,
                          title='Parula Colorscale for Trisurf Plot')
py.iplot(trace3)

```

### Acknowledgment

Special thanks to [Stéfan van der Walt](https://github.com/stefanv) and [Nathaniel Smith](https://github.com/njsmith) for the statistics of colormaps.

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/csshref="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade

import publisher
publisher.publish(
    'matplotlib-colorscales.ipynb', 'python/matplotlib-colorscales/', 'Matplotlib Colorscales',
    'How to make Matplotlib Colorscales in Python with Plotly.',
    title = 'Python Matplotlib Colorscales | plotly',
    name = 'Matplotlib Colorscales',
    has_thumbnail='true', thumbnail='thumbnail/colorbars.jpg',
    language='python', page_type='example_index',
    display_as='style_opt', order=8,
    ipynb= '~notebook_demo/48')

```

```python

```
