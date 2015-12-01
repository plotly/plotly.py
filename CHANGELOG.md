# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

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
