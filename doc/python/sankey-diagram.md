---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.2.1
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
    version: 3.7.3
  plotly:
    description: How to make Sankey Diagrams in Python with Plotly.
    display_as: basic
    language: python
    layout: base
    name: Sankey Diagram
    order: 13
    page_type: u-guide
    permalink: python/sankey-diagram/
    thumbnail: thumbnail/sankey.jpg
---

A [Sankey diagram](https://en.wikipedia.org/wiki/Sankey_diagram) is a flow diagram, in which the width of arrows is proportional to the flow quantity.


### Basic Sankey Diagram
Sankey diagrams visualize the contributions to a flow by defining [source](https://plot.ly/python/reference/#sankey-link-source) to represent the source node, [target](https://plot.ly/python/reference/#sankey-link-target) for the target node, [value](https://plot.ly/python/reference/#sankey-link-value) to set the flow volum, and [label](https://plot.ly/python/reference/#sankey-node-label) that shows the node name. 

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
      source = [0, 1, 0, 2, 3, 3], # indices correspond to labels, eg A1, A2, A2, B1, ...
      target = [2, 3, 3, 4, 4, 5],
      value = [8, 4, 2, 8, 4, 2]
  ))])

fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
fig.show()
```

### More complex Sankey diagram

```python inputHidden=false outputHidden=false
import plotly.graph_objects as go
import urllib, json

url = 'https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json'
response = urllib.request.urlopen(url)
data = json.loads(response.read())
fig = go.Figure(data=[go.Sankey(
    valueformat = ".0f",
    valuesuffix = "TWh",
    # Define nodes
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
      label =  data['data'][0]['link']['label']
  ))])

fig.update_layout(title_text="Energy forecast for 2050<br>Source: Department of Energy & Climate Change, Tom Counsell via <a href='https://bost.ocks.org/mike/sankey/'>Mike Bostock</a>",
                  font_size=10)
fig.show()
```

### Style Sankey Diagram
This example also uses [hovermode](https://plot.ly/python/reference/#layout-hovermode) to enable multiple tooltips. 

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

### Define Node Position

The following example sets [node.x](https://plot.ly/python/reference/#sankey-node-x) and `node.y` to place nodes in the specified locations, except in the `snap arrangement` (default behaviour when `node.x` and `node.y` are not defined) to avoid overlapping of the nodes, therefore, an automatic snapping of elements will be set to define the padding between nodes via [nodepad](https://plot.ly/python/reference/#sankey-node-pad). The other possible arrangements are:<font color='blue'> 1)</font> perpendicular <font color='blue'>2)</font> freeform <font color='blue'>3)</font> fixed

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

See [https://plot.ly/python/reference/#sankey](https://plot.ly/python/reference/#sankey) for more information and options!
