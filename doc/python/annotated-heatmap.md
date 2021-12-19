---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.4
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
    version: 3.8.11
  plotly:
    description: How to make Annotated Heatmaps in Python with Plotly.
    display_as: scientific
    language: python
    layout: base
    name: Annotated Heatmaps
    order: 7
    page_type: u-guide
    permalink: python/annotated-heatmap/
    redirect_from: python/annotated_heatmap/
    thumbnail: thumbnail/ann_heat.jpg
---

### Annotated Heatmaps with Plotly Express

*New in v5.5*

As of version 5.5.0 of `plotly`, the **recommended way to [display annotated heatmaps is to use `px.imshow()`](/python/heatmaps/)** rather than the now-deprecated `create_annotated_heatmap` figure factory documented below for historical reasons.


#### Basic Annotated Heatmap for z-annotations

After creating a figure with `px.imshow`, you can add z-annotations with `.update_traces(texttemplate="%{z}")`.

```python
import plotly.express as px

z = [[.1, .3, .5, .7, .9],
     [1, .8, .6, .4, .2],
     [.2, 0, .5, .7, .9],
     [.9, .8, .4, .2, 0],
     [.3, .4, .5, .7, 1]]

fig = px.imshow(z, text_auto=True)
fig.show()
```

### Deprecated Figure Factory

The remaining examples show how to create Annotated Heatmaps with the deprecated `create_annotated_heatmap` [figure factory](/python/figure-factories/).


#### Simple Annotated Heatmap

```python
import plotly.figure_factory as ff

z = [[.1, .3, .5, .7, .9],
     [1, .8, .6, .4, .2],
     [.2, 0, .5, .7, .9],
     [.9, .8, .4, .2, 0],
     [.3, .4, .5, .7, 1]]

fig = ff.create_annotated_heatmap(z)
fig.show()
```

#### Custom Text and X & Y Labels
set `annotation_text` to a matrix with the same dimensions as `z`

> WARNING: this legacy figure factory requires the `y` array to be provided in reverse order, and will map the `z_text` to the `z` values in reverse order. **The use of the `px.imshow()` version below is highly recommended**

```python
import plotly.figure_factory as ff

z = [[.1, .3, .5],
     [1.0, .8, .6],
     [.6, .4, .2]]

x = ['Team A', 'Team B', 'Team C']
y = ['Game Three', 'Game Two', 'Game One']

z_text = [['Win', 'Lose', 'Win'],
          ['Lose', 'Lose', 'Win'],
          ['Win', 'Win', 'Lose']]

fig = ff.create_annotated_heatmap(z, x=x, y=y, annotation_text=z_text, colorscale='Viridis')
fig.show()
```

Here is the same figure using `px.imshow()`

```python
import plotly.express as px

x = ['Team A', 'Team B', 'Team C']
y = ['Game One', 'Game Two', 'Game Three']

z = [[.1, .3, .5],
     [1.0, .8, .6],
     [.6, .4, .2]]

z_text = [['Win', 'Lose', 'Win'],
          ['Lose', 'Lose', 'Win'],
          ['Win', 'Win', 'Lose']]

fig = px.imshow(z, x=x, y=y, color_continuous_scale='Viridis', aspect="auto")
fig.update_traces(text=z_text, texttemplate="%{text}")
fig.update_xaxes(side="top")
fig.show()
```

#### Annotated Heatmap with numpy

```python
import plotly.figure_factory as ff
import numpy as np
np.random.seed(1)

z = np.random.randn(20, 20)
z_text = np.around(z, decimals=2) # Only show rounded value (full value on hover)

fig = ff.create_annotated_heatmap(z, annotation_text=z_text, colorscale='Greys',
                                  hoverinfo='z')

# Make text size smaller
for i in range(len(fig.layout.annotations)):
    fig.layout.annotations[i].font.size = 8

fig.show()
```

Here is the same figure using `px.imshow()`

```python
import plotly.express as px
import numpy as np
np.random.seed(1)

z = np.random.randn(20, 20)

fig = px.imshow(z, text_auto=".2f", color_continuous_scale='Greys', aspect="auto")
fig.show()
```

#### Reference

For more info on Plotly heatmaps, see: https://plotly.com/python/reference/heatmap/.<br> For more info on using colorscales with Plotly see: https://plotly.com/python/heatmap-and-contour-colorscales/ <br>For more info on `ff.create_annotated_heatmap()`, see the [full function reference](https://plotly.com/python-api-reference/generated/plotly.figure_factory.create_annotated_heatmap.html#plotly.figure_factory.create_annotated_heatmap)
