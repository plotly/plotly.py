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
    description: How to make 3D Network Graphs in Python.
    display_as: 3d_charts
    language: python
    layout: base
    name: 3D Network Graphs
    order: 13
    page_type: example_index
    permalink: python/3d-network-graph/
    thumbnail: thumbnail/3dnetwork.jpg
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Network reflecting coappearances of characters in <br>Victor Hugo's novel Les Miserables


We define our graph as an `igraph.Graph` object. [Python `igraph`](http://igraph.org/python/)
is a library for high-performance graph generation  and analysis. Install the Python library with `sudo pip install python-igraph`.

```python
import igraph as ig
```

Read graph data from a `json` file:

```python
import json
import urllib2

data = []
req = urllib2.Request("https://raw.githubusercontent.com/plotly/datasets/master/miserables.json")
opener = urllib2.build_opener()
f = opener.open(req)
data = json.loads(f.read())

print data.keys()
```

Get the number of nodes:

```python
N=len(data['nodes'])
N
```

Define the list of edges and the Graph object from Edges:

```python
L=len(data['links'])
Edges=[(data['links'][k]['source'], data['links'][k]['target']) for k in range(L)]

G=ig.Graph(Edges, directed=False)
```

Extract the node attributes, 'group', and 'name':

```python
data['nodes'][0]
```

```python
labels=[]
group=[]
for node in data['nodes']:
    labels.append(node['name'])
    group.append(node['group'])
```

Get the node positions, set by the Kamada-Kawai layout for 3D graphs:

```python
layt=G.layout('kk', dim=3)
```

`layt` is a list of three elements lists (the coordinates of nodes):

```python
layt[5]
```

Set data for the Plotly plot of the graph:

```python
Xn=[layt[k][0] for k in range(N)]# x-coordinates of nodes
Yn=[layt[k][1] for k in range(N)]# y-coordinates
Zn=[layt[k][2] for k in range(N)]# z-coordinates
Xe=[]
Ye=[]
Ze=[]
for e in Edges:
    Xe+=[layt[e[0]][0],layt[e[1]][0], None]# x-coordinates of edge ends
    Ye+=[layt[e[0]][1],layt[e[1]][1], None]
    Ze+=[layt[e[0]][2],layt[e[1]][2], None]
```

```python
import plotly.plotly as py
import plotly.graph_objs as go

trace1=go.Scatter3d(x=Xe,
               y=Ye,
               z=Ze,
               mode='lines',
               line=dict(color='rgb(125,125,125)', width=1),
               hoverinfo='none'
               )

trace2=go.Scatter3d(x=Xn,
               y=Yn,
               z=Zn,
               mode='markers',
               name='actors',
               marker=dict(symbol='circle',
                             size=6,
                             color=group,
                             colorscale='Viridis',
                             line=dict(color='rgb(50,50,50)', width=0.5)
                             ),
               text=labels,
               hoverinfo='text'
               )

axis=dict(showbackground=False,
          showline=False,
          zeroline=False,
          showgrid=False,
          showticklabels=False,
          title=''
          )

layout = go.Layout(
         title="Network of coappearances of characters in Victor Hugo's novel<br> Les Miserables (3D visualization)",
         width=1000,
         height=1000,
         showlegend=False,
         scene=dict(
             xaxis=dict(axis),
             yaxis=dict(axis),
             zaxis=dict(axis),
        ),
     margin=dict(
        t=100
    ),
    hovermode='closest',
    annotations=[
           dict(
           showarrow=False,
            text="Data source: <a href='http://bost.ocks.org/mike/miserables/miserables.json'>[1] miserables.json</a>",
            xref='paper',
            yref='paper',
            x=0,
            y=0.1,
            xanchor='left',
            yanchor='bottom',
            font=dict(
            size=14
            )
            )
        ],    )
```

```python
data=[trace1, trace2]
fig=go.Figure(data=data, layout=layout)

py.iplot(fig, filename='Les-Miserables')
```

#### Reference
See https://plot.ly/python/reference/#scatter3d for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade

import publisher
publisher.publish(
    'Les-miserables-network.ipynb', 'python/3d-network-graph/', 'Python 3D Network Graphs',
    'How to make 3D Network Graphs in Python. ',
    title = '3D Network Graphs in Python | plotly',
    name = '3D Network Graphs',
    has_thumbnail='true', thumbnail='thumbnail/3dnetwork.jpg',
    language='python', page_type='example_index',
    display_as='3d_charts', order=13,
    ipynb= '~notebook_demo/226')
```

```python

```
