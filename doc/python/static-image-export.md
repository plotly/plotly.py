---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.6
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

<!-- #region -->
### Static Image Export
It's possible to programmatically export figures as high quality static images while fully offline.

#### Install Dependencies
Static image generation requires the [orca](https://github.com/plotly/orca) commandline utility and the [psutil](https://github.com/giampaolo/psutil) and [requests](https://2.python-requests.org/en/master/) Python libraries. There are 3 general approach to installing these dependencies.

##### conda
Using the [conda](https://conda.io/docs/) package manager, you can install these dependencies in a single command:
```
$ conda install -c plotly plotly-orca psutil requests
```

**Note:** Even if you do not want to use conda to manage your Python dependencies, it is still useful as a cross platform tool for managing native libraries and command-line utilities (e.g. git, wget, graphviz, boost, gcc, nodejs, cairo, etc.).  For this use-case, start with [Miniconda](https://conda.io/miniconda.html) (~60MB) and tell the installer to add itself to your system `PATH`.  Then run `conda install plotly-orca` and the orca executable will be available system wide.

##### npm + pip
You can use the [npm](https://www.npmjs.com/get-npm) package manager to install `orca` (and its `electron` dependency), and then use pip to install `psutil`:

```
$ npm install -g electron@1.8.4 orca
$ pip install psutil requests
```

##### Standalone Binaries + pip
If you are unable to install conda or npm, you can install orca as a precompiled binary for your operating system. Follow the instructions in the orca [README](https://github.com/plotly/orca) to install orca and add it to your system `PATH`. Then use pip to install `psutil`.

```
$ pip install psutil requests
```
<!-- #endregion -->

### Create a Figure
Now let's create a simple scatter plot with 100 random points of variying color and size.

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


Orca can output figures to several raster image formats including **PNG**, ...

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


Orca can also output figures in several vector formats including **SVG**, ...

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

### Summary
In summary, to export high-quality static images from plotly.py, all you need to do is install orca, psutil, and requests and then use the `plotly.io.write_image` and `plotly.io.to_image` functions (or the `.write_image` and `.to_image` graph object figure methods).

If you want to know more about how the orca integration works, or if you need to troubleshoot an issue, please check out the [Orca Management](/python/orca-management/) section.
