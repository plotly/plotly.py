---
description: How to make Sankey Diagrams in Python with Plotly.
---
A [Sankey diagram](https://en.wikipedia.org/wiki/Sankey_diagram) is a flow diagram, in which the width of arrows is proportional to the flow quantity.


### Basic Sankey Diagram
Sankey diagrams visualize the contributions to a flow by defining [source](reference/graph_objects/sankey-package/Link.md#plotly.graph_objects.sankey.Link.source) to represent the source node, [target](reference/graph_objects/sankey-package/Link.md#plotly.graph_objects.sankey.Link.target) for the target node, [value](reference/graph_objects/sankey-package/Link.md#plotly.graph_objects.sankey.Link.value) to set the flow volume, and [label](reference/graph_objects/sankey-package/Node.md#plotly.graph_objects.sankey.Node.label) that shows the node name.

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
import urllib.request, json

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

Get started  with [the official Dash docs](https://dash.plotly.com/installation) and **learn how to effortlessly [style](https://plotly.com/dash/design-kit/) & publish apps like this with <a class="plotly-red" href="https://plotly.com/dash/">Dash Enterprise</a> or <a class="plotly-red" href="https://plotly.com/cloud/">Plotly Cloud</a>.**


<pre hide_code="true">
```python
from IPython.display import IFrame
snippet_url = 'https://python-docs-dash-snippets.herokuapp.com/python-docs-dash-snippets/'
IFrame(snippet_url + 'sankey-diagram', width='100%', height=1200)
```
</pre>

<iframe src="https://python-docs-dash-snippets.herokuapp.com/python-docs-dash-snippets/sankey-diagram" width="100%" height="1200" style="border:none;"></iframe>

<div style="font-size: 0.9em;"><div style="width: calc(100% - 30px); box-shadow: none; border: thin solid rgb(229, 229, 229);"><div style="padding: 5px;"><div><p><strong>Sign up for Dash Club</strong> → Free cheat sheets plus updates from Chris Parmer and Adam Schroeder delivered to your inbox every two months. Includes tips and tricks, community apps, and deep dives into the Dash architecture.
<u><a href="https://go.plotly.com/dash-club?utm_source=Dash+Club+2022&utm_medium=graphing_libraries&utm_content=inline">Join now</a></u>.</p></div></div></div></div>


### Style Sankey Diagram
This example also uses [hovermode](reference/graph_objects/Layout.md#plotly.graph_objects.Layout.hovermode) to enable multiple tooltips.

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
    title=dict(text="Energy forecast for 2050<br>Source: Department of Energy & Climate Change, Tom Counsell via <a href='https://bost.ocks.org/mike/sankey/'>Mike Bostock</a>"),
    font=dict(size = 10, color = 'white'),
    plot_bgcolor='black',
    paper_bgcolor='black'
)

fig.show()
```

### Link Hover Color

*New in 5.19*

Set `link.hovercolor` to change the colors of links on hover. `link.hovercolor` accepts either one color, specified as a string, that will apply to all links, or a list of colors to specify different colors for each link. Here, we use a list to specify a different color for each link:

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
      source = [0, 1, 0, 2, 3, 3],
      target = [2, 3, 3, 4, 4, 5],
      value = [8, 4, 2, 8, 4, 2],
      hovercolor=["midnightblue", "lightskyblue", "gold", "mediumturquoise", "lightgreen", "cyan"],
  ))])

fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
fig.show()
```

### Hovertemplate and customdata of Sankey diagrams

Links and nodes have their own hovertemplate, in which link- or node-specific attributes can be displayed. To add more data to links and nodes, it is possible to use the `customdata` attribute of `link` and `nodes`, as in the following example. For more information about hovertemplate and customdata, please see the [tutorial on hover text](hover-text-and-formatting.md).

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

The following example sets [node.x](reference/graph_objects/sankey-package/Node.md#plotly.graph_objects.sankey.Node.x) and `node.y` to place nodes in the specified locations, except in the `snap arrangement` (default behaviour when `node.x` and `node.y` are not defined) to avoid overlapping of the nodes, therefore, an automatic snapping of elements will be set to define the padding between nodes via [nodepad](reference/graph_objects/sankey-package/Node.md#plotly.graph_objects.sankey.Node.pad). The other possible arrangements are:<font color='blue'> 1)</font> perpendicular <font color='blue'>2)</font> freeform <font color='blue'>3)</font> fixed

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

### Sankey Diagram with Arrow Links

*New in 5.10*

Create a Sankey diagram with arrow links by setting the `arrowlen` attribute of `link`:

```python
import plotly.graph_objects as go

fig = go.Figure(go.Sankey(
    arrangement='snap',
    node=dict(
        label=['A', 'B', 'C', 'D', 'E', 'F'],
        x=[0.2, 0.1, 0.5, 0.7, 0.3, 0.5],
        y=[0.7, 0.5, 0.2, 0.4, 0.2, 0.3],
        pad=10,
        align="right",
    ),
    link=dict(
        arrowlen=15,
        source=[0, 0, 1, 2, 5, 4, 3, 5],
        target=[5, 3, 4, 3, 0, 2, 2, 3],
        value=[1, 2, 1, 1, 1, 1, 1, 2]
    )
))

fig.show()
```

### Node Alignment

*New in 5.19*

You can set the alignment of nodes using `node.align`. Here are two examples with the same `source` and `target`. The first example has nodes aligned "left" and the second has nodes aligned "right". `node.align` also supports "center" and "justify". "justify" is the default if `node.align` is not set, and is similar to aligning to the "left", except that nodes without outgoing links are moved to the right of the figure.

```python
import plotly.graph_objects as go

fig = go.Figure(go.Sankey(
    arrangement='snap',
    node=dict(
        label=["0", "1", "2", "3", "4", "5"],
        align='left'

    ),
    link=dict(
        arrowlen=15,
        source=[0, 1, 4, 2, 1],
        target=[1, 4, 5, 4, 3],
        value=[4, 2, 3, 1, 2]
    )
))

fig.show()
```

```python
import plotly.graph_objects as go

fig = go.Figure(go.Sankey(
    arrangement='snap',
    node=dict(
        label=["0", "1", "2", "3", "4", "5"],
        align="right",
    ),
    link=dict(
        arrowlen=15,
        source=[0, 1, 4, 2, 1],
        target=[1, 4, 5, 4, 3],
        value=[4, 2, 3, 1, 2]
    )
))

fig.show()
```

### Reference

See the [full reference for `go.Sankey`](reference/graph_objects/Sankey.md) for more information and options!
