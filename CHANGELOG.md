# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [3.4.1] - 2018-11-09

### Updated
 - Updated Plotly.js to version 1.42.5. See the
 [plotly.js CHANGELOG](https://github.com/plotly/plotly.js/blob/master/CHANGELOG.md#1423----2018-11-06)
 for more information.
 
### Fixed
 - Fixed histogram binning with pandas `Series` or numpy array
 (regression introduced in 3.4.0)
 ([#1257](https://github.com/plotly/plotly.py/issues/1257), 
  [plotly/plotly.js#3211](https://github.com/plotly/plotly.js/pull/3211))
 - Fixed incorrect validation error on the `args` property of
  `layout.updatemenu.Button()` when value is a `list` that starts with a `list`
  ([#1265](https://github.com/plotly/plotly.py/issues/1265))
 - Fixed deadlock causing `plotly.io.write_image` to hang on Windows after
 exporting more than ~25 images
 ([#1255](https://github.com/plotly/plotly.py/issues/1255))
 - Fixed plot display error for `scattergl` trace with `mode='lines'` and 
 more than 100k points
 ([#1271](https://github.com/plotly/plotly.py/issues/1271))
 - Fixed responsive resizing error with `iplot` in the classic notebook
 ([#1263](https://github.com/plotly/plotly.py/pull/1263))

## [3.4.0] - 2018-11-02

### Updated
 - Updated Plotly.js to version 1.42.2. Select highlights included below, see
 the [plotly.js CHANGELOG](https://github.com/plotly/plotly.js/blob/master/CHANGELOG.md#1422----2018-11-01)
 for more information.
 
### Added
 - Default figure properties may now be customized using figure
 templates (themes) and 7 new predefined templates are bundled with
 plotly.py
 ([#1224](https://github.com/plotly/plotly.py/pull/1224))
 - Added Parallel Categories (`parcats`) trace type for the visualization
 of multi-dimensional categorical datasets
 ([plotly/plotly.js#2963](https://github.com/plotly/plotly.js/pull/2963))
 - Added LaTeX typesetting support for figures displayed in the Jupyter
 Notebook using `plotly.offline.iplot` and `plotly.graph_objs.FigureWidget`.
 **Note:** There are still outstanding issues with MathJax rendering in FireFox,
 but it is now working well in Chrome.
 ([#1243](https://github.com/plotly/plotly.py/pull/1243))
 - Added `include_mathjax` argument to `plotly.offline.plot` to support
 the creation of HTML files with LaTeX typesetting
 ([#1243](https://github.com/plotly/plotly.py/pull/1243))
 - Added new `plotly.offline.get_plotlyjs` function that returns the
 contents of the bundled plotly.js library as a string
 ([#637](https://github.com/plotly/plotly.py/issues/637),
  [#1246](https://github.com/plotly/plotly.py/pull/1246))
 - Added new `plotly.offline.get_plotlyjs_version` function that returns
 the version of the bundled plotly.js library
 ([#1246](https://github.com/plotly/plotly.py/pull/1246))
 - HTML div strings returned by `plotly.offline.plot` now contain logic
 to automatically resize the figure responsively.  This logic was previously
 only added for html files.
 ([#1043](https://github.com/plotly/plotly.py/issues/1043),
  [#1234](https://github.com/plotly/plotly.py/pull/1234))
 - Figures displayed using `plotly.offline.iplot` in the classic Jupyter
 Notebook will now resize responsively
 ([#1234](https://github.com/plotly/plotly.py/pull/1234))
 - Added `'cdn'`, `'directory'`, and path string `include_plotlyjs` options
 in `plotly.offline.plot`
 ([#1234](https://github.com/plotly/plotly.py/pull/1234))
   - When `'cdn'`, the resulting html file/div includes a script tag reference
   to the plotlyjs cdn.
   - When `'directory'`, the resulting html file/div includes a script tag
   reference to a plotly.min.js bundle in the same directory as the html file.
   If `output_type` is `'file'` then this plotly.min.js bundle is created in
   the output directory if it doesn't already exist.
   - When a string ending with `'.js'`, the resulting html file/div includes
   a script tag that references this exact path. This can be used to point
   to a plotly.js bundle from an alternative CDN.
 - Added a new `color_threshold` argument to the `create_dendrogram` figure
 factory to control the dendrogram clustering cutoff
 ([#995](https://github.com/plotly/plotly.py/issues/995),
  [#1075](https://github.com/plotly/plotly.py/pull/1075),
  [#1214](https://github.com/plotly/plotly.py/pull/1214))  
 - Added support for `autorange='reversed'` in 3D axes 
 ([#803](https://github.com/plotly/plotly.py/issues/803),
  [plotly/plotly.js#3141](https://github.com/plotly/plotly.js/pull/3141))
 - Added new gl3d tick and title auto-rotation algorithm that limits text
 overlaps
 ([plotly/plotly.js#3084](https://github.com/plotly/plotly.js/pull/3084),
  [plotly/plotly.js#3131](https://github.com/plotly/plotly.js/pull/3131))
 - Added `modebar` layout style attributes:
 `orientation`, `bgcolor`, `color` and `activecolor`
 ([plotly/plotly.js#3068](https://github.com/plotly/plotly.js/pull/3068),
  [plotly/plotly.js#3091](https://github.com/plotly/plotly.js/pull/3091))
 - Added `title`, `titleposition` and `titlefont` attributes to pie traces
 ([plotly/plotly.js#2987](https://github.com/plotly/plotly.js/pull/2987))
 - Added `hoverlabel.split` attribute to `ohlc` and `candlestick` traces to
 split hover labels into multiple pieces
 ([plotly/plotly.js#2959](https://github.com/plotly/plotly.js/pull/2959))
 - Added support for `line.shape` values `'hv'`, `'vh'`, `'hvh'`
 and `'vhv'` in `scattergl` traces
 ([plotly/plotly.js#3087](https://github.com/plotly/plotly.js/pull/3087))
 - Added trace, node and link `hoverinfo` for `sankey` traces
 ([#3096](https://github.com/plotly/plotly.js/pull/3096),
  [#3150](https://github.com/plotly/plotly.js/pull/3150))
 - Added per-sector `textfont` settings in pie traces
 ([#3130](https://github.com/plotly/plotly.js/pull/3130))
 
 
### Changed
 - Use new Plotly logo in "Produced with Plotly" modebar button
 ([plotly/plotly.js#3068](https://github.com/plotly/plotly.js/pull/3068))


### Fixed
 - Plotly's use of MathJax for LaTeX typesetting no longer interferes with
 the Jupyter Notebook's use of MathJax
 ([#445](https://github.com/plotly/plotly.py/issues/445), 
  [#360](https://github.com/plotly/plotly.py/issues/360))
 - Fixed several issues with the use of `reversescale=True` in the
 `create_annotated_heatmap` figure factory
 ([#1251](https://github.com/plotly/plotly.py/pull/1251))
 - Fixed case where `plotly.offline.iplot` would fail to render in the classic
 Jupyter Notebook if the notebook contained a Markdown headline with the text
 "Plotly"
 ([#816](https://github.com/plotly/plotly.py/issues/816))
 - `None` values in a `scatter.hovertext` list are now omitted from the 
 hover label rather than being displayed as the string `"None"`
 ([#1244](https://github.com/plotly/plotly.py/issues/1244))
 - Subplot titles created by `plotly.tools.make_subplots` are now positioned
 properly when custom `row_width`/`column_width` arguments are specified
 ([#1229](https://github.com/plotly/plotly.py/issues/1229))
 - The `bar.width` property may now be specified as a numpy array or a pandas
 series
 ([#1231](https://github.com/plotly/plotly.py/issues/1231), 
 [plotly/plotly.js#3169](https://github.com/plotly/plotly.js/pull/3169))
 - Error bars are now scaled correctly for logarithmic `scatter3d` traces
 ([#1139](https://github.com/plotly/plotly.py/issues/1139))
 - Use `uuid.uuid4` rather than `uuid.uuid1` to work around an upstream
 Python bug
  ([#1235](https://github.com/plotly/plotly.py/issues/1235),
   [#1236](https://github.com/plotly/plotly.py/pull/1236))
 - The `layout.grid.subplots` property may now be specified as a 2D list of 
 subplot identifiers
 ([#1220](https://github.com/plotly/plotly.py/issues/1220),
  [#1240](https://github.com/plotly/plotly.py/pull/1240))
 - Fixed `scatter3d` text alignment
 ([#1055](https://github.com/plotly/plotly.py/issues/1055),
  [plotly/plotly.js#3180](https://github.com/plotly/plotly.js/pull/3180))
 

### JupyterLab Versions
For use with JupyterLab, the following versions of the following packages
must be installed:

 - Python Packages
   - plotly==3.4.0
   - ipywidgets>=7.2
   - notebook>=5.3
   - jupyterlab==0.35
   
 - JupyterLab Extensions
   - plotlywidget@0.5.0
   - @jupyter-widgets/jupyterlab-manager@0.38
   - @jupyterlab/plotly-extension@0.18

## [3.3.0] - 2018-09-28

### Updated
 - Updated Plotly.js to version 1.41.3.  Select highlights included below, see
 [the plotly.js CHANGELOG](https://github.com/plotly/plotly.js/blob/master/CHANGELOG.md#1413----2018-09-25)
 for more information.
 - Do not create or check permissions on the `~/.plotly` configuration
 directory until a configuration write operation is performed
 ([#1195](https://github.com/plotly/plotly.py/pull/1195)). This change
 avoids some concurrency problems associated with running many instances of
 plotly.py simultaneously
 ([#1068](https://github.com/plotly/plotly.py/issues/1068)).
 
### Added
 - Enable selection by clicking on points via new layout attribute `clickmode` and flag `'select'`
 ([#2944](https://github.com/plotly/plotly.js/pull/2944))
 - Added stacked area charts via new attributes `stackgroup` and `stackgaps` in scatter traces
 ([#2960](https://github.com/plotly/plotly.js/pull/2960))
 - Added `barpolar` trace type - which replace and augment area traces
 ([#2954](https://github.com/plotly/plotly.js/pull/2954))
 - Added `polar.hole` layout parameter to punch hole at the middle of polar
 subplot offsetting the start of the radial range
 ([#2977](https://github.com/plotly/plotly.js/pull/2977), [#2996](https://github.com/plotly/plotly.js/pull/2996))
 - Figures may now be easily converted to and from JSON using the new
 `to_json`, `from_json`, `read_json`, and `write_json` functions in the
 `plotly.io` package
 ([#1188](https://github.com/plotly/plotly.py/pull/1188))
 - Figures and graph objects now support `deepcopy` and `pickle` operations
 ([#1191](https://github.com/plotly/plotly.py/pull/1191))
 - The location of the `"~/.plotly"` settings directory may now be customized
 using the `PLOTLY_DIR` environment variable
 ([#1195](https://github.com/plotly/plotly.py/pull/1195))
 - Added optional `scaleratio` argument to the `create_quiver` figure factory.
 When specified, the axes are restricted to this ratio and the quiver arrows
 are computed to have consistent lengths across angles.
 ([#1197](https://github.com/plotly/plotly.py/pull/1197))
 
### Fixed
 - Replace use of `pkg_resources.resource_string` with `pkgutil.get_data` to
 improve compatibility with `cx_Freeze`
 ([#1201](https://github.com/plotly/plotly.py/pull/1201))
 - An exception is no longer raised when an optional dependency raises an
 exception on import.  The exception is logged and plotly.py continues as if
 the dependency were not installed
 ([#1192](https://github.com/plotly/plotly.py/pull/1192))
 - Fixed invalid dendrogram axis labels when the points being clustered contain
 duplicate values
 ([#1186](https://github.com/plotly/plotly.py/pull/1186))
 - Added missing LICENSE.txt file to PyPI source distribution
 ([#765](https://github.com/plotly/plotly.py/issues/765))

### JupyterLab Versions
For use with JupyterLab, the following versions of the following packages
must be installed:

 - Python Packages
   - plotly==3.3.0
   - ipywidgets>=7.2
   - notebook>=5.3
   - jupyterlab==0.34
   
 - JupyterLab Extensions
   - plotlywidget@0.4.0
   - @jupyter-widgets/jupyterlab-manager@0.37
   - @jupyterlab/plotly-extension@0.17

## [3.2.1] - 2018-09-14
This is a patch release that fixes a few bugs and reintroduces a few
version 2 features that were not supported in version 3.

The bundled version of plotly.js remains at 1.40.1

### JupyterLab Versions
For use with JupyterLab, the following versions of the following packages
must be installed:

 - Python Packages
   - plotly==3.2.1
   - ipywidgets>=7.2
   - notebook>=5.3
   - jupyterlab==0.34
   
 - JupyterLab Extensions
   - plotlywidget@0.3.0
   - @jupyter-widgets/jupyterlab-manager@0.37
   - @jupyterlab/plotly-extension@0.17

### Added
 - An optional `skip_invalid` argument has been added to the `Figure` and
  `FigureWidget` constructors. By default, `skip_invalid` is `False` and invalid
  figure properties will result in an exception (this is identical to the
  previous behavior).  When `skip_invalid` is set to `True`, invalid properties
  will instead be silently ignored. This argument replaces the `_raise`
  argument that was available in version 2, and makes it possible to import
  figure definitions from different plotly versions, where incompatible
  properties are ignored rather than causing an exception.
 - A `to_ordered_dict` method has been added to the `Figure` and `FigureWidget`
  classes. This method returns a representation of the figure as a nested
  structure of `OrdererdDict` and `list` instances where the keys in each
  `OrderedDict` are sorted alphabetically.  This method replaces the
  `get_ordered` method that was available in version 2, and makes it possible
  to traverse the nested structure of a figure in a deterministic order.

### Fixed
 - Pandas `Series` and `Index` objects storing `datetime` values were
   incorrectly cast to numeric arrays
   ([plotly/plotly.py#1160](https://github.com/plotly/plotly.py/issues/1160),
    [plotly/plotly.py#1163](https://github.com/plotly/plotly.py/pull/1163))
 - Numpy arrays with `uint64` datatype caused a `FigureWidget` error,
   and no figure was displayed
   ([plotly/plotly.py#1155](https://github.com/plotly/plotly.py/issues/1155),
    [plotly/plotly.py#1163](https://github.com/plotly/plotly.py/pull/1163))

## [3.2.0] - 2018-09-05
This release introduces the long-anticipated ability to programmatically
export figures as high quality static images in both raster and vector
formats.

### JupyterLab Versions (Python 3.5+)
For use with JupyterLab, the following versions of the following packages
must be installed:

 - Python Packages
   - plotly==3.2.0
   - ipywidgets>=7.2
   - notebook>=5.3
   - jupyterlab==0.34
   
 - JupyterLab Extensions
   - plotlywidget@0.3.0
   - @jupyter-widgets/jupyterlab-manager@0.37
   - @jupyterlab/plotly-extension@0.17

### Added
 - plotly.js version 1.40.1, which introduces the following features:
    - Allow `contour`, `contourcarpet` and `histogram2dcontour` to have corresponding legend items using `showlegend`
      ([plotly/plotly.js#2891](https://github.com/plotly/plotly.js/pull/2891),
      [plotly/plotly.js#2914](https://github.com/plotly/plotly.js/pull/2914))
    - Add scatterpolar and scatterpolargl attributes `r0`, `dr`, `theta0` and `dtheta`
      ([plotly/plotly.js#2895](https://github.com/plotly/plotly.js/pull/2895))
    - Add layout attributes `piecolorway` and `extendpiecolors` for more control over pie colors
      ([plotly/plotly.js#2870](https://github.com/plotly/plotly.js/pull/2870))
    - Add `splom` attribute `dimensions[i].axis.type` to easily override axis type in splom-generated axes
      ([plotly/plotly.js#2899](https://github.com/plotly/plotly.js/pull/2870))
    - Add support for on-graph text in `scatterpolargl` traces
      ([plotly/plotly.js#2895](https://github.com/plotly/plotly.js/pull/2895))
    - See [the plotly.js CHANGELOG](https://github.com/plotly/plotly.js/blob/master/CHANGELOG.md#1400----2018-08-16)
      for bug fixes and more information.
 - Support for offline static image export with the `to_image` and `write_image`
   functions in the new `plotly.io` package ([#1120](https://github.com/plotly/plotly.py/pull/1120)).
    - Note: Image export requires the plotly [orca](https://github.com/plotly/orca)
      command line utility and the [`psutil`](https://github.com/giampaolo/psutil) Python package.
 - New documentation sections covering [Static Image Export](https://plot.ly/python/static-image-export/)
   and [Orca Management](https://plot.ly/python/orca-management/) 
 - Support for displaying `FigureWidget` instances in static contexts
   (e.g. [nbviewer](http://nbviewer.jupyter.org/)) just like the built-in ipywidgets
 ([#1117](https://github.com/plotly/plotly.py/pull/1117))
 - Full integration of the Cividis colorscale ([#883](https://github.com/plotly/plotly.py/pull/883))
 - conda packaging
   - From here forward, new versions of plotly.py will be published to the [plotly anaconda channel](https://anaconda.org/plotly/)
     on the same day they are published to PyPI.
     ([72ad0e4](https://github.com/plotly/plotly.py/commit/72ad0e4bf54bb8a06445d2ca55488ffc11c836a7))
   - The [`README`](README.md) now includes conda installation instructions alongside the pip instructions. 
   - In addition to the existing installation approaches, orca is now also available as a
     [conda package](https://anaconda.org/plotly/plotly-orca) from the plotly anaconda channel.
 
### Updated
 - Show traces at the top of the Gantt chart's colorbar ([#1110](https://github.com/plotly/plotly.py/pull/1110))
 - Significantly improved validation performance for numeric pandas `Series` objects ([#1149](https://github.com/plotly/plotly.py/pull/1149))
 - Specialize auto-generated docstrings for Python syntax
 - More robust and specific logic for retrying requests to the plot.ly cloud service ([#1146](https://github.com/plotly/plotly.py/pull/1146))
 - Support basic authentication when using the streaming API behind a proxy server ([#1133](https://github.com/plotly/plotly.py/pull/1133))

### Fixed
 - Validators for `dash` properties (e.g. `scatter.line.dash`) incorrectly rejected dash length lists ([#1136](https://github.com/plotly/plotly.py/pull/1136))
 - Annotated heatmap error when custom colorscale was specified ([#1151](https://github.com/plotly/plotly.py/pull/1151))
 - Incorrect deprecation warning for deprecated `plotly.graph_objs.Annotations` class ([#1138](https://github.com/plotly/plotly.py/pull/1138))
 - Harmless JavaScript console error when opening an html file produced by `plotly.offline.plot` ([#1152](https://github.com/plotly/plotly.py/pull/1152))
 - Incorrect validation errors when writing data to the streaming API ([#1145](https://github.com/plotly/plotly.py/pull/1145))
 

## [3.1.1] - 2018-08-10
This release is a minor bug-fix update to version 3.1.0

### JupyterLab Versions
For use with JupyterLab, the following versions of the following packages
must be installed:

 - Python Packages
   - plotly==3.1.1
   - ipywidgets>=7.2
   - notebook>=5.3
   - jupyterlab==0.33
   
 - JupyterLab Extensions
   - plotlywidget@0.2.1
   - @jupyter-widgets/jupyterlab-manager@0.36
   - @jupyterlab/plotly-extension@0.16

### Updated
 - Updated plotly.js to version 1.39.4.
   - This is a bug-fix release of plotly.js
   - See [the plotly.js CHANGELOG](https://github.com/plotly/plotly.js/blob/master/CHANGELOG.md#1394----2018-08-02) for more information

### Fixed
 - Fixed error in validation of configkeys
   [plotly/plotly.js#1065](https://github.com/plotly/plotly.py/pull/1065)
 - Fixed error in presentation of named colorscales
   [plotly/plotly.js#1089](https://github.com/plotly/plotly.py/pull/1089)
 - Fixed numerical precision error when using `plotly.tools.make_subplots`
   to create figures with a large number of subplots
   [plotly/plotly.js#1091](https://github.com/plotly/plotly.py/pull/1091)
 - Fixed problem that prevented the use of the `.update` method to initialize
   an array property (e.g. `layout.shapes`)
   [plotly/plotly.js#1091](https://github.com/plotly/plotly.py/pull/1092)
 - Fixed `FigureWidget` problem causing scroll zoom on 3D plots to stutter
   [plotly/plotly.js#1094](https://github.com/plotly/plotly.py/pull/1094) 
 - Fixed invalid `tickmode` property in `matplotlylib`
   [plotly/plotly.js#1101](https://github.com/plotly/plotly.py/pull/1101)

## [3.1.0] - 2018-07-20

### JupyterLab Versions
For use with JupyterLab, the following versions of the following packages
must be installed. See [README.md](README.md) for instructions.

 - Python Packages
   - plotly==3.1.0
   - ipywidgets>=7.2
   - notebook>=5.3
   - jupyterlab==0.32.1
   
 - JupyterLab Extensions
   - plotlywidget@0.2.0
   - @jupyter-widgets/jupyterlab-manager@0.35
   - @jupyterlab/plotly-extension@0.16

### Updated
 - Updated Plotly.js to version 1.39.2
 - See highlights below
 - See [the plotly.js CHANGELOG](https://github.com/plotly/plotly.js/blob/master/CHANGELOG.md#1392----2018-07-16) for more information.
   
### Added
 - Added 3D streamtube traces
   [plotly/plotly.js#2658](https://github.com/plotly/plotly.js/pull/2658)
 - Added support for on-graph text in scattergl traces
 - Added gridshape attribute to polar subplots with values 'circular' (the default) and 'linear' (to draw polygon grids)
   [plotly/plotly.js#2739](https://github.com/plotly/plotly.js/pull/2739)

## [3.0.2] - 2018-07-17
This is a minor bug-fix release to 3.0.0

### JupyterLab plotlywidget version: 0.1.1

### Plotly.js version: 1.38.3

### Fixed
 - Several errors related to numbered subplot labels (e.g. xaxis2, polar3, etc.)
   [GH1057](https://github.com/plotly/plotly.py/pull/1057)
 - Error where the `v` property was ignored in `cone` traces
   [GH1060](https://github.com/plotly/plotly.py/pull/1060)
 - Assorted performance improvements when constructing graph objects
   [GH1061](https://github.com/plotly/plotly.py/pull/1061)
   
## [3.0.1] - 2018-07-17 [YANKED]
Note: This release's installation was broken. It has been removed from PyPI

## [3.0.0] - 2018-07-05

This is a major version with many exciting updates. See the [Introducing plotly.py 3.0.0](https://medium.com/@plotlygraphs/introducing-plotly-py-3-0-0-7bb1333f69c6) post for more information.

### JupyterLab plotlywidget version: 0.1.1

### Plotly.js version: 1.38.3

### Added
- Full Jupyter ipywidgets integration with the new `graph_objs.FigureWidget` class
- `FigureWidget` figures can be updated interactively using property assignment syntax
- The full trace and layout API is generated from the plotly schema to provide a great experience for interactive use in the notebook
- Support for setting array properties as numpy arrays. When numpy arrays are used, ipywidgets binary serialization protocol is used to avoid converting these to JSON strings.
- Context manager API for animation. Run `help(go.Figure().batch_animate)` for the full doc string.
- Perform automatic retries when communicating with plot.ly services. This introduces a new required dependency on the [retrying](https://pypi.org/project/retrying/) library.
- Improved data validation covering the full API with clear, informative error messages. This means that incorrect properties and/or values now always raise a `ValueError` with a description of the error, the invalid property, and the available properties on the level that it was placed in the graph object. Eg. `go.Scatter(foo=123)` raises a validation error. See https://plot.ly/python/reference/ for a reference to all valid properties and values in the Python API.
- Error message for `plotly.figure_factory.create_choropleth` is now helpful to Anaconda users who do not have the correct modules installed for the County Choropleth figure factory.

### Changed / Deprecated
Please see the [migration guid](migration-guide.md) for a full list of the changes and deprecations in version 3.0.0



## [2.7.0] - 2018-05-23
### Updated
- Updated `plotly.min.js` to version 1.38.0.
  - New features include a `3D cone` trace to visualize vector fields.
  - See [the plotly.js CHANGELOG](https://github.com/plotly/plotly.js/blob/master/CHANGELOG.md#1380----2018-05-23) for additional information regarding the updates.

## [2.6.0] - 2018-05-09
### Updated
- Updated `plotly.min.js` to version 1.37.1.
  - New features include a `splom` (scatter plot matrix) trace type.
  - See [the plotly.js CHANGELOG](https://github.com/plotly/plotly.js/blob/master/CHANGELOG.md#1371----2018-05-02) for additional information regarding the updates.
- Error message for `plotly.figure_factory.create_choropleth` is more helpful for Windows users on installing `geopandas` and dependencies including `shapely`.

## [2.5.1] - 2018-03-26
### Fixed
- `plotly.figure_factory.create_choropleth` now works in Windows without raising an OSError. The module now uses cross-platform path tools from `os` to manipulate and manage the shapefiles contained in this package.

## [2.5.0] - 2018-03-12
### Fixed
- `import plotly.figure_factory` does not fail if `pandas` is not installed. See  https://github.com/plotly/plotly.py/pull/958
### Added
- New parameter `fill_percent` to the `.insert` method for the dashboards API. You can now insert a box into the dashboard layout and specify what proportion of the original container box it will occupy. Run `help(plotly.dashboard_objs.Dashboard.insert)` for more information on `fill_percent`.
### Updated
- Updated `plotly.min.js` to version 1.35.2.
  - New features include adding an `automargin` attribute to cartesian axes and a layout `grids` attribute for easy subplot generation.
  - See [the plotly.js CHANGELOG](https://github.com/plotly/plotly.js/blob/master/CHANGELOG.md#1352----2018-03-09) for additional information regarding the updates.
- `plotly.figure_factory.create_choropleth` has changed some of the default plotting options:
  - 'offline_mode' param has been removed from call signature.
  - Persistent selection api for the centroid points is automatically enabled. See https://plot.ly/python/reference/#scatter-selected and https://plot.ly/python/reference/#scatter-unselected for details
  - FIPS values that appear on hover are 0-padded to ensure they are 5 digits.
  - `hover_info='none'` is now default for the county lines data.

## [2.4.1] - 2018-02-21
### Fixed
- The required shapefiles to generate the choropleths via `plotly.figure_factory.create_choropleth` are now shipped in the package data.

## [2.4.0] - 2018-02-16
### Added
- County Choropleth figure factory. Call `help(plotly.figure_factory.create_choropleth)` for examples and how to get started making choropleths of US counties with the Python API.

Note: Calling `plotly.figure_factory.create_choropleth` will fail with an IOError due to missing shapefiles see: https://github.com/plotly/plotly.py/blob/master/CHANGELOG.md#241---2018-02-21

## [2.3.0] - 2018-01-25
### Fixed
- Merged [pull request](https://github.com/plotly/plotly.py/commit/a226e07393c158e01c34c050aaf492da9d77679a) that fixes `GraphWidget` for IPython > v6
### Updated
- Updated `plotly.min.js` to version 1.33.1.
  - New plot types include a `violin` trace type.
  - New features include completely rewritten `scattergl` using `regl` and a completely rewritten polar chart renderer.
  - See [the plotly.js CHANGELOG](https://github.com/plotly/plotly.js/blob/master/CHANGELOG.md#1331----2018-01-24) for additional information regarding the updates.

## [2.2.3] - 2017-12-04
### Added
-`column_width` and `row_width` parameters for `plotly.tools.make_subplots`. Call `help(plotly.tools.make_subplots)` for documentation.
### Updated
- Updated `plotly.min.js` to version 1.31.2.
  - Fixes include adjustments to `table` trace for offline plotting.
  - See [the plotly.js CHANGELOG](https://github.com/plotly/plotly.js/blob/master/CHANGELOG.md#1312----2017-10-23) for additional information regarding the updates.

## [2.2.2] - 2017-11-23
### Added
- Bullet chart figure factory. Call `help(plotly.figure_factory.create_bullet)` for examples and how to get started making bullet charts with the API.

## [2.2.1] - 2017-10-26
### Fixed
- Presentation objects now added to setup.py

## [2.2.0] - 2017-10-26
### Added
- NEW Presentations API for Python! Run `help(plotly.presentation_objs.Presentations)` for help or check out the new [documentation](https://plot.ly/python/presentations-api/)

## [2.1.0] - 2017-10-10
### Updated
- Updated `plotly.min.js` to version 1.31.0.
  - New features include a `table` trace type.
  - See [the plotly.js CHANGELOG](https://github.com/plotly/plotly.js/blob/master/CHANGELOG.md#1310----2017-10-05) for additional information regarding the updates.

## [2.0.16] - 2017-10-06
### Updated
- Updated `plotly.min.js` to version 1.31.0 for `plotly.offline`.
  - See [the plotly.js CHANGELOG](https://github.com/plotly/plotly.js/blob/master/CHANGELOG.md#1310----2017-10-05) for additional information regarding the updates.

## [2.0.15] - 2017-08-22
### Updated
- Updated `plotly.min.js` to version 1.30.0 for `plotly.offline`.
  - See [the plotly.js CHANGELOG](https://github.com/plotly/plotly.js/blob/master/CHANGELOG.md#1300----2017-08-21) for additional information regarding the updates.

## [2.0.14] - 2017-08-09
### Fixed
- [Sharekey enabling issue](https://github.com/plotly/plotly.py/issues/719) where plots were made private instead of secret.
- Issue removing rug plots from violin plots with multiple traces.

## [2.0.13] - 2017-08-04
### Updated
- Updated `plotly.min.js` to version 1.29.1 for `plotly.offline`.
  - See [the plotly.js CHANGELOG]() for additional information regarding the updates.
- `figure_factory.create_gantt` and `figure_factory.create_dendrogram` now return a Plotly figure (consistent with other figure factory chart types).
- `offline.init_notebook_mode()` is now optional when using `offline.iplot()`.

## [2.0.12] - 2017-06-30
### Updated
- Updated `plotly.min.js` to version 1.28.3 for `plotly.offline`.
  - See [the plotly.js CHANGELOG](https://github.com/plotly/plotly.js/blob/master/CHANGELOG.md#1283----2017-06-26) for additional information regarding the updates.
### Added
- `figure_factory.create_facet_grid` now supports histogram, bar, and box traces.

## [2.0.11] - 2017-06-20
### Updated
- Updated `plotly.min.js` to version 1.28.1 for `plotly.offline`.
  - See [the plotly.js CHANGELOG](https://github.com/plotly/plotly.js/blob/master/CHANGELOG.md#1281----2017-06-20) for additional information regarding the updates.

## [2.0.10] - 2017-06-12
### Added
- The figure_factory can now create facet grids with `.create_facet_grid`. Check it out with:
```
import plotly.figure_factory as ff
help(ff.create_facet_grid)
```

## [2.0.9] - 2017-05-30
### Fixed
- Fixes issue [https://github.com/plotly/plotly.py/issues/721](https://github.com/plotly/plotly.py/issues/721). There was an issue when running `import plotly` with old versions of the `decorator` package. We now require installations to use at least version `4.0.6` of the `decorator` package. See [https://github.com/micheles/decorator/blob/master/CHANGES.md](https://github.com/micheles/decorator/blob/master/CHANGES.md) for the `decorator` package changelog.

### Added
- 'sort' parameter to `FF.create_violin` to control whether violin plots are sorted alphabetically.

## [2.0.8] - 2017-04-21
### Added
- Beta: Added API methods that wrap the API endpoint for managing Dash objects on plot.ly. The API interface is under `plotly.api.v2.dash_apps`
- offline embedded plots are now responsive to window resizing when `output_type == "div"` is set in `plotly.offline.iplot()`.
- Offline embedded plots are now responsive to window resizing when `output_type == "div"` is set in `plotly.offline.iplot()`.
- Offline animations are now supported on Plotly Cloud.

### Updated
- Updated `plotly.min.js` to version 1.26.0 for `plotly.offline`.
  - See [the plotly.js CHANGELOG](https://github.com/plotly/plotly.js/blob/master/CHANGELOG.md) for additional information regarding the updates.

### Updated
- `plotly.offline.plot` and `plotly.offline.iplot` now accept various [configuration options](https://plot.ly/javascript/configuration-options/) for their arguments.

## [2.0.7] - 2017-04-07
### Updated
- Updated `plotly.min.js` to version 1.25.0 for `plotly.offline`.
  - See [the plotly.js CHANGELOG](https://github.com/plotly/plotly.js/blob/master/CHANGELOG.md) for additional information regarding the updates.

### Added
- Added check to verify the share key is enabled when secret charts are created.

## [2.0.6] - 2017-03-20
### Added
- Added a new mimetype 'text/vnd.plotly.v1+html' for `iplot` outputs.

## [2.0.5] - 2017-03-07
### Fixed
- `import plotly` was broken in `2.0.3` and `2.0.2` because the new `dashboard_objs` wasn't included in our `setup.py`'s "`packages`". Now it is and `import plotly` and the other features introduced in `2.0.3` and `2.0.2` should work.

## [2.0.4] - 2017-03-07 [YANKED]
Note: This release's installation was broken. It has been removed from PyPI
### Added
- Added `dashboard_objs` to top level import.

## [2.0.3] - 2017-03-06 [YANKED]
Note: This release's installation was broken. It has been removed from PyPI
### Added
- Dashboards can now be created using the API and uploaded to Plotly. Use `import plotly.dashboard_objs` to create a `Dashboard` object. You can learn more about `Dashboard` objects by running `help(plotly.dashboard_objs)` and `help(plotly.plotly.plotly.dashboard_ops)` for uploading and retrieving dashboards from the cloud.


## [2.0.2] - 2017-02-20
### Fixed
- Offline plots created with `plotly.offline.plot` now resize as expected when the window is resized.
- `plotly.figure_factory.create_distplot` now can support more than 10 traces without raising an error. Updated so that if the list of `colors` (default colors too) is less than your number of traces, the color for your traces will loop around to start when it hits the end.

## [2.0.1] - 2017-02-07
### Added
- Support for rendering plots in [nteract](https://nteract.io/)!
  See [https://github.com/nteract/nteract/pull/662](https://github.com/nteract/nteract/pull/662)
  for the associated PR in nteract.
- As part of the above, plotly output now prints with a [custom mimetype](https://github.com/plotly/plotly.py/blob/f65724f06b894a5db94245ee4889c632b887d8ce/plotly/offline/offline.py#L348) - `application/vnd.plotly.v1+json`
- `memoize` decorator added to `plotly.utils`

### Changed
- a `Grid` from `plotly.grid_objs` now accepts a `pandas.Dataframe` as its argument.
- computationally-intensive `graph_reference` functions are memoized.

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
  - See [the plotly.js CHANGELOG](https://github.com/plotly/plotly.js/blob/master/CHANGELOG.md) for additional information regarding the updates.
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
