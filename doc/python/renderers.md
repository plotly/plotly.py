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
    description: Displaying Figures from Python
    display_as: file_settings
    language: python
    name: Displaying Figures
    page_type: example_index
    layout: base
    permalink: python/renderers/
    redirect_from: python/offline/
    thumbnail: thumbnail/displaying-figures.png
    order: 1
---

### Displaying plotly figures
This section covers the many ways to display plotly figures from Python.  At the highest level, there are three general approaches:

 1. Using the renderers framework in the context of a script or notebook
 2. Using Dash in a web app context
 3. Using a `FigureWidget` in an ipywidgets context

Each of these approaches is discussed below.

### Displaying figures using the renderers framework

The renderers framework is a flexible approach for displaying plotly figures in a variety of contexts.  To display a figure using the renderers framework, you call the `.show` method on a graph object figure, or pass the figure to the `plotly.io.show` function. With either approach, plotly.py will display the figure using the current default renderer(s).

```python
import plotly.graph_objects as go
fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Figure Displayed with fig.show()"
)
fig.show()
```

In most situations, you can omit the call to `.show()` and allow the figure to display itself.

```python
import plotly.graph_objects as go
fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Figure Displaying Itself"
)
fig
```

> To be precise, figures will display themselves using the current default renderer when the two following conditions are true. First, the last expression in a cell must evaluates to a figure. Second, plotly.py must be running from within an IPython kernel.

**In many contexts, an appropriate renderer will be chosen automatically and you will not need to perform any additional configuration.** These contexts include the classic Jupyter Notebook, JupyterLab (provided the `jupyterlab-plotly` JupyterLab extension is installed), Visual Studio Code notebooks, Colab, Kaggle notebooks, Azure notebooks, and the Python interactive shell.  Additional contexts are supported by choosing a compatible renderer including the IPython console, QtConsole, Spyder, and more.

Next, we will show how to configure the default renderer.  After that, we will describe all of the built-in renderers and discuss why you might choose to use each one.

> Note: The renderers framework is a generalization of the `plotly.offline.iplot` and `plotly.offline.plot` functions that were the recommended way to display figures prior to plotly.py version 4.  These functions have been reimplemented using the renderers framework and are still supported for backward compatibility, but they will not be discussed here.

#### Setting the default renderer
The current and available renderers are configured using the `plotly.io.renderers` configuration object.  Display this object to see the current default renderer and the list of all available renderers.

```python
import plotly.io as pio
pio.renderers
```

The default renderer that you see when you display `pio.renderers` might be different than what is shown here.  This is because plotly.py attempts to autodetect an appropriate renderer at startup.  You can change the default renderer by assigning the name of an available renderer to the `pio.renderers.default` property.  For example, to switch to the `'browser'` renderer, which opens figures in a tab of the default web browser, you would run the following.

> Note: Default renderers persist for the duration of a single session, but they do not persist across sessions. If you are working in an IPython kernel, this means that default renderers will persist for the life of the kernel, but they will not persist across kernel restarts.

```python
import plotly.io as pio
pio.renderers.default = "browser"
```

It is also possible to set the default renderer using a system environment variable.  At startup, plotly.py checks for the existence of an environment variable named `PLOTLY_RENDERER`.  If this environment variable is set to the name of an available renderer, this renderer is set as the default.

#### Overriding the default renderer
It is also possible to override the default renderer temporarily by passing the name of an available renderer as the `renderer` keyword argument to the `.show` method.  Here is an example of displaying a figure using the `svg` renderer (described below) without changing the default renderer.

```python
import plotly.graph_objects as go
fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Figure Displayed with the 'svg' Renderer"
)
fig.show(renderer="svg")
```

#### The built-in renderers
In this section, we will describe the built-in renderers so that you can choose the one(s) that best suit your needs.

##### Interactive renderers
Interactive renderers display figures using the Plotly.js JavaScript library and are fully interactive, supporting pan, zoom, hover tooltips, etc.

###### `notebook`
This renderer is intended for use in the classic [Jupyter Notebook](https://jupyter.org/install.html) (not JupyterLab).  The full Plotly.js JavaScript library bundle is added to the notebook the first time a figure is rendered, so this renderer will work without an internet connection.

This renderer is a good choice for notebooks that will be exported to HTML files (Either using [nbconvert](https://nbconvert.readthedocs.io/en/latest/) or the "Download as HTML" menu action) because the exported HTML files will work without an internet connection.

> Note: Adding the Plotly.js bundle to the notebook does add a few megabytes to the notebook size, so if you can count on having an internet connection you may want to consider the `notebook_connected` renderer.

###### `notebook_connected`
This renderer is the same as `notebook`, except the Plotly.js JavaScript library bundle is loaded from an online CDN location.  This saves a few megabytes in notebook size, but an internet connection is required in order to display figures that are rendered this way.

This renderer is a good choice for notebooks that will be shared with [nbviewer](https://nbviewer.jupyter.org/) since users must have an active internet connection to access nbviewer in the first place.

###### `kaggle` and `azure`
These are aliases for `notebook_connected` because this renderer is a good choice for use with [Kaggle kernels](https://www.kaggle.com/docs/kernels) and [Azure Notebooks](https://notebooks.azure.com/).

###### `colab`
This is a custom renderer for use with [Google Colab](https://colab.research.google.com).

###### `browser`
This renderer will open a figure in a browser tab using the default web browser.  This renderer can only be used when the Python kernel is running locally on the same machine as the web browser, so it is not compatible with Jupyter Hub or online notebook services.

> Implementation Note 1: The "default browser" is the browser that is chosen by the Python [`webbrowser`](https://docs.python.org/3.7/library/webbrowser.html) module.

> Implementation Note 2: The `browser` renderer works by setting up a single use local webserver on a local port. Since the webserver is shut down as soon as the figure is served to the browser, the figure will not be restored if the browser is refreshed.

###### `firefox`, `chrome`, and `chromium`
These renderers are the same as the `browser` renderer, but they force the use of a particular browser.

###### `iframe` and `iframe_connected`
These renderers write figures out as standalone HTML files and then display [`iframe`](https://www.w3schools.com/html/html_iframe.asp) elements that reference these HTML files. The `iframe` renderer will include the Plotly.js JavaScript bundle in each HTML file that is written, while the `iframe_connected` renderer includes only a reference to an online CDN location from which to load Plotly.js.  Consequently, the `iframe_connected` renderer outputs files that are smaller than the `iframe` renderer, but it requires an internet connection while the `iframe` renderer can operate offline.

This renderer may be useful when working with notebooks than contain lots of large figures.  When using the `notebook` or `notebook_connected` renderer, all of the data for all of the figures in a notebook are stored inline in the notebook itself. If this would result in a prohibitively large notebook size, an `iframe` or `iframe_connected` renderer could be used instead. With the iframe renderers, the figure data are stored in the individual HTML files rather than in the notebook itself, resulting in a smaller notebook size.

> Implementation Note: The HTML files written by the iframe renderers are stored in a subdirectory named `iframe_figures`.  The HTML files are given names based on the execution number of the notebook cell that produced the figure. This means that each time a notebook kernel is restarted, any prior HTML files will be overwritten.  This also means that you should not store multiple notebooks using an iframe renderer in the same directory, because this could result in figures from one notebook overwriting figures from another notebook.


###### `plotly_mimetype`

The `plotly_mimetype` renderer creates a specification of the plotly figure (called a MIME-type bundle), and requests that the current user interface displays it. User interfaces that support this renderer include [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) (requires the [`jupyterlab-plotly`](https://www.npmjs.com/package/jupyterlab-plotly) extension), [nteract](https://nteract.io/), and the Visual Studio Code [notebook interface](https://code.visualstudio.com/docs/python/jupyter-support).

###### `jupyterlab`, `nteract`, and `vscode`
These are aliases for `plotly_mimetype` since this renderer is a good choice when working in JupyterLab, nteract, and the Visual Studio Code notebook interface.

##### Static image renderers
A set of renderers is provided for displaying figures as static images.  These renderers all rely on the orca static image export utility. See the [Static Image Export](https://plot.ly/python/static-image-export/) page for more information on getting set up with orca.

###### `png`, `jpeg`, and `svg`
These renderers display figures as static PNG, JPEG, and SVG images respectively.  These renderers are useful for user interfaces that do not support inline HTML output, but do support inline static images.  Examples include the [QtConsole](https://qtconsole.readthedocs.io/en/stable/), [Spyder](https://www.spyder-ide.org/), and the PyCharm [notebook interface](https://www.jetbrains.com/help/pycharm/jupyter-notebook-support.html).

```python
import plotly.graph_objects as go
fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Figure Displayed with the 'png' Renderer"
)
fig.show(renderer="png")
```

###### `pdf`
This renderer displays figures as static PDF files. This is especially useful for notebooks that will be exported to PDF files using the LaTeX export capabilities of nbconvert.

##### Other renderers
Other miscellaneous renderers

###### `json`
In editors that support it (JupyterLab, nteract, and the Visual Studio Code notebook interface), this renderer displays the JSON representation of a figure in a collapsible interactive tree structure.  This can be very useful for examining the structure of complex figures

##### Multiple renderers
You can specify that multiple renderers should be used by joining their names on `"+"` characters.  This is useful when writing code that needs to support multiple contexts.  For example, if a notebook specifies a default renderer string of  `"notebook+plotly_mimetype+pdf"`then this notebook would be able to run in the classic Jupyter Notebook, in JupyterLab, and it would support being exported to PDF using nbconvert.

#### Customizing built-in renderers
Most built-in renderers have configuration options to customize their behavior.  To view a description of a renderer, including its configuration options, access the renderer object using dictionary-style key lookup on the `plotly.io.renderers` configuration object and then display it.  Here is an example of accessing and displaying the `png` renderer.

```python
import plotly.io as pio
png_renderer = pio.renderers["png"]
png_renderer
```

From this output, you can see that the `png` renderer supports 3 properties: `width`, `height`, and `scale`.  You can customize these properties by assigning new values to them.

Here is an example that customizes the `png` renderer to change the resulting image size, sets the `png` renderer as the default, and then displays a figure.

```python
import plotly.io as pio
png_renderer = pio.renderers["png"]
png_renderer.width = 500
png_renderer.height = 500

pio.renderers.default = "png"

import plotly.graph_objects as go
fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Figure Displayed with the 'png' Renderer"
)
fig.show()
```

You can also override the values of renderer parameters temporarily by passing them as keyword arguments to the `.show` method.  For example

```python
import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Bar(y=[2, 1, 3])],
    layout_title_text="A Figure Displayed with the 'png' Renderer"
)
fig.show(renderer="png", width=800, height=300)
```

### Displaying figures using Dash
Dash is a Python framework for building web applications, and it provides built-in support for displaying Plotly figures. See the [Dash User Guide](https://dash.plot.ly/) for more information.

It is important to note that Dash does not use the renderers framework discussed above, so you should not use the `.show` figure method or the `plotly.io.show` function inside Dash applications.

## Displaying figures using ipywidgets
Plotly figures can be displayed in [ipywidgets](https://ipywidgets.readthedocs.io/en/stable/) contexts using `plotly.graph_objects.FigureWidget` objects.  `FigureWidget` is a figure graph object (Just like `plotly.graph_objects.Figure`) so you can add traces to it and update it just like a regular `Figure`.  But `FigureWidget` is also an ipywidgets object, which means that you can display it alongside other ipywidgets to build user interfaces right in the notebook.  See the [Plotly FigureWidget Overview](https://plot.ly/python/figurewidget/) for more information on integrating plotly figures with ipywidgets.

It is important to note that `FigureWidget` does not use the renderers framework discussed above, so you should not use the `.show` figure method or the `plotly.io.show` function on `FigureWidget` objects.
