# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

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
