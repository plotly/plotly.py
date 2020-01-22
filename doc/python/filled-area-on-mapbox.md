---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: "1.1"
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
    description: How to make an area on Map in Python with Plotly.
    display_as: maps
    language: python
    layout: base
    name: Filled Area on Maps
    order: 3
    page_type: example_index
    permalink: python/filled-area-on-mapbox/
    thumbnail: thumbnail/area.jpg
---

<!-- #region -->

### Mapbox Access Token and Base Map Configuration

To plot on Mapbox maps with Plotly you _may_ need a Mapbox account and a public [Mapbox Access Token](https://www.mapbox.com/studio). See our [Mapbox Map Layers](/python/mapbox-layers/) documentation for more information.

There are three different ways to show a filled area in a Mapbox map:

1. Use a [Scattermapbox](https://plot.ly/python/reference/#scattermapbox) trace and set `fill` attribute to 'toself'
2. Use a Mapbox layout (i.e. by minimally using an empty [Scattermapbox](https://plot.ly/python/reference/#scattermapbox) trace) and add a GeoJSON layer
3. Use the [Choroplethmapbox](https://plot.ly/python/mapbox-county-choropleth/) trace type
   <!-- #endregion -->

### Filled `Scattermapbox` Trace

The following example uses `Scattermapbox` and sets `fill = 'toself'`

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scattermapbox(
    fill = "toself",
    lon = [-74, -70, -70, -74], lat = [47, 47, 45, 45],
    marker = { 'size': 10, 'color': "orange" }))

fig.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': {'lon': -73, 'lat': 46 },
        'zoom': 5},
    showlegend = False)

fig.show()
```

### Multiple Filled Areas with a `Scattermapbox` trace

The following example shows how to use `None` in your data to draw multiple filled areas. Such gaps in trace data are unconnected by default, but this can be controlled via the [connectgaps](https://plot.ly/python/reference/#scattermapbox-connectgaps) attribute.

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scattermapbox(
    mode = "lines", fill = "toself",
    lon = [-10, -10, 8, 8, -10, None, 30, 30, 50, 50, 30, None, 100, 100, 80, 80, 100],
    lat = [30, 6, 6, 30, 30,    None, 20, 30, 30, 20, 20, None, 40, 50, 50, 40, 40]))

fig.update_layout(
    mapbox = {'style': "stamen-terrain", 'center': {'lon': 30, 'lat': 30}, 'zoom': 2},
    showlegend = False,
    margin = {'l':0, 'r':0, 'b':0, 't':0})

fig.show()
```

### GeoJSON Layers

In this map we add a GeoJSON layer.

```python
import plotly.graph_objects as go

fig = go.Figure(go.Scattermapbox(
    mode = "markers",
    lon = [-73.605], lat = [45.51],
    marker = {'size': 20, 'color': ["cyan"]}))

fig.update_layout(
    mapbox = {
        'style': "stamen-terrain",
        'center': { 'lon': -73.6, 'lat': 45.5},
        'zoom': 12, 'layers': [{
            'source': {
                'type': "FeatureCollection",
                'features': [{
                    'type': "Feature",
                    'geometry': {
                        'type': "MultiPolygon",
                        'coordinates': [[[
                            [-73.606352888, 45.507489991], [-73.606133883, 45.50687600],
                            [-73.605905904, 45.506773980], [-73.603533905, 45.505698946],
                            [-73.602475870, 45.506856969], [-73.600031904, 45.505696003],
                            [-73.599379992, 45.505389066], [-73.599119902, 45.505632008],
                            [-73.598896977, 45.505514039], [-73.598783894, 45.505617001],
                            [-73.591308727, 45.516246185], [-73.591380782, 45.516280145],
                            [-73.596778656, 45.518690062], [-73.602796770, 45.521348046],
                            [-73.612239983, 45.525564037], [-73.612422919, 45.525642061],
                            [-73.617229085, 45.527751983], [-73.617279234, 45.527774160],
                            [-73.617304713, 45.527741334], [-73.617492052, 45.527498362],
                            [-73.617533258, 45.527512253], [-73.618074188, 45.526759105],
                            [-73.618271651, 45.526500673], [-73.618446320, 45.526287943],
                            [-73.618968507, 45.525698560], [-73.619388002, 45.525216750],
                            [-73.619532966, 45.525064183], [-73.619686662, 45.524889290],
                            [-73.619787038, 45.524770086], [-73.619925742, 45.524584939],
                            [-73.619954486, 45.524557690], [-73.620122362, 45.524377961],
                            [-73.620201713, 45.524298907], [-73.620775593, 45.523650879]
                        ]]]
                    }
                }]
            },
            'type': "fill", 'below': "traces", 'color': "royalblue"}]},
    margin = {'l':0, 'r':0, 'b':0, 't':0})

fig.show()
```

#### Reference

See https://plot.ly/python/reference/#scattermapbox for more information about mapbox and their attribute options.
