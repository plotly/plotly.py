---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.1
  kernelspec:
    display_name: Python 2
    language: python
    name: python2
  plotly:
    description: How to plot car-travel routes between USA and Canada Telsa Supercharging
      Stations in Python.
    display_as: maps
    language: python
    layout: base
    name: Tesla Supercharging Stations
    order: 10
    page_type: u-guide
    permalink: python/tesla-supercharging-stations/
    thumbnail: thumbnail/tesla-stations.jpg
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Version Check
Run  `pip install plotly --upgrade` to update your Plotly version

```python
import plotly
plotly.__version__
```

#### Mapbox Access Token

To plot on Mapbox maps with Plotly you'll need a Mapbox account and a [Public Mapbox Access Token](https://www.mapbox.com/studio) which you can add to your [Plotly settings](https://plot.ly/settings/mapbox). If you're using a Chart Studio Enterprise server, please see additional instructions here: https://help.plot.ly/mapbox-atlas/.


#### Google Maps API
In order to use the `Google Maps - Directions API`, you need to create an account with Google and get your API key [here](https://developers.google.com/maps/documentation/directions/).

```python
import plotly.plotly as py
from plotly.graph_objs import *

import numpy as np
import requests
import copy
import googlemaps

# add your google maps api key here
my_google_maps_api_key = 'YOUR_API_KEY'
```

#### Parse Tesla Locations
Perform a `GET` request to retrieve the HTML of the [Google Maps Page](https://www.tesla.com/en_CA/findus#/bounds/70,-50,42,-142,d?search=supercharger,&name=Canada) with all Tesla locations, then parse through to collect all the USA, Canada ones and store them in a dictionary. The dictionary is indexed by `address` and each address has a parameter for `postal_code`, `country`, `latitude` and `longitude`. Be Patient, it takes a while.

```python
r = requests.get('https://www.tesla.com/en_CA/findus#/bounds/70,-50,42,-142,d?search=supercharger,&name=Canada')
r_copy = copy.deepcopy(r.text)
```

```python
supercharger_locations = {}
params_for_locations = ['latitude":"', 'longitude":"']
location_param = 'location_id":"'

while True:
    # add address line to the dictionary
    index = r_copy.find(location_param)
    if index == -1:
        break
    index += len(location_param)

    index_end = index
    while r_copy[index_end] != '"':
        index_end += 1
    address_line_1 = r_copy[index:index_end]
    address_line_1 = str(address_line_1)
    supercharger_locations[address_line_1] = {}

    for param in params_for_locations:
        index = r_copy.find(param)
        if index == -1:
            break
        index += len(param)

        index_end = index
        while r_copy[index_end] != '"':
            index_end += 1
        supercharger_locations[address_line_1][param[0:-3]] = r_copy[index:index_end]

    r_copy = r_copy[index_end:len(r.text)]  # slice off the traversed code

all_keys = supercharger_locations.keys()
```

#### Table of Locations
Create a table with a sample of the `supercharger_locations` data.

```python
import plotly.plotly as py
import plotly.figure_factory as ff

data_matrix = [['Location ID', 'Latitude', 'Longitude']]
first_ten_keys = supercharger_locations.keys()[0:10]

for key in first_ten_keys:
    row = [key,
           supercharger_locations[key]['latitude'],
           supercharger_locations[key]['longitude']]
    data_matrix.append(row)

table = ff.create_table(data_matrix)
py.iplot(table, filename='supercharger-locations-sample')
```

#### Plot the Route
The server_key should be replaced with your own Google Maps Directions API key.

Be careful! Make sure you are picking a start and end point that can be driven between, eg. both in the United States of America. Otherwise, the Google Maps API cannot comupute directions and will return an empty list.

```python
def plot_route_between_tesla_stations(address_start, address_end, zoom=3, endpt_size=6):
    start = (supercharger_locations[address_start]['latitude'], supercharger_locations[address_start]['longitude'])
    end = (supercharger_locations[address_end]['latitude'], supercharger_locations[address_end]['longitude'])

    #start = address_start
    #end = address_end

    directions = gmaps.directions(start, end)
    steps = []
    steps.append(start)  # add starting coordinate to trip

    for index in range(len(directions[0]['legs'][0]['steps'])):
        start_coords = directions[0]['legs'][0]['steps'][index]['start_location']
        steps.append((start_coords['lat'], start_coords['lng']))

        if index == len(directions[0]['legs'][0]['steps']) - 1:
            end_coords = directions[0]['legs'][0]['steps'][index]['end_location']
            steps.append((end_coords['lat'], end_coords['lng']))

    steps.append(end)  # add ending coordinate to trip

    mapbox_access_token = "ADD_YOUR_TOKEN_HERE"

    data = Data([
        Scattermapbox(
            lat=[item_x[0] for item_x in steps],
            lon=[item_y[1] for item_y in steps],
            mode='markers+lines',
            marker=Marker(
                size=[endpt_size] + [4 for j in range(len(steps) - 2)] + [endpt_size]
            ),
        )
    ])
    layout = Layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            style='streets',
            center=dict(
                lat=np.mean([float(step[0]) for step in steps]),
                lon=np.mean([float(step[1]) for step in steps]),
            ),
            pitch=0,
            zoom=zoom
        ),
    )

    fig = dict(data=data, layout=layout)
    return fig

server_key = my_google_maps_api_key
gmaps = googlemaps.Client(key=server_key)
address_start = supercharger_locations.keys()[0]
address_end = supercharger_locations.keys()[501]
zoom=12.2
endpt_size=20

fig = plot_route_between_tesla_stations(address_start, address_end, zoom=10.2, endpt_size=20)
py.iplot(fig, filename='tesla-driving-directions-between-superchargers')
```

#### Reference
See http://moderndata.plot.ly/visualize-tesla-supercharging-stations-with-mysql-and-plotly/ to visualize Tesla supercharging stations with MYSQL and https://plot.ly/python/scattermapbox/ for more information on how to plot scatterplots on maps.

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

#! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'tesla-supercharging-stations.ipynb', 'python/tesla-supercharging-stations/', 'Python Tesla Supercharging Stations | Examples | Plotly',
    'How to plot car-travel routes between USA and Canada Telsa Supercharging Stations in Python.',
    title = 'Tesla Supercharging Stations | Plotly',
    name = 'Tesla Supercharging Stations',
    has_thumbnail='true', thumbnail='thumbnail/tesla-stations.jpg',
    language='python',
    display_as='maps', order=10,
    ipynb= '~notebook_demo/124')
```

```python

```
