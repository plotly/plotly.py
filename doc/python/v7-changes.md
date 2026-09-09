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
    description: Guide to changes in version 7 of Plotly.py and how to migrate from
      version 6
    display_as: file_settings
    language: python
    layout: base
    name: Changes in Version 7
    order: 9
    page_type: example_index
    permalink: python/v7-migration/
    thumbnail: thumbnail/v4-migration.png
---

This page outlines the changes in Plotly.py version 7 and cases where you may need to update your charts or the tools you use for working with Plotly.py.

Version 7 upgrades the bundled Plotly.js from version 3 to version 4, so it includes the Plotly.js changes as well as the Plotly.py ones. Most figures render without any changes. The sections below cover the cases where you need to update your code.

## Removed Traces

The Mapbox-based traces were deprecated in version 6 and have been removed in version 7. Use the MapLibre-based traces instead, which have the same attributes.

| Removed | Use instead |
|---|---|
| `go.Scattermapbox` | `go.Scattermap` |
| `go.Choroplethmapbox` | `go.Choroplethmap` |
| `go.Densitymapbox` | `go.Densitymap` |
| `px.scatter_mapbox` | `px.scatter_map` |
| `px.line_mapbox` | `px.line_map` |
| `px.choropleth_mapbox` | `px.choropleth_map` |
| `px.density_mapbox` | `px.density_map` |

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scattermap(
    lon=[-73.57, -79.38, -123.12],
    lat=[45.50, 43.65, 49.28],
    mode="markers",
    marker=dict(size=12),
))

fig.show()
```

See [Migrate to MapLibre](/python/mapbox-to-maplibre/) for the full list of changes when moving from the Mapbox traces.

## Removed Attributes

### `layout.mapbox`

The `mapbox` subplot has been removed. Use `layout.map`, which takes the same attributes. In Plotly Express, `mapbox_style` becomes `map_style`.

### `stream`

The `stream` attribute has been removed from all traces. It configured the Chart Studio streaming service, which is no longer available.

### `*src` attributes

Attributes ending in `src` (`xsrc`, `ysrc`, `textsrc`, `marker.colorsrc`, and so on) have been removed, along with `layout.hidesources`. They referenced data sources in Chart Studio.

### Chart Studio configuration options

The `showLink`, `link_text`, `sendData`, `showSources`, and `showEditInChartStudio` configuration options have been removed. To let users share a chart, use `showSendToCloud`, which is enabled by default in version 7 and adds a "Share chart…" button to the mode bar.

## Removed Figure Factories

The deprecated figure factories `create_2d_density`, `create_annotated_heatmap`, `create_bullet`, `create_candlestick`, `create_choropleth`, `create_distplot`, `create_facet_grid`, `create_gantt`, `create_hexbin_mapbox`, `create_ohlc`, `create_scatterplotmatrix`, and `create_violin` have been removed. [Figure Factories](/python/figure-factories/) lists the recommended alternative for each one.

## Static Image Export

Support for Kaleido versions earlier than 1.0.0 has been removed, along with support for Orca. The `engine` argument has been removed from `fig.write_image()`, `fig.to_image()`, `pio.write_image()`, `pio.write_images()`, `pio.to_image()`, `pio.full_figure_for_development()`, and from renderer constructors. See [Static Image Export](/python/static-image-export/).

## Changed Defaults

### Maps fit to your data

`geo` subplots (used by `go.Scattergeo` and `go.Choropleth`) now fit their initial view to the locations they plot: `layout.geo.fitbounds` defaults to `"locations"` instead of `False`. Tile-based `map` subplots do the same, through a new `layout.map.fitbounds` attribute that also defaults to `"locations"`.

Figures that already set a view render unchanged. To get the previous world view, set `fitbounds=False`:

```python
import plotly.graph_objects as go

fig = go.Figure(go.Choropleth(locations=["CAN", "MEX"], z=[1, 2], showscale=False))

fig.update_layout(geo=dict(fitbounds=False))

fig.show()
```

Setting your own view attributes also turns auto-fitting off. On a `geo` subplot, `center` and `projection.scale` always do this, and `projection.rotation`, `lonaxis.range`, and `lataxis.range` do except on a scoped subplot with a clipped projection. On a `map` subplot, `center` or `zoom` does it.

### Overlaying axes share tick positions

An axis that overlays another (`yaxis2.overlaying="y"`) now defaults `tickmode` to `"sync"`: it draws ticks and gridlines at the base axis's positions, labeled from its own range, so the two axes share one grid. Set `tickmode="auto"` on the overlaying axis for the previous behavior of two independent grids.

### Scatter plot matrix axes are linked

`go.Splom` now defaults `axis.matches` to `True`, so axes in the same row and column are linked and pan and zoom together. Plotly Express already set this on the figures it generated. Set `matches=False` on the relevant axes for the previous behavior.

## Color Parsing

Plotly.js now parses colors according to the CSS Color 4 specification. Four color string formats that previously worked no longer produce the same color, and an unparseable color falls back to the attribute's default:

| No longer works | Example | Use instead |
|---|---|---|
| The `hsv()` color function | `"hsv(200, 80%, 80%)"` | `"hsl(200, 67%, 47%)"`, `"hwb()"`, hexadecimal, or `"rgb()"` |
| Comma separated saturation and lightness values without percent units | `"hsl(0, 100, 40)"` | `"hsl(0, 100%, 40%)"`, or the space separated `"hsl(0 100 40)"` |
| Channel values given as fractions of 1 | `"rgb(0.5, 0.5, 0.5)"` (now renders as near black) | `"rgb(128, 128, 128)"` |
| Hexadecimal values without a leading `#` | `"fff"` | `"#fff"` |

These rules apply to color *strings* only. Numeric arrays used with a colorscale are unaffected. Automatically computed contrast colors, such as text on heatmap cells, can also shift slightly around mid-luminance backgrounds.

Separately, `plotly.colors.hex_to_rgb` now parses 3-digit shorthand hexadecimal colors such as `#FFF` correctly.

## Country Names

`locationmode="country names"` is now resolved by [country-iso-search](https://github.com/plotly/country-iso-search) rather than a set of regular expressions. It accepts more forms — ISO-3166 codes, UN M49 numeric codes, flag emoji, historical and native names such as `"Burma"` and `"Türkiye"` — and ignores case, accents, and punctuation. It rejects partial phrases that previously matched by accident. Unrecognized names are logged and their locations are skipped. Use `locationmode="ISO-3"` with ISO codes if you need certainty.

## Tile Map Rendering

Three rendering details changed for `go.Scattermap`:

- Marker icons are tinted with `marker.color`. Previously they were always black. Pass `marker=dict(color="black")` for the previous appearance.
- The Maki icon set was updated from version 2.1 to 8.2. A few icon names were removed between those versions.
- Legend swatches always draw a circle, regardless of `marker.symbol`.

## Sankey Layout

The Sankey layout algorithm was updated (`@plotly/d3-sankey` 0.7.2 to 0.12.3). Node positions and link paths shift slightly for the same data, with links tending to cross less.

Two new Sankey attributes let you override the automatic ordering: `node.sort` and `link.sort`.

For both attributes, the default value `"auto"` reorders nodes within a column, and links within a node, to reduce crossings. `"input"` keeps the order given in `node.label` and in `link.source` / `link.target`, which is useful when the order carries meaning or you need a layout that is stable across renders.

```python
import plotly.graph_objects as go

fig = go.Figure(go.Sankey(
    node=dict(label=["A", "B", "C", "D", "Z", "Y", "X", "W"], pad=15, thickness=20,
              sort="input"),
    link=dict(source=[0, 1, 2, 3], target=[4, 5, 6, 7], value=[4, 3, 2, 1],
              sort="input"),
))

fig.show()
```
A third attribute, `direction`, controls the flow along the `orientation` axis. The default value of `"forward"` results in a chart which flows from left to right horizontally, or top to bottom vertically. Set it to `"reversed"` to create a chart which flows from right to left or bottom to top. See [Sankey Diagram](/python/sankey-diagram/).

## New Traces and Attributes

### `go.Quiver`

Version 7 adds a `Quiver` trace type for 2D vector fields, which supercedes the `create_quiver` figure factory as the recommended approach for creating quiver plots. See [Quiver Plots](/python/quiver-plots/) for more detail.

```python
import plotly.graph_objects as go

fig = go.Figure(go.Quiver(x=[0, 1, 2, 0, 1, 2], y=[0, 0, 0, 1, 1, 1],
                          u=[1, 0.5, 0, 0.5, 0, -0.5], v=[0, 0.5, 1, 0.5, 1, 0.5]))

fig.show()
```

### Geo zoom limits

New attributes `layout.geo.projection.minscale` and `maxscale` clamp how far users can zoom a `geo` subplot. Both are multipliers of `projection.scale`:

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scattergeo(lon=[2.35, 13.4, 12.5, -3.7], lat=[48.86, 52.52, 41.9, 40.42],
                              mode="markers"))

fig.update_layout(geo=dict(scope="europe",
                           projection=dict(scale=1, minscale=0.5, maxscale=4)))

fig.show()
```

## MathJax

Plotly.js now supports MathJax version 3 and version 4 for rendering LaTeX, and support for MathJax version 2 has been removed. If you render figures in an environment that loads MathJax itself, such as a notebook or a custom HTML page, make sure it loads version 3 or later.
