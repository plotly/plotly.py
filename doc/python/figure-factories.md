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

### `plotly.figure_factory`

The `plotly.figure_factory` module contains dedicated functions for creating very specific types of plots that were at the time of their creation difficult to create with [graph objects](graph-objects.md) and prior to the existence of [Plotly Express](plotly-express.md). As new functionality gets added to [Plotly.js](https://plotly.com/javascript/) and to Plotly Express, certain Figure Factories become unnecessary and are therefore deprecated as "legacy", but remain in the module for backwards-compatibility reasons.

The following types of plots are still difficult to create with Graph Objects or Plotly Express and therefore the corresponding Figure Factories are *not* deprecated:

  * [Dendrograms](dendrogram.md)
  * [Hexagonal Binning Tile Map](hexbin-mapbox.md)
  * [Quiver Plots](quiver-plots.md)
  * [Streamline Plots](streamline-plots.md)
  * [Tables](figure-factory-table.md)
  * [Ternary Contour Plots](ternary-contour.md)
  * [Triangulated Surface Plots](trisurf.md)

Deprecated "legacy" Figure Factories include:

  * [Annotated Heatmaps](annotated-heatmap.md), deprecated by [heatmaps with `px.imshow()`](heatmaps.md)
  * [County Choropleth Maps](county-choropleth.md), deprecated by regular [Choropleth maps with GeoJSON input](choropleth-maps.md)
  * [Distplots](distplot.md), mostly deprecated by [`px.histogram`](histograms.md) except for KDE plots, which `px.histogram` doesn't support yet
  * [Gantt Charts](gantt.md), deprecated by [`px.timeline`](gantt.md)

### Reference

For more information about the contents of `plotly.figure_factory`, including deprecated methods, please refer to our [API Reference documentation](reference/figure-factory.md).

