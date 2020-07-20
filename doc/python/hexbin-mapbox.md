---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.2
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
    version: 3.7.7
  plotly:
    description: How to make a map with Hexagonal Binning of data in Python with Plotly.
    display_as: maps
    language: python
    layout: base
    name: Hexbin Mapbox
    order: 13
    page_type: u-guide
    permalink: python/hexbin-mapbox/
    thumbnail: thumbnail/hexbin_mapbox.jpg
---

#### Simple Count Hexbin

This page details the use of a [figure factory](/python/figure-factories/). For more examples with Choropleth maps, see [this page](/python/choropleth-maps/).

In order to use mapbox styles that require a mapbox token, set the token with `plotly.express`. You can also use styles that do not require a mapbox token. See more information on [this page](/python/mapbox-layers/).

```python
import plotly.figure_factory as ff
import plotly.express as px

px.set_mapbox_access_token(open(".mapbox_token").read())
df = px.data.carshare()

fig = ff.create_hexbin_mapbox(
    data_frame=df, lat="centroid_lat", lon="centroid_lon",
    nx_hexagon=10, opacity=0.9, labels={"color": "Point Count"},
)
fig.update_layout(margin=dict(b=0, t=0, l=0, r=0))
fig.show()
```

#### Count Hexbin with Minimum Count and Opacity

```python
import plotly.figure_factory as ff
import plotly.express as px

px.set_mapbox_access_token(open(".mapbox_token").read())
df = px.data.carshare()

fig = ff.create_hexbin_mapbox(
    data_frame=df, lat="centroid_lat", lon="centroid_lon",
    nx_hexagon=10, opacity=0.5, labels={"color": "Point Count"},
    min_count=1,
)
fig.show()
```

#### Display the Underlying Data

```python
import plotly.figure_factory as ff
import plotly.express as px

px.set_mapbox_access_token(open(".mapbox_token").read())
df = px.data.carshare()

fig = ff.create_hexbin_mapbox(
    data_frame=df, lat="centroid_lat", lon="centroid_lon",
    nx_hexagon=10, opacity=0.5, labels={"color": "Point Count"},
    min_count=1, color_continuous_scale="Viridis",
    show_original_data=True,
    original_data_marker=dict(size=4, opacity=0.6, color="deeppink")
)
fig.show()
```

#### Compute the Mean Value per Hexbin

```python
import plotly.figure_factory as ff
import plotly.express as px
import numpy as np

px.set_mapbox_access_token(open(".mapbox_token").read())
df = px.data.carshare()

fig = ff.create_hexbin_mapbox(
    data_frame=df, lat="centroid_lat", lon="centroid_lon",
    nx_hexagon=10, opacity=0.9, labels={"color": "Average Peak Hour"},
    color="peak_hour", agg_func=np.mean, color_continuous_scale="Icefire", range_color=[0,23]
)
fig.show()
```

#### Compute the Sum Value per Hexbin

```python
import plotly.figure_factory as ff
import plotly.express as px
import numpy as np

px.set_mapbox_access_token(open(".mapbox_token").read())
df = px.data.carshare()

fig = ff.create_hexbin_mapbox(
    data_frame=df, lat="centroid_lat", lon="centroid_lon",
    nx_hexagon=10, opacity=0.9, labels={"color": "Summed Car.Hours"},
    color="car_hours", agg_func=np.sum, color_continuous_scale="Magma"
)
fig.show()
```

#### Hexbin with Animation

```python
import plotly.figure_factory as ff
import plotly.express as px
import numpy as np

px.set_mapbox_access_token(open(".mapbox_token").read())
np.random.seed(0)

N = 500
n_frames = 12
lat = np.concatenate([
    np.random.randn(N) * 0.5 + np.cos(i / n_frames * 2 * np.pi) + 10
    for i in range(n_frames)
])
lon = np.concatenate([
    np.random.randn(N) * 0.5 + np.sin(i / n_frames * 2 * np.pi)
    for i in range(n_frames)
])
frame = np.concatenate([
    np.ones(N, int) * i for i in range(n_frames)
])

fig = ff.create_hexbin_mapbox(
    lat=lat, lon=lon, nx_hexagon=15, animation_frame=frame,
    color_continuous_scale="Cividis", labels={"color": "Point Count", "frame": "Period"},
    opacity=0.5, min_count=1,
    show_original_data=True, original_data_marker=dict(opacity=0.6, size=4, color="deeppink")
)
fig.update_layout(margin=dict(b=0, t=0, l=0, r=0))
fig.layout.sliders[0].pad.t=20
fig.layout.updatemenus[0].pad.t=40
fig.show()
```

#### Reference

For more info on Plotly maps, see: https://plotly.com/python/maps.<br> For more info on using colorscales with Plotly see: https://plotly.com/python/heatmap-and-contour-colorscales/ <br>For more info on `ff.create_annotated_heatmap()`, see the [full function reference](https://plotly.com/python-api-reference/generated/plotly.figure_factory.create_hexbin_mapbox.html#plotly.figure_factory.create_hexbin_mapbox)
