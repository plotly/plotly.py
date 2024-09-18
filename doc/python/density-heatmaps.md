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
    description: How to make a density heatmap in Python with Plotly.
    display_as: maps
    language: python
    layout: base
    name: Density Heatmap
    order: 6
    page_type: u-guide
    permalink: python/density-heatmaps/
    redirect_from: python/mapbox-density-heatmaps/
    thumbnail: thumbnail/mapbox-density.png
---

### Density map with `plotly.express`

[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/).

With `px.density_map`, each row of the DataFrame is represented as a point smoothed with a given radius of influence.

```python
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')

import plotly.express as px
fig = px.density_map(df, lat='Latitude', lon='Longitude', z='Magnitude', radius=10,
                        center=dict(lat=0, lon=180), zoom=0,
                        map_style="open-street-map")
fig.show()
```

### Density map with `plotly.graph_objects`

If Plotly Express does not provide a good starting point, it is also possible to use [the more generic `go.Densitymap` class from `plotly.graph_objects`](/python/graph-objects/).

```python
import pandas as pd
quakes = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')

import plotly.graph_objects as go
fig = go.Figure(go.Densitymap(lat=quakes.Latitude, lon=quakes.Longitude, z=quakes.Magnitude,
                                 radius=10))
fig.update_layout(map_style="open-street-map", map_center_lon=180)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

<!-- #region -->
### Mapbox Maps

> Mapbox traces are deprecated and may be removed in a future version of Plotly.py.

The earlier examples using `px.density_map` and `go.Densitymap` use [Maplibre](https://maplibre.org/maplibre-gl-js/docs/) for rendering. These traces were introduced in Plotly.py 5.24. These trace types are now the recommended way to make tile-based density heatmaps. There are also traces that use [Mapbox](https://docs.mapbox.com): `density_mapbox` and `go.Densitymapbox`.

To use these trace types, in some cases you _may_ need a Mapbox account and a public [Mapbox Access Token](https://www.mapbox.com/studio). See our [Mapbox Map Layers](/python/mapbox-layers/) documentation for more information.

Here's one of the earlier examples rewritten to use `px.density_mapbox`.

```python
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')

import plotly.express as px
fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', z='Magnitude', radius=10,
                        center=dict(lat=0, lon=180), zoom=0,
                        mapbox_style="open-street-map")
fig.show()
```

<!-- #endregion -->

<!-- #region -->
#### Stamen Terrain base map with Mapbox (Stadia Maps token needed): density heatmap with `plotly.express`

Some base maps require a token. To use "stamen" base maps, you'll need a [Stadia Maps](https://www.stadiamaps.com) token, which you can provide to the `mapbox_accesstoken` parameter on `fig.update_layout`. Here, we have the token saved in a file called `.mapbox_token`, load it in to the variable `token`, and then pass it to `mapbox_accesstoken`.

```python
import plotly.express as px
import pandas as pd

token = open(".mapbox_token").read() # you will need your own token

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')

fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', z='Magnitude', radius=10,
                        center=dict(lat=0, lon=180), zoom=0,
                        map_style="stamen-terrain")
fig.update_layout(mapbox_accesstoken=token)
fig.show()
```


<!-- #endregion -->

#### Reference

See [function reference for `px.(density_map)`](https://plotly.com/python-api-reference/generated/plotly.express.density_mapbox) or https://plotly.com/python/reference/densitymap/ for available attribute options.

For Mapbox-based maps, see [function reference for `px.(density_mapbox)`](https://plotly.com/python-api-reference/generated/plotly.express.density_mapbox) or https://plotly.com/python/reference/densitymapbox/.
