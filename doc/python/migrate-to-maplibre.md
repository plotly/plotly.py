---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.1
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
    version: 3.10.11
  plotly:
    description: Migrating from Mapbox traces to MapLibre traces.
    display_as: maps
    language: python
    layout: base
    name: MapLibre Migration
    order: 1
    page_type: u-guide
    permalink: python/mapbox-to-maplibre/
    thumbnail: thumbnail/mapbox-layers.png
---

## Migrating from Mapbox traces to MapLibre traces

With the release of Plotly.py v5.24.0, we are introducing a new set of trace types for maps with tile underlays, including from Plotly Express:
- `px.scatter_map`
- `px.line_map`
- `px.choropleth_map`
- `px.density_map`

as well as Plotly Graph Objects:
- `go.Choroplethmap`
- `go.Scattermap`
- `go.Densitymap`

These traces replace the existing Mapbox traces, `px.scatter_mapbox`, `px.line_mapbox`, etc., but use [MapLibre](https://maplibre.org) as the map renderer rather than Mapbox.

When switching to the new traces, keep an eye out for improved rendering performance, WebGL2 support, and over time, improved features in the Plotly map traces inherited from the MapLibre renderer, including projection support, globe views, terrain support, and support for modern mapping standards.

You can learn more about the motivations for this change in our [announcement post](https://plotly.com/blog/plotly-is-switching-to-maplibre/).

As a result of removing Mapbox as the rendering engine, we're also removing the Mapbox branding from these trace names. This means that migrating from Mapbox traces to MapLibre traces will require some code changes in your projects.

1. Change trace names from `*mapbox` to `*map`. For any existing trace name ending in `*mapbox`, ensure you've removed the "`box`" suffix.
2. If in use, update `layout.mapbox` argument in your layout configuration to `layout.map`. The nested properties are identical in the new map traces, so no other changes should be required.
3. If in use, update `mapbox_style` to `map_style`.
4. Verify your `map_style` settings. With `mapbox` traces, we bundle `basic`, `streets`, `outdoors`, `light`, `dark`, `satellite`, and `satellite-streets` styles, using Mapbox styling. These style names are still available, but they now reference slightly different styles provided by other tools.

Note that Mapbox API keys are no longer required for Plotly-provided styles, but using external styles in your Plotly maps remains supported with the existing API.

### Style changes
Built-in styles in map traces are free styles from [Carto](https://carto.com) and [ESRI](https://www.esri.com/en-us/home). Several names are re-used from the previous Mapbox styles.
<p align="center">
  <img src="https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/baselines/map_predefined-styles1.png" alt="Style comparison part 1" width="45%" />
  <img src="https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/baselines/map_predefined-styles2.png" alt="Style comparison part 2" width="45%" />
</p>

Compare to the previous Mapbox styles:
<p align="center">
  <img src="https://raw.githubusercontent.com/plotly/graphing-library-docs/master/all_static/images/mapbox_1.png" alt="Style comparison part 1" width="45%" />
  <img src="https://raw.githubusercontent.com/plotly/graphing-library-docs/master/all_static/images/mapbox_2.png" alt="Style comparison part 2" width="45%" />
</p>