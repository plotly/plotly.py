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
    description: Comparing a Network Graph created with igraph to one created with
      networkx in Python with Plotly.
    display_as: scientific
    language: python
    layout: base
    name: Network Graphs Comparison
    order: 14
    page_type: u-guide
    permalink: python/igraph-networkx-comparison/
    thumbnail: thumbnail/networks.jpg
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!# Network Graphs with Plotly


#### Comparison
In this tutorial we plot the same network - the coauthorship network of scientists working on network theory and experiment - first as an `igraph.Graph` object, with the Kamada-Kawai layout, and then as a `networkx.Graph`, with the Fruchterman-Reingold layout. Install the Python libraries with `sudo pip install python-igraph` and `sudo pip install networkx`.

The graph data are read from a gml file, posted at UC Irvine [Network Data Repository](http://networkdata.ics.uci.edu/data/netscience/netscience.gml):


#### igraph

```python
import igraph as ig

G=ig.Graph.Read_GML('netscience.gml.txt')
labels=list(G.vs['label'])
N=len(labels)
E=[e.tuple for e in G.es]# list of edges
layt=G.layout('kk') #kamada-kawai layout
type(layt)
```

```python
import plotly.plotly as py
from plotly.graph_objs import *

Xn=[layt[k][0] for k in range(N)]
Yn=[layt[k][1] for k in range(N)]
Xe=[]
Ye=[]
for e in E:
    Xe+=[layt[e[0]][0],layt[e[1]][0], None]
    Ye+=[layt[e[0]][1],layt[e[1]][1], None]

trace1=Scatter(x=Xe,
               y=Ye,
               mode='lines',
               line= dict(color='rgb(210,210,210)', width=1),
               hoverinfo='none'
               )
trace2=Scatter(x=Xn,
               y=Yn,
               mode='markers',
               name='ntw',
               marker=dict(symbol='circle-dot',
                                        size=5,
                                        color='#6959CD',
                                        line=dict(color='rgb(50,50,50)', width=0.5)
                                        ),
               text=labels,
               hoverinfo='text'
               )

axis=dict(showline=False, # hide axis line, grid, ticklabels and  title
          zeroline=False,
          showgrid=False,
          showticklabels=False,
          title=''
          )

width=800
height=800
layout=Layout(title= "Coauthorship network of scientists working on network theory and experiment"+\
              "<br> Data source: <a href='https://networkdata.ics.uci.edu/data.php?id=11'> [1]</a>",
    font= dict(size=12),
    showlegend=False,
    autosize=False,
    width=width,
    height=height,
    xaxis=layout.XAxis(axis),
    yaxis=layout.YAxis(axis),
    margin=layout.Margin(
        l=40,
        r=40,
        b=85,
        t=100,
    ),
    hovermode='closest',
    annotations=[
           dict(
           showarrow=False,
            text='This igraph.Graph has the Kamada-Kawai layout',
            xref='paper',
            yref='paper',
            x=0,
            y=-0.1,
            xanchor='left',
            yanchor='bottom',
            font=dict(
            size=14
            )
            )
        ]
    )

data=[trace1, trace2]
fig=Figure(data=data, layout=layout)
py.iplot(fig, filename='Coautorship-network-igraph')
```

#### Networkx
Now let us read the same gml file, define the network as a networkx.Graph, and plot it with Fruchterman Reingold layout (networkx does not provide the Kamada-Kawai layout).

Because networkx cannot read the gml file (why?!!), we define the networkx.Graph from data provided by the igraph approach above.

```python
import networkx as nx

V=range(N)# list of vertices
g=nx.Graph()
g.add_nodes_from(V)
g.add_edges_from(E)# E is the list of edges

pos=nx.fruchterman_reingold_layout(g)
```

Data for the Plotly plot of the same network but with a different layout:

```python
Xv=[pos[k][0] for k in range(N)]
Yv=[pos[k][1] for k in range(N)]
Xed=[]
Yed=[]
for edge in E:
    Xed+=[pos[edge[0]][0],pos[edge[1]][0], None]
    Yed+=[pos[edge[0]][1],pos[edge[1]][1], None]

trace3=Scatter(x=Xed,
               y=Yed,
               mode='lines',
               line=dict(color='rgb(210,210,210)', width=1),
               hoverinfo='none'
               )
trace4=Scatter(x=Xv,
               y=Yv,
               mode='markers',
               name='net',
               marker=dict(symbol='circle-dot',
                             size=5,
                             color='#6959CD',
                             line=dict(color='rgb(50,50,50)', width=0.5)
                             ),
               text=labels,
               hoverinfo='text'
               )

annot="This networkx.Graph has the Fruchterman-Reingold layout<br>Code:"+\
"<a href='http://nbviewer.ipython.org/gist/empet/07ea33b2e4e0b84193bd'> [2]</a>"

data1=[trace3, trace4]
fig1=Figure(data=data1, layout=layout)
fig1['layout']['annotations'][0]['text']=annot
py.iplot(fig1, filename='Coautorship-network-nx')
```

Zoom in a selected region of nodes to see that edges are also plotted, but due to the node positions assigned by FR layout, they are invisible at the first sight.

We get a similar plot setting pos=nx.spring_layout(g).


#### Reference
See https://plot.ly/python/reference/#scatter for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'igraph_vs_networkx.ipynb', 'python/igraph-networkx-comparison/', 'Python Network Graphs Comparison | plotly',
    'Comparing a Network Graph created with igraph to one created with networkx in Python with Plotly. ',
    name = 'Network Graphs Comparison',
    thumbnail='thumbnail/networks.jpg', language='python',
    has_thumbnail='true', display_as='scientific', order=14,
    ipynb= '~notebook_demo/222')
```

```python

```
