---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.4
  kernelspec:
    display_name: Python 3
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
    version: 3.8.11
  plotly:
    description: Figure Factories are dedicated functions for creating very specific
      types of plots.
    display_as: file_settings
    language: python
    layout: base
    name: Figure Factories
    order: 33
    permalink: python/figure-factories/
    thumbnail: thumbnail/streamline.jpg
---

#### `plotly.figure_factory`

The `plotly.figure_factory` module contains dedicated functions for creating very specific types of plots that were at the time of their creation difficult to create with [graph objects](/python/graph-objects/) and prior to the existence of [Plotly Express](/python/plotly-express/). As new functionality gets added to [Plotly.js](https://plotly.com/javascript/) and to Plotly Express, certain Figure Factories become unnecessary and have therefore been removed.

The following types of plots are still difficult to create with Graph Objects or Plotly Express and therefore the corresponding Figure Factories are *not* deprecated:

  * [Dendrograms](/python/dendrogram/)
  * [Hexagonal Binning Tile Map](/python/hexbin-mapbox/)
  * [Quiver Plots](/python/quiver-plots/)
  * [Streamline Plots](/python/streamline-plots/)
  * [Tables](/python/figure-factory-table/)
  * [Ternary Contour Plots](/python/ternary-contour/)
  * [Triangulated Surface Plots](/python/trisurf/)

The following "legacy" Figure Factories have been removed. Use the recommended alternative instead:

  * `create_2d_density`: use [`px.density_heatmap`](/python/2D-Histogram/)
  * `create_annotated_heatmap`: use [`px.imshow`](/python/heatmaps/)
  * `create_bullet`: use [`go.Indicator`](/python/indicator/)
  * `create_candlestick`: use [`go.Candlestick`](/python/candlestick-charts/)
  * `create_choropleth`: use [`px.choropleth`](/python/choropleth-maps/) with custom GeoJSON
  * `create_distplot`: use [Plotly Express](/python/plotly-express/) functions like [`px.histogram`](/python/histograms/)
  * `create_facet_grid`: use [Plotly Express](/python/plotly-express/) functions with the [`facet_row` and `facet_col` arguments](/python/facet-plots/)
  * `create_gantt`: use [`px.timeline`](/python/gantt/)
  * `create_hexbin_mapbox`: use [`create_hexbin_map`](/python/hexbin-mapbox/)
  * `create_ohlc`: use [`go.Ohlc`](/python/ohlc-charts/)
  * `create_scatterplotmatrix`: use [`go.Splom`](/python/splom/)
  * `create_violin`: use [`go.Violin`](/python/violin/)

#### Reference

For more information about the contents of `plotly.figure_factory`, including deprecated methods, please refer to our [API Reference documentation](https://plotly.com/python-api-reference/plotly.figure_factory.html).

