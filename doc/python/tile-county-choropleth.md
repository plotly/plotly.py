---
description: How to make tile choropleth maps in Python with Plotly.
redirect_from: python/mapbox-county-choropleth/
---
A [Choropleth Map](https://en.wikipedia.org/wiki/Choropleth_map) is a map composed of colored polygons. It is used to represent spatial variations of a quantity. This page documents how to build **tile-map** choropleth maps, but you can also build [**outline** choropleth maps](choropleth-maps.md).

Below we show how to create Choropleth Maps using either Plotly Express' `px.choropleth_map` function or the lower-level `go.Choroplethmap` graph object.

### Introduction: main parameters for choropleth tile maps

Making choropleth maps requires two main types of input:

1. GeoJSON-formatted geometry information where each feature has either an `id` field or some identifying value in `properties`.
2. A list of values indexed by feature identifier.

The GeoJSON data is passed to the `geojson` argument, and the data is passed into the `color` argument of `px.choropleth_map` (`z` if using `graph_objects`), in the same order as the IDs are passed into the `location` argument.

!!! note

    The `geojson` attribute can also be the URL to a GeoJSON file, which can speed up map rendering in certain cases.

#### GeoJSON with `feature.id`

Here we load a GeoJSON file containing the geometry information for US counties, where `feature.id` is a [FIPS code](https://en.wikipedia.org/wiki/FIPS_county_code).

```python
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

counties["features"][0]
```

#### Data indexed by `id`

Here we load unemployment data by county, also indexed by [FIPS code](https://en.wikipedia.org/wiki/FIPS_county_code).

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})
df.head()
```

### Choropleth map using plotly.express and carto base map

[Plotly Express](plotly-express.md) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](px-arguments.md) and produces [easy-to-style figures](styling-plotly-express.md).

With `px.choropleth_map`, each row of the DataFrame is represented as a region of the choropleth.

```python
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})

import plotly.express as px

fig = px.choropleth_map(df, geojson=counties, locations='fips', color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           map_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

### Choropleth maps in Dash

[Dash](https://plotly.com/dash/) is the best way to build analytical apps in Python using Plotly figures. To run the app below, run `pip install dash`, click "Download" to get the code and run `python app.py`.

Get started  with [the official Dash docs](https://dash.plotly.com/installation) and **learn how to effortlessly [style](https://plotly.com/dash/design-kit/) & publish apps like this with <a class="plotly-red" href="https://plotly.com/dash/">Dash Enterprise</a> or <a class="plotly-red" href="https://plotly.com/cloud/">Plotly Cloud</a>.**


<pre hide_code="true">
```python
from IPython.display import IFrame
snippet_url = 'https://python-docs-dash-snippets.herokuapp.com/python-docs-dash-snippets/'
IFrame(snippet_url + 'mapbox-county-choropleth', width='100%', height=1200)
```
</pre>

<iframe src="https://python-docs-dash-snippets.herokuapp.com/python-docs-dash-snippets/mapbox-county-choropleth" width="100%" height="1200" style="border:none;"></iframe>

<div style="font-size: 0.9em;"><div style="width: calc(100% - 30px); box-shadow: none; border: thin solid rgb(229, 229, 229);"><div style="padding: 5px;"><div><p><strong>Sign up for Dash Club</strong> → Free cheat sheets plus updates from Chris Parmer and Adam Schroeder delivered to your inbox every two months. Includes tips and tricks, community apps, and deep dives into the Dash architecture.
<u><a href="https://go.plotly.com/dash-club?utm_source=Dash+Club+2022&utm_medium=graphing_libraries&utm_content=inline">Join now</a></u>.</p></div></div></div></div>


### Indexing by GeoJSON Properties

If the GeoJSON you are using either does not have an `id` field or you wish you use one of the keys in the `properties` field, you may use the `featureidkey` parameter to specify where to match the values of `locations`.

In the following GeoJSON object/data-file pairing, the values of `properties.district` match the values of the `district` column:

```python
import plotly.express as px

df = px.data.election()
geojson = px.data.election_geojson()

print(df["district"][2])
print(geojson["features"][0]["properties"])
```

To use them together, we set `locations` to `district` and `featureidkey` to `"properties.district"`. The `color` is set to the number of votes by the candidate named Bergeron.

```python
import plotly.express as px

df = px.data.election()
geojson = px.data.election_geojson()

fig = px.choropleth_map(df, geojson=geojson, color="Bergeron",
                           locations="district", featureidkey="properties.district",
                           center={"lat": 45.5517, "lon": -73.7073},
                           map_style="carto-positron", zoom=9)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

### Discrete Colors

In addition to [continuous colors](colorscales.md), we can [discretely-color](discrete-color.md) our choropleth maps by setting `color` to a non-numerical column, like the name of the winner of an election.

```python
import plotly.express as px

df = px.data.election()
geojson = px.data.election_geojson()

fig = px.choropleth_map(df, geojson=geojson, color="winner",
                           locations="district", featureidkey="properties.district",
                           center={"lat": 45.5517, "lon": -73.7073},
                           map_style="carto-positron", zoom=9)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

### Using GeoPandas Data Frames

`px.choropleth_map` accepts the `geometry` of a [GeoPandas](https://geopandas.org/) data frame as the input to `geojson` if the `geometry` contains polygons.

```python
import plotly.express as px
import geopandas as gpd

df = px.data.election()
geo_df = gpd.GeoDataFrame.from_features(
    px.data.election_geojson()["features"]
).merge(df, on="district").set_index("district")

fig = px.choropleth_map(geo_df,
                           geojson=geo_df.geometry,
                           locations=geo_df.index,
                           color="Joly",
                           center={"lat": 45.5517, "lon": -73.7073},
                           map_style="open-street-map",
                           zoom=8.5)
fig.show()
```

### Choropleth map using plotly.graph_objects and carto base map

If Plotly Express does not provide a good starting point, it is also possible to use [the more generic `go.Choroplethmap` class from `plotly.graph_objects`](graph-objects.md).

```python
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})

import plotly.graph_objects as go

fig = go.Figure(go.Choroplethmap(geojson=counties, locations=df.fips, z=df.unemp,
                                    colorscale="Viridis", zmin=0, zmax=12,
                                    marker_opacity=0.5, marker_line_width=0))
fig.update_layout(map_style="carto-positron",
                  map_zoom=3, map_center = {"lat": 37.0902, "lon": -95.7129})
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

### Mapbox Maps

!!! note

    Mapbox traces are deprecated and may be removed in a future version of Plotly.py.

The earlier examples using `px.choropleth_map` and `go.Choroplethmap` use [Maplibre](https://maplibre.org/maplibre-gl-js/docs/) for rendering. These traces were introduced in Plotly.py 5.24 and are now the recommended way to create tile-based choropleth maps. There are also choropleth traces that use [Mapbox](https://docs.mapbox.com): `px.choropleth_mapbox` and `go.Choroplethmapbox`

To plot on Mapbox maps with Plotly you _may_ need a Mapbox account and a public [Mapbox Access Token](https://www.mapbox.com/studio). See our [Mapbox Map Layers](../mapbox-layers/) documentation for more information.

Here's an exmaple of using the Mapbox Light base map, which requires a free token.

```python
token = open(".mapbox_token").read() # you will need your own token

from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})

import plotly.graph_objects as go

fig = go.Figure(go.Choroplethmapbox(geojson=counties, locations=df.fips, z=df.unemp,
                                    colorscale="Viridis", zmin=0, zmax=12, marker_line_width=0))
fig.update_layout(mapbox_style="light", mapbox_accesstoken=token,
                  mapbox_zoom=3, mapbox_center = {"lat": 37.0902, "lon": -95.7129})
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

#### Reference

See [function reference for `px.choropleth_map`](reference/plotly-express.md#plotly.express.choropleth_map) or the [full reference for `go.Choroplethmap`](reference/graph_objects/Choroplethmap.md) for more information about the attributes available.

For (deprecated) Mapbox-based tile maps, see [function reference for `px.choropleth_mapbox`](reference/plotly-express.md#plotly.express.choropleth_mapbox) or the [full reference for `go.Choroplethmapbox`](reference/graph_objects/Choroplethmapbox.md).
