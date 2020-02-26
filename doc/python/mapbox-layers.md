---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: "1.2"
      jupytext_version: 1.3.1
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
    description:
      How to make Mapbox maps in Python with various base layers, with
      or without needing a Mapbox Access token.
    display_as: maps
    language: python
    layout: base
    name: Mapbox Map Layers
    order: 9
    page_type: u-guide
    permalink: python/mapbox-layers/
    thumbnail: thumbnail/mapbox-layers.png
---

<!-- #region -->

### Mapbox Maps vs Geo Maps

Plotly supports two different kinds of maps:

1. **Mapbox maps** are [tile-based maps](https://en.wikipedia.org/wiki/Tiled_web_map). If your figure is created with a `px.scatter_mapbox`, `px.line_mapbox`, `px.choropleth_mapbox` or `px.density_mapbox` function or otherwise contains one or more traces of type `go.Scattermapbox`, `go.Choroplethmapbox` or `go.Densitymapbox`, the `layout.mapbox` object in your figure contains configuration information for the map itself.
2. **Geo maps** are outline-based maps. If your figure is created with a `px.scatter_geo`, `px.line_geo` or `px.choropleth` function or otherwise contains one or more traces of type `go.Scattergeo` or `go.Choropleth`, the `layout.geo` object in your figure contains configuration information for the map itself.

This page documents Mapbox tile-based maps, and the [Geo map documentation](/python/map-configuration/) describes how to configure outline-based maps.

#### How Layers Work in Mapbox Tile Maps

Mapbox tile maps are composed of various layers, of three different types:

1. `layout.mapbox.style` defines is the lowest layers, also known as your "base map"
2. The various traces in `data` are by default rendered above the base map (although this can be controlled via the `below` attribute).
3. `layout.mapbox.layers` is an array that defines more layers that are by default rendered above the traces in `data` (although this can also be controlled via the `below` attribute).

#### Mapbox Access Tokens and When You Need Them

The word "mapbox" in the trace names and `layout.mapbox` refers to the Mapbox.js open-source library, which is integrated into Plotly.py. If your basemap in `layout.mapbox.style` uses data from the Mapbox _service_, then you will need to register for a free account at https://mapbox.com/ and obtain a Mapbox Access token. This token should be provided in `layout.mapbox.access_token` (or, if using Plotly Express, via the `px.set_mapbox_access_token()` configuration function).

> If your `layout.mapbox.style` does not use data from the Mapbox service, you do _not_ need to register for a Mapbox account.

#### Base Maps in `layout.mapbox.style`

The accepted values for `layout.mapbox.style` are one of:

- `"white-bg"` yields an empty white canvas which results in no external HTTP requests
- `"open-street-map"`, `"carto-positron"`, `"carto-darkmatter"`, `"stamen-terrain"`, `"stamen-toner"` or `"stamen-watercolor"` yeild maps composed of _raster_ tiles from various public tile servers which do not require signups or access tokens
- `"basic"`, `"streets"`, `"outdoors"`, `"light"`, `"dark"`, `"satellite"`, or `"satellite-streets"` yeild maps composed of _vector_ tiles from the Mapbox service, and _do_ require a Mapbox Access Token or an on-premise Mapbox installation.
- A Mapbox service style URL, which requires a Mapbox Access Token or an on-premise Mapbox installation.
- A Mapbox Style object as defined at https://docs.mapbox.com/mapbox-gl-js/style-spec/

#### OpenStreetMap tiles: no token needed

Here is a simple map rendered with OpenStreetMaps tiles, without needing a Mapbox Access Token:

<!-- #endregion -->

```python
import pandas as pd
us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

import plotly.express as px

fig = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

<!-- #region -->

#### Using `layout.mapbox.layers` to Specify a Base Map

If you have access to your own private tile servers, or wish to use a tile server not included in the list above, the recommended approach is to set `layout.mapbox.style` to `"white-bg"` and to use `layout.mapbox.layers` with `below` to specify a custom base map.

> If you omit the `below` attribute when using this approach, your data will likely be hidden by fully-opaque raster tiles!

#### Base Tiles from the USGS: no token needed

Here is an example of a map which uses a public USGS imagery map, specified in `layout.mapbox.layers`, and which is rendered _below_ the `data` layer.

<!-- #endregion -->

```python
import pandas as pd
us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

import plotly.express as px

fig = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
fig.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
            ]
        }
      ])
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

<!-- #region -->

#### Base Tiles from the USGS, radar overlay from Environment Canada: no token needed

Here is the same example, with in addition, a WMS layer from Environment Canada which displays near-real-time radar imagery in partly-transparent raster tiles, rendered above the `go.Scattermapbox` trace, as is the default:

<!-- #endregion -->

```python
import pandas as pd
us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

import plotly.express as px

fig = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
fig.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
            ]
        },
        {
            "sourcetype": "raster",
            "source": ["https://geo.weather.gc.ca/geomet/?"
                       "SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX={bbox-epsg-3857}&CRS=EPSG:3857"
                       "&WIDTH=1000&HEIGHT=1000&LAYERS=RADAR_1KM_RDBR&TILED=true&FORMAT=image/png"],
        }
      ])
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

<!-- #region -->

#### Dark tiles from Mapbox service: free token needed

Here is a map rendered with the `"dark"` style from the Mapbox service, which requires an Access Token:

<!-- #endregion -->

```python
token = open(".mapbox_token").read() # you will need your own token

import pandas as pd
us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

import plotly.express as px

fig = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"],
                        color_discrete_sequence=["fuchsia"], zoom=3, height=300)
fig.update_layout(mapbox_style="dark", mapbox_accesstoken=token)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

#### Using a mapbox image layer to display a datashader raster image

See the example in the [plotly and datashader tutorial](/python/datashader).

#### Reference

See https://plot.ly/python/reference/#layout-mapbox for more information and options!
