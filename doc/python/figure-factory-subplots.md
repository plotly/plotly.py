---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.6
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
    description: Subplots with Plotly Figure Factory Charts
    display_as: multiple_axes
    language: python
    layout: base
    name: Figure Factory Subplots
    order: 4
    page_type: u-guide
    permalink: python/figure-factory-subplots/
    thumbnail: thumbnail/ff-subplots.jpg
---

#### Plotly's Figure Factory Module
Plotly's Python API contains a figure factory module which includes many wrapper functions that create unique chart types that are not yet included in [plotly.js](https://github.com/plotly/plotly.js), Plotly's open-source graphing library. The figure factory functions create a full figure, so some Plotly features, such as subplotting, should be implemented slightly differently with these charts.


#### Vertical Figure Factory Charts
First create the figures that you'd like to appear in the subplot:

```python
import plotly.figure_factory as ff
import plotly.graph_objects as go

import numpy as np

## Create first figure
x1,y1 = np.meshgrid(np.arange(0, 2, .2), np.arange(0, 2, .2))
u1 = np.cos(x1)*y1
v1 = np.sin(x1)*y1

fig1 = ff.create_quiver(x1, y1, u1, v1, name='Quiver')

## Create second figure
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
Y, X = np.meshgrid(x, y)
u = -1 - X**2 + Y
v = 1 + X - Y**2

fig2 = ff.create_streamline(x, y, u, v, arrow_scale=.1, name='Steamline')
```

Edit the figures' x and y axes attributes to create subplots:

```python
for i in range(len(fig1.data)):
    fig1.data[i].xaxis='x1'
    fig1.data[i].yaxis='y1'

fig1.layout.xaxis1.update({'anchor': 'y1'})
fig1.layout.yaxis1.update({'anchor': 'x1', 'domain': [.55, 1]})

for i in range(len(fig2.data)):
    fig2.data[i].xaxis='x2'
    fig2.data[i].yaxis='y2'

# initialize xaxis2 and yaxis2
fig2['layout']['xaxis2'] = {}
fig2['layout']['yaxis2'] = {}

fig2.layout.xaxis2.update({'anchor': 'y2'})
fig2.layout.yaxis2.update({'anchor': 'x2', 'domain': [0, .45]})
```

Combine the data and layout objects to create a figure

```python
fig = go.Figure()
fig.add_traces([fig1.data[0], fig2.data[0]])

fig.layout.update(fig1.layout)
fig.layout.update(fig2.layout)

fig.show()
```

#### Horizontal Table and Chart

```python
import plotly.graph_objects as go
import plotly.figure_factory as ff

table_data = [['Team', 'Wins', 'Losses', 'Ties'],
              ['Montréal<br>Canadiens', 18, 4, 0],
              ['Dallas Stars', 18, 5, 0],
              ['NY Rangers', 16, 5, 0],
              ['Boston<br>Bruins', 13, 8, 0],
              ['Chicago<br>Blackhawks', 13, 8, 0],
              ['LA Kings', 13, 8, 0],
              ['Ottawa<br>Senators', 12, 5, 0]]

fig = ff.create_table(table_data, height_constant=60)

teams = ['Montréal Canadiens', 'Dallas Stars', 'NY Rangers',
         'Boston Bruins', 'Chicago Blackhawks', 'LA Kings', 'Ottawa Senators']
GFPG = [3.54, 3.48, 3.0, 3.27, 2.83, 2.45, 3.18]
GAPG = [2.17, 2.57, 2.0, 2.91, 2.57, 2.14, 2.77]

trace1 = go.Scatter(x=teams, y=GFPG,
                    marker=dict(color='#0099ff'),
                    name='Goals For<br>Per Game',
                    xaxis='x2', yaxis='y2')
trace2 = go.Scatter(x=teams, y=GAPG,
                    marker=dict(color='#404040'),
                    name='Goals Against<br>Per Game',
                    xaxis='x2', yaxis='y2')

fig.add_traces([trace1, trace2])

# initialize xaxis2 and yaxis2
fig['layout']['xaxis2'] = {}
fig['layout']['yaxis2'] = {}

# Edit layout for subplots
fig.layout.xaxis.update({'domain': [0, .5]})
fig.layout.xaxis2.update({'domain': [0.6, 1.]})

# The graph's yaxis MUST BE anchored to the graph's xaxis
fig.layout.yaxis2.update({'anchor': 'x2'})
fig.layout.yaxis2.update({'title': 'Goals'})

# Update the margins to add a title and see graph x-labels.
fig.layout.margin.update({'t':50, 'b':100})
fig.layout.update({'title': '2016 Hockey Stats'})

fig.show()
```

#### Vertical Table and Chart

```python
import plotly.graph_objects as go
import plotly.figure_factory as ff

# Add table data
table_data = [['Team', 'Wins', 'Losses', 'Ties'],
              ['Montréal<br>Canadiens', 18, 4, 0],
              ['Dallas Stars', 18, 5, 0],
              ['NY Rangers', 16, 5, 0],
              ['Boston<br>Bruins', 13, 8, 0],
              ['Chicago<br>Blackhawks', 13, 8, 0],
              ['Ottawa<br>Senators', 12, 5, 0]]

# Initialize a figure with ff.create_table(table_data)
fig = ff.create_table(table_data, height_constant=60)

# Add graph data
teams = ['Montréal Canadiens', 'Dallas Stars', 'NY Rangers',
         'Boston Bruins', 'Chicago Blackhawks', 'Ottawa Senators']
GFPG = [3.54, 3.48, 3.0, 3.27, 2.83, 3.18]
GAPG = [2.17, 2.57, 2.0, 2.91, 2.57, 2.77]

# Make traces for graph
trace1 = go.Bar(x=teams, y=GFPG, xaxis='x2', yaxis='y2',
                marker=dict(color='#0099ff'),
                name='Goals For<br>Per Game')
trace2 = go.Bar(x=teams, y=GAPG, xaxis='x2', yaxis='y2',
                marker=dict(color='#404040'),
                name='Goals Against<br>Per Game')

# Add trace data to figure
fig.add_traces([trace1, trace2])

# initialize xaxis2 and yaxis2
fig['layout']['xaxis2'] = {}
fig['layout']['yaxis2'] = {}

# Edit layout for subplots
fig.layout.yaxis.update({'domain': [0, .45]})
fig.layout.yaxis2.update({'domain': [.6, 1]})

# The graph's yaxis2 MUST BE anchored to the graph's xaxis2 and vice versa
fig.layout.yaxis2.update({'anchor': 'x2'})
fig.layout.xaxis2.update({'anchor': 'y2'})
fig.layout.yaxis2.update({'title': 'Goals'})

# Update the margins to add a title and see graph x-labels.
fig.layout.margin.update({'t':75, 'l':50})
fig.layout.update({'title': '2016 Hockey Stats'})

# Update the height because adding a graph vertically will interact with
# the plot height calculated for the table
fig.layout.update({'height':800})

# Plot!
fig.show()
```

#### Reference
See https://plot.ly/python/subplots/ for more information on working with subplots. See https://plot.ly/python/reference/ for more information regarding chart attributes!
