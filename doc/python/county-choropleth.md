---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
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
    description: How to create colormaped representations of USA counties by FIPS
      values in Python.
    display_as: maps
    language: python
    layout: base
    name: USA County Choropleth Maps
    order: 11
    page_type: u-guide
    permalink: python/county-choropleth/
    thumbnail: thumbnail/county-choropleth-usa-greybkgd.jpg
---

### Deprecation warning


This page describes a legacy "figure factory" method for creating map-like figures using [self-filled scatter traces](/python/shapes). **This is no longer the recommended way to make county-level choropleth maps**, instead we recommend using a [GeoJSON-based approach to making outline choropleth maps](/python/choropleth-maps/) or the alternative [Mapbox tile-based choropleth maps](/python/mapbox-county-choropleth).


#### Required Packages
`geopandas`, `pyshp` and `shapely` must be installed for this figure factory.

Run the following commands to install the correct versions of the following modules:

```python
!pip install geopandas==0.3.0
!pip install pyshp==1.2.10
!pip install shapely==1.6.3
```

If you are using Windows, follow this post to properly install geopandas and dependencies: http://geoffboeing.com/2014/09/using-geopandas-windows/. If you are using Anaconda, do not use PIP to install the packages above. Instead use conda to install them:

<!-- #raw -->
conda install plotly
conda install geopandas
<!-- #endraw -->

#### FIPS and Values
Every US state and county has an assined ID regulated by the US Federal Government under the term FIPS (Federal Information Processing Standards) codes. There are state codes and county codes: the 2016 state and county FIPS codes can be found at the [US Census Website](https://www.census.gov/geographies/reference-files/2016/demo/popest/2016-fips.html).

Combine a state FIPS code (eg. `06` for California) with a county FIPS code of the state (eg. `059` for Orange county) and this new state-county FIPS code (`06059`) uniquely refers to the specified state and county.

`ff.create_choropleth` only needs a list of FIPS codes and a list of values. Each FIPS code points to one county and each corresponding value in `values` determines the color of the county.


#### Simple Example
A simple example of this is a choropleth a few counties in California:

```python
import plotly.figure_factory as ff

fips = ['06021', '06023', '06027',
        '06029', '06033', '06059',
        '06047', '06049', '06051',
        '06055', '06061']
values = range(len(fips))

fig = ff.create_choropleth(fips=fips, values=values)
fig.layout.template = None
fig.show()
```

#### Change the Scope
Even if your FIPS values belong to a single state, the scope defaults to the entire United States as displayed in the example above. Changing the scope of the choropleth shifts the zoom and position of the USA map. You can define the scope with a list of state names and the zoom will automatically adjust to include the state outlines of the selected states.

By default `scope` is set to `['USA']` which the API treats as identical to passing a list of all 50 state names:<br>

`['AK', 'AL', 'CA', ...]`

State abbreviations (eg. `CA`) or the proper names (eg. `California`) as strings are accepted. If the state name is not recognized, the API will throw a Warning and indicate which FIPS values were ignored.

Another param used in the example below is `binning_endpoints`. If your `values` is a list of numbers, you can bin your values into half-open intervals on the real line.

```python
import plotly.figure_factory as ff

import numpy as np
import pandas as pd

df_sample = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/minoritymajority.csv')
df_sample_r = df_sample[df_sample['STNAME'] == 'California']

values = df_sample_r['TOT_POP'].tolist()
fips = df_sample_r['FIPS'].tolist()

colorscale = [
    'rgb(193, 193, 193)',
    'rgb(239,239,239)',
    'rgb(195, 196, 222)',
    'rgb(144,148,194)',
    'rgb(101,104,168)',
    'rgb(65, 53, 132)'
]

fig = ff.create_choropleth(
    fips=fips, values=values, scope=['CA', 'AZ', 'Nevada', 'Oregon', ' Idaho'],
    binning_endpoints=[14348, 63983, 134827, 426762, 2081313], colorscale=colorscale,
    county_outline={'color': 'rgb(255,255,255)', 'width': 0.5}, round_legend_values=True,
    legend_title='Population by County', title='California and Nearby States'
)
fig.layout.template = None
fig.show()
```

#### Single State

```python
import plotly.figure_factory as ff

import numpy as np
import pandas as pd

df_sample = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/minoritymajority.csv')
df_sample_r = df_sample[df_sample['STNAME'] == 'Florida']

values = df_sample_r['TOT_POP'].tolist()
fips = df_sample_r['FIPS'].tolist()

endpts = list(np.mgrid[min(values):max(values):4j])
colorscale = ["#030512","#1d1d3b","#323268","#3d4b94","#3e6ab0",
              "#4989bc","#60a7c7","#85c5d3","#b7e0e4","#eafcfd"]
fig = ff.create_choropleth(
    fips=fips, values=values, scope=['Florida'], show_state_data=True,
    colorscale=colorscale, binning_endpoints=endpts, round_legend_values=True,
    plot_bgcolor='rgb(229,229,229)',
    paper_bgcolor='rgb(229,229,229)',
    legend_title='Population by County',
    county_outline={'color': 'rgb(255,255,255)', 'width': 0.5},
    exponent_format=True,
)
fig.layout.template = None
fig.show()
```

#### Multiple States

```python
import plotly.figure_factory as ff

import pandas as pd

NE_states = ['Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', 'Rhode Island', 'Vermont']
df_sample = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/minoritymajority.csv')
df_sample_r = df_sample[df_sample['STNAME'].isin(NE_states)]

values = df_sample_r['TOT_POP'].tolist()
fips = df_sample_r['FIPS'].tolist()

colorscale = [
    'rgb(68.0, 1.0, 84.0)',
    'rgb(66.0, 64.0, 134.0)',
    'rgb(38.0, 130.0, 142.0)',
    'rgb(63.0, 188.0, 115.0)',
    'rgb(216.0, 226.0, 25.0)'
]

fig = ff.create_choropleth(
    fips=fips, values=values,
    scope=NE_states, county_outline={'color': 'rgb(255,255,255)', 'width': 0.5},
    legend_title='Population per county'

)
fig.update_layout(
    legend_x = 0,
    annotations = {'x': -0.12, 'xanchor': 'left'}
)

fig.layout.template = None
fig.show()
```

#### Simplify County, State Lines
Below is a choropleth that uses several other parameters. For a full list of all available params call `help(ff.create_choropleth)`

- `simplify_county` determines the simplification factor for the counties. The larger the number, the fewer vertices and edges each polygon has. See http://toblerity.org/shapely/manual.html#object.simplify for more information.
- `simplify_state` simplifies the state outline polygon. See the [documentation](http://toblerity.org/shapely/manual.html#object.simplify) for more information.
Default for both `simplify_county` and `simplif_state` is 0.02

Note: This choropleth uses a divergent categorical colorscale. See http://react-colorscales.getforge.io/ for other cool colorscales.

```python
import plotly.figure_factory as ff

import pandas as pd

scope = ['Oregon']
df_sample = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/minoritymajority.csv'
)
df_sample_r = df_sample[df_sample['STNAME'].isin(scope)]

values = df_sample_r['TOT_POP'].tolist()
fips = df_sample_r['FIPS'].tolist()

colorscale = ["#8dd3c7", "#ffffb3", "#bebada", "#fb8072",
              "#80b1d3", "#fdb462", "#b3de69", "#fccde5",
              "#d9d9d9", "#bc80bd", "#ccebc5", "#ffed6f",
              "#8dd3c7", "#ffffb3", "#bebada", "#fb8072",
              "#80b1d3", "#fdb462", "#b3de69", "#fccde5",
              "#d9d9d9", "#bc80bd", "#ccebc5", "#ffed6f",
              "#8dd3c7", "#ffffb3", "#bebada", "#fb8072",
              "#80b1d3", "#fdb462", "#b3de69", "#fccde5",
              "#d9d9d9", "#bc80bd", "#ccebc5", "#ffed6f"]

fig = ff.create_choropleth(
    fips=fips, values=values, scope=scope,
    colorscale=colorscale, round_legend_values=True,
    simplify_county=0, simplify_state=0,
    county_outline={'color': 'rgb(15, 15, 55)', 'width': 0.5},
    state_outline={'width': 1},
    legend_title='pop. per county',
    title='Oregon'
)

fig.layout.template = None
fig.show()
```

#### The Entire USA

```python
import plotly.figure_factory as ff

import numpy as np
import pandas as pd

df_sample = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/laucnty16.csv')
df_sample['State FIPS Code'] = df_sample['State FIPS Code'].apply(lambda x: str(x).zfill(2))
df_sample['County FIPS Code'] = df_sample['County FIPS Code'].apply(lambda x: str(x).zfill(3))
df_sample['FIPS'] = df_sample['State FIPS Code'] + df_sample['County FIPS Code']

colorscale = ["#f7fbff","#ebf3fb","#deebf7","#d2e3f3","#c6dbef","#b3d2e9","#9ecae1",
              "#85bcdb","#6baed6","#57a0ce","#4292c6","#3082be","#2171b5","#1361a9",
              "#08519c","#0b4083","#08306b"]
endpts = list(np.linspace(1, 12, len(colorscale) - 1))
fips = df_sample['FIPS'].tolist()
values = df_sample['Unemployment Rate (%)'].tolist()

fig = ff.create_choropleth(
    fips=fips, values=values,
    binning_endpoints=endpts,
    colorscale=colorscale,
    show_state_data=False,
    show_hover=True, centroid_marker={'opacity': 0},
    asp=2.9, title='USA by Unemployment %',
    legend_title='% unemployed'
)

fig.layout.template = None
fig.show()
```

Also see Mapbox county choropleths made in Python: [https://plot.ly/python/mapbox-county-choropleth/](https://plot.ly/python/mapbox-county-choropleth/)


#### Reference

```python
help(ff.create_choropleth)
```
