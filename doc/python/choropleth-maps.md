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
    description: How to make choropleth maps in Python with Plotly.
    display_as: maps
    language: python
    layout: base
    name: Choropleth Maps
    order: 8
    page_type: u-guide
    permalink: python/choropleth-maps/
    thumbnail: thumbnail/choropleth.jpg
---

A [Choropleth Map](https://en.wikipedia.org/wiki/Choropleth_map) is a map composed of colored polygons. It is used to represent spatial variations of a quantity. This page documents how to build **outline** choropleth maps, but you can also build [choropleth **tile maps** using our Mapbox trace types](/python/mapbox-county-choropleth).

Below we show how to create Choropleth Maps using either Plotly Express' `px.choropleth` function or the lower-level `go.Choropleth` graph object.

#### Base Map Configuration

Plotly figures made with `px.scatter_geo`, `px.line_geo` or `px.choropleth` functions or containing `go.Choropleth` or `go.Scattergeo` graph objects have a `go.layout.Geo` object which can be used to [control the appearance of the base map](/python/map-configuration/) onto which data is plotted.

### Introduction: main parameters for choropleth outline maps

Making choropleth maps requires two main types of input:

1. Geometry information:
   1. This can either be a supplied GeoJSON file where each feature has either an `id` field or some identifying value in `properties`; or
   2. one of the built-in geometries within `plotly`: US states and world countries (see below)
2. A list of values indexed by feature identifier.

The GeoJSON data is passed to the `geojson` argument, and the data is passed into the `color` argument of `px.choropleth` (`z` if using `graph_objects`), in the same order as the IDs are passed into the `location` argument.

**Note** the `geojson` attribute can also be the URL to a GeoJSON file, which can speed up map rendering in certain cases.

### Choropleth Map with plotly.express

[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on "tidy" data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/).

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

### Choropleth map using GeoJSON

**Note** In this example we set `layout.geo.scope` to `usa` to automatically configure the map to display USA-centric data in an appropriate projection. See the [Geo map configuration documentation](/python/map-configuration/) for more information on scopes.

```python
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})

import plotly.express as px

fig = px.choropleth(df, geojson=counties, locations='fips', color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           scope="usa",
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

### Indexing by GeoJSON Properties

If the GeoJSON you are using either does not have an `id` field or you wish you use one of the keys in the `properties` field, you may use the `featureidkey` parameter to specify where to match the values of `locations`.

In the following GeoJSON object/data-file pairing, the values of `properties.district` match the values of the `district` column:

```python
import plotly.express as px

df = px.data.election()
geojson = px.data.election_geojson()

print(df["district"][2])
print(geojson["features"][0]["properties"])
```

To use them together, we set `locations` to `district` and `featureidkey` to `"properties.district"`. The `color` is set to the number of votes by the candidate named Bergeron.

**Note** In this example we set `layout.geo.visible` to `False` to hide the base map and frame, and we set `layout.geo.fitbounds` to `'locations'` to automatically zoom the map to show just the area of interest. See the [Geo map configuration documentation](/python/map-configuration/) for more information on projections and bounds.

```python
import plotly.express as px

df = px.data.election()
geojson = px.data.election_geojson()

fig = px.choropleth(df, geojson=geojson, color="Bergeron",
                    locations="district", featureidkey="properties.district",
                    projection="mercator"
                   )
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

### Discrete Colors

In addition to [continuous colors](/python/colorscales/), we can [discretely-color](/python/discrete-color/) our choropleth maps by setting `color` to a non-numerical column, like the name of the winner of an election.

**Note** In this example we set `layout.geo.visible` to `False` to hide the base map and frame, and we set `layout.geo.fitbounds` to `'locations'` to automatically zoom the map to show just the area of interest. See the [Geo map configuration documentation](/python/map-configuration/) for more information on projections and bounds.

```python
import plotly.express as px

df = px.data.election()
geojson = px.data.election_geojson()

fig = px.choropleth(df, geojson=geojson, color="winner",
                    locations="district", featureidkey="properties.district",
                    projection="mercator", hover_data=["Bergeron", "Coderre", "Joly"]
                   )
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
```

<!-- #region -->

### Using Built-in Country and State Geometries

Plotly comes with two built-in geometries which do not require an external GeoJSON file:

1. USA States
2. Countries as defined in the Natural Earth dataset.

**Note and disclaimer:** cultural (as opposed to physical) features are by definition subject to change, debate and dispute. Plotly includes data from Natural Earth "as-is" and defers to the [Natural Earth policy regarding disputed borders](https://www.naturalearthdata.com/downloads/50m-cultural-vectors/50m-admin-0-countries-2/) which read:

> Natural Earth Vector draws boundaries of countries according to defacto status. We show who actually controls the situation on the ground.

To use the built-in countries geometry, provide `locations` as [three-letter ISO country codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3).

<!-- #endregion -->

```python
import plotly.express as px

df = px.data.gapminder().query("year==2007")
fig = px.choropleth(df, locations="iso_alpha",
                    color="lifeExp", # lifeExp is a column of gapminder
                    hover_name="country", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma)
fig.show()
```

To use the USA States geometry, set `locationmode='USA-states'` and provide `locations` as two-letter state abbreviations:

```python
import plotly.express as px

fig = px.choropleth(locations=["CA", "TX", "NY"], locationmode="USA-states", color=[1,2,3], scope="usa")
fig.show()
```

### Choropleth Maps with go.Choropleth

#### United States Choropleth Map

```python
import plotly.graph_objects as go

# Load data frame and tidy it.
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')

fig = go.Figure(data=go.Choropleth(
    locations=df['code'], # Spatial coordinates
    z = df['total exports'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Reds',
    colorbar_title = "Millions USD",
))

fig.update_layout(
    title_text = '2011 US Agriculture Exports by State',
    geo_scope='usa', # limite map scope to USA
)

fig.show()
```

#### Customize choropleth chart

```python
import plotly.graph_objects as go

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')

for col in df.columns:
    df[col] = df[col].astype(str)

df['text'] = df['state'] + '<br>' + \
    'Beef ' + df['beef'] + ' Dairy ' + df['dairy'] + '<br>' + \
    'Fruits ' + df['total fruits'] + ' Veggies ' + df['total veggies'] + '<br>' + \
    'Wheat ' + df['wheat'] + ' Corn ' + df['corn']

fig = go.Figure(data=go.Choropleth(
    locations=df['code'],
    z=df['total exports'].astype(float),
    locationmode='USA-states',
    colorscale='Reds',
    autocolorscale=False,
    text=df['text'], # hover text
    marker_line_color='white', # line markers between states
    colorbar_title="Millions USD"
))

fig.update_layout(
    title_text='2011 US Agriculture Exports by State<br>(Hover for breakdown)',
    geo = dict(
        scope='usa',
        projection=go.layout.geo.Projection(type = 'albers usa'),
        showlakes=True, # lakes
        lakecolor='rgb(255, 255, 255)'),
)

fig.show()
```

#### World Choropleth Map

```python
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')

fig = go.Figure(data=go.Choropleth(
    locations = df['CODE'],
    z = df['GDP (BILLIONS)'],
    text = df['COUNTRY'],
    colorscale = 'Blues',
    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_tickprefix = '$',
    colorbar_title = 'GDP<br>Billions US$',
))

fig.update_layout(
    title_text='2014 Global GDP',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    annotations = [dict(
        x=0.55,
        y=0.1,
        xref='paper',
        yref='paper',
        text='Source: <a href="https://www.cia.gov/library/publications/the-world-factbook/fields/2195.html">\
            CIA World Factbook</a>',
        showarrow = False
    )]
)

fig.show()
```

#### County Choropleth Figure Factory

Plotly also includes a [legacy "figure factory" for creating US county-level choropleth maps](/python/county-choropleth/).

```python
import plotly.figure_factory as ff

import numpy as np
import pandas as pd

df_sample = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/laucnty16.csv')
df_sample['State FIPS Code'] = df_sample['State FIPS Code'].apply(lambda x: str(x).zfill(2))
df_sample['County FIPS Code'] = df_sample['County FIPS Code'].apply(lambda x: str(x).zfill(3))
df_sample['FIPS'] = df_sample['State FIPS Code'] + df_sample['County FIPS Code']

colorscale = ["#f7fbff", "#ebf3fb", "#deebf7", "#d2e3f3", "#c6dbef", "#b3d2e9", "#9ecae1",
    "#85bcdb", "#6baed6", "#57a0ce", "#4292c6", "#3082be", "#2171b5", "#1361a9",
    "#08519c", "#0b4083", "#08306b"
]
endpts = list(np.linspace(1, 12, len(colorscale) - 1))
fips = df_sample['FIPS'].tolist()
values = df_sample['Unemployment Rate (%)'].tolist()


fig = ff.create_choropleth(
    fips=fips, values=values, scope=['usa'],
    binning_endpoints=endpts, colorscale=colorscale,
    show_state_data=False,
    show_hover=True,
    asp = 2.9,
    title_text = 'USA by Unemployment %',
    legend_title = '% unemployed'
)
fig.layout.template = None
fig.show()
```

#### Reference

See https://plot.ly/python/reference/#choropleth for more information and chart attribute options!
