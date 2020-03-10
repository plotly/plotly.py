---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: "1.1"
      jupytext_version: 1.1.1
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
    description: Getting Started with Plotly for Python.
    has_thumbnail: false
    language: python
    layout: base
    name: Getting Started with Plotly
    page_type: u-guide
    permalink: python/getting-started/
    redirect_from:
      - python/getting_started/
      - /python/pytables/
---

<!-- #region -->

### Overview

The plotly Python library ([plotly.py](https://plot.ly/python/)) is an interactive, [open-source](https://github.com/plotly/plotly.py) plotting library that supports over 40 unique chart types covering a wide range of statistical, financial, geographic, scientific, and 3-dimensional use-cases.

Built on top of the Plotly JavaScript library ([plotly.js](https://plot.ly/javascript/)), plotly.py enables Python users to create beautiful interactive web-based visualizations that can be displayed in Jupyter notebooks, saved to standalone HTML files, or served as part of pure Python-built web applications using Dash.

Thanks to deep integration with the [orca](https://github.com/plotly/orca) image export utility, plotly.py also provides great support for non-web contexts including desktop editors (e.g. QtConsole, Spyder, PyCharm) and static document publishing (e.g. exporting notebooks to PDF with high-quality vector images).

### Installation

plotly.py may be installed using pip...

```
$ pip install plotly==4.5.2
```

or conda.

```
$ conda install -c plotly plotly=4.5.2
```

This package contains everything you need to write figures to standalone HTML files.

> Note: **No internet connection, account, or payment is required to use plotly.py.** Prior to version 4, this library could operate in either an "online" or "offline" mode. The documentation tended to emphasize the online mode, where graphs get published to the Chart Studio web service. In version 4, all "online" functionality was removed from the `plotly` package and is now available as the separate, optional, `chart-studio` package (See below). **plotly.py version 4 is "offline" only, and does not include any functionality for uploading figures or data to cloud services.**

<!-- #endregion -->

```python
import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
fig.write_html('first_figure.html', auto_open=True)
```

<!-- #region -->

#### Jupyter Notebook Support

For use in the classic [Jupyter Notebook](https://jupyter.org/), install the `notebook` and `ipywidgets`
packages using pip...

```
$ pip install "notebook>=5.3" "ipywidgets>=7.2"
```

or conda.

```
$ conda install "notebook>=5.3" "ipywidgets>=7.2"
```

These packages contain everything you need to run a Jupyter notebook...

```
$ jupyter notebook
```

and display plotly figures inline using the notebook renderer...

<!-- #endregion -->

```python
import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
fig.show()
```

or using `FigureWidget` objects.

```python
import plotly.graph_objects as go
fig = go.FigureWidget(data=go.Bar(y=[2, 3, 1]))
fig
```

<!-- #region -->

See [_Displaying Figures in Python_](/python/renderers/) for more information on the renderers framework, and see [_Plotly FigureWidget Overview_](/python/figurewidget/) for more information on using `FigureWidget`.

#### JupyterLab Support (Python 3.5+)

For use in [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/), install the `jupyterlab` and `ipywidgets`
packages using pip...

```
$ pip install jupyterlab==1.2 "ipywidgets>=7.5"
```

or conda.

```
$ conda install jupyterlab=1.2
$ conda install "ipywidgets=7.5"
```

Then run the following commands to install the required JupyterLab extensions (note that this will require [`node`](https://nodejs.org/) to be installed):

```
# Avoid "JavaScript heap out of memory" errors during extension installation
# (OS X/Linux)
export NODE_OPTIONS=--max-old-space-size=4096
# (Windows)
set NODE_OPTIONS=--max-old-space-size=4096

# Jupyter widgets extension
jupyter labextension install @jupyter-widgets/jupyterlab-manager@1.1 --no-build

# jupyterlab renderer support
jupyter labextension install jupyterlab-plotly@1.5.2 --no-build

# FigureWidget support
jupyter labextension install plotlywidget@1.5.2 --no-build

# Build extensions (must be done to activate extensions since --no-build is used above)
jupyter lab build

# Unset NODE_OPTIONS environment variable
# (OS X/Linux)
unset NODE_OPTIONS
# (Windows)
set NODE_OPTIONS=
```

These packages contain everything you need to run JupyterLab...

```
$ jupyter lab
```

and display plotly figures inline using the `plotly_mimetype` renderer...

<!-- #endregion -->

```python
import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
fig.show()
```

or using `FigureWidget` objects.

```python
import plotly.graph_objects as go
fig = go.FigureWidget(data=go.Bar(y=[2, 3, 1]))
fig
```

<!-- #region -->

See [_Displaying Figures in Python_](/python/renderers/) for more information on the renderers framework, and see [_Plotly FigureWidget Overview_](/python/figurewidget/) for more information on using `FigureWidget`.

#### Static Image Export Support

plotly.py supports static image export using the `to_image` and `write_image`
functions in the `plotly.io` package. This functionality requires the
installation of the plotly [orca](https://github.com/plotly/orca) command line utility and the
[`psutil`](https://github.com/giampaolo/psutil) and [`requests`](https://2.python-requests.org/en/master/) Python packages.

> Note: The `requests` library is used to communicate between the Python process and a local orca server process, it is not used to communicate with any external services.

These dependencies can all be installed using conda:

```
$ conda install -c plotly plotly-orca psutil requests
```

Or, `psutil` and `requests` can be installed using pip...

```
$ pip install psutil requests
```

and orca can be installed according to the instructions in the [orca README](https://github.com/plotly/orca).

These packages contain everything you need to save figures as static images.

<!-- #endregion -->

```python
import plotly.graph_objects as go
fig = go.FigureWidget(data=go.Bar(y=[2, 3, 1]))
fig.write_image('figure.png')
```

<!-- #region -->

See [_Static Image Export in Python_](/python/static-image-export/) for more information on static image export.

#### Extended Geo Support

Some plotly.py features rely on fairly large geographic shape files. The county
choropleth figure factory is one such example. These shape files are distributed as a
separate `plotly-geo` package. This package can be installed using pip...

```
$ pip install plotly-geo==1.0.0
```

or conda.

```
$ conda install -c plotly plotly-geo=1.0.0
```

See [_USA County Choropleth Maps in Python_](https://plot.ly/python/county-choropleth/) for more information on the county choropleth figure factory.

#### Chart Studio Support

The `chart-studio` package can be used to upload plotly figures to Plotly's Chart
Studio Cloud or On-Prem services. This package can be installed using pip...

```
$ pip install chart-studio==1.0.0
```

or conda.

```
$ conda install -c plotly chart-studio=1.0.0
```

> **Note:** This package is optional, and if it is not installed it is not possible for figures to be uploaded to the Chart Studio cloud service.

### Where to next?

Now that you have everything installed, you are ready to start reading and running examples of [basic charts](/python/basic-charts/), [statistical charts](/python/statistical-charts/), [scientific charts](/python/scientific-charts/), [financial charts](/python/#financial-charts), [geographic charts and maps](/python/maps/), and [3-dimensional charts](/python/3d-charts/).

For a complete overview of all of the ways that figures can be created and updated, see the [_Plotly User Guide for Python_](/python/user-guide/).

For information on configuring figure layout options (e.g. axes, titles, legends, etc) and styling figures (e.g. colors, fonts, annotations, images, shapes, etc.), see [_Plotly Fundamentals_](/python/plotly-fundamentals).

For information on theming plotly figures, see [_Theming and templates with plotly for Python_](/python/templates/).

For information on all of the ways that plotly figures can be displayed, see [_Displaying plotly figures with plotly for Python_](/python/renderers/).

For the full searchable reference of every figure property, see the [_Python figure reference_](https://plot.ly/python/reference/).

For information on using Python to build web applications containing plotly figures, see the [_Dash User Guide_](https://dash.plot.ly/).

<!-- #endregion -->
