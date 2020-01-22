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
    description: How to configure and style base maps for Choropleths and Bubble Maps.
    display_as: maps
    language: python
    layout: base
    name: Map Configuration and Styling
    order: 13
    page_type: u-guide
    permalink: python/map-configuration/
    thumbnail: thumbnail/county-level-choropleth.jpg
---

### Mapbox Maps vs Geo Maps

Plotly supports two different kinds of maps:

1. **Mapbox maps** are [tile-based maps](https://en.wikipedia.org/wiki/Tiled_web_map). If your figure is created with a `px.scatter_mapbox`, `px.line_mapbox`, `px.choropleth_mapbox` or `px.density_mapbox` function or otherwise contains one or more traces of type `go.Scattermapbox`, `go.Choroplethmapbox` or `go.Densitymapbox`, the `layout.mapbox` object in your figure contains configuration information for the map itself.
2. **Geo maps** are outline-based maps. If your figure is created with a `px.scatter_geo`, `px.line_geo` or `px.choropleth` function or otherwise contains one or more traces of type `go.Scattergeo` or `go.Choropleth`, the `layout.geo` object in your figure contains configuration information for the map itself.

This page documents Geo outline-based maps, and the [Mapbox Layers documentation](/python/mapbox-layers/) describes how to configure Mapbox tile-based maps.

**Note:** Plotly Express cannot create empty figures, so the examples below mostly create an "empty" map using `fig = go.Figure(go.Scattergeo())`. That said, every configuration option here is equally applicable to non-empty maps created with the Plotly Express `px.scatter_geo`, `px.line_geo` or `px.choropleth` functions.

### Physical Base Maps

Plotly Geo maps have a built-in base map layer composed of "physical" and "cultural" (i.e. administrative border) data from the [Natural Earth Dataset](https://www.naturalearthdata.com/downloads/). Various lines and area fills can be shown or hidden, and their color and line-widths specified. In the [default `plotly` template](/python/templates/), a map frame and physical features such as a coastal outline and filled land areas are shown, at a small-scale 1:110m resolution:

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scattergeo())
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

Here is a map with all physical features enabled and styled, at a larger-scale 1:50m resolution:

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scattergeo())
fig.update_geos(
    resolution=50,
    showcoastlines=True, coastlinecolor="RebeccaPurple",
    showland=True, landcolor="LightGreen",
    showocean=True, oceancolor="LightBlue",
    showlakes=True, lakecolor="Blue",
    showrivers=True, rivercolor="Blue"
)
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

### Disabling Base Maps

In certain cases, such as large scale [choropleth maps](/python/choropleth-maps/), the default physical map can be distracting. In this case the `layout.geo.visible` attribute can be set to `False` to hide all base map attributes except those which are explicitly set to true. For example in the following map we hide all physical features except rivers and lakes, neither of which are shown by default:

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scattergeo())
fig.update_geos(
    visible=False,
    resolution=50,
    showlakes=True, lakecolor="Blue",
    showrivers=True, rivercolor="Blue"
)
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})

fig.show()
```

### Cultural Base Maps

In addition to physical base map features, a "cultural" base map is included which is composed of country borders and selected sub-country borders such as states.

**Note and disclaimer:** cultural features are by definition subject to change, debate and dispute. Plotly includes data from Natural Earth "as-is" and defers to the [Natural Earth policy regarding disputed borders](https://www.naturalearthdata.com/downloads/50m-cultural-vectors/50m-admin-0-countries-2/) which read:

> Natural Earth Vector draws boundaries of countries according to defacto status. We show who actually controls the situation on the ground.

**To create a map with your own cultural features** please refer to our [choropleth documentation](/python/choropleth-maps/).

Here is a map with only cultural features enabled and styled, at a 1:50m resolution, which includes only country boundaries. See below for country sub-unit cultural base map features:

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scattergeo())
fig.update_geos(
    visible=False, resolution=50,
    showcountries=True, countrycolor="RebeccaPurple"
)
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

### Map Projections

Geo maps are drawn according to a given map [projection](https://en.wikipedia.org/wiki/Map_projection) that flattens the Earth's roughly-spherical surface into a 2-dimensional space.

The available projections are `'equirectangular'`, `'mercator'`, `'orthographic'`, `'natural earth'`, `'kavrayskiy7'`, `'miller'`, `'robinson'`, `'eckert4'`, `'azimuthal equal area'`, `'azimuthal equidistant'`, `'conic equal area'`, `'conic conformal'`, `'conic equidistant'`, `'gnomonic'`, `'stereographic'`, `'mollweide'`, `'hammer'`, `'transverse mercator'`, `'albers usa'`, `'winkel tripel'`, `'aitoff'` and `'sinusoidal'`.

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scattergeo())
fig.update_geos(projection_type="orthographic")
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scattergeo())
fig.update_geos(projection_type="natural earth")
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

Map projections can be rotated using the `layout.geo.projection.rotation` attribute, and maps can be translated using the `layout.geo.center` attributed, as well as truncated to a certain longitude and latitude range using the `layout.geo.lataxis.range` and `layout.geo.lonaxis.range`.

The map below uses all of these attributes to demonstrate the types of effect this can yield:

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scattergeo())
fig.update_geos(
    center=dict(lon=-30, lat=-30),
    projection_rotation=dict(lon=30, lat=30, roll=30),
    lataxis_range=[-50,20], lonaxis_range=[0, 200]
)
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

### Automatic Zooming or Bounds Fitting

The `layout.geo.fitbounds` attribute can be set to `locations` to automatically set the center and latitude and longitude range according to the data being plotted. See the [choropleth maps](/python/choropleth-maps/) documentation for more information.

```python
import plotly.express as px

fig = px.line_geo(lat=[0,15,20,35], lon=[5,10,25,30])
fig.update_geos(fitbounds="locations")
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

### Named Map Scopes and Country Sub-Units

In addition, the named "scope" of a map defines a sub-set of the earth's surface to draw. Each scope has a _default projection type, center and roll, as well as bounds_, and certain scopes contain country sub-unit cultural layers certain resolutions, such as `scope="north america"` at `resolution=50` which contains US state and Canadian province boundaries.

The available scopes are: `'world'`, `'usa'`, `'europe'`, `'asia'`, `'africa'`, `'north america'`, `'south america'`.

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scattergeo())
fig.update_geos(
    visible=False, resolution=50, scope="north america",
    showcountries=True, countrycolor="Black",
    showsubunits=True, subunitcolor="Blue"
)
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

The `"usa"` scope contains state boundaries at both resolutions, and uses the special `'albers usa'` projection which moves Alaska and Hawaii closer to the "lower 48 states" to reduce projection distortion and produce a more compact map.

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scattergeo())
fig.update_geos(
    visible=False, resolution=110, scope="usa",
    showcountries=True, countrycolor="Black",
    showsubunits=True, subunitcolor="Blue"
)
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

### Graticules (Latitude and Longitude Grid Lines)

A graticule can be drawn using `layout.geo.lataxis.showgrid` and `layout.geo.lonaxis.showgrid` with options similar to [2d cartesian ticks](/python/axes/).

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scattergeo())
fig.update_geos(lataxis_showgrid=True, lonaxis_showgrid=True)
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

### Reference

See https://plot.ly/python/reference/#layout-geo for more information and chart attribute options!

```python

```
