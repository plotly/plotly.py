---
description: How to make a map with Hexagonal Binning of data in Python with Plotly.
---

### Simple Count Hexbin

This page details the use of a [figure factory](figure-factories.md). For more examples with Choropleth maps, see [this page](choropleth-maps.md).

In order to use mapbox styles that require a mapbox token, set the token with `plotly.express`. You can also use styles that do not require a mapbox token. See more information on [this page](../mapbox-layers/).

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

**Error:**
```
Error executing code: [Errno 2] No such file or directory: '.mapbox_token'
Traceback (most recent call last):
  File "/Users/daelenia/Desktop/plotly/plotly.py/bin/run_markdown.py", line 253, in _run_code
    exec(code, exec_globals)
  File "<string>", line 4, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '.mapbox_token'
```

### Count Hexbin with Minimum Count and Opacity

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

**Error:**
```
Error executing code: [Errno 2] No such file or directory: '.mapbox_token'
Traceback (most recent call last):
  File "/Users/daelenia/Desktop/plotly/plotly.py/bin/run_markdown.py", line 253, in _run_code
    exec(code, exec_globals)
  File "<string>", line 4, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '.mapbox_token'
```

### Display the Underlying Data

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

**Error:**
```
Error executing code: [Errno 2] No such file or directory: '.mapbox_token'
Traceback (most recent call last):
  File "/Users/daelenia/Desktop/plotly/plotly.py/bin/run_markdown.py", line 253, in _run_code
    exec(code, exec_globals)
  File "<string>", line 4, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '.mapbox_token'
```

### Compute the Mean Value per Hexbin

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

**Error:**
```
Error executing code: [Errno 2] No such file or directory: '.mapbox_token'
Traceback (most recent call last):
  File "/Users/daelenia/Desktop/plotly/plotly.py/bin/run_markdown.py", line 253, in _run_code
    exec(code, exec_globals)
  File "<string>", line 5, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '.mapbox_token'
```

### Compute the Sum Value per Hexbin

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

**Error:**
```
Error executing code: [Errno 2] No such file or directory: '.mapbox_token'
Traceback (most recent call last):
  File "/Users/daelenia/Desktop/plotly/plotly.py/bin/run_markdown.py", line 253, in _run_code
    exec(code, exec_globals)
  File "<string>", line 5, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '.mapbox_token'
```

### Hexbin with Animation

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

**Error:**
```
Error executing code: [Errno 2] No such file or directory: '.mapbox_token'
Traceback (most recent call last):
  File "/Users/daelenia/Desktop/plotly/plotly.py/bin/run_markdown.py", line 253, in _run_code
    exec(code, exec_globals)
  File "<string>", line 5, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '.mapbox_token'
```

### Reference

For more info on Plotly maps, see [examples of maps](maps.md).<br> For more info on using colorscales with Plotly see the [colorscales page](colorscales.md) <br>For more info on `ff.create_annotated_heatmap()`, see the [full function reference](/reference/figure-factory.md#plotly.figure_factory.create_hexbin_mapbox)
