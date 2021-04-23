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
    version: 3.6.7
  plotly:
    description: How to make Ternary plots in Python with Plotly.
    display_as: scientific
    language: python
    layout: base
    name: Ternary Plots
    order: 4
    page_type: example_index
    permalink: python/ternary-plots/
    thumbnail: thumbnail/v4-migration.png
---

## Ternary Plots

A ternary plot depicts the ratios of three variables as positions in an equilateral triangle.

## Ternary scatter plot with Plotly Express

[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/).

Here we use `px.scatter_ternary` to visualize the three-way split between the three major candidates in a municipal election.

```python
import plotly.express as px
df = px.data.election()
fig = px.scatter_ternary(df, a="Joly", b="Coderre", c="Bergeron")
fig.show()
```

We can scale and color the markers to produce a ternary bubble chart.

```python
import plotly.express as px
df = px.data.election()
fig = px.scatter_ternary(df, a="Joly", b="Coderre", c="Bergeron", hover_name="district",
    color="winner", size="total", size_max=15,
    color_discrete_map = {"Joly": "blue", "Bergeron": "green", "Coderre":"red"} )
fig.show()
```

### Ternary scatter plot with Plotly Graph Objects

```python
import plotly.graph_objects as go

rawData = [
    {'journalist':75,'developer':25,'designer':0,'label':'point 1'},
    {'journalist':70,'developer':10,'designer':20,'label':'point 2'},
    {'journalist':75,'developer':20,'designer':5,'label':'point 3'},
    {'journalist':5,'developer':60,'designer':35,'label':'point 4'},
    {'journalist':10,'developer':80,'designer':10,'label':'point 5'},
    {'journalist':10,'developer':90,'designer':0,'label':'point 6'},
    {'journalist':20,'developer':70,'designer':10,'label':'point 7'},
    {'journalist':10,'developer':20,'designer':70,'label':'point 8'},
    {'journalist':15,'developer':5,'designer':80,'label':'point 9'},
    {'journalist':10,'developer':10,'designer':80,'label':'point 10'},
    {'journalist':20,'developer':10,'designer':70,'label':'point 11'},
];

def makeAxis(title, tickangle):
    return {
      'title': title,
      'titlefont': { 'size': 20 },
      'tickangle': tickangle,
      'tickfont': { 'size': 15 },
      'tickcolor': 'rgba(0,0,0,0)',
      'ticklen': 5,
      'showline': True,
      'showgrid': True
    }

fig = go.Figure(go.Scatterternary({
    'mode': 'markers',
    'a': [i for i in map(lambda x: x['journalist'], rawData)],
    'b': [i for i in map(lambda x: x['developer'], rawData)],
    'c': [i for i in map(lambda x: x['designer'], rawData)],
    'text': [i for i in map(lambda x: x['label'], rawData)],
    'marker': {
        'symbol': 100,
        'color': '#DB7365',
        'size': 14,
        'line': { 'width': 2 }
    }
}))

fig.update_layout({
    'ternary': {
        'sum': 100,
        'aaxis': makeAxis('Journalist', 0),
        'baxis': makeAxis('<br>Developer', 45),
        'caxis': makeAxis('<br>Designer', -45)
    },
    'annotations': [{
      'showarrow': False,
      'text': 'Simple Ternary Plot with Markers',
        'x': 0.5,
        'y': 1.3,
        'font': { 'size': 15 }
    }]
})

fig.show()
```

#### Reference
See [function reference for `px.(scatter_ternary)`](https://plotly.com/python-api-reference/generated/plotly.express.scatter_ternary) or https://plotly.com/python/reference/scatterternary/ for more information and chart attribute options!
