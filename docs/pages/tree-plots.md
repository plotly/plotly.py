---
description: How to make interactive tree-plot in Python with Plotly. An examples
  of a tree-plot in Plotly.
---

### Set Up Tree with [igraph](http://igraph.org/python/)

Install igraph with the following version:

```
igraph==0.11.9
```

```python
import igraph
from igraph import Graph, EdgeSeq
nr_vertices = 25
v_label = list(map(str, range(nr_vertices)))
G = Graph.Tree(nr_vertices, 2) # 2 stands for children number
lay = G.layout('rt')

position = {k: lay[k] for k in range(nr_vertices)}
Y = [lay[k][1] for k in range(nr_vertices)]
M = max(Y)

es = EdgeSeq(G) # sequence of edges
E = [e.tuple for e in G.es] # list of edges

L = len(position)
Xn = [position[k][0] for k in range(L)]
Yn = [2*M-position[k][1] for k in range(L)]
Xe = []
Ye = []
for edge in E:
    Xe+=[position[edge[0]][0],position[edge[1]][0], None]
    Ye+=[2*M-position[edge[0]][1],2*M-position[edge[1]][1], None]

labels = v_label
```

### Create Plotly Traces

```python
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(x=Xe,
                   y=Ye,
                   mode='lines',
                   line=dict(color='rgb(210,210,210)', width=1),
                   hoverinfo='none'
                   ))
fig.add_trace(go.Scatter(x=Xn,
                  y=Yn,
                  mode='markers',
                  name='bla',
                  marker=dict(symbol='circle-dot',
                                size=18,
                                color='#6175c1',    #'#DB4551',
                                line=dict(color='rgb(50,50,50)', width=1)
                                ),
                  text=labels,
                  hoverinfo='text',
                  opacity=0.8
                  ))
```

### Create Text Inside the Circle via Annotations

```python
def make_annotations(pos, text, font_size=10, font_color='rgb(250,250,250)'):
    L=len(pos)
    if len(text)!=L:
        raise ValueError('The lists pos and text must have the same len')
    annotations = []
    for k in range(L):
        annotations.append(
            dict(
                text=labels[k], # or replace labels with a different list for the text within the circle
                x=pos[k][0], y=2*M-position[k][1],
                xref='x1', yref='y1',
                font=dict(color=font_color, size=font_size),
                showarrow=False)
        )
    return annotations
```

### Add Axis Specifications and Create the Layout

```python
axis = dict(showline=False, # hide axis line, grid, ticklabels and  title
            zeroline=False,
            showgrid=False,
            showticklabels=False,
            )

fig.update_layout(title= 'Tree with Reingold-Tilford Layout',
              annotations=make_annotations(position, v_label),
              font_size=12,
              showlegend=False,
              xaxis=axis,
              yaxis=axis,
              margin=dict(l=40, r=40, b=85, t=100),
              hovermode='closest',
              plot_bgcolor='rgb(248,248,248)'
              )
fig.show()
```
<div>                        <script type="text/javascript">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>
        <script charset="utf-8" src="https://cdn.plot.ly/plotly-3.1.0.min.js" integrity="sha256-Ei4740bWZhaUTQuD6q9yQlgVCMPBz6CZWhevDYPv93A=" crossorigin="anonymous"></script>                <div id="plotly-div-1" class="plotly-graph-div" style="height:100%; width:100%;"></div>            <script type="text/javascript">                window.PLOTLYENV=window.PLOTLYENV || {};                                if (document.getElementById("plotly-div-1")) {                    Plotly.newPlot(                        "plotly-div-1",                        [{"hoverinfo":"none","line":{"color":"rgb(210,210,210)","width":1},"mode":"lines","x":[-3.333333333333333,-3.333333333333333,null,-3.333333333333333,0.0,null,-3.333333333333333,-5.333333333333333,null,-3.333333333333333,-1.333333333333333,null,0.0,0.666666666666667,null,0.0,2.666666666666667,null,-5.333333333333333,-6.333333333333333,null,-5.333333333333333,-4.333333333333333,null,-1.333333333333333,-2.333333333333333,null,-1.333333333333333,-0.33333333333333304,null,0.666666666666667,0.16666666666666696,null,0.666666666666667,1.166666666666667,null,2.666666666666667,2.166666666666667,null,2.666666666666667,3.166666666666667,null,-6.333333333333333,-6.833333333333333,null,-6.333333333333333,-5.833333333333333,null,-4.333333333333333,-4.833333333333333,null,-4.333333333333333,-3.833333333333333,null,-2.333333333333333,-2.833333333333333,null,-2.333333333333333,-1.833333333333333,null,-0.33333333333333304,-0.833333333333333,null,-0.33333333333333304,0.16666666666666696,null,0.16666666666666696,-0.33333333333333304,null,0.16666666666666696,0.666666666666667,null],"y":[9.0,8.0,null,9.0,10.0,null,8.0,7.0,null,8.0,7.0,null,10.0,9.0,null,10.0,9.0,null,7.0,6.0,null,7.0,6.0,null,7.0,6.0,null,7.0,6.0,null,9.0,8.0,null,9.0,8.0,null,9.0,8.0,null,9.0,8.0,null,6.0,5.0,null,6.0,5.0,null,6.0,5.0,null,6.0,5.0,null,6.0,5.0,null,6.0,5.0,null,6.0,5.0,null,6.0,5.0,null,8.0,7.0,null,8.0,7.0,null],"type":"scatter"},{"hoverinfo":"text","marker":{"color":"#6175c1","line":{"color":"rgb(50,50,50)","width":1},"size":18,"symbol":"circle-dot"},"mode":"markers","name":"bla","opacity":0.8,"text":["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"],"x":[-3.333333333333333,-3.333333333333333,0.0,-5.333333333333333,-1.333333333333333,0.666666666666667,2.666666666666667,-6.333333333333333,-4.333333333333333,-2.333333333333333,-0.33333333333333304,0.16666666666666696,1.166666666666667,2.166666666666667,3.166666666666667,-6.833333333333333,-5.833333333333333,-4.833333333333333,-3.833333333333333,-2.833333333333333,-1.833333333333333,-0.833333333333333,0.16666666666666696,-0.33333333333333304,0.666666666666667],"y":[9.0,8.0,10.0,7.0,7.0,9.0,9.0,6.0,6.0,6.0,6.0,8.0,8.0,8.0,8.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,5.0,7.0,7.0],"type":"scatter"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermap":[{"type":"scattermap","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"font":{"size":12},"xaxis":{"showline":false,"zeroline":false,"showgrid":false,"showticklabels":false},"yaxis":{"showline":false,"zeroline":false,"showgrid":false,"showticklabels":false},"margin":{"l":40,"r":40,"b":85,"t":100},"title":{"text":"Tree with Reingold-Tilford Layout"},"annotations":[{"font":{"color":"rgb(250,250,250)","size":10},"showarrow":false,"text":"0","x":-3.333333333333333,"xref":"x","y":9.0,"yref":"y"},{"font":{"color":"rgb(250,250,250)","size":10},"showarrow":false,"text":"1","x":-3.333333333333333,"xref":"x","y":8.0,"yref":"y"},{"font":{"color":"rgb(250,250,250)","size":10},"showarrow":false,"text":"2","x":0.0,"xref":"x","y":10.0,"yref":"y"},{"font":{"color":"rgb(250,250,250)","size":10},"showarrow":false,"text":"3","x":-5.333333333333333,"xref":"x","y":7.0,"yref":"y"},{"font":{"color":"rgb(250,250,250)","size":10},"showarrow":false,"text":"4","x":-1.333333333333333,"xref":"x","y":7.0,"yref":"y"},{"font":{"color":"rgb(250,250,250)","size":10},"showarrow":false,"text":"5","x":0.666666666666667,"xref":"x","y":9.0,"yref":"y"},{"font":{"color":"rgb(250,250,250)","size":10},"showarrow":false,"text":"6","x":2.666666666666667,"xref":"x","y":9.0,"yref":"y"},{"font":{"color":"rgb(250,250,250)","size":10},"showarrow":false,"text":"7","x":-6.333333333333333,"xref":"x","y":6.0,"yref":"y"},{"font":{"color":"rgb(250,250,250)","size":10},"showarrow":false,"text":"8","x":-4.333333333333333,"xref":"x","y":6.0,"yref":"y"},{"font":{"color":"rgb(250,250,250)","size":10},"showarrow":false,"text":"9","x":-2.333333333333333,"xref":"x","y":6.0,"yref":"y"},{"font":{"color":"rgb(250,250,250)","size":10},"showarrow":false,"text":"10","x":-0.33333333333333304,"xref":"x","y":6.0,"yref":"y"},{"font":{"color":"rgb(250,250,250)","size":10},"showarrow":false,"text":"11","x":0.16666666666666696,"xref":"x","y":8.0,"yref":"y"},{"font":{"color":"rgb(250,250,250)","size":10},"showarrow":false,"text":"12","x":1.166666666666667,"xref":"x","y":8.0,"yref":"y"},{"font":{"color":"rgb(250,250,250)","size":10},"showarrow":false,"text":"13","x":2.166666666666667,"xref":"x","y":8.0,"yref":"y"},{"font":{"color":"rgb(250,250,250)","size":10},"showarrow":false,"text":"14","x":3.166666666666667,"xref":"x","y":8.0,"yref":"y"},{"font":{"color":"rgb(250,250,250)","size":10},"showarrow":false,"text":"15","x":-6.833333333333333,"xref":"x","y":5.0,"yref":"y"},{"font":{"color":"rgb(250,250,250)","size":10},"showarrow":false,"text":"16","x":-5.833333333333333,"xref":"x","y":5.0,"yref":"y"},{"font":{"color":"rgb(250,250,250)","size":10},"showarrow":false,"text":"17","x":-4.833333333333333,"xref":"x","y":5.0,"yref":"y"},{"font":{"color":"rgb(250,250,250)","size":10},"showarrow":false,"text":"18","x":-3.833333333333333,"xref":"x","y":5.0,"yref":"y"},{"font":{"color":"rgb(250,250,250)","size":10},"showarrow":false,"text":"19","x":-2.833333333333333,"xref":"x","y":5.0,"yref":"y"},{"font":{"color":"rgb(250,250,250)","size":10},"showarrow":false,"text":"20","x":-1.833333333333333,"xref":"x","y":5.0,"yref":"y"},{"font":{"color":"rgb(250,250,250)","size":10},"showarrow":false,"text":"21","x":-0.833333333333333,"xref":"x","y":5.0,"yref":"y"},{"font":{"color":"rgb(250,250,250)","size":10},"showarrow":false,"text":"22","x":0.16666666666666696,"xref":"x","y":5.0,"yref":"y"},{"font":{"color":"rgb(250,250,250)","size":10},"showarrow":false,"text":"23","x":-0.33333333333333304,"xref":"x","y":7.0,"yref":"y"},{"font":{"color":"rgb(250,250,250)","size":10},"showarrow":false,"text":"24","x":0.666666666666667,"xref":"x","y":7.0,"yref":"y"}],"showlegend":false,"hovermode":"closest","plot_bgcolor":"rgb(248,248,248)"},                        {"responsive": true}                    )                };            </script>        </div>

### Reference
See the [full graph objectsreference](/reference/graph_objects/index.md) for more information and chart attribute options and http://igraph.org/python/ for more information about the igraph package!
