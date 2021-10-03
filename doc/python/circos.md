---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.0
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
    version: 3.9.6
  plotly:
    # description:
    display_as: bio
    language: python
    layout: base
    name: Circos
    order: 1
    page_type: u-guide
    permalink: python/circos/
    thumbnail: thumbnail/circos.png
---

## Default Circos
An example of a default Circos component without any extra properties.

```python
from jupyter_dash import JupyterDash

import json
import urllib.request as urlreq
from dash.dependencies import Input, Output, State
import dash_bio as dashbio
from dash import html
from dash import dcc

app = JupyterDash(__name__)

data = urlreq.urlopen(
    'https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/' +
    'circos_graph_data.json'
).read()

circos_graph_data = json.loads(data.decode('utf-8'))

app.layout = html.Div([
    dashbio.Circos(
        id='my-dashbio-default-circos',
        layout=circos_graph_data['GRCh37'],
        selectEvent={"0": "hover", "1": "click", "2": "both"},
        tracks=[{
            'type': 'CHORDS',
            'data': circos_graph_data['chords'],
            'config': {
                'tooltipContent': {
                    'source': 'source',
                    'sourceID': 'id',
                    'target': 'target',
                    'targetID': 'id',
                    'targetEnd': 'end'
                }
            }
        }]
    ),
    "Graph type:",
    dcc.Dropdown(
        id='histogram-chords-default-circos',
        options=[
            {'label': x, 'value': x}
            for x in ['histogram', 'chords']
        ],
        value='chords'
    ),
    "Event data:",
    html.Div(id='default-circos-output')
])

@app.callback(
    Output('default-circos-output', 'children'),
    Input('my-dashbio-default-circos', 'eventDatum')
)
def update_output(value):
    if value is not None:
        return [html.Div('{}: {}'.format(v.title(), value[v]))
                for v in value.keys()]
    return 'There are no event data. Click or hover on a data point to get more information.'

@app.callback(
    Output('my-dashbio-default-circos', 'tracks'),
    Input('histogram-chords-default-circos', 'value'),
    State('my-dashbio-default-circos', 'tracks')
)
def change_graph_type(value, current):
    if value == 'histogram':
        current[0].update(
            data=circos_graph_data['histogram'],
            type='HISTOGRAM'
        )

    elif value == 'chords':
        current[0].update(
            data=circos_graph_data['chords'],
            type='CHORDS',
            config={
                'tooltipContent': {
                    'source': 'source',
                    'sourceID': 'id',
                    'target': 'target',
                    'targetID': 'id',
                    'targetEnd': 'end'
                }
            }
        )
    return current

app.run_server(mode="inline")
```

## Inner And Outer Radii
Change the inner and outer radii of your Circos graph.


```python
from jupyter_dash import JupyterDash

import json
import urllib.request as urlreq
import dash_bio as dashbio

data = urlreq.urlopen('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/circos_graph_data.json').read()
circos_graph_data = json.loads(data)
app = JupyterDash(__name__)

app.layout = dashbio.Circos(
    layout=circos_graph_data['GRCh37'],
    tracks=[{
        'type': 'CHORDS',
        'data': circos_graph_data['chords']
    }],
    config={
        'innerRadius': 40,
        'outerRadius': 200
    }
)

app.run_server(mode="inline")
```


## Circos Properties


> Access this documentation in your Python terminal with:
> ```
> >>> help(dash_bio.Circos)
> ```
> Our recommended IDE for writing Dash apps is Dash Enterprise's
> **[Data Science Workspaces](https://plotly.com/dash/workspaces)**,
> which has typeahead support for Dash Component Properties.
> **[Find out if your company is using
> Dash Enterprise](https://go.plotly.com/company-lookup)**.


**id** (_string_; optional): The ID of the component to be used in Dash callbacks.

**config** (_dict_; optional): Configuration of overall layout of the graph.

**enableDownloadSVG** (_boolean_; optional): Allow for an SVG snapshot of the Circos graph to be downloaded.

**enableZoomPan** (_boolean_; optional): Allow for zooming and panning the Circos graph.

**eventDatum** (_dict_; optional): A Dash prop that returns data on clicking or hovering of the tracks. Depending on what is specified for prop "selectEvent".

**layout** (_list_ of dicts; required): The overall layout of the Circos graph, provided as a list of dictionaries.

```layout``` is a list of dicts with keys:
- **color** (_string_; required): The color of the block.
- **id** (_string_; required): The id of the block, where it will recieve data from the specified "track" id.
- **label** (_string_; required): The labels of the block.
- **len** (_number_; required): The length of the block.

**selectEvent** (_dict_; optional): A dictionary used to choose whether tracks should return data on click, hover, or both, with the dash prop "eventDatum". The keys of the dictionary represent the index of the list specified for "tracks". Ex: selectEvent={ "0": "hover", "1": "click", "2": "both" },.

**size** (_number_; default `800`): The overall size of the SVG container holding the graph. Set on initilization and unchangeable thereafter.

**style** (_dict_; optional): The CSS styling of the div wrapping the component.

**tracks** (_list_ of dicts; optional): Tracks that specify specific layouts. For a complete list of tracks and usage, please check the docs.

```tracks``` is a list of dicts with keys:
- **color** (_dict_; optional): Specify which dictonary key to grab color values from, in the passed in dataset. This can be a string or an object. If using a string, you can specify hex, RGB, and colors from d3 scale chromatic (Ex: RdYlBu). The key "name" is required for this dictionary, where the input for "name" points to some list of dictionaries color values. Ex: "color": {"name": "some key that refers to color in a data set"}.

    ```color``` is a string

    Or dict with keys:
    - **name** (_string_; required)<br><br>

- **config** (_dict_; optional): The layout of the tracks, where the user can configure innerRadius, outterRadius, ticks, labels, and more.
- **data** (_list_; required): The data that makes up the track. It can be a Json object.
- **id** (_string_; optional): The id of a specific piece of track data.
- **tooltipContent** (_dict_; optional): Specify what data for tooltipContent is displayed. The entry for the "name" key, is any of the keys used in the data loaded into tracks. Ex: "tooltipContent": {"name": "block_id"}, To display all data in the dataset use "all" as the entry for the key "name". Ex: "tooltipContent": {"name": "all"} Ex: This will return (source) + ' > ' + (target) + ': ' + (targetEnd)'. "tooltipContent": { "source": "block_id", "target": "position", "targetEnd": "value" }, Ex: This will return (source)(sourceID) + ' > ' + (target)(targetID) + ': ' (target)(targetEnd)'. "tooltipContent": { "source": "source", "sourceID": "id", "target": "target", "targetID": "id", "targetEnd": "end" }.

    ```tooltipContent``` is a _string_
    
    Or dict with keys:
    - **name** (_string_; required)
    - **source** (_string_; required)
    - **sourceID** (_string_; optional)
    - **target** (_string_; required)
    - **targetEnd** (string; required)
    - **targetID** (string; optional) <br><br>

- **type** (a _value equal to: 'CHORDS', 'HEATMAP', 'HIGHLIGHT', 'HISTOGRAM', 'LINE', 'SCATTER', 'STACK', 'TEXT'_; optional): Specify the type of track this is. Please check the docs for a list of tracks you can use, and ensure the name is typed in all capitals.
