---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.1
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
    version: 3.6.8
  plotly:
    description: How to make a Mapbox Choropleth Map of US Counties in Python with
      Plotly.
    display_as: maps
    language: python
    layout: base
    name: Mapbox Choropleth Maps
    order: 1
    page_type: example_index
    permalink: python/mapbox-county-choropleth/
    thumbnail: thumbnail/mapbox-choropleth.png
---


#### Mapbox Access Token

To plot on Mapbox maps with Plotly you *may* need a Mapbox account and a public [Mapbox Access Token](https://www.mapbox.com/studio). See our [Mapbox Map Layers](/python/mapbox-layers/) documentation for more information.


Making choropleth maps with `go.Choroplethmapbox` requires two main types of input: GeoJSON-formatted geometry information *where each `feature` has an `id`* and a list of values indexed by feature id. The GeoJSON data is passed to the `geojson` attribute, and the data is passed into the `z` attribute, in the same order as the IDs are passed into the `location` attribute.


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

#### Carto base map: no token needed

```python
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})

import plotly.graph_objects as go

fig = go.Figure(go.Choroplethmapbox(geojson=counties, locations=df.fips, z=df.unemp,
                                    colorscale="Viridis", zmin=0, zmax=12,
                                    marker_opacity=0.5, marker_line_width=0))
fig.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=3, mapbox_center = {"lat": 37.0902, "lon": -95.7129})
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

#### Mapbox Light base map: free token needed

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
See https://plot.ly/python/reference/#choroplethmapbox for more information about mapbox and their attribute options.
