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
      How to use datashader to rasterize large datasets, and visualize
      the generated raster data with plotly.
    display_as: scientific
    language: python
    layout: base
    name: Plotly and Datashader
    order: 21
    page_type: u-guide
    permalink: python/datashader/
    thumbnail: thumbnail/datashader.jpg
---

[datashader](https://datashader.org/) creates rasterized representations of large datasets for easier visualization, with a pipeline approach consisting of several steps: projecting the data on a regular grid, creating a color representation of the grid, etc.

### Passing datashader rasters as a mabox image layer

We visualize here the spatial distribution of taxi rides in New York City. A higher density
is observed on major avenues. For more details about mapbox charts, see [the mapbox layers tutorial](/python/mapbox-layers). No mapbox token is needed here.

```python
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/uber-rides-data1.csv')
dff = df.query('Lat < 40.82').query('Lat > 40.70').query('Lon > -74.02').query('Lon < -73.91')

import datashader as ds
cvs = ds.Canvas(plot_width=1000, plot_height=1000)
agg = cvs.points(dff, x='Lon', y='Lat')
# agg is an xarray object, see http://xarray.pydata.org/en/stable/ for more details
coords_lat, coords_lon = agg.coords['Lat'].values, agg.coords['Lon'].values
# Corners of the image, which need to be passed to mapbox
coordinates = [[coords_lon[0], coords_lat[0]],
               [coords_lon[-1], coords_lat[0]],
               [coords_lon[-1], coords_lat[-1]],
               [coords_lon[0], coords_lat[-1]]]

from colorcet import fire
import datashader.transfer_functions as tf
img = tf.shade(agg, cmap=fire)[::-1].to_pil()

import plotly.express as px
# Trick to create rapidly a figure with mapbox axes
fig = px.scatter_mapbox(dff[:1], lat='Lat', lon='Lon', zoom=12)
# Add the datashader image as a mapbox layer image
fig.update_layout(mapbox_style="carto-darkmatter",
                 mapbox_layers = [
                {
                    "sourcetype": "image",
                    "source": img,
                    "coordinates": coordinates
                }]
)
fig.show()
```

### Exploring correlations of a large dataset

Here we explore the flight delay dataset from https://www.kaggle.com/usdot/flight-delays. In order to get a visual impression of the correlation between features, we generate a datashader rasterized array which we plot using a `Heatmap` trace. It creates a much clearer visualization than a scatter plot of (even a fraction of) the data points, as shown below.

Note that instead of datashader it would theoretically be possible to create a [2d histogram](/python/2d-histogram-contour/) with plotly but this is not recommended here because you would need to load the whole dataset (5M rows !) in the browser for plotly.js to compute the heatmap, which is practically not tractable. Datashader offers the possibility to reduce the size of the dataset before passing it to the browser.

```python
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import datashader as ds
df = pd.read_parquet('https://raw.githubusercontent.com/plotly/datasets/master/2015_flights.parquet')
fig = go.Figure(go.Scattergl(x=df['SCHEDULED_DEPARTURE'][::200],
                             y=df['DEPARTURE_DELAY'][::200],
                             mode='markers')
)
fig.update_layout(title_text='A busy plot')
fig.show()
```

```python
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import datashader as ds
df = pd.read_parquet('https://raw.githubusercontent.com/plotly/datasets/master/2015_flights.parquet')

cvs = ds.Canvas(plot_width=100, plot_height=100)
agg = cvs.points(df, 'SCHEDULED_DEPARTURE', 'DEPARTURE_DELAY')
x = np.array(agg.coords['SCHEDULED_DEPARTURE'])
y = np.array(agg.coords['DEPARTURE_DELAY'])

# Assign nan to zero values so that the corresponding pixels are transparent
agg = np.array(agg.values, dtype=np.float)
agg[agg<1] = np.nan

fig = go.Figure(go.Heatmap(
    z=np.log10(agg), x=x, y=y,
    hoverongaps=False,
    hovertemplate='Scheduled departure: %{x:.1f}h <br>Depature delay: %{y} <br>Log10(Count): %{z}',
    colorbar=dict(title='Count (Log)', tickprefix='1.e')))
fig.update_xaxes(title_text='Scheduled departure')
fig.update_yaxes(title_text='Departure delay')
fig.show()

```

```python

```
