---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.4
  kernelspec:
    display_name: Python 3 (ipykernel)
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
    version: 3.11.10
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

This page demonstrates how to export interactive Plotly figures to static image formats like PNG, JPEG, SVG, and PDF. If you want to export Plotly figures to HTML to retain interactivity, see the [Interactive HTML Export page](/python/interactive-html-export/)

<!-- #region -->
## Install Dependencies

### Kaleido

Static image generation requires [Kaleido](https://github.com/plotly/Kaleido).
Install Kaleido with pip:
```
$ pip install -U kaleido
```
or with conda:
```
$ conda install -c conda-forge python-kaleido
```

It's also possible to generate static images using [orca](https://github.com/plotly/orca), though support for orca will be removed after September 2025. See the [Orca Management](/python/orca-management/) page for more details.

### Chrome

Kaleido uses Chrome for static image generation. Versions of Kaleido prior to v1 included Chrome. Kaleido v1 and later uses Chrome that's available on the machine on which it's running. If you need to install Chrome for static image generation, Plotly provides a CLI.

Run `plotly_get_chrome` to install Chrome. 

You can also install Chrome from within Python using `plotly.io.install_chrome()`

```python
import plotly.io as pio

pio.install_chrome()
```
<!-- #endregion -->

## Write Image to a File

Plotly figures have a `write_image` method to write a figure to a file. `write_image` supports PNG, JPEG, WebP, SVG, and PDF. 

To export a figure using `write_image`, call `write_image` on the figure with the filename where you want to save the figure on the figure. The file format is inferred from the extension: 


### Raster Formats

**PNG** 
~~~python
import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, x='year', y='pop')
fig.write_image("fig1.png")
~~~

**JPEG**

~~~python
...
fig.write_image("images/fig1.jpeg")
~~~

**WebP**

~~~python
...
fig.write_image("images/fig1.webp")
~~~

### Vector Formats

**SVG**
~~~python
...
fig.write_image("images/fig1.svg")
~~~

**PDF**

~~~python
...
fig.write_image("images/fig1.pdf")
~~~

---

**EPS** (Kaleido<1.0.0)

Kaleido versions earlier than 1.0.0 also support **EPS** (requires the poppler library)

~~~python
...
fig.write_image("images/fig1.eps")
~~~


**Note:** Figures containing WebGL traces (i.e. of type `scattergl`, `contourgl`, `scatter3d`, `surface`, `mesh3d`, `scatterpolargl`, `cone`, `streamtube`, `splom`, or `parcoords`) that are exported in a vector format will include encapsulated rasters, instead of vectors, for some parts of the image.


### Specifying a Format

In the earlier example, Plotly inferred the image format from the extension of the filename. You can also specify this with the `format` parameter.

~~~python
import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, x='year', y='pop')
fig.write_image("fig1", format="png")
~~~



## Get Image as Bytes

As well as exporting to a file, Plotly figures also support conversion to a bytes object. 
To convert a figure to a **PNG** bytes object, call the figure's `to_image` method with a `format`

```python
import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, x='year', y='pop')

img_bytes = fig.to_image(format="png")
```

### Display Bytes as Image Using `IPython.display.Image`
A bytes object representing a PNG image can be displayed directly in the notebook using the `IPython.display.Image` class. This also works in the [Qt Console for Jupyter](https://qtconsole.readthedocs.io/en/stable/)!

```python
from IPython.display import Image
Image(img_bytes)
```

## Change Image Dimensions and Scale
In addition to the image format, the `to_image` and `write_image` functions provide arguments to specify the image `width` and `height` in logical pixels. They also provide a `scale` parameter that can be used to increase (`scale` > 1) or decrease (`scale` < 1) the physical resolution of the resulting image.

```python
img_bytes = fig.to_image(format="png", width=600, height=350, scale=2)
Image(img_bytes)
```

## Specify Image Export Engine

> The `engine` parameter is deprecated in Plotly.py 6.1.0 and will be removed after September 2025.

If `kaleido` is installed, it will automatically be used to perform image export.  If it is not installed, plotly.py will attempt to use `orca` instead. The `engine` argument to the `to_image` and `write_image` functions can be used to override this default behavior.

Here is an example of specifying that orca should be used:
~~~python
fig.to_image(format="png", engine="orca")
~~~

And, here is an example of specifying that Kaleido should be used:
~~~python
fig.to_image(format="png", engine="kaleido")
~~~


<!-- #region -->
## plotly.io Functions

Previous examples on this page access `write_image` and `to_image` as methods on Plotly Figure objects. This functionality is also available via the `plotly.io` subpackage.

The following example uses the `write_image` function from  `plotly.io`. The function takes the figure or a `dict` representing a figure (as shown in the example) as it's first argument.


~~~python
import plotly.io as pio


fig = dict({
    "data": [{"type": "bar",
              "x": [1, 2, 3],
              "y": [1, 3, 2]}],
    "layout": {"title": {"text": "A Figure Specified By Python Dictionary"}}
})

pio.write_image(fig, "fig.png")
~~~
<!-- #endregion -->

## Image Export Settings

As well as configuring height, width, and other settings by passing arguments when calling `write_image` and `to_image`, you can specify defaults to be used. 

### Available Settings

The following settings are availble. 

`default_width`: The default pixel width to use on image export.

`default_height`: The default pixel height to use on image export.

`default_scale`: The default image scale factor applied on image export.

`default_format`: The default image format used on export. One of "png", "jpeg", "webp", "svg", "pdf", or "eps" (Kaleido v1 only).

`mathjax`: Location of the MathJax bundle needed to render LaTeX characters. Defaults to a CDN location. If fully offline export is required, set this to a local MathJax bundle.

`topojson`: Location of the topojson files needed to render choropleth traces. Defaults to a CDN location. If fully offline export is required, set this to a local directory containing the Plotly.js topojson files.

`mapbox_access_token`: The default Mapbox access token.

### Configuring Defaults

Since Plotly.py 6.1, settings are available on `plotly.io.defaults`

To set the `default_format` to "jpeg":

~~~python
import plotly.io as pio
pio.defaults.default_format = "jpeg"
~~~

You can also access current defaults. To see the default value for height:

~~~python
import plotly.io as pio
pio.defaults.default_height
~~~

In earlier versions of Plotly.py, these settings are available on `plotly.io.kaleido.scope`. This is deprecated since version 6.1. Use `plotly.io.defaults` instead.

~~~python
import plotly.io as pio
pio.kaleido.scope.default_format = "jpeg"
~~~

