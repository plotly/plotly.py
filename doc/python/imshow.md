---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.0
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
    version: 3.7.3
  plotly:
    description: How to display image data in Python with Plotly.
    display_as: scientific
    has_thumbnail: true
    ipynb: ~notebook_demo/34
    language: python
    layout: base
    name: Imshow
    order: 3
    page_type: example_index
    permalink: python/imshow/
    thumbnail: thumbnail/imshow.jpg
    v4upgrade: true
---

This tutorial shows how to display and explore image data. If you would like
instead a logo or static image, use `go.layout.Image` as explained
[here](/python/images).

### Displaying RBG image data with px.imshow

`px.imshow` displays multichannel (RGB) or single-channel ("grayscale") image data.

```python
import plotly.express as px
import numpy as np
img_rgb = np.array([[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
                    [[0, 255, 0], [0, 0, 255], [255, 0, 0]]
                   ], dtype=np.uint8)
fig = px.imshow(img_rgb)
fig.show()
```

### Read image arrays from image files

In order to create a numerical array to be passed to `px.imshow`, you can use a third-party library like [PIL](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open), [scikit-image](https://scikit-image.org/docs/dev/user_guide/getting_started.html) or [opencv](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html). We show below how to open an image from a file with `skimage.io.imread`, and alternatively how to load a demo image from `skimage.data`.

```python
import plotly.express as px
from skimage import io
img = io.imread('https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Crab_Nebula.jpg/240px-Crab_Nebula.jpg')
fig = px.imshow(img)
fig.show()
```

```python
import plotly.express as px
from skimage import data
img = data.astronaut()
fig = px.imshow(img)
fig.show()
```

### Display single-channel 2D image as grayscale

For a 2D image, `px.imshow` uses a colorscale to map scalar data to colors. The default colorscale is the one of the active template (see [the tutorial on templates](/python/templates/)).

```python
import plotly.express as px
import numpy as np
img = np.arange(15**2).reshape((15, 15))
fig = px.imshow(img)
fig.show()
```

### Choose the colorscale to display a single-channel image


```python
import plotly.express as px
import numpy as np
img = np.arange(100).reshape((10, 10))
fig = px.imshow(img, color_continuous_scale='gray')
fig.show()
```

### Hiding the colorbar when displaying a single-channel image

See [the tutorial on coloraxis](/python/colorscales/#share-color-axis) for more details on coloraxis.

```python
import plotly.express as px
from skimage import data
img = data.camera()
fig = px.imshow(img, color_continuous_scale='gray')
fig.update_layout(coloraxis_showscale=False)
fig.show()
```

### Display multichannel image data with go.Image

It is also possible to use the `go.Image` trace from the low-level `graph_objects` API in order to display image data. Note that `go.Image` only accepts multichannel images. For single images, use [`go.Heatmap`](/python/heatmaps).

Note that the `go.Image` trace is different from the `go.layout.Image` class, which can be used for [adding background images or logos to figures](/python/images).

```python
import plotly.graph_objects as go
img_rgb = [[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
           [[0, 255, 0], [0, 0, 255], [255, 0, 0]]]
fig = go.Figure(go.Image(z=img_rgb))
fig.show()
```

### Defining the data range covered by the color range with zmin and zmax

The data range and color range are mapped together using the parameters `zmin` and `zmax`, which correspond respectively to the data values mapped to black `[0, 0, 0]` and white `[255, 255, 255]`, or to the extreme colors of the colorscale in the case on single-channel data.

For single-channel data, the defaults values of `zmin` and `zmax` used by `px.imshow` and `go.Heatmap` are the extrema of the data range. For multichannel data, `px.imshow` and `go.Image` use slightly different default values for `zmin` and `zmax`. For `go.Image`, the default value is `zmin=[0, 0, 0]` and `zmax=[255, 255, 255]`, no matter the data type. On the other hand, `px.imshow` adapts the default `zmin` and `zmax` to the data type:
- for integer data types, `zmin` and `zmax` correspond to the extreme values of the data type, for example 0 and 255 for `uint8`, 0 and 65535 for `uint16`, etc.
- for float numbers, the maximum value of the data is computed, and zmax is 1 if the max is smaller than 1, 255 if the max is smaller than 255, etc. (with higher thresholds 2**16 - 1 and 2**32 -1).

These defaults can be overriden by setting the values of `zmin` and `zmax`. For `go.Image`, `zmin` and `zmax` need to be given for all channels, whereas it is also possible to pass a scalar value (used for all channels) to `px.imshow`.

```python
import plotly.express as px
from skimage import data
img = data.astronaut()
# Increase contrast by clipping the data range between 50 and 200
fig = px.imshow(img, zmin=50, zmax=200)
# We customize the hovertemplate to show both the data and the color values
# See https://plot.ly/python/hover-text-and-formatting/#customize-tooltip-text-with-a-hovertemplate
fig.update_traces(hovertemplate="x: %{x} <br> y: %{y} <br> z: %{z} <br> color: %{color}")
fig.show()
```

```python
import plotly.express as px
from skimage import data
img = data.astronaut()
# Stretch the contrast of the red channel only, resulting in a more red image
fig = px.imshow(img, zmin=[50, 0, 0], zmax=[200, 255, 255])
fig.show()
```

### Ticks and margins around image data

```python
import plotly.express as px
from skimage import data
img = data.astronaut()
fig = px.imshow(img)
fig.update_layout(width=400, height=400, margin=dict(l=10, r=10, b=10, t=10))
fig.update_xaxes(showticklabels=False).update_yaxes(showticklabels=False)
fig.show()
```

### Combining image charts and other traces

```python
import plotly.express as px
import plotly.graph_objects as go
from skimage import data
img = data.camera()
fig = px.imshow(img, color_continuous_scale='gray')
fig.add_trace(go.Contour(z=img, showscale=False,
                         contours=dict(start=0, end=70, size=70, coloring='lines'),
                         line_width=2))
fig.add_trace(go.Scatter(x=[230], y=[100], marker=dict(color='red', size=16)))
fig.show()
```

### Displaying an image and the histogram of color values

```python
from plotly.subplots import make_subplots
from skimage import data
img = data.chelsea()
fig = make_subplots(1, 2)
# We use go.Image because subplots require traces, whereas px functions return a figure
fig.add_trace(go.Image(z=img), 1, 1)
for channel, color in enumerate(['red', 'green', 'blue']):
    fig.add_trace(go.Histogram(x=img[..., channel].ravel(), opacity=0.5,
                               marker_color=color, name='%s channel' %color), 1, 2)
fig.update_layout(height=400)
fig.show()
```

#### Reference
See https://plot.ly/python/reference/#image for more information and chart attribute options!

