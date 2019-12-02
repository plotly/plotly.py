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
    description: How to make an interactive chord diagram in Python with Plotly and
      iGraph.
    display_as: scientific
    language: python
    layout: base
    name: Python Chord Diagram
    order: 24
    page_type: u-guide
    permalink: python/chord-diagram/
    thumbnail: thumbnail/chord.jpg
---

# Chord Diagrams with Plotly
A circular layout places the graph nodes uniformly on a circle. In this example we illustrate how to  draw the graph edges in order to avoid a cluttered visualization.


### Eurovision Song Contest Example

As an example, we consider a circular graph with the European countries as nodes. Among these countries, some qualified for the grand final [Eurovision Song Contest](http://www.eurovision.tv/page/timeline).

Each european country is a jury member and rates some contestants on a scale from 1 to 12 (in 2015 a contestant from Australia led to adding this country to the graph).

There is a directed edge from a jury member country to a contestant country  if the contestant acquired at least one point from the jury country voters.

The jury member countries are placed uniformly, in alphabetical order, on the unit circle. If there is an edge between two nodes, then we draw a cubic [B&eacute;zier curve](http://nbviewer.ipython.org/github/empet/geom_modeling/blob/master/FP-Bezier-Bspline.ipynb) having  as the first and the last control point the given nodes.

To avoid cluttered edges we adopted the following procedure in choosing the interior control points for the B&eacute;zier curve:

- we consider five  equally spaced  points on the unit circle, corresponding to the angles $0, \:\pi/4$ $\pi/2,\: 3\pi/4, \:\pi$: $$P_1(1,0), \: P_2=(\sqrt{2}/2,\: \sqrt{2}/2),\: P_3(0,1), \: P_4=(-\sqrt{2}/2, \sqrt{2}/2),\:  P_5(-1,0)$$

- define a list,  `Dist`, having as elements the distances between the following pairs of points:
$$(P_1, P_1), \:(P_1, P_2), \: (P_1, P_3),\: (P_1, P_4),\: (P_1, P_5)$$

- In order to assign the control poligon to the B&eacute;zier curve that will be the edge between two connected
nodes, `V[i], V[j]`, we compute the distance between these nodes, and deduce the interval $k$, of two consecutive values in `Dist`, this distance  belongs to.

- Since there are four such intervals indexed $k=0,1,2,3$, we  define the control poligon as follows: $${\bf b}_0=V[i],\:\: {\bf b}_1=V[i]/param,\:\: {\bf b}_2=V[j]/param, \:\:{\bf b}_3=V[j],$$ where `param` is chosen from the list: `params=[1.2, 1.5, 1.8, 2.1]`.

Namely, if the distance(`V[i], V[j]`), belongs to the $K^{th}$ interval associated to `Dist`, then we choose `param= params[K]`.


We processed data provided by [Eurovision Song Contest](http://www.eurovision.tv/page/history/by-year/contest?event=2083#Scoreboard), and saved  the corresponding graph in a `gml` file. Now we can read the `gml` file and define  an [`igraph.Graph`](http://igraph.org/python/) object.

Install the Python libraries with `sudo pip install python-igraph` and `sudo pip install networkx`.

```python
import igraph as ig

G = ig.Graph.Read_GML('Eurovision15.gml')
```

Define the list of nodes (vs stands for vertices):

```python
V=list(G.vs)
G.vs.attributes()# list node attributes
```

Define the  label list. Labels  will be displayed in the Plotly plot:

```python
labels=[v['label']  for v in V]
```

`G.es` is the sequence of graph edges

```python
G.es.attributes()# the edge attributes
```

Get the edge list as a list of tuples, having as elements the end nodes indices:

```python
E=[e.tuple for e in G.es]# list of edges
len(E)
```

Get the list of Contestant countries:

```python
ContestantLst=[G.vs[e[1]] for e in E]
Contestant=list(set([v['label'] for  v in ContestantLst]))
len(Contestant)
```

Get the node positions, assigned by the circular layout:

```python
layt=G.layout('circular') #circular layout
```

`layt` is a list of 2-elements lists, representing the coordinates of nodes placed on the unit circle:

```python
L=len(layt)
layt[7]
```

Define the list of edge weights:

```python
Weights= map(int, G.es["weight"])
```

In the sequel we define a few functions that lead to the edge definition as a B&eacute;zier curve:<br>`dist(A,B)` computes the distance between two 2D points, A, B:

```python
import numpy as np

def dist (A,B):
    return np.linalg.norm(np.array(A)-np.array(B))
dist(layt[0], layt[5])
```

Define the list `Dist` of threshold distances between nodes on the unit circle and the list of parameters for interior control points:

```python
Dist=[0, dist([1,0], 2*[np.sqrt(2)/2]), np.sqrt(2),
      dist([1,0],  [-np.sqrt(2)/2, np.sqrt(2)/2]), 2.0]
params=[1.2, 1.5, 1.8, 2.1]
```

The function `get_idx_interv` returns the index of the interval  the distance `d` belongs to:

```python
def get_idx_interv(d, D):
    k=0
    while(d>D[k]):
        k+=1
    return  k-1
```

Below are defined the function `deCasteljau`  and `BezierCv`. The former  returns the point corresponding to the parameter `t`, on a B&eacute;zier curve of control points given in the list `b`.

The latter returns an array of shape (nr, 2) containing the coordinates of
`nr` points evaluated on the B&eacute;zier curve, at equally spaced parameters in [0,1].

For our purpose the default number of points evaluated on a B&eacute;zier edge is 5. Then setting the Plotly `shape` of the edge line as `spline`, the five points are  interpolated.

```python
class InvalidInputError(Exception):
    pass

def deCasteljau(b,t):
    N=len(b)
    if(N<2):
        raise InvalidInputError("The  control polygon must have at least two points")
    a=np.copy(b) #shallow copy of the list of control points
    for r in range(1,N):
        a[:N-r,:]=(1-t)*a[:N-r,:]+t*a[1:N-r+1,:]
    return a[0,:]

def BezierCv(b, nr=5):
    t=np.linspace(0, 1, nr)
    return np.array([deCasteljau(b, t[k]) for k in range(nr)])
```

Finally we set data and layout for the Plotly plot of the circular graph:

```python
import plotly.plotly as py
import plotly.graph_objs as go

node_color=['rgba(0,51,181, 0.85)'  if v['label'] in Contestant else '#CCCCCC' for v in G.vs]
line_color=['#FFFFFF'  if v['label'] in Contestant else 'rgb(150,150,150)' for v in G.vs]
edge_colors=['#d4daff','#84a9dd', '#5588c8', '#6d8acf']
```

Define the lists of x, respectively y-coordinates of the nodes:

```python
Xn=[layt[k][0] for k in range(L)]
Yn=[layt[k][1] for k in range(L)]
```

On each B&eacute;zier edge, at the point corresponding to the parameter $t=0.9$, one displays the source and the target node labels, as well as  the number of points (votes) assigned by source to target.

```python
lines=[]# the list of dicts defining   edge  Plotly attributes
edge_info=[]# the list of points on edges where  the information is placed

for j, e in enumerate(E):
    A=np.array(layt[e[0]])
    B=np.array(layt[e[1]])
    d=dist(A, B)
    K=get_idx_interv(d, Dist)
    b=[A, A/params[K], B/params[K], B]
    color=edge_colors[K]
    pts=BezierCv(b, nr=5)
    text=V[e[0]]['label']+' to '+V[e[1]]['label']+' '+str(Weights[j])+' pts'
    mark=deCasteljau(b,0.9)
    edge_info.append(go.Scatter(x=[mark[0]],
                             y=[mark[1]],
                             mode='markers',
                             marker=dict( size=0.5,  color=edge_colors),
                             text=text,
                             hoverinfo='text'
                             )
                    )
    lines.append(go.Scatter(x=pts[:,0],
                         y=pts[:,1],
                         mode='lines',
                         line=dict(color=color,
                                  shape='spline',
                                  width=Weights[j]/5#The  width is proportional to the edge weight
                                 ),
                        hoverinfo='none'
                       )
                )

trace2=go.Scatter(x=Xn,
           y=Yn,
           mode='markers',
           name='',
           marker=dict(symbol='circle',
                         size=15,
                         color=node_color,
                         line=dict(color=line_color, width=0.5)
                         ),
           text=labels,
           hoverinfo='text',
           )

axis=dict(showline=False, # hide axis line, grid, ticklabels and  title
          zeroline=False,
          showgrid=False,
          showticklabels=False,
          title=''
          )

def make_annotation(anno_text, y_coord):
    return dict(showarrow=False,
                      text=anno_text,
                      xref='paper',
                      yref='paper',
                      x=0,
                      y=y_coord,
                      xanchor='left',
                      yanchor='bottom',
                      font=dict(size=12)
                     )

anno_text1='Blue nodes mark the countries that are both contestants and jury members'
anno_text2='Grey nodes mark the countries that are only jury members'
anno_text3='There is an edge from a Jury country to a contestant country '+\
           'if the jury country assigned at least one vote to that contestant'
width=800
height=850
title="A circular graph associated to Eurovision Song Contest, 2015<br>Data source:"+\
"<a href='http://www.eurovision.tv/page/history/by-year/contest?event=2083#Scoreboard'> [1]</a>"
layout=go.Layout(title= title,
              font= dict(size=12),
              showlegend=False,
              autosize=False,
              width=width,
              height=height,
              xaxis=dict(axis),
              yaxis=dict(axis),
              margin=dict(l=40,
                            r=40,
                            b=85,
                            t=100,
                          ),
              hovermode='closest',
              annotations=list([make_annotation(anno_text1, -0.07),
                                       make_annotation(anno_text2, -0.09),
                                       make_annotation(anno_text3, -0.11)]
                                     )
              )

data=lines+edge_info+[trace2]
fig=go.Figure(data=data, layout=layout)
py.iplot(fig, filename='Eurovision-15')
```

Now we can compare to the Eurovision graph as a networkx.Graph:

```python
import networkx as nx
import matplotlib.pyplot as plt
%matplotlib inline

G=nx.DiGraph()
G.add_nodes_from(range(L))
G.add_edges_from(E)

plt.figure(figsize=(18,18))
nx.draw_circular(G,node_color='g', edge_color='#909090', node_size=900)
plt.axis('equal')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install publisher --upgrade
import publisher
publisher.publish(
    'chord.ipynb', 'python/chord-diagram/', 'Python Chord Diagram',
    'How to make an interactive chord diagram in Python with Plotly and iGraph. ',
    title = 'Chord Diagram | Plotly',
    thumbnail='thumbnail/chord.jpg', language='python',
    has_thumbnail='true', display_as='scientific', order=24,
    ipynb= '~notebook_demo/225')
```

```python

```
