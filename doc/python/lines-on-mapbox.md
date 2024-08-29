---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.3
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
    version: 3.10.0
  plotly:
    description: How to draw a line on tile-based maps in Python with Plotly.
    display_as: maps
    language: python
    layout: base
    name: Lines on Tile Maps
    order: 3
    page_type: example_index
    permalink: python/lines-on-tile-maps/
    redirect_from: python/lines-on-mapbox/
    thumbnail: thumbnail/line_mapbox.jpg
---

### Lines on tile maps using Plotly Express

To draw a line on a map, you either can use `px.line_map` in Plotly Express, or `go.Scattermap` in Plotly Graph Objects. Here's an example of drawing a line on a tile-based map using Plotly Express.

```python
import pandas as pd

us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")
us_cities = us_cities.query("State in ['New York', 'Ohio']")

import plotly.express as px

fig = px.line_map(us_cities, lat="lat", lon="lon", color="State", zoom=3, height=300)

fig.update_layout(map_style="open-street-map", map_zoom=4, map_center_lat = 41,
    margin={"r":0,"t":0,"l":0,"b":0})

fig.show()
```

### Lines on maps from GeoPandas

Given a GeoPandas geo-data frame with `linestring` or `multilinestring` features, one can extra point data and use `px.line_map`.

```python
import plotly.express as px
import geopandas as gpd
import shapely.geometry
import numpy as np
import wget

# download a zipped shapefile
wget.download("https://plotly.github.io/datasets/ne_50m_rivers_lake_centerlines.zip")

# open a zipped shapefile with the zip:// pseudo-protocol
geo_df = gpd.read_file("zip://ne_50m_rivers_lake_centerlines.zip")

lats = []
lons = []
names = []

for feature, name in zip(geo_df.geometry, geo_df.name):
    if isinstance(feature, shapely.geometry.linestring.LineString):
        linestrings = [feature]
    elif isinstance(feature, shapely.geometry.multilinestring.MultiLineString):
        linestrings = feature.geoms
    else:
        continue
    for linestring in linestrings:
        x, y = linestring.xy
        lats = np.append(lats, y)
        lons = np.append(lons, x)
        names = np.append(names, [name]*len(y))
        lats = np.append(lats, None)
        lons = np.append(lons, None)
        names = np.append(names, None)

fig = px.line_map(lat=lats, lon=lons, hover_name=names,
                     map_style="open-street-map", zoom=1)
fig.show()
```

### Lines on maps using `Scattermap` traces

This example uses `go.Scattermap` and sets
the [mode](https://plotly.com/python/reference/scattermapbox/#scattermap-mode) attribute to a combination of markers and line.

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scattermap(
    mode = "markers+lines",
    lon = [10, 20, 30],
    lat = [10, 20,30],
    marker = {'size': 10}))

fig.add_trace(go.Scattermap(
    mode = "markers+lines",
    lon = [-50, -60,40],
    lat = [30, 10, -20],
    marker = {'size': 10}))

fig.update_layout(
    margin ={'l':0,'t':0,'b':0,'r':0},
    map = {
        'center': {'lon': 10, 'lat': 10},
        'style': "open-street-map",
        'center': {'lon': -20, 'lat': -20},
        'zoom': 1})

fig.show()
```

### Mapbox Maps

> Mapbox traces are deprecated and may be removed in a future version of Plotly.py.

The earlier examples using `px.line_map` and `go.Scattermap` use [Maplibre](https://maplibre.org/maplibre-gl-js/docs/) for rendering. These traces were introduced in Plotly.py 5.24 and are now the recommended way to draw lines on tile-based maps. There are also traces that use [Mapbox](https://docs.mapbox.com): `px.line_mapbox` and `go.Scattermapbox`

To plot on Mapbox maps with Plotly you _may_ need a Mapbox account and a public [Mapbox Access Token](https://www.mapbox.com/studio). See our [Mapbox Map Layers](/python/mapbox-layers/) documentation for more information.

To draw a line on your map, you either can use [`px.line_mapbox`](https://plotly.com/python-api-reference/generated/plotly.express.line_mapbox.html) in Plotly Express, or [`Scattermapbox`](https://plotly.com/python/reference/scattermapbox/) traces. Below we show you how to draw a line on Mapbox using Plotly Express.

Here's an example of using `Scattermapbox`.

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scattermapbox(
    mode = "markers+lines",
    lon = [10, 20, 30],
    lat = [10, 20,30],
    marker = {'size': 10}))

fig.add_trace(go.Scattermapbox(
    mode = "markers+lines",
    lon = [-50, -60,40],
    lat = [30, 10, -20],
    marker = {'size': 10}))

fig.update_layout(
    margin ={'l':0,'t':0,'b':0,'r':0},
    mapbox = {
        'center': {'lon': 10, 'lat': 10},
        'style': "open-street-map",
        'center': {'lon': -20, 'lat': -20},
        'zoom': 1})

fig.show()
```

#### Reference

See [function reference for `px.line_map`](https://plotly.com/python-api-reference/generated/plotly.express.line_map) or
https://plotly.com/python/reference/scattermap/ for more information about the attributes available.

For Mapbox-based tile maps, see [function reference for `px.line_mapbox`](https://plotly.com/python-api-reference/generated/plotly.express.line_mapbox) or
https://plotly.com/python/reference/scattermapbox/.
