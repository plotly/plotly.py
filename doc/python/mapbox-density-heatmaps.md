---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.15.1
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
    version: 3.10.4
  plotly:
    description: How to make a Mapbox Density Heatmap in Python with Plotly.
    display_as: maps
    language: python
    layout: base
    name: Mapbox Density Heatmap
    order: 5
    page_type: u-guide
    permalink: python/mapbox-density-heatmaps/
    thumbnail: thumbnail/mapbox-density.png
---

### Stamen Terrain base map (Stadia Maps token needed): density mapbox with `plotly.express`

[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/).

With `px.density_mapbox`, each row of the DataFrame is represented as a point smoothed with a given radius of influence.

To use the mapbox_style "stamen-terrain", you'll need a [Stadia Maps](https://www.stadiamaps.com) token, which you can provide to the `mapbox_accesstoken` parameter on `fig.update_layout`.

Here, we have the token saved in a file called `.mapbox_token`, load it in to the variable `token`, and then pass it to `mapbox_accesstoken`.

<!-- #region -->
```python
import plotly.express as px
import pandas as pd

token = open(".mapbox_token").read() # you will need your own token

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')

fig = px.density_mapbox(df, lat='Latitude', lon='Longitude', z='Magnitude', radius=10,
                        center=dict(lat=0, lon=180), zoom=0,
                        mapbox_style="stamen-terrain")
fig.update_layout(mapbox_accesstoken=token)
fig.show()
```
<!-- #endregion -->

![Stamen terrain Plotly Express example](https://raw.githubusercontent.com/plotly/documentation/gh-pages/all_static/images/stamen-terrain-1.jpeg)


### Stamen Terrain base map (Stadia Maps token needed): density mapbox with `plotly.graph_objects`

If Plotly Express does not provide a good starting point, it is also possible to use [the more generic `go.Densitymapbox` class from `plotly.graph_objects`](/python/graph-objects/).

<!-- #region -->
```python
import plotly.graph_objects as go
import pandas as pd

token = open(".mapbox_token").read() # you will need your own token

quakes = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/earthquakes-23k.csv')

fig = go.Figure(go.Densitymapbox(lat=quakes.Latitude, lon=quakes.Longitude, z=quakes.Magnitude,
                                 radius=10))
fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=180, mapbox_accesstoken=token)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

```
<!-- #endregion -->

![Stamen terrain Graph Objects example](https://raw.githubusercontent.com/plotly/documentation/gh-pages/all_static/images/stamen-terrain-2.jpeg)


#### Reference

See [function reference for `px.(density_mapbox)`](https://plotly.com/python-api-reference/generated/plotly.express.density_mapbox) or https://plotly.com/python/reference/densitymapbox/ for more information about mapbox and their attribute options.
