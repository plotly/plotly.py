# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

## [1.8.2] - 2015-08-11
### Added
- CHANGELOG
- `sharing` keyword argument for `plotly.plotly.plot` and `plotly.plotly.iplot` with options `'public' | 'private' | 'secret'` to control the privacy of the charts. Depreciates `world_readable`

### Changed
- If the response from `plot` or `iplot` contains an error message, raise an exception

### Fixed
- The height of the graph in `iplot` respects the figure's height in layout
