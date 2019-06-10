# Release history

## Unreleased

## 3.0.0 - 2017-06-30
### Breaking changes
* `toml`, `coffee` and `cson` are no longer supported by default. Please see [`options.engines`](README.md#optionsengines) and the [examples](./examples) to learn how to add engines.

### Added
* Support for [excerpts](README.md#optionsexcerpt).
* The returned object now has non-enumerable `matter` and `stringify` properties.

### Changed
* Refactored engines (parsers), so that it's easier to add parsers and stringifiers.
* `options.parsers` was renamed to [`options.engines`](README.md#optionsengines)
