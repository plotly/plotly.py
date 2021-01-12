---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.6.0
  kernel_info:
    name: python2
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
    version: 3.7.6
  plotly:
    description: How to make Sankey Diagrams in Python with Plotly.
    display_as: basic
    language: python
    layout: base
    name: Sankey Diagram
    order: 12
    page_type: u-guide
    permalink: python/sankey-diagram/
    thumbnail: thumbnail/sankey.jpg
---

A [Sankey diagram](https://en.wikipedia.org/wiki/Sankey_diagram) is a flow diagram, in which the width of arrows is proportional to the flow quantity.


### Basic Sankey Diagram
Sankey diagrams visualize the contributions to a flow by defining [source](https://plotly.com/python/reference/sankey/#sankey-link-source) to represent the source node, [target](https://plotly.com/python/reference/sankey/#sankey-link-target) for the target node, [value](https://plotly.com/python/reference/sankey/#sankey-link-value) to set the flow volume, and [label](https://plotly.com/python/reference/sankey/#sankey-node-label) that shows the node name.

```python
import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = ["A1", "A2", "B1", "B2", "C1", "C2"],
      color = "blue"
    ),
    link = dict(
      source = [0, 1, 0, 2, 3, 3], # indices correspond to labels, eg A1, A2, A1, B1, ...
      target = [2, 3, 3, 4, 4, 5],
      value = [8, 4, 2, 8, 4, 2]
  ))])

fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
fig.show()
```

### More complex Sankey diagram with colored links

```python
import plotly.graph_objects as go
import urllib, json

url = 'https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json'
response = urllib.request.urlopen(url)
data = json.loads(response.read())

# override gray link colors with 'source' colors
opacity = 0.4
# change 'magenta' to its 'rgba' value to add opacity
data['data'][0]['node']['color'] = ['rgba(255,0,255, 0.8)' if color == "magenta" else color for color in data['data'][0]['node']['color']]
data['data'][0]['link']['color'] = [data['data'][0]['node']['color'][src].replace("0.8", str(opacity))
                                    for src in data['data'][0]['link']['source']]

fig = go.Figure(data=[go.Sankey(
    valueformat = ".0f",
    valuesuffix = "TWh",
    # Define nodes
    node = dict(
      pad = 15,
      thickness = 15,
      line = dict(color = "black", width = 0.5),
      label =  data['data'][0]['node']['label'],
      color =  data['data'][0]['node']['color']
    ),
    # Add links
    link = dict(
      source =  data['data'][0]['link']['source'],
      target =  data['data'][0]['link']['target'],
      value =  data['data'][0]['link']['value'],
      label =  data['data'][0]['link']['label'],
      color =  data['data'][0]['link']['color']
))])

fig.update_layout(title_text="Energy forecast for 2050<br>Source: Department of Energy & Climate Change, Tom Counsell via <a href='https://bost.ocks.org/mike/sankey/'>Mike Bostock</a>",
                  font_size=10)
fig.show()
```

### Sankey Diagram in Dash

[Dash](https://plotly.com/dash/) is the best way to build analytical apps in Python using Plotly figures. To run the app below, run `pip install dash`, click "Download" to get the code and run `python app.py`.

Get started  with [the official Dash docs](https://dash.plotly.com/installation) and **learn how to effortlessly [style](https://plotly.com/dash/design-kit/) & [deploy](https://plotly.com/dash/app-manager/) apps like this with <a class="plotly-red" href="https://plotly.com/dash/">Dash Enterprise</a>.**


```python hide_code=true
from IPython.display import IFrame
snippet_url = 'https://dash-gallery.plotly.host/python-docs-dash-snippets/'
IFrame(snippet_url + 'sankey-diagram', width='100%', height=630)
```

### Style Sankey Diagram
This example also uses [hovermode](https://plotly.com/python/reference/layout/#layout-hovermode) to enable multiple tooltips.

```python
import plotly.graph_objects as go
import urllib, json

url = 'https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json'
response = urllib.request.urlopen(url)
data = json.loads(response.read())

fig = go.Figure(data=[go.Sankey(
    valueformat = ".0f",
    valuesuffix = "TWh",
    node = dict(
      pad = 15,
      thickness = 15,
      line = dict(color = "black", width = 0.5),
      label =  data['data'][0]['node']['label'],
      color =  data['data'][0]['node']['color']
    ),
    link = dict(
      source =  data['data'][0]['link']['source'],
      target =  data['data'][0]['link']['target'],
      value =  data['data'][0]['link']['value'],
      label =  data['data'][0]['link']['label']
  ))])

fig.update_layout(
    hovermode = 'x',
    title="Energy forecast for 2050<br>Source: Department of Energy & Climate Change, Tom Counsell via <a href='https://bost.ocks.org/mike/sankey/'>Mike Bostock</a>",
    font=dict(size = 10, color = 'white'),
    plot_bgcolor='black',
    paper_bgcolor='black'
)

fig.show()
```

### Hovertemplate and customdata of Sankey diagrams

Links and nodes have their own hovertemplate, in which link- or node-specific attributes can be displayed. To add more data to links and nodes, it is possible to use the `customdata` attribute of `link` and `nodes`, as in the following example. For more information about hovertemplate and customdata, please see the [tutorial on hover text](/python/hover-text-and-formatting/).

```python
import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = ["A1", "A2", "B1", "B2", "C1", "C2"],
      customdata = ["Long name A1", "Long name A2", "Long name B1", "Long name B2",
                    "Long name C1", "Long name C2"],
      hovertemplate='Node %{customdata} has total value %{value}<extra></extra>',
      color = "blue"
    ),
    link = dict(
      source = [0, 1, 0, 2, 3, 3], # indices correspond to labels, eg A1, A2, A2, B1, ...
      target = [2, 3, 3, 4, 4, 5],
      value = [8, 4, 2, 8, 4, 2],
      customdata = ["q","r","s","t","u","v"],
      hovertemplate='Link from node %{source.customdata}<br />'+
        'to node%{target.customdata}<br />has value %{value}'+
        '<br />and data %{customdata}<extra></extra>',
  ))])

fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
fig.show()
```

### Define Node Position

The following example sets [node.x](https://plotly.com/python/reference/sankey/#sankey-node-x) and `node.y` to place nodes in the specified locations, except in the `snap arrangement` (default behaviour when `node.x` and `node.y` are not defined) to avoid overlapping of the nodes, therefore, an automatic snapping of elements will be set to define the padding between nodes via [nodepad](https://plotly.com/python/reference/sankey/#sankey-node-pad). The other possible arrangements are:<font color='blue'> 1)</font> perpendicular <font color='blue'>2)</font> freeform <font color='blue'>3)</font> fixed

```python
import plotly.graph_objects as go

fig = go.Figure(go.Sankey(
    arrangement = "snap",
    node = {
        "label": ["A", "B", "C", "D", "E", "F"],
        "x": [0.2, 0.1, 0.5, 0.7, 0.3, 0.5],
        "y": [0.7, 0.5, 0.2, 0.4, 0.2, 0.3],
        'pad':10},  # 10 Pixels
    link = {
        "source": [0, 0, 1, 2, 5, 4, 3, 5],
        "target": [5, 3, 4, 3, 0, 2, 2, 3],
        "value": [1, 2, 1, 1, 1, 1, 1, 2]}))

fig.show()
```

### Reference

See [https://plotly.com/python/reference/sankey](https://plotly.com/python/reference/sankey/) for more information and options!
