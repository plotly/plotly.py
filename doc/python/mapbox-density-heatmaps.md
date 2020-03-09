---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: "1.2"
      jupytext_version: 1.3.0
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
    version: 3.7.3
  plotly:
    description: How to make a Mapbox Density Heatmap in Python with Plotly.
    display_as: maps
    language: python
    layout: base
    name: Mapbox Density Heatmap
    order: 6
    page_type: u-guide
    permalink: python/mapbox-density-heatmaps/
    thumbnail: thumbnail/mapbox-density.png
---

#### Mapbox Access Token

To plot on Mapbox maps with Plotly you _may_ need a Mapbox account and a public [Mapbox Access Token](https://www.mapbox.com/studio). See our [Mapbox Map Layers](/python/mapbox-layers/) documentation for more information.

### Stamen Terrain base map (no token needed): density mapbox with `plotly.express`

[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on "tidy" data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/).

With `px.density_mapbox`, each row of the DataFrame is represented as a point smoothed with a given radius of influence.

```python
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')

import plotly.express as px
fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', z='Magnitude', radius=10,
                        center=dict(lat=0, lon=180), zoom=0,
                        mapbox_style="stamen-terrain")
fig.show()
```

### Stamen Terrain base map (no token needed): density mapbox with `plotly.graph_objects`

If Plotly Express does not provide a good starting point, it is also possible to use the more generic `go.Densitymapbox` function from `plotly.graph_objects`.

```python
import pandas as pd
quakes = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')

import plotly.graph_objects as go
fig = go.Figure(go.Densitymapbox(lat=quakes.Latitude, lon=quakes.Longitude, z=quakes.Magnitude,
                                 radius=10))
fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=180)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

#### Reference

See https://plot.ly/python/reference/#densitymapbox for more information about mapbox and their attribute options.
