---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.17.1
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
    version: 3.13.3
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
$ pip install --upgrade kaleido
```
or with conda:
```
$ conda install -c conda-forge python-kaleido
```

It's also possible to generate static images using [Orca](https://github.com/plotly/orca), though support for Orca will be removed after September 2025. See the [Orca Management](/python/orca-management/) page for more details.

### Chrome

Kaleido uses Chrome for static image generation. Versions of Kaleido prior to v1 included Chrome. Kaleido v1 and later uses Chrome (or Chromium) if it can find a compatible version on the machine on which it's running. If you need to install Chrome for static image generation, Plotly provides a CLI.

Run `plotly_get_chrome` to install Chrome.

You can also install Chrome from within Python using `plotly.io.install_chrome()`

```python
import plotly.io as pio

pio.install_chrome()
```

See the **Additional Information on Browsers with Kaleido** section below for more details on browser compatibility for Kaleido.

<!-- #endregion -->

## Write Image to a File

Plotly figures have a `write_image` method to write a figure to a file. `write_image` supports PNG, JPEG, WebP, SVG, and PDF formats.

To export a figure using `write_image`, call `write_image` on the figure, and pass as an argument the filename where you want to save the figure. The file format is inferred from the extension:


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


### Specify a Format

In the earlier example, Plotly inferred the image format from the extension of the filename. You can also specify the format explicitly using the `format` parameter.

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

Here's the bytes object displayed using `IPython.display.Image`:

```python
from IPython.display import Image
Image(img_bytes)
```

## Specify Image Dimensions and Scale
In addition to the image format, the `to_image` and `write_image` functions provide arguments to specify the image `width` and `height` in logical pixels. They also provide a `scale` parameter that can be used to increase (`scale` > 1) or decrease (`scale` < 1) the physical resolution of the resulting image.

```python
img_bytes = fig.to_image(format="png", width=600, height=350, scale=2)
Image(img_bytes)
```

## Specify Image Export Engine

> The `engine` parameter, as well as Orca support, is deprecated in Plotly.py 6.1.0 and will be removed after September 2025.

If `kaleido` is installed, it will automatically be used to perform image export.  If it is not installed, plotly.py will attempt to use `orca` instead. The `engine` argument to the `to_image` and `write_image` functions can be used to override this default behavior.

Here is an example of specifying `orca` for the image export engine:
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

The following example uses the `write_image` function from  `plotly.io`. The function takes the figure or a `dict` representing a figure (as shown in the example) as its first argument.


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

## Image Export Settings (Kaleido)

As well as configuring height, width, and other settings by passing arguments when calling `write_image` and `to_image`, you can also set a single default to be used throughout the duration of the program.

### Available Settings

The following settings are available.

`default_width`: The default pixel width to use on image export.

`default_height`: The default pixel height to use on image export.

`default_scale`: The default image scale factor applied on image export.

`default_format`: The default image format used on export. One of "png", "jpeg", "webp", "svg", or "pdf". ("eps" support is deprecated and available with Kaleido v0 only)

`mathjax`: Location of the MathJax bundle needed to render LaTeX characters. Defaults to a CDN location. If fully offline export is required, set this to a local MathJax bundle.

`topojson`: Location of the topojson files needed to render choropleth traces. Defaults to a CDN location. If fully offline export is required, set this to a local directory containing the Plotly.js topojson files.

`mapbox_access_token`: The default Mapbox access token (Kaleido v0 only). Mapbox traces are deprecated. See the [MapLibre Migration](https://plotly.com/python/mapbox-to-maplibre/) page for more details.

### Set Defaults

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
# Example using deprecated `plotly.io.kaleido.scope`
pio.kaleido.scope.default_format = "jpeg"
~~~

### Additional Information on Browsers with Kaleido

When exporting images from Plotly.py, Kaleido will attempt to find a version of [Chrome](https://www.google.com/chrome/index.html) or [Chromium](https://www.chromium.org/getting-involved/download-chromium/) that it can use for the export. It checks in the operating system's PATH for executables with the following names: "chromium", "chromium-browser",  "chrome", "Chrome", "google-chrome" "google-chrome-stable", "Chrome.app", "Google Chrome", "Google Chrome.app", and "Google Chrome for Testing".

Kaleido will also check the following locations:

**Windows**

- r"c:\Program Files\Google\Chrome\Application\chrome.exe"
- f"c:\\Users\\{os.environ.get('USER', 'default')}\\AppData\\"
- "Local\\Google\\Chrome\\Application\\chrome.exe"

**Linux"**

- "/usr/bin/google-chrome-stable"
- "/usr/bin/google-chrome"
- "/usr/bin/chrome"

**Mac OS**

- "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

---

Most recent versions of Chrome or Chromium should work with Kaleido. When you run `plotly_get_chrome`, [the following Chrome version](https://github.com/plotly/choreographer/blob/main/choreographer/resources/last_known_good_chrome.json#L2C17-L2C30) is installed.

Other Chromium-based browsers may also work, though Kaleido won't discover them automatically. You can set a browser to use by setting the path to search using an environment variable called `BROWSER_PATH`. For example:

```
BROWSER_PATH=/Applications/Microsoft\ Edge.app/Contents/MacOS/Microsoft\ Edge
```
