# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [2.0.0] - 2017-01-25

### Changed
- `plotly.exceptions.PlotlyRequestException` is *always* raised for network
failures. Previously either a `PlotlyError`, `PlotlyRequestException`, or a
`requests.exceptions.ReqestException` could be raised. In particular, scripts
which depend on `try-except` blocks containing network requests should be
revisited.
- `plotly.py:sign_in` now validates to the plotly server specified in your
  config. If it cannot make a successful request, it raises a `PlotlyError`.
- `plotly.figure_factory` will raise an `ImportError` if `numpy` is not
  installed.
- `plotly.figure_factory.create_violin()` now has a `rugplot` parameter which
  determines whether or not a rugplot is draw beside each violin plot.

### Deprecated
- `plotly.tools.FigureFactory`. Use `plotly.figure_factory.*`.
- (optional imports) `plotly.tools._*_imported` It was private anyhow, but now
it's gone. (e.g., `_numpy_imported`)
- (plotly v2 helper) `plotly.py._api_v2` It was private anyhow, but now it's
gone.

## [1.13.0] - 2016-12-17
### Added
- Python 3.5 has been added as a tested environment for this package.

### Updated
- `plotly.plotly.create_animations` and `plotly.plotly.icreate_animations` now return appropriate error messages if the response is not successful.
- `frames` are now integrated into GRAPH_REFERENCE and figure validation.

### Changed
- The plot-schema from `https://api.plot.ly/plot-schema` is no longer updated on import.

## [1.12.12] - 2016-12-06
### Updated
- Updated `plotly.min.js` to version 1.20.5 for `plotly.offline`.
	- See [the plotly.js CHANGELOG](https://github.com/plotly/plotly.js/blob/master/CHANGELOG.md) for additional information regarding the updates
- `FF.create_scatterplotmatrix` now by default does not show the trace labels for the box plots, only if `diag=box` is selected for the diagonal subplot type.

## [1.12.11] - 2016-12-01
### Fixed
- The `link text` in the bottom right corner of the offline plots now properly displays `Export to [Domain Name]` for the given domain name set in the users' `.config` file.

## [1.12.10] - 2016-11-28
### Updated
- `FF.create_violin` and `FF.create_scatterplotmatrix` now by default do not print subplot grid information in output
- Removed alert that occured when downloading plot images offline. Please note: for higher resolution images and more export options, consider making requests to our image servers. See: `help(py.image)` for more details.

### Added
- Plot configuration options for offline plots. See the list of [configuration options](https://github.com/Rikorose/plotly.py/blob/master/plotly/offline/offline.py#L189) and [examples](https://plot.ly/javascript/configuration-options/) for more information.
	- Please note that these configuration options are for offline plots ONLY. For configuration options when embedding online plots please see our [embed tutorial](http://help.plot.ly/embed-graphs-in-websites/#step-8-customize-the-iframe).
- `colors.py` file which contains functions for manipulating and validating colors and arrays of colors
- 'scale' param in `FF.create_trisurf` which now can set the interpolation on the colorscales
- animations now work in offline mode. By running `plotly.offline.plot()` and `plotly.offline.iplot()` with a `fig` with `frames`, the resulting plot will cycle through the figures defined in `frames` either in the browser or in an ipython notebook respectively. Here's an example:
```
import IPython.display
from IPython.display import display, HTML
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

figure_or_data = {'data': [{'x': [1, 2], 'y': [0, 1]}],
                  'layout': {'xaxis': {'range': [0, 3], 'autorange': False},
                             'yaxis': {'range': [0, 20], 'autorange': False},
                  'title': 'First Title'},
                  'frames': [{'data': [{'x': [1, 2], 'y': [5, 7]}]},
                             {'data': [{'x': [-1, 3], 'y': [3, 9]}]},
                             {'data': [{'x': [2, 2.6], 'y': [7, 5]}]},
                             {'data': [{'x': [1.5, 3], 'y': [7.5, 4]}]},
                             {'data': [{'x': [1, 2], 'y': [0, 1]}],
                              'layout': {'title': 'End Title'}}]}
iplot(figure_or_data)
```
More examples can be found at https://plot.ly/python/animations/.
- animations now work in online mode: use `plotly.plotly.create_animations` and `plotly.plotly.icreate_animations` which animate a figure with the `frames` argument. Here is a simple example:
```
import plotly.plotly as py
from plotly.grid_objs import Grid, Column

column_1 = Column([0.5], 'x')
column_2 = Column([0.5], 'y')
column_3 = Column([1.5], 'x2')
column_4 = Column([1.5], 'y2')

grid = Grid([column_1, column_2, column_3, column_4])
py.grid_ops.upload(grid, 'ping_pong_grid', auto_open=False)

# create figure
figure = {
    'data': [
        {
            'xsrc': grid.get_column_reference('x'),
            'ysrc': grid.get_column_reference('y'),
            'mode': 'markers',
        }
    ],
    'layout': {'title': 'Ping Pong Animation',
               'xaxis': {'range': [0, 2], 'autorange': False},
               'yaxis': {'range': [0, 2], 'autorange': False},
               'updatemenus': [{
                   'buttons': [
                       {'args': [None],
                        'label': u'Play',
                        'method': u'animate'}
               ],
               'pad': {'r': 10, 't': 87},
               'showactive': False,
               'type': 'buttons'
                }]},
    'frames': [
        {
            'data': [
                {
                    'xsrc': grid.get_column_reference('x2'),
                    'ysrc': grid.get_column_reference('y2'),
                    'mode': 'markers',
                }
            ]
        },
        {
            'data': [
                {
                    'xsrc': grid.get_column_reference('x'),
                    'ysrc': grid.get_column_reference('y'),
                    'mode': 'markers',
                }
            ]
        }
    ]
}

py.create_animations(figure, 'ping_pong')
```

### Fixed
- Trisurf now uses correct `Plotly Colorscales` when called
- Fixed a bug in the format of unique-identifiers in columns of grids that are uploaded to plotly via `plotly.plotly.upload`. See https://github.com/plotly/plotly.py/pull/599 for details. In particular, creating plots that are based off of plotly grids is no longer broken. Here is an example:

```
import plotly.plotly as py
from plotly.grid_objs import Grid, Column

c1 = Column([6, 6, 6, 5], 'column 1')
c2 = Column(['a', 'b', 'c', 'd'], 'column 2')
g = Grid([c1, c2])

# Upload the grid
py.grid_ops.upload(g, 'my-grid', auto_open=False)

# Make a graph that with data that is referenced from that grid
trace = Scatter(xsrc=g[0], ysrc=g[1])
url = py.plot([trace], filename='my-plot')
```
Then, whenever you update the data in `'my-grid'`, the associated plot will update too. See https://plot.ly/python/data-api for more details on usage and examples.

## [1.12.9] - 2016-08-22
### Fixed
- the colorbar in `.create_trisurf` now displays properly in `offline mode`.

### Updated
- the colorbar in `.create_trisurf` now displays the appropriate max and min values on the ends of the bar which corresponding to the coloring metric of the figure
- `edges_color` is now a param in `.create_trisurf` which only takes `rgb` values at the moment

## [1.12.8] - 2016-08-18
### Fixed
- Fixed color bug with trisurf plots where certain triangles were colored strangely. The coordinates of `rgb(...)` are now rounded to their nearest integer (using Python3 method of rounding), then placed in the color string to fix the issue.

## [1.12.7] - 2016-08-17
### Fixed
- Edited `plotly.min.js` due to issue using `iplot` to plot offline in Jupyter Notebooks
	- Please note that `plotly.min.js` may be cached in your Jupyter Notebook. Therefore, if you continue to experience this issue after upgrading the Plotly package please open a new notebook or clear the cache to ensure the correct `plotly.min.js` is referenced.

## [1.12.6] - 2016-08-09
### Updated
- Updated `plotly.min.js` from 1.14.1 to 1.16.2
	- Trace type scattermapbox is now part of the main bundle
	- Add updatemenus (aka dropdowns) layout components
	- See [the plotly.js CHANGELOG](https://github.com/plotly/plotly.js/blob/master/CHANGELOG.md) for additional information regarding the updates

## [1.12.5] - 2016-08-03
### Updated
- `.create_trisurf` now supports a visible colorbar for the trisurf plots. Check out the docs for help:
```
import plotly.tools as tls
help(tls.FigureFactory.create_trisurf)
```

## [1.12.4] - 2016-07-14
### Added
- The FigureFactory can now create 2D-density charts with `.create_2D_density`. Check it out with:
```
import plotly.tools as tls
help(tls.FigureFactory.create_2D_density)
```

## [1.12.3] - 2016-06-30
### Updated
- Updated `plotly.min.js` from 1.13.0 to 1.14.1
	- Numerous additions and changes where made to the mapbox layout layers attributes
	- Attribute line.color in scatter3d traces now support color scales
	- Layout shapes can now be moved and resized (except for 'path' shapes) in editable contexts
	- See [the plotly.js CHANGELOG](https://github.com/plotly/plotly.js/blob/master/CHANGELOG.md#1141----2016-06-28) for additional information regarding the updates
- Updated `default-schema`

### Added
- Added `update_plotlyjs_for_offline` in makefile in order to automate updating `plotly.min.js` for offline mode

## [1.12.2] - 2016-06-20
### Updated
- Updated plotly.min.js so the offline mode is using plotly.js v1.13.0
	- Fix `Plotly.toImage` and `Plotly.downloadImage` bug specific to Chrome 51 on OSX
	- Beta version of the scattermapbox trace type - which allows users to create mapbox-gl maps using the plotly.js API. Note that scattermapbox is only available through custom bundling in this release.
	- See [the plotly.js CHANGELOG](https://github.com/plotly/plotly.js/blob/master/CHANGELOG.md#1130----2016-05-26) for additional additions and updates.

### Added
- The FigureFactory can now create gantt charts with `.create_gantt`. Check it out with:
```
import plotly.tools as tls
help(tls.FigureFactory.create_gantt)
```
- Ability to download images in offline mode. By providing an extra keyword `image` to the existing plot calls, you can now download the images of the plots you make in offline mode.

### Fixed
- Fixed check for the height parameter passed to `_plot_html`, and now sets the correct `link text` for plots
generated in offline mode.


## [1.12.1] - 2016-06-19
### Added
- The FigureFactory can now create violin plots with `.create_violin`. Check it out with:
```
import plotly.tools as tls
help(tls.FigureFactory.create_violin)
```

## [1.12.0] - 2016-06-06
### Added
- Added ability to enable/disable SSL certificate verification for streaming. Disabling SSL certification verification requires Python v2.7.9 / v3.4.3 (or above). This feature can be toggled via the `plotly_ssl_verification` configuration setting.

## [1.11.0] - 2016-05-27
### Updated
- Changed the default option for `create_distplot` in the figure factory from `probability` to `probability density` and also added the `histnorm` parameter to allow the user to choose between the two options.
Note: This is a backwards incompatible change.

- Updated plotly.min.js so the offline mode is using plotly.js v1.12.0
	- Light position is now configurable in surface traces
	- surface and mesh3d lighting attributes are now accompanied with comprehensive descriptions

- Allowed `create_scatterplotmatrix` and `create_trisurf` to use divergent and categorical colormaps. The parameter `palette` has been replaced by `colormap` and `use_palette` has been removed. In `create_scatterplotmatrix`, users can now:
	- Input a list of different color types (hex, tuple, rgb) to `colormap` to map colors divergently
	- Use the same list to categorically group the items in the index column
	- Pass a singlton color type to `colormap` to color all the data with one color
	- Input a dictionary to `colormap` to map index values to a specific color
	- 'cat' and 'seq' are valid options for `colormap_type`, which specify the type of colormap being used

- In `create_trisurf`, the parameter `dist_func` has been replaced by `color_func`. Users can now:
	- Input a list of different color types (hex, tuple, rgb) to `colormap` to map colors divergently
	- Input a list|array of hex and rgb colors to `color_func` to assign each simplex to a color

### Added
- Added the option to load plotly.js from a CDN by setting the parameter `connected=True`
 in the `init_notebook_mode()` function call
- The FigureFactory can now create trisurf plots with `.create_trisurf`. Check it out with:
```
import plotly.tools as tls
help(tls.FigureFactory.create_trisurf)
```



## [1.10.0] - 2016-05-19
### Fixed
- Version 1.9.13 fixed an issue in offline mode where if you ran `init_notebook_mode`
more than once the function would skip importing (because it saw that it had
already imported the library) but then accidentally clear plotly.js from the DOM.
This meant that if you ran `init_notebook_mode` more than once, your graphs would
not appear when you refreshed the page.
Version 1.9.13 solved this issue by injecting plotly.js with every iplot call.
While this works, it also injects the library excessively, causing notebooks
to have multiple versions of plotly.js inline in the DOM, potentially making
notebooks with many `iplot` calls very large.
Version 1.10.0 brings back the requirement to call `init_notebook_mode` before
making an `iplot` call. It makes `init_notebook_mode` idempotent: you can call
it multiple times without worrying about losing your plots on refresh.


## [1.9.13] - 2016-05-19
### Fixed
- Fixed issue in offline mode related to the inability to reload plotly.js on page refresh and extra init_notebook_mode calls.

## [1.9.12] - 2016-05-16
### Added
- SSL support for streaming.

## [1.9.11] - 2016-05-02
### Added
- The FigureFactory can now create scatter plot matrices with `.create_scatterplotmatrix`. Check it out with:
```
import plotly.tools as tls
help(tls.FigureFactory.create_scatterplotmatrix)
```

## [1.9.10] - 2016-04-27
### Updated
- Updated plotly.min.js so the offline mode is using plotly.js v1.10.0
	- Added beta versions of two new 2D WebGL trace types: heatmapgl, contourgl
	- Added fills for scatterternary traces
	- Added configurable shapes layer positioning with the shape attribute: `layer`

## [1.9.9] - 2016-04-15
### Fixed
- Fixed `require is not defined` issue when plotting offline outside of Ipython Notebooks.

## [1.9.8] - 2016-04-14
### Fixed
- Error no longer results from a "Run All" cells when working in a Jupyter Notebook.

### Updated
- Updated plotly.min.js so offline is using plotly.js v1.9.0
	- Added Ternary plots with support for scatter traces (trace type `scatterternary`, currently only available in offline mode)
	- For comprehensive update list see the [plotly.js CHANGELOG](https://github.com/plotly/plotly.js/blob/master/CHANGELOG.md)

## [1.9.7] - 2016-04-04
### Fixed
- Offline mode will no longer delete the Jupyter Notebook's require, requirejs, and define variables.

### Updated
- Updated plotly.min.js so offline is using plotly.js v1.8.0
	- Added range selector functionality for cartesian plots
	- Added range slider functionality for scatter traces
	- Added custom surface color functionality
	- Added ability to subplot multiple graph types (SVG cartesian, 3D, maps, pie charts)
	- For comprehensive update list see the [plotly.js CHANGELOG](https://github.com/plotly/plotly.js/blob/master/CHANGELOG.md)

## [1.9.6] - 2016-02-18
### Updated
- Updated plotly.min.js so offline is using plotly.js v1.5.2

## [1.9.5] - 2016-01-17
### Added
- Offline matplotlib to Plotly figure conversion. Use `offline.plot_mpl` to convert and plot a matplotlib figure as a Plotly figure independently of IPython/Jupyter notebooks or use `offline.iplot_mpl` to convert and plot inside of IPython/Jupyter notebooks. Additionally, use `offline.enable_mpl_offline` to convert and plot all matplotlib figures as plotly figures inside an IPython/Jupyter notebook. See examples below:

An example independent of IPython/Jupyter notebooks:
```
from plotly.offline import init_notebook_mode, plot_mpl
import matplotlib.pyplot as plt

init_notebook_mode()

fig = plt.figure()
x = [10, 15, 20]
y = [100, 150, 200]
plt.plot(x, y, "o")

plot_mpl(fig)
```

An example inside of an IPython/Jupyter notebook:
```
from plotly.offline import init_notebook_mode, iplot_mpl
import matplotlib.pyplot as plt

init_notebook_mode()

fig = plt.figure()
x = [10, 15, 20]
y = [100, 150, 200]
plt.plot(x, y, "o")

iplot_mpl(fig)
```

An example of enabling all matplotlib figures to be converted to
Plotly figures inside of an IPython/Jupyter notebook:
```
from plotly.offline import init_notebook_mode, enable_mpl_offline
import matplotlib.pyplot as plt

init_notebook_mode()
enable_mpl_offline()

fig = plt.figure()
x = [10, 15, 20, 25, 30]
y = [100, 250, 200, 150, 300]
plt.plot(x, y, "o")
fig
```

## [1.9.4] - 2016-01-11
### Added
- Offline plotting now works outside of the IPython/Jupyter notebook. Here's an example:
```
from plotly.offline import plot
from plotly.graph_objs import Scatter

plot([Scatter(x=[1, 2, 3], y=[3, 1, 6])])
```

This command works entirely locally. It writes to a local HTML file with the necessary [plotly.js](https://plot.ly/javascript) code to render the graph. Your browser will open the file after you make the call.

The call signature is very similar to `plotly.offline.iplot` and `plotly.plotly.plot` and `plotly.plotly.iplot`, so you can basically use these commands interchangeably.

If you want to publish your graphs to the web, use `plotly.plotly.plot`, as in:

```
import plotly.plotly as py
from plotly.graph_objs import Scatter

py.plot([Scatter(x=[1, 2, 3], y=[5, 1, 6])])
```

This will upload the graph to your online plotly account.

## [1.9.3] - 2015-12-08
### Added
- Check for `no_proxy` when determining if the streaming request should pass through a proxy in the chunked_requests submodule. Example: `no_proxy='my_stream_url'` and `http_proxy=my.proxy.ip:1234`, then `my_stream_url` will not get proxied. Previously it would.

## [1.9.2] - 2015-11-30
**Bug Fix**: Previously, the "Export to plot.ly" link on
offline charts would export your figures to the
public plotly cloud, even if your `config_file`
(set with `plotly.tools.set_config_file` to the file
`~/.plotly/.config`) set `plotly_domain` to a plotly enterprise
URL like `https://plotly.acme.com`.

This is now fixed. Your graphs will be exported to your
`plotly_domain` if it is set.

## [1.9.1] - 2015-11-26
### Added
- The FigureFactory can now create annotated heatmaps with `.create_annotated_heatmap`. Check it out with:
```
import plotly.tools as tls
help(tls.FigureFactory.create_annotated_heatmap)
```
- The FigureFactory can now create tables with `.create_table`.
```
import plotly.tools as tls
help(tls.FigureFactory.create_table)
```

## [1.9.0] - 2015-11-15
- Previously, using plotly offline required a paid license.
No more: `plotly.js` is now shipped inside this package to allow
unlimited free use of plotly inside the ipython notebook environment.
The `plotly.js` library that is included in this package is free,
open source, and maintained independently on GitHub at
[https://github.com/plotly/plotly.js](https://github.com/plotly/plotly.js).
- The `plotly.js` bundle that is required for offline use is no longer downloaded
and installed independently from this package: `plotly.offline.download_plotlyjs`
is **deprecated**.
- New versions of `plotly.js` will be tested and incorporated
  into this package as new versioned pip releases;
  `plotly.js` is not automatically kept in sync with this package.

## [1.8.12] - 2015-11-02
- *Big data* warning mentions `plotly.graph_objs.Scattergl` as possible solution.

## [1.8.9] - 2015-10-11
- If you're behind a proxy, you can make requests by setting the environmental variable HTTP_PROXY and HTTPS_PROXY (http://docs.python-requests.org/en/v1.0.4/user/advanced/#proxies). This didn't work for streaming, but now it does.

## [1.8.8] - 2015-10-05
- Sometimes creating a graph with a private share-key doesn't work -
the graph is private, but not accessible with the share key.
Now we check to see if it didn't work, and re-try a few times until
it does.

## [1.8.7] - 2015-10-01
### Added
- The FigureFactory can now create dendrogram plots with `.create_dendrogram`.

## [1.8.6] - 2015-09-28
### Fixed
- Saving "world_readable" to your config file via `plotly.tools.set_config` actually works.

### Added
- You can also save `auto_open` and `sharing` to the config file so that you can forget these
  keyword argument in `py.iplot` and `py.plot`.

## [1.8.5] - 2015-09-29
### Fixed
- Fixed validation errors (validate=False workaround no longer required)

### Added
- Auto-sync API request on import to get the latest schema from Plotly
- `.`-access for nested attributes in plotly graph objects
- General `.help()` method for plotly graph objects
- Specific attribute `.help(<attribute>)` also included

### Removed
- No more *is streamable*, streaming validation.

## [1.8.3] - 2015-08-14
### Fixed
- Fixed typos in `plot` and `iplot` documentations

## [1.8.2] - 2015-08-11
### Added
- CHANGELOG
- `sharing` keyword argument for `plotly.plotly.plot` and `plotly.plotly.iplot` with options `'public' | 'private' | 'secret'` to control the privacy of the charts. Depreciates `world_readable`

### Changed
- If the response from `plot` or `iplot` contains an error message, raise an exception

### Removed
- `height` and `width` are no longer accepted in `iplot`. Just stick them into your figure's layout instead, it'll be more consistent when you view it outside of the IPython notebook environment. So, instead of this:

	```
	py.iplot([{'x': [1, 2, 3], 'y': [3, 1, 5]}], height=800)
	```

	do this:

	```
	py.iplot({
		'data': [{'x': [1, 2, 3], 'y': [3, 1, 5]}],
		'layout': {'height': 800}
	})
	```

### Fixed
- The height of the graph in `iplot` respects the figure's height in layout
