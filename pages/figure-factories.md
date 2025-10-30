---
description: Figure Factories are dedicated functions for creating very specific types
  of plots.
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

