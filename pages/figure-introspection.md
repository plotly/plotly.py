---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.2
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
    version: 3.7.7
  plotly:
    description: How to dig into and learn more about the figure data structure.
    display_as: file_settings
    language: python
    layout: base
    name: Introspecting Figures
    order: 36
    page_type: u-guide
    permalink: python/figure-introspection/
    thumbnail: thumbnail/violin.jpg
---

### The Figure Lifecycle

As explained in the [Figure Data Structure documentation](figure-structure.md), when building a figure object with Plotly.py, it is not necessary to populate every possible attribute. At render-time, figure objects (whether generated via [Plotly Express](plotly-express.md) or [Graph Objects](graph-objects.md)) are passed from Plotly.py to [Plotly.js](https://plotly.com/javascript/), which is the Javascript library responsible for turning JSON descriptions of figures into graphical representations.

As part of this rendering process, Plotly.js will determine, based on the attributes that have been set, which other attributes require values in order to draw the figure. Plotly.js will then apply either static or dynamic defaults to all of the remaining required attributes and render the figure. A good example of a static default would be the text font size: if unspecified, the default value is always the same. A good example of a dynamic default would be the range of an axis: if unspecified, the default will be computed based on the range of the data in traces associated with that axis.


### Introspecting Plotly Express Figures

Figure objects created by [Plotly Express](plotly-express.md) have a number of attributes automatically set, and these can be introspected using the Python `print()` function, or in JupyterLab, the special `fig.show("json")` renderer, which gives an interactive drilldown interface with search:

```python
import plotly.express as px

fig = px.scatter(x=[10, 20], y=[20, 10], height=400, width=400)
fig.show()
print(fig)
```

**Output:**
```
Figure({
    'data': [{'hovertemplate': 'x=%{x}<br>y=%{y}<extra></extra>',
              'legendgroup': '',
              'marker': {'color': '#636efa', 'symbol': 'circle'},
              'mode': 'markers',
              'name': '',
              'orientation': 'v',
              'showlegend': False,
              'type': 'scatter',
              'x': {'bdata': 'ChQ=', 'dtype': 'i1'},
              'xaxis': 'x',
              'y': {'bdata': 'FAo=', 'dtype': 'i1'},
              'yaxis': 'y'}],
    'layout': {'height': 400,
               'legend': {'tracegroupgap': 0},
               'margin': {'t': 60},
               'template': '...',
               'width': 400,
               'xaxis': {'anchor': 'y', 'domain': [0.0, 1.0], 'title': {'text': 'x'}},
               'yaxis': {'anchor': 'x', 'domain': [0.0, 1.0], 'title': {'text': 'y'}}}
})
```
<div>                        <script type="text/javascript">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>
        <script charset="utf-8" src="https://cdn.plot.ly/plotly-3.1.0.min.js" integrity="sha256-Ei4740bWZhaUTQuD6q9yQlgVCMPBz6CZWhevDYPv93A=" crossorigin="anonymous"></script>                <div id="plotly-div-1" class="plotly-graph-div" style="height:400px; width:400px;"></div>            <script type="text/javascript">                window.PLOTLYENV=window.PLOTLYENV || {};                                if (document.getElementById("plotly-div-1")) {                    Plotly.newPlot(                        "plotly-div-1",                        [{"hovertemplate":"x=%{x}\u003cbr\u003ey=%{y}\u003cextra\u003e\u003c\u002fextra\u003e","legendgroup":"","marker":{"color":"#636efa","symbol":"circle"},"mode":"markers","name":"","orientation":"v","showlegend":false,"x":{"dtype":"i1","bdata":"ChQ="},"xaxis":"x","y":{"dtype":"i1","bdata":"FAo="},"yaxis":"y","type":"scatter"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermap":[{"type":"scattermap","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"xaxis":{"anchor":"y","domain":[0.0,1.0],"title":{"text":"x"}},"yaxis":{"anchor":"x","domain":[0.0,1.0],"title":{"text":"y"}},"legend":{"tracegroupgap":0},"margin":{"t":60},"height":400,"width":400},                        {"responsive": true}                    )                };            </script>        </div>

We can learn more about the attributes Plotly Express has set for us with the Python `help()` function:

```python
help(fig.data[0].__class__.mode)
```

**Output:**
```
Help on property:

    Determines the drawing mode for this scatter trace. If the
    provided `mode` includes "text" then the `text` elements appear
    at the coordinates. Otherwise, the `text` elements appear on
    hover. If there are less than 20 points and the trace is not
    stacked then the default is "lines+markers". Otherwise,
    "lines".

    The 'mode' property is a flaglist and may be specified
    as a string containing:

    - Any combination of ['lines', 'markers', 'text'] joined with '+' characters
        (e.g. 'lines+markers')
        OR exactly one of ['none'] (e.g. 'none')

    Returns
    -------
    Any
```

### Accessing Javascript-Computed Defaults

_new in 4.10_

The `.full_figure_for_development()` method provides Python-level access to the default values computed by Plotly.js. This method requires [the Kaleido package](static-image-export.md), which is easy to install and also used for [static image export](static-image-export.md).

By way of example, here is an extremely simple figure created with [Graph Objects](graph-objects.md) (although it could have been made with [Plotly Express](plotly-express.md) as well just like above) where we have disabled the default template for maximum readability. Note how in this figure the text labels on the markers are clipped, and sit on top of the markers.

```python
import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Scatter(
        mode="markers+text",
        x=[10,20],
        y=[20, 10],
        text=["Point A", "Point B"]
    )],
    layout=dict(height=400, width=400, template="none")
)
fig.show()
```
<div>                        <script type="text/javascript">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>
        <script charset="utf-8" src="https://cdn.plot.ly/plotly-3.1.0.min.js" integrity="sha256-Ei4740bWZhaUTQuD6q9yQlgVCMPBz6CZWhevDYPv93A=" crossorigin="anonymous"></script>                <div id="plotly-div-2" class="plotly-graph-div" style="height:400px; width:400px;"></div>            <script type="text/javascript">                window.PLOTLYENV=window.PLOTLYENV || {};                                if (document.getElementById("plotly-div-2")) {                    Plotly.newPlot(                        "plotly-div-2",                        [{"mode":"markers+text","text":["Point A","Point B"],"x":[10,20],"y":[20,10],"type":"scatter"}],                        {"height":400,"template":{"data":{"scatter":[{"type":"scatter"}]}},"width":400},                        {"responsive": true}                    )                };            </script>        </div>

Let's print this figure to see the very small JSON object that is passed to Plotly.js as input:

```python
print(fig)
```

**Output:**
```
Figure({
    'data': [{'mode': 'markers+text', 'text': ['Point A', 'Point B'], 'type': 'scatter', 'x': [10, 20], 'y': [20, 10]}],
    'layout': {'height': 400, 'template': '...', 'width': 400}
})
```

Now let's look at the "full" figure after Plotly.js has computed the default values for every necessary attribute.

> Heads-up: the full figure is quite long and intimidating, and this page is meant to help demystify things so **please read on**!

Please also note that the `.full_figure_for_development()` function is really meant for interactive learning and debugging, rather than production use, hence its name and the warning it produces by default, which you can see below, and which can be suppressed with `warn=False`.

```python
full_fig = fig.full_figure_for_development()
print(full_fig)
```

**Output:**
```
Figure({
    'data': [{'cliponaxis': True,
              'error_x': {'visible': False},
              'error_y': {'visible': False},
              'fill': 'none',
              'hoverinfo': 'x+y+z+text',
              'hoverlabel': {'align': 'auto',
                             'font': {'family': 'Arial, sans-serif',
                                      'lineposition': 'none',
                                      'shadow': 'none',
                                      'size': 13,
                                      'style': 'normal',
                                      'textcase': 'normal',
                                      'variant': 'normal',
                                      'weight': 'normal'},
                             'namelength': 15,
                             'showarrow': True},
              'hoveron': 'points',
              'hovertemplate': '',
              'hovertext': '',
              'legend': 'legend',
              'legendgroup': '',
              'legendgrouptitle': {'font': {'color': '#444',
                                            'family': '"Open Sans", verdana, arial, sans-serif',
                                            'lineposition': 'none',
                                            'shadow': 'none',
                                            'size': 13,
                                            'style': 'normal',
                                            'textcase': 'normal',
                                            'variant': 'normal',
                                            'weight': 'normal'},
                                   'text': ''},
              'legendrank': 1000,
              'marker': {'angle': 0,
                         'angleref': 'up',
                         'color': '#1f77b4',
                         'gradient': {'type': 'none'},
                         'line': {'color': '#444', 'width': 0},
                         'maxdisplayed': 0,
                         'opacity': 1,
                         'size': 6,
                         'standoff': 0,
                         'symbol': 'circle'},
              'mode': 'markers+text',
              'name': 'trace 0',
              'opacity': 1,
              'selected': {'marker': {'opacity': 1}},
              'showlegend': True,
              'stackgroup': '',
              'text': [Point A, Point B],
              'textfont': {'color': '#444',
                           'family': '"Open Sans", verdana, arial, sans-serif',
                           'lineposition': 'none',
                           'shadow': 'none',
                           'size': 12,
                           'style': 'normal',
                           'textcase': 'normal',
                           'variant': 'normal',
                           'weight': 'normal'},
              'textposition': 'middle center',
              'texttemplate': '',
              'type': 'scatter',
              'uid': '053df7',
              'unselected': {'marker': {'opacity': 0.2}},
              'visible': True,
              'x': [10, 20],
              'xaxis': 'x',
              'xcalendar': 'gregorian',
              'xhoverformat': '',
              'xperiod': 0,
              'y': [20, 10],
              'yaxis': 'y',
              'ycalendar': 'gregorian',
              'yhoverformat': '',
              'yperiod': 0,
              'zorder': 0}],
    'layout': {'activeselection': {'fillcolor': 'rgba(0,0,0,0)', 'opacity': 0.5},
               'activeshape': {'fillcolor': 'rgb(255,0,255)', 'opacity': 0.5},
               'autosize': False,
               'autotypenumbers': 'convert types',
               'calendar': 'gregorian',
               'clickmode': 'event',
               'colorscale': {'diverging': [[0, 'rgb(5,10,172)'], [0.35,
                                            'rgb(106,137,247)'], [0.5,
                                            'rgb(190,190,190)'], [0.6,
                                            'rgb(220,170,132)'], [0.7,
                                            'rgb(230,145,90)'], [1,
                                            'rgb(178,10,28)']],
                              'sequential': [[0, 'rgb(220,220,220)'], [0.2,
                                             'rgb(245,195,157)'], [0.4,
                                             'rgb(245,160,105)'], [1,
                                             'rgb(178,10,28)']],
                              'sequentialminus': [[0, 'rgb(5,10,172)'], [0.35,
                                                  'rgb(40,60,190)'], [0.5,
                                                  'rgb(70,100,245)'], [0.6,
                                                  'rgb(90,120,245)'], [0.7,
                                                  'rgb(106,137,247)'], [1,
                                                  'rgb(220,220,220)']]},
               'colorway': [#1f77b4, #ff7f0e, #2ca02c, #d62728, #9467bd, #8c564b,
                            #e377c2, #7f7f7f, #bcbd22, #17becf],
               'computed': {'margin': {'b': 80, 'l': 80, 'r': 80, 't': 100}},
               'dragmode': 'zoom',
               'font': {'color': '#444',
                        'family': '"Open Sans", verdana, arial, sans-serif',
                        'lineposition': 'none',
                        'shadow': 'none',
                        'size': 12,
                        'style': 'normal',
                        'textcase': 'normal',
                        'variant': 'normal',
                        'weight': 'normal'},
               'height': 400,
               'hidesources': False,
               'hoverdistance': 20,
               'hoverlabel': {'align': 'auto',
                              'font': {'family': 'Arial, sans-serif',
                                       'lineposition': 'none',
                                       'shadow': 'none',
                                       'size': 13,
                                       'style': 'normal',
                                       'textcase': 'normal',
                                       'variant': 'normal',
                                       'weight': 'normal'},
                              'grouptitlefont': {'family': 'Arial, sans-serif',
                                                 'lineposition': 'none',
                                                 'shadow': 'none',
                                                 'size': 13,
                                                 'style': 'normal',
                                                 'textcase': 'normal',
                                                 'variant': 'normal',
                                                 'weight': 'normal'},
                              'namelength': 15,
                              'showarrow': True},
               'hovermode': 'closest',
               'hoversubplots': 'overlaying',
               'margin': {'autoexpand': True, 'b': 80, 'l': 80, 'pad': 0, 'r': 80, 't': 100},
               'minreducedheight': 64,
               'minreducedwidth': 64,
               'modebar': {'activecolor': 'rgba(68, 68, 68, 0.7)',
                           'add': '',
                           'bgcolor': 'rgba(255, 255, 255, 0.5)',
                           'color': 'rgba(68, 68, 68, 0.3)',
                           'orientation': 'h',
                           'remove': ''},
               'newselection': {'line': {'dash': 'dot', 'width': 1}, 'mode': 'immediate'},
               'newshape': {'drawdirection': 'diagonal',
                            'fillcolor': 'rgba(0,0,0,0)',
                            'fillrule': 'evenodd',
                            'label': {'text': '', 'texttemplate': ''},
                            'layer': 'above',
                            'legend': 'legend',
                            'legendgroup': '',
                            'legendgrouptitle': {'font': {'lineposition': 'none',
                                                          'shadow': 'none',
                                                          'style': 'normal',
                                                          'textcase': 'normal',
                                                          'variant': 'normal',
                                                          'weight': 'normal'},
                                                 'text': ''},
                            'legendrank': 1000,
                            'line': {'color': '#444', 'dash': 'solid', 'width': 4},
                            'opacity': 1,
                            'showlegend': False,
                            'visible': True},
               'paper_bgcolor': '#fff',
               'plot_bgcolor': '#fff',
               'scattermode': 'overlay',
               'separators': '.,',
               'showlegend': False,
               'spikedistance': -1,
               'template': '...',
               'title': {'automargin': False,
                         'font': {'color': '#444',
                                  'family': '"Open Sans", verdana, arial, sans-serif',
                                  'lineposition': 'none',
                                  'shadow': 'none',
                                  'size': 17,
                                  'style': 'normal',
                                  'textcase': 'normal',
                                  'variant': 'normal',
                                  'weight': 'normal'},
                         'pad': {'b': 0, 'l': 0, 'r': 0, 't': 0},
                         'subtitle': {'font': {'color': '#444',
                                               'family': '"Open Sans", verdana, arial, sans-serif',
                                               'lineposition': 'none',
                                               'shadow': 'none',
                                               'size': 12,
                                               'style': 'normal',
                                               'textcase': 'normal',
                                               'variant': 'normal',
                                               'weight': 'normal'},
                                      'text': 'Click to enter Plot subtitle'},
                         'text': 'Click to enter Plot title',
                         'x': 0.5,
                         'xanchor': 'auto',
                         'xref': 'container',
                         'yanchor': 'auto',
                         'yref': 'container'},
               'uniformtext': {'mode': False},
               'width': 400,
               'xaxis': {'anchor': 'y',
                         'automargin': False,
                         'autorange': True,
                         'autotickangles': [0, 30, 90],
                         'autotypenumbers': 'convert types',
                         'color': '#444',
                         'constrain': 'range',
                         'constraintoward': 'center',
                         'domain': [0, 1],
                         'dtick': 5,
                         'exponentformat': 'B',
                         'fixedrange': False,
                         'gridcolor': 'rgb(238, 238, 238)',
                         'griddash': 'solid',
                         'gridwidth': 1,
                         'hoverformat': '',
                         'layer': 'above traces',
                         'minexponent': 3,
                         'modebardisable': 'none',
                         'nticks': 0,
                         'range': [9.244604316546763, 20.755395683453237],
                         'rangemode': 'normal',
                         'separatethousands': False,
                         'showexponent': 'all',
                         'showgrid': True,
                         'showline': False,
                         'showspikes': False,
                         'showticklabels': True,
                         'side': 'bottom',
                         'tick0': 0,
                         'tickfont': {'color': '#444',
                                      'family': '"Open Sans", verdana, arial, sans-serif',
                                      'lineposition': 'none',
                                      'shadow': 'none',
                                      'size': 12,
                                      'style': 'normal',
                                      'textcase': 'normal',
                                      'variant': 'normal',
                                      'weight': 'normal'},
                         'tickformat': '',
                         'ticklabeloverflow': 'hide past div',
                         'ticklabelposition': 'outside',
                         'ticklabelshift': 0,
                         'ticklabelstandoff': 0,
                         'ticklabelstep': 1,
                         'tickmode': 'auto',
                         'tickprefix': '',
                         'ticks': '',
                         'ticksuffix': '',
                         'title': {'font': {'color': '#444',
                                            'family': '"Open Sans", verdana, arial, sans-serif',
                                            'lineposition': 'none',
                                            'shadow': 'none',
                                            'size': 14,
                                            'style': 'normal',
                                            'textcase': 'normal',
                                            'variant': 'normal',
                                            'weight': 'normal'},
                                   'text': 'Click to enter X axis title'},
                         'type': 'linear',
                         'unifiedhovertitle': {'text': ''},
                         'visible': True,
                         'zeroline': True,
                         'zerolinecolor': '#444',
                         'zerolinelayer': 'below traces',
                         'zerolinewidth': 1},
               'yaxis': {'anchor': 'x',
                         'automargin': False,
                         'autorange': True,
                         'autotypenumbers': 'convert types',
                         'color': '#444',
                         'constrain': 'range',
                         'constraintoward': 'middle',
                         'domain': [0, 1],
                         'dtick': 2,
                         'exponentformat': 'B',
                         'fixedrange': False,
                         'gridcolor': 'rgb(238, 238, 238)',
                         'griddash': 'solid',
                         'gridwidth': 1,
                         'hoverformat': '',
                         'layer': 'above traces',
                         'minexponent': 3,
                         'modebardisable': 'none',
                         'nticks': 0,
                         'range': [9.225721784776903, 20.7742782152231],
                         'rangemode': 'normal',
                         'separatethousands': False,
                         'showexponent': 'all',
                         'showgrid': True,
                         'showline': False,
                         'showspikes': False,
                         'showticklabels': True,
                         'side': 'left',
                         'tick0': 0,
                         'tickfont': {'color': '#444',
                                      'family': '"Open Sans", verdana, arial, sans-serif',
                                      'lineposition': 'none',
                                      'shadow': 'none',
                                      'size': 12,
                                      'style': 'normal',
                                      'textcase': 'normal',
                                      'variant': 'normal',
                                      'weight': 'normal'},
                         'tickformat': '',
                         'ticklabeloverflow': 'hide past div',
                         'ticklabelposition': 'outside',
                         'ticklabelshift': 0,
                         'ticklabelstandoff': 0,
                         'ticklabelstep': 1,
                         'tickmode': 'auto',
                         'tickprefix': '',
                         'ticks': '',
                         'ticksuffix': '',
                         'title': {'font': {'color': '#444',
                                            'family': '"Open Sans", verdana, arial, sans-serif',
                                            'lineposition': 'none',
                                            'shadow': 'none',
                                            'size': 14,
                                            'style': 'normal',
                                            'textcase': 'normal',
                                            'variant': 'normal',
                                            'weight': 'normal'},
                                   'text': 'Click to enter Y axis title'},
                         'type': 'linear',
                         'unifiedhovertitle': {'text': ''},
                         'visible': True,
                         'zeroline': True,
                         'zerolinecolor': '#444',
                         'zerolinelayer': 'below traces',
                         'zerolinewidth': 1}}
})
```

**Warnings/Messages:**
```
/Users/liamconnors/Documents/plotly.py/plotly/io/_kaleido.py:765: UserWarning:

full_figure_for_development is not recommended or necessary for production use in most circumstances. 
To suppress this warning, set warn=False
```

As you can see, Plotly.js does a lot of work filling things in for us! Let's look at the examples described at the top of the page of static and dynamic defaults. If we look just at `layout.font` and `layout.xaxis.range` we can see that the static default font size is 12 and that the dynamic default range is computed to be a bit beyond the data range which was 10-20:

```python
print("full_fig.layout.font.size: ", full_fig.layout.font.size)
print("full_fig.layout.xaxis.range: ", full_fig.layout.xaxis.range)
```

**Output:**
```
full_fig.layout.font.size:  12
full_fig.layout.xaxis.range:  (9.244604316546763, 20.755395683453237)
```

### Learning About Attributes


What else can we use this `full_fig` for? Let's start by looking at the first entry of the `data`

```python
print(full_fig.data[0])
```

**Output:**
```
Scatter({
    'cliponaxis': True,
    'error_x': {'visible': False},
    'error_y': {'visible': False},
    'fill': 'none',
    'hoverinfo': 'x+y+z+text',
    'hoverlabel': {'align': 'auto',
                   'font': {'family': 'Arial, sans-serif',
                            'lineposition': 'none',
                            'shadow': 'none',
                            'size': 13,
                            'style': 'normal',
                            'textcase': 'normal',
                            'variant': 'normal',
                            'weight': 'normal'},
                   'namelength': 15,
                   'showarrow': True},
    'hoveron': 'points',
    'hovertemplate': '',
    'hovertext': '',
    'legend': 'legend',
    'legendgroup': '',
    'legendgrouptitle': {'font': {'color': '#444',
                                  'family': '"Open Sans", verdana, arial, sans-serif',
                                  'lineposition': 'none',
                                  'shadow': 'none',
                                  'size': 13,
                                  'style': 'normal',
                                  'textcase': 'normal',
                                  'variant': 'normal',
                                  'weight': 'normal'},
                         'text': ''},
    'legendrank': 1000,
    'marker': {'angle': 0,
               'angleref': 'up',
               'color': '#1f77b4',
               'gradient': {'type': 'none'},
               'line': {'color': '#444', 'width': 0},
               'maxdisplayed': 0,
               'opacity': 1,
               'size': 6,
               'standoff': 0,
               'symbol': 'circle'},
    'mode': 'markers+text',
    'name': 'trace 0',
    'opacity': 1,
    'selected': {'marker': {'opacity': 1}},
    'showlegend': True,
    'stackgroup': '',
    'text': [Point A, Point B],
    'textfont': {'color': '#444',
                 'family': '"Open Sans", verdana, arial, sans-serif',
                 'lineposition': 'none',
                 'shadow': 'none',
                 'size': 12,
                 'style': 'normal',
                 'textcase': 'normal',
                 'variant': 'normal',
                 'weight': 'normal'},
    'textposition': 'middle center',
    'texttemplate': '',
    'uid': '053df7',
    'unselected': {'marker': {'opacity': 0.2}},
    'visible': True,
    'x': [10, 20],
    'xaxis': 'x',
    'xcalendar': 'gregorian',
    'xhoverformat': '',
    'xperiod': 0,
    'y': [20, 10],
    'yaxis': 'y',
    'ycalendar': 'gregorian',
    'yhoverformat': '',
    'yperiod': 0,
    'zorder': 0
})
```

We see that this is an instance of `go.Scatter` (as expected, given the input) and that it has an attribute we've maybe never heard of called `cliponaxis` which by default seems to be set to `True` in this case. Let's find out more about this attribute using the built-in Python `help()` function

```python
help(go.Scatter.cliponaxis)
```

**Output:**
```
Help on property:

    Determines whether or not markers and text nodes are clipped
    about the subplot axes. To show markers and text nodes above
    axis lines and tick labels, make sure to set `xaxis.layer` and
    `yaxis.layer` to *below traces*.

    The 'cliponaxis' property must be specified as a bool
    (either True, or False)

    Returns
    -------
    bool
```

Aha!  This explains why in our original figure above, the text was cut off by the edge of the plotting area! Let's try forcing that to `False`, and let's also use the attribute `textposition` which we see in the full figure is by default set to `"middle center"` to get our text off of our markers:

```python
fig.update_traces(cliponaxis=False, textposition="top right")
fig.show()
```
<div>                        <script type="text/javascript">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>
        <script charset="utf-8" src="https://cdn.plot.ly/plotly-3.1.0.min.js" integrity="sha256-Ei4740bWZhaUTQuD6q9yQlgVCMPBz6CZWhevDYPv93A=" crossorigin="anonymous"></script>                <div id="plotly-div-3" class="plotly-graph-div" style="height:400px; width:400px;"></div>            <script type="text/javascript">                window.PLOTLYENV=window.PLOTLYENV || {};                                if (document.getElementById("plotly-div-3")) {                    Plotly.newPlot(                        "plotly-div-3",                        [{"mode":"markers+text","text":["Point A","Point B"],"x":[10,20],"y":[20,10],"type":"scatter","cliponaxis":false,"textposition":"top right"}],                        {"height":400,"template":{"data":{"scatter":[{"type":"scatter"}]}},"width":400},                        {"responsive": true}                    )                };            </script>        </div>

We can use this technique (of making a figure, and querying Plotly.js for the "full" version of that figure, and then exploring the attributes that are automatically set for us) to learn more about the range of possibilities that the figure schema makes available. We can drill down into `layout` attributes also:

```python
help(go.layout.XAxis.autorange)
```

**Output:**
```
Help on property:

    Determines whether or not the range of this axis is computed in
    relation to the input data. See `rangemode` for more info. If
    `range` is provided and it has a value for both the lower and
    upper bound, `autorange` is set to False. Using "min" applies
    autorange only to set the minimum. Using "max" applies
    autorange only to set the maximum. Using *min reversed* applies
    autorange only to set the minimum on a reversed axis. Using
    *max reversed* applies autorange only to set the maximum on a
    reversed axis. Using "reversed" applies autorange on both ends
    and reverses the axis direction.

    The 'autorange' property is an enumeration that may be specified as:

    - One of the following enumeration values:

        [True, False, 'reversed', 'min reversed', 'max reversed',
        'min', 'max']

    Returns
    -------
    Any
```

### More about Layout

In the figure we introspected above, we had added [a `scatter` trace](line-and-scatter.md), and Plotly.js automatically filled in for us the `xaxis` and `yaxis` values of that trace object to be `x` and `y`, and then also filled out the corresponding `layout.xaxis` and `layout.yaxis` objects for us, complete with their [extensive set of defaults for gridlines, tick labels and so on](axes.md).

If we create a figure with [a `scattergeo` trace](scatter-plots-on-maps.md) instead, however, Plotly.js will fill in a totally different set of objects in `layout`, corresponding to [a `geo` subplot, with all of its defaults for whether or not to show rivers, lakes, country borders, coastlines etc](map-configuration.md).

```python
import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Scattergeo(
        mode="markers+text",
        lat=[10, 20],
        lon=[20, 10],
        text=["Point A", "Point B"]
    )],
    layout=dict(height=400, width=400,
                margin=dict(l=0,r=0,b=0,t=0),
                template="none")
)
fig.show()
full_fig = fig.full_figure_for_development()
print(full_fig)
```

**Output:**
```
Figure({
    'data': [{'fill': 'none',
              'geo': 'geo',
              'hoverinfo': 'lon+lat+location+text',
              'hoverlabel': {'align': 'auto',
                             'font': {'family': 'Arial, sans-serif',
                                      'lineposition': 'none',
                                      'shadow': 'none',
                                      'size': 13,
                                      'style': 'normal',
                                      'textcase': 'normal',
                                      'variant': 'normal',
                                      'weight': 'normal'},
                             'namelength': 15,
                             'showarrow': True},
              'hovertemplate': '',
              'hovertext': '',
              'lat': [10, 20],
              'legend': 'legend',
              'legendgroup': '',
              'legendgrouptitle': {'font': {'color': '#444',
                                            'family': '"Open Sans", verdana, arial, sans-serif',
                                            'lineposition': 'none',
                                            'shadow': 'none',
                                            'size': 13,
                                            'style': 'normal',
                                            'textcase': 'normal',
                                            'variant': 'normal',
                                            'weight': 'normal'},
                                   'text': ''},
              'legendrank': 1000,
              'lon': [20, 10],
              'marker': {'angle': 0,
                         'angleref': 'up',
                         'color': '#1f77b4',
                         'gradient': {'type': 'none'},
                         'line': {'color': '#444', 'width': 0},
                         'opacity': 1,
                         'size': 6,
                         'standoff': 0,
                         'symbol': 'circle'},
              'mode': 'markers+text',
              'name': 'trace 0',
              'opacity': 1,
              'selected': {'marker': {'opacity': 1}},
              'showlegend': True,
              'text': [Point A, Point B],
              'textfont': {'color': '#444',
                           'family': '"Open Sans", verdana, arial, sans-serif',
                           'lineposition': 'none',
                           'shadow': 'none',
                           'size': 12,
                           'style': 'normal',
                           'textcase': 'normal',
                           'variant': 'normal',
                           'weight': 'normal'},
              'textposition': 'middle center',
              'texttemplate': '',
              'type': 'scattergeo',
              'uid': '2be8a1',
              'unselected': {'marker': {'opacity': 0.2}},
              'visible': True}],
    'layout': {'activeselection': {'fillcolor': 'rgba(0,0,0,0)', 'opacity': 0.5},
               'activeshape': {'fillcolor': 'rgb(255,0,255)', 'opacity': 0.5},
               'autosize': False,
               'autotypenumbers': 'convert types',
               'calendar': 'gregorian',
               'clickmode': 'event',
               'colorscale': {'diverging': [[0, 'rgb(5,10,172)'], [0.35,
                                            'rgb(106,137,247)'], [0.5,
                                            'rgb(190,190,190)'], [0.6,
                                            'rgb(220,170,132)'], [0.7,
                                            'rgb(230,145,90)'], [1,
                                            'rgb(178,10,28)']],
                              'sequential': [[0, 'rgb(220,220,220)'], [0.2,
                                             'rgb(245,195,157)'], [0.4,
                                             'rgb(245,160,105)'], [1,
                                             'rgb(178,10,28)']],
                              'sequentialminus': [[0, 'rgb(5,10,172)'], [0.35,
                                                  'rgb(40,60,190)'], [0.5,
                                                  'rgb(70,100,245)'], [0.6,
                                                  'rgb(90,120,245)'], [0.7,
                                                  'rgb(106,137,247)'], [1,
                                                  'rgb(220,220,220)']]},
               'colorway': [#1f77b4, #ff7f0e, #2ca02c, #d62728, #9467bd, #8c564b,
                            #e377c2, #7f7f7f, #bcbd22, #17becf],
               'computed': {'margin': {'b': 0, 'l': 0, 'r': 0, 't': 0}},
               'dragmode': 'pan',
               'font': {'color': '#444',
                        'family': '"Open Sans", verdana, arial, sans-serif',
                        'lineposition': 'none',
                        'shadow': 'none',
                        'size': 12,
                        'style': 'normal',
                        'textcase': 'normal',
                        'variant': 'normal',
                        'weight': 'normal'},
               'geo': {'bgcolor': '#fff',
                       'center': {'lat': 0, 'lon': 0},
                       'coastlinecolor': '#444',
                       'coastlinewidth': 1,
                       'domain': {'x': [0, 1], 'y': [0, 1]},
                       'fitbounds': False,
                       'framecolor': '#444',
                       'framewidth': 1,
                       'lataxis': {'dtick': 10, 'range': [-90, 90], 'showgrid': False, 'tick0': 0},
                       'lonaxis': {'dtick': 30, 'range': [-180, 180], 'showgrid': False, 'tick0': 0},
                       'projection': {'rotation': {'lat': 0, 'lon': 0, 'roll': 0}, 'scale': 1, 'type': 'equirectangular'},
                       'resolution': 110,
                       'scope': 'world',
                       'showcoastlines': True,
                       'showcountries': False,
                       'showframe': True,
                       'showlakes': False,
                       'showland': False,
                       'showocean': False,
                       'showrivers': False,
                       'visible': True},
               'height': 400,
               'hidesources': False,
               'hoverdistance': 20,
               'hoverlabel': {'align': 'auto',
                              'font': {'family': 'Arial, sans-serif',
                                       'lineposition': 'none',
                                       'shadow': 'none',
                                       'size': 13,
                                       'style': 'normal',
                                       'textcase': 'normal',
                                       'variant': 'normal',
                                       'weight': 'normal'},
                              'grouptitlefont': {'family': 'Arial, sans-serif',
                                                 'lineposition': 'none',
                                                 'shadow': 'none',
                                                 'size': 13,
                                                 'style': 'normal',
                                                 'textcase': 'normal',
                                                 'variant': 'normal',
                                                 'weight': 'normal'},
                              'namelength': 15,
                              'showarrow': True},
               'hovermode': 'closest',
               'hoversubplots': 'overlaying',
               'margin': {'autoexpand': True, 'b': 0, 'l': 0, 'pad': 0, 'r': 0, 't': 0},
               'minreducedheight': 64,
               'minreducedwidth': 64,
               'modebar': {'activecolor': 'rgba(68, 68, 68, 0.7)',
                           'add': '',
                           'bgcolor': 'rgba(255, 255, 255, 0.5)',
                           'color': 'rgba(68, 68, 68, 0.3)',
                           'orientation': 'h',
                           'remove': ''},
               'newselection': {'line': {'dash': 'dot', 'width': 1}, 'mode': 'immediate'},
               'newshape': {'drawdirection': 'diagonal',
                            'fillcolor': 'rgba(0,0,0,0)',
                            'fillrule': 'evenodd',
                            'label': {'text': '', 'texttemplate': ''},
                            'layer': 'above',
                            'legend': 'legend',
                            'legendgroup': '',
                            'legendgrouptitle': {'font': {'lineposition': 'none',
                                                          'shadow': 'none',
                                                          'style': 'normal',
                                                          'textcase': 'normal',
                                                          'variant': 'normal',
                                                          'weight': 'normal'},
                                                 'text': ''},
                            'legendrank': 1000,
                            'line': {'color': '#444', 'dash': 'solid', 'width': 4},
                            'opacity': 1,
                            'showlegend': False,
                            'visible': True},
               'paper_bgcolor': '#fff',
               'scattermode': 'overlay',
               'separators': '.,',
               'showlegend': False,
               'spikedistance': -1,
               'template': '...',
               'title': {'automargin': False,
                         'font': {'color': '#444',
                                  'family': '"Open Sans", verdana, arial, sans-serif',
                                  'lineposition': 'none',
                                  'shadow': 'none',
                                  'size': 17,
                                  'style': 'normal',
                                  'textcase': 'normal',
                                  'variant': 'normal',
                                  'weight': 'normal'},
                         'pad': {'b': 0, 'l': 0, 'r': 0, 't': 0},
                         'subtitle': {'font': {'color': '#444',
                                               'family': '"Open Sans", verdana, arial, sans-serif',
                                               'lineposition': 'none',
                                               'shadow': 'none',
                                               'size': 12,
                                               'style': 'normal',
                                               'textcase': 'normal',
                                               'variant': 'normal',
                                               'weight': 'normal'},
                                      'text': 'Click to enter Plot subtitle'},
                         'text': 'Click to enter Plot title',
                         'x': 0.5,
                         'xanchor': 'auto',
                         'xref': 'container',
                         'yanchor': 'auto',
                         'yref': 'container'},
               'uniformtext': {'mode': False},
               'width': 400}
})
```

**Warnings/Messages:**
```
/Users/liamconnors/Documents/plotly.py/plotly/io/_kaleido.py:765: UserWarning:

full_figure_for_development is not recommended or necessary for production use in most circumstances. 
To suppress this warning, set warn=False
```
<div>                        <script type="text/javascript">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>
        <script charset="utf-8" src="https://cdn.plot.ly/plotly-3.1.0.min.js" integrity="sha256-Ei4740bWZhaUTQuD6q9yQlgVCMPBz6CZWhevDYPv93A=" crossorigin="anonymous"></script>                <div id="plotly-div-4" class="plotly-graph-div" style="height:400px; width:400px;"></div>            <script type="text/javascript">                window.PLOTLYENV=window.PLOTLYENV || {};                                if (document.getElementById("plotly-div-4")) {                    Plotly.newPlot(                        "plotly-div-4",                        [{"lat":[10,20],"lon":[20,10],"mode":"markers+text","text":["Point A","Point B"],"type":"scattergeo"}],                        {"height":400,"margin":{"b":0,"l":0,"r":0,"t":0},"template":{"data":{"scatter":[{"type":"scatter"}]}},"width":400},                        {"responsive": true}                    )                };            </script>        </div>

If I then set `showrivers=True` and re-query the full figure, I see that new keys have appeared in the `layout.geo` object for `rivercolor` and `riverwidth`, showing the dynamic nature of these defaults.

```python
fig.update_geos(showrivers=True)
full_fig = fig.full_figure_for_development()
print(full_fig.layout.geo)
```

**Output:**
```
layout.Geo({
    'bgcolor': '#fff',
    'center': {'lat': 0, 'lon': 0},
    'coastlinecolor': '#444',
    'coastlinewidth': 1,
    'domain': {'x': [0, 1], 'y': [0, 1]},
    'fitbounds': False,
    'framecolor': '#444',
    'framewidth': 1,
    'lataxis': {'dtick': 10, 'range': [-90, 90], 'showgrid': False, 'tick0': 0},
    'lonaxis': {'dtick': 30, 'range': [-180, 180], 'showgrid': False, 'tick0': 0},
    'projection': {'rotation': {'lat': 0, 'lon': 0, 'roll': 0}, 'scale': 1, 'type': 'equirectangular'},
    'resolution': 110,
    'rivercolor': '#3399FF',
    'riverwidth': 1,
    'scope': 'world',
    'showcoastlines': True,
    'showcountries': False,
    'showframe': True,
    'showlakes': False,
    'showland': False,
    'showocean': False,
    'showrivers': True,
    'visible': True
})
```

**Warnings/Messages:**
```
/Users/liamconnors/Documents/plotly.py/plotly/io/_kaleido.py:765: UserWarning:

full_figure_for_development is not recommended or necessary for production use in most circumstances. 
To suppress this warning, set warn=False
```

### Reference

You can learn more about [all the available attributes in the plotly figure schema](/reference/graph_objects/index.md) (and read about its [high-level structure](figure-structure.md)) or about [all the classes and functions in the `plotly` module](/python-api-reference/).

```python

```
