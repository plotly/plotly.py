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

The `plotly.figure_factory` module contains dedicated functions for creating very specific types of plots that were at the time of their creation difficult to create with [graph objects](../graph-objects/) and prior to the existence of [Plotly Express](../plotly-express/). As new functionality gets added to [Plotly.js](https://plotly.com/javascript/) and to Plotly Express, certain Figure Factories become unnecessary and are therefore deprecated as "legacy", but remain in the module for backwards-compatibility reasons.

The following types of plots are still difficult to create with Graph Objects or Plotly Express and therefore the corresponding Figure Factories are *not* deprecated:

  * [Dendrograms](../dendrogram/)
  * [Hexagonal Binning Tile Map](../hexbin-mapbox/)
  * [Quiver Plots](../quiver-plots/)
  * [Streamline Plots](../streamline-plots/)
  * [Tables](../figure-factory-table/)
  * [Ternary Contour Plots](../ternary-contour/)
  * [Triangulated Surface Plots](../trisurf/)

Deprecated "legacy" Figure Factories include:

  * [Annotated Heatmaps](../annotated-heatmap/), deprecated by [heatmaps with `px.imshow()`](../heatmaps/)
  * [County Choropleth Maps](../county-choropleth/), deprecated by regular [Choropleth maps with GeoJSON input](../choropleth-maps/)
  * [Distplots](../distplot/), mostly deprecated by [`px.histogram`](../histograms/) except for KDE plots, which `px.histogram` doesn't support yet
  * [Gantt Charts](../gantt/), deprecated by [`px.timeline`](../gantt/)

#### Reference

For more information about the contents of `plotly.figure_factory`, including deprecated methods, please refer to our [API Reference documentation](https://plotly.com/python-api-reference/plotly.figure_factory.html).

