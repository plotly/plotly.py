# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [1.0.0] - ???

The initial release of the stand-alone `chart-studio` package.  This package contains utilities for interfacing with Plotly's Chart Studio service (both Chart Studio cloud and Chart Studio On-Prem).  Prior to plotly.py version 4, This functionality was included in the `plotly` package under the `plotly.plotly` module. As part of plotly.py version 4, the Chart Studio functionality was removed from the `plotly` package and released in this `chart-studio` package.


### Updated
 - The `chart_studio.plotly.plot`/`iplot` functions have been ported to the Chart Studio [v2 API](https://api.plot.ly/v2/).
 - The `chart_studio.plotly.plot`/`iplot` functions now support uploading figures that contain frames. This makes the legacy `chart_studio.plotly.create_animations`/`icreate_animations` functions unnecessary, though they are still included for backward compatibility.

### Fixed
 - Fixed iframe warning resulting from `chart_studio.plotly.iplot`  
 
### Removed
 - The `fileopt` argument to `chart_studio.plotly.plot`/`iplot` was deprecated in plotly.py version 3.9.0 and has been removed in this initial release of the `chart-studio` package.
