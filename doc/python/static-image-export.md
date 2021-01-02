---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.6.0
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
    version: 3.7.6
  plotly:
    description: Plotly allows you to save static images of your plots. Save the image
      to your local computer, or embed it inside your Jupyter notebooks as a static
      image.
    display_as: file_settings
    language: python
    layout: base
    name: Static Image Export
    order: 6
    page_type: u-guide
    permalink: python/static-image-export/
    thumbnail: thumbnail/static-image-export.png
---

### Interactive vs Static Export

Plotly figures are interactive when viewed in a web browser: you can hover over data points, pan and zoom axes, and show and hide traces by clicking or double-clicking on the legend. You can export figures either to static image file formats like PNG, JPEG, SVG or PDF or you can [export them to HTML files which can be opened in a browser and remain interactive](/python/interactive-html-export/). This page explains how to do the former.


<!-- #region -->
#### Install Dependencies

Static image generation requires either [Kaleido](https://github.com/plotly/Kaleido) (recommended, supported as of `plotly` 4.9) or [orca](https://github.com/plotly/orca) (legacy as of `plotly` 4.9). The `kaleido` package can be installed using pip...
```
$ pip install -U kaleido
```

or conda.
```
$ conda install -c conda-forge python-kaleido
```

While Kaleido is now the recommended approach, image export can also be supported by the legacy [orca](https://github.com/plotly/orca) command line utility. See the [Orca Management](/python/orca-management/) section for instructions on installing, configuring, and troubleshooting orca.

<!-- #endregion -->

### Create a Figure

Now let's create a simple scatter plot with 100 random points of varying color and size.

```python
import plotly.graph_objects as go
import numpy as np
np.random.seed(1)

N = 100
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sz = np.random.rand(N) * 30

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode="markers",
    marker=go.scatter.Marker(
        size=sz,
        color=colors,
        opacity=0.6,
        colorscale="Viridis"
    )
))

fig.show()
```

### Write Image File

The `plotly.io.write_image` function is used to write an image to a file or file-like python object.  You can also use the `.write_image` graph object figure method.

Let's first create an output directory to store our images

```python
import os

if not os.path.exists("images"):
    os.mkdir("images")
```

If you are running this notebook live, click to [open the output directory](./images) so you can examine the images as they are written.


#### Raster Formats: PNG, JPEG, and WebP


plotly.py can output figures to several raster image formats including **PNG**, ...

```python
fig.write_image("images/fig1.png")
```

**JPEG**, ...

```python
fig.write_image("images/fig1.jpeg")
```

and **WebP**

```python
fig.write_image("images/fig1.webp")
```

#### Vector Formats: SVG and PDF...


plotly.py can also output figures in several vector formats including **SVG**, ...

```python
fig.write_image("images/fig1.svg")
```

**PDF**, ...

```python
fig.write_image("images/fig1.pdf")
```

and **EPS** (requires the poppler library)

```python
fig.write_image("images/fig1.eps")
```

**Note:** It is important to note that any figures containing WebGL traces (i.e. of type `scattergl`, `heatmapgl`, `contourgl`, `scatter3d`, `surface`, `mesh3d`, `scatterpolargl`, `cone`, `streamtube`, `splom`, or `parcoords`) that are exported in a vector format will include encapsulated rasters, instead of vectors, for some parts of the image.


### Image Export in Dash

[Dash](https://plotly.com/dash/) is the best way to build analytical apps in Python using Plotly figures. To run the app below, run `pip install dash`, click "Download" to get the code and run `python app.py`.

Get started  with [the official Dash docs](https://dash.plotly.com/installation) and **learn how to effortlessly [style](https://plotly.com/dash/design-kit/) & [deploy](https://plotly.com/dash/app-manager/) apps like this with <a class="plotly-red" href="https://plotly.com/dash/">Dash Enterprise</a>.**


```python hide_code=true
from IPython.display import IFrame
snippet_url = 'https://dash-gallery.plotly.host/python-docs-dash-snippets/'
IFrame(snippet_url + 'static-image-export', width='100%', height=630)
```

### Get Image as Bytes

The `plotly.io.to_image` function is used to return an image as a bytes object. You can also use the `.to_image` graph object figure method.

Let convert the figure to a **PNG** bytes object...

```python
img_bytes = fig.to_image(format="png")
```

and then display the first 20 bytes.

```python
img_bytes[:20]
```

#### Display Bytes as Image Using `IPython.display.Image`
A bytes object representing a PNG image can be displayed directly in the notebook using the `IPython.display.Image` class. This also works in the [Qt Console for Jupyter](https://qtconsole.readthedocs.io/en/stable/)!

```python
from IPython.display import Image
Image(img_bytes)
```

### Change Image Dimensions and Scale
In addition to the image format, the `to_image` and `write_image` functions provide arguments to specify the image `width` and `height` in logical pixels. They also provide a `scale` parameter that can be used to increase (`scale` > 1) or decrease (`scale` < 1) the physical resolution of the resulting image.

```python
img_bytes = fig.to_image(format="png", width=600, height=350, scale=2)
Image(img_bytes)
```

<!-- #region -->
### Specify Image Export Engine
If `kaleido` is installed, it will automatically be used to perform image export.  If it is not installed, plotly.py will attempt to use `orca` instead. The `engine` argument to the `to_image` and `write_image` functions can be used to override this default behavior.

Here is an example of specifying that orca should be used:
```python
fig.to_image(format="png", engine="orca")
```

And, here is an example of specifying that Kaleido should be used:
```python
fig.to_image(format="png", engine="kaleido")
```

<!-- #endregion -->

<!-- #region -->
### Image Export Settings (Kaleido)
Various image export settings can be configured using the `plotly.io.kaleido.scope` object. For example, the `default_format` property can be used to specify that the default export format should be `svg` instead of `png`

```python
import plotly.io as pio
pio.kaleido.scope.default_format = "svg"
```

Here is a complete listing of the available image export settings:

 - **`default_width`**: The default pixel width to use on image export.
 - **`default_height`**: The default pixel height to use on image export.
 - **`default_scale`**: The default image scale factor applied on image export.
 - **`default_format`**: The default image format used on export. One of `"png"`, `"jpeg"`, `"webp"`, `"svg"`, `"pdf"`, or `"eps"`.
 - **`mathjax`**: Location of the MathJax bundle needed to render LaTeX characters. Defaults to a CDN location. If fully offline export is required, set this to a local MathJax bundle.
 - **`topojson`**: Location of the topojson files needed to render choropleth traces. Defaults to a CDN location. If fully offline export is required, set this to a local directory containing the [Plotly.js topojson files](https://github.com/plotly/plotly.js/tree/master/dist/topojson).
 - **`mapbox_access_token`**: The default Mapbox access token.

<!-- #endregion -->

### Image Export Settings (Orca)
See the [Orca Management](/python/orca-management/) section for information on how to specify image export settings when using orca.

### Summary
In summary, to export high-quality static images from plotly.py, all you need to do is install the `kaleido` package and then use the `plotly.io.write_image` and `plotly.io.to_image` functions (or the `.write_image` and `.to_image` graph object figure methods).
