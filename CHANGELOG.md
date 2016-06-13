# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

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
