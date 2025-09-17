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
    description: This section covers the low-level details of how plotly.py uses orca
      to perform static image generation.
    display_as: file_settings
    language: python
    layout: base
    name: Orca Management
    order: 9
    permalink: python/orca-management/
    thumbnail: thumbnail/orca-management.png
---

> Orca support in Plotly.py is deprecated and will be removed after September 2025. See the [Static Image Export page](static-image-export.md) for details on using Kaleido for static image generation.

### Overview
This section covers the lower-level details of how plotly.py can use orca to perform static image generation.

Please refer to the [Static Image Export](static-image-export.md) section for general information on creating static images from plotly.py figures.

### What is orca?
Orca is an [Electron](https://electronjs.org/) application that inputs plotly figure specifications and converts them into static images.  Orca can run as a command-line utility or as a long-running server process. In order to provide the fastest possible image export experience, plotly.py launches orca in server mode, and communicates with it over a local port. See https://github.com/plotly/orca for more information.

By default, plotly.py launches the orca server process the first time an image export operation is performed, and then leaves it running until the main Python process exits. Because of this, the first image export operation in an interactive session will typically take a couple of seconds, but then all subsequent export operations will be significantly faster, since the server is already running.

### Installing orca
There are 3 general approaches to installing orca and its Python dependencies.

##### conda
Using the [conda](https://conda.io/docs/) package manager, you can install these dependencies in a single command:
<!-- #raw -->
$ conda install -c plotly plotly-orca==1.2.1 psutil requests
<!-- #endraw -->

**Note:** Even if you do not want to use conda to manage your Python dependencies, it is still useful as a cross platform tool for managing native libraries and command-line utilities (e.g. git, wget, graphviz, boost, gcc, nodejs, cairo, etc.).  For this use-case, start with [Miniconda](https://conda.io/miniconda.html) (~60MB) and tell the installer to add itself to your system `PATH`.  Then run `conda install plotly-orca==1.2.1` and the orca executable will be available system wide.

##### npm + pip
You can use the [npm](https://www.npmjs.com/get-npm) package manager to install `orca` (and its `electron` dependency), and then use pip to install `psutil`:

<!-- #raw -->
$ npm install -g electron@1.8.4 orca
$ pip install psutil requests
<!-- #endraw -->

##### Standalone Binaries + pip
If you are unable to install conda or npm, you can install orca as a precompiled binary for your operating system. Follow the instructions in the orca [README](https://github.com/plotly/orca) to install orca and add it to your system `PATH`. Then use pip to install `psutil`.

<!-- #raw -->
$ pip install psutil requests
<!-- #endraw -->

<!-- #region -->
### Install orca on Google Colab
```
!pip install plotly>=4.7.1
!wget https://github.com/plotly/orca/releases/download/v1.2.1/orca-1.2.1-x86_64.AppImage -O /usr/local/bin/orca
!chmod +x /usr/local/bin/orca
!apt-get install xvfb libgtk2.0-0 libgconf-2-4
```

Once this is done you can use this code to make, show and export a figure:

```python
import plotly.graph_objects as go
fig = go.Figure( go.Scatter(x=[1,2,3], y=[1,3,2] ) )
fig.write_image("fig1.svg")
fig.write_image("fig1.png")
```

The files can then be downloaded with:

```python
from google.colab import files
files.download('fig1.svg')
files.download('fig1.png')
```
<!-- #endregion -->

### Create a Figure
Now let's create a simple scatter plot with 100 random points of varying color and size.

```python
import plotly.graph_objects as go

import numpy as np
np.random.seed(1)

# Generate scatter plot data
N = 100
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sz = np.random.rand(N) * 30

# Build and display figure
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode="markers",
    marker={"size": sz,
            "color": colors,
            "opacity": 0.6,
            "colorscale": "Viridis"
            }
))

fig.show()
```

### config
We can use the `plotly.io.orca.config` object to view the current orca configuration settings.

```python
import plotly.io as pio
pio.orca.config
```

### status
We can use the `plotly.io.orca.status` object to see the current status of the orca server

```python
import plotly.io as pio
pio.orca.status
```

Since no image export operations have been performed yet, the orca server is not yet running.

Let's export this figure as an SVG image, and record the runtime.

```python
%%time
import plotly.io as pio
from IPython.display import SVG, display
img_bytes = pio.to_image(fig, format="svg")
display(SVG(img_bytes))
```

By checking the `status` object again, we see that the orca server is now running

```python
import plotly.io as pio
pio.orca.status
```

Let's perform this same export operation again, now that the server is already running.

```python
%%time
import plotly.io as pio
from IPython.display import SVG, display
img_bytes = pio.to_image(fig, format="svg")
display(SVG(img_bytes))
```

The difference in runtime is dramatic. Starting the server and exporting the first image takes a couple seconds, while exporting an image with a running server is much faster.


### Shutdown the Server
By default, the orca server will continue to run until the main Python process exits.  It can also be manually shut down by calling the `plotly.io.orca.shutdown_server()` function.  Additionally, it is possible to configure the server to shut down automatically after a certain period of inactivity. See the `timeout` configuration parameter below for more information.

Regardless of how the server is shut down, it will start back up automatically the next time an image export operation is performed.

```python
import plotly.io as pio
pio.orca.shutdown_server()
pio.orca.status
```

```python
import plotly.io as pio
img_bytes = pio.to_image(fig, format="svg")
display(SVG(img_bytes))
```

```python
import plotly.io as pio
pio.orca.status
```

<!-- #region -->
### Configuring the Executable
By default, plotly.py searches the `PATH` for an executable named `orca` and checks that it is a valid plotly orca executable. If plotly.py is unable to find the executable, you'll get an error message that looks something like this:

```
----------------------------------------------------------------------------
ValueError:
The orca executable is required in order to export figures as static images,
but it could not be found on the system path.

Searched for executable 'orca' on the following path:
    /anaconda3/envs/plotly_env/bin
    /usr/local/bin
    /usr/bin
    /bin
    /usr/sbin
    /sbin

If you haven't installed orca yet, you can do so using conda as follows:

    $ conda install -c plotly plotly-orca==1.2.1

Alternatively, see other installation methods in the orca project README at
https://github.com/plotly/orca.

After installation is complete, no further configuration should be needed.

If you have installed orca, then for some reason plotly.py was unable to
locate it. In this case, set the `plotly.io.orca.config.executable`
property to the full path to your orca executable. For example:

    >>> plotly.io.orca.config.executable = '/path/to/orca'

After updating this executable property, try the export operation again.
If it is successful then you may want to save this configuration so that it
will be applied automatically in future sessions. You can do this as follows:

    >>> plotly.io.orca.config.save()

If you're still having trouble, feel free to ask for help on the forums at
https://community.plotly.com/c/api/python
----------------------------------------------------------------------------
```
If this happens, follow the instructions in the error message and specify the full path to you orca executable using the `plotly.io.orca.config.executable` configuration property.
<!-- #endregion -->

### Other Configuration Settings
In addition to the `executable` property, the `plotly.io.orca.config` object can also be used to configure the following options:

 - **`server_url`**: The URL to an externally running instance of Orca. When this is set, plotly.py will not launch an orca server process and instead use the one provided.
 - **`port`**: The specific port to use to communicate with the orca server, or `None` if the port will be chosen automatically.
 - **`timeout`**: The number of seconds of inactivity required before the orca server is shut down. For example, if timeout is set to 20, then the orca server will shutdown once is has not been used for at least 20 seconds. If timeout is set to `None` (the default), then the server will not be automatically shut down due to inactivity.
 - **`default_width`**: The default pixel width to use on image export.
 - **`default_height`**: The default pixel height to use on image export.
 - **`default_scale`**: The default image scale factor applied on image export.
 - **`default_format`**: The default image format used on export. One of `"png"`, `"jpeg"`, `"webp"`, `"svg"`, `"pdf"`, or `"eps"`.
 - **`mathjax`**: Location of the MathJax bundle needed to render LaTeX characters. Defaults to a CDN location. If fully offline export is required, set this to a local MathJax bundle.
 - **`topojson`**: Location of the topojson files needed to render choropleth traces. Defaults to a CDN location. If fully offline export is required, set this to a local directory containing the [Plotly.js topojson files](https://github.com/plotly/plotly.js/tree/master/dist/topojson).
 - **`mapbox_access_token`**: Mapbox access token required to render `scattermapbox` traces.
 - **`use_xvfb`**: Whether to call orca using [Xvfb](https://www.x.org/releases/X11R7.6/doc/man/man1/Xvfb.1.xhtml) on Linux. Xvfb is needed for orca to work in a Linux environment if an X11 display server is not available.  By default, plotly.py will automatically use Xvfb if it is installed, and no active X11 display server is detected.  This can be set to `True` to force the use of Xvfb, or it can be set to `False` to disable the use of Xvfb.


### Saving Configuration Settings
Configuration options can optionally be saved to the `~/.plotly/` directory by calling the `plotly.io.config.save()` method.  Saved setting will be automatically loaded at the start of future sessions.
