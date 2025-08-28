---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.6
  kernelspec:
    display_name: Python 3 (ipykernel)
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
    version: 3.10.11
  plotly:
    description: How to make Treemap Charts with Plotly
    display_as: basic
    language: python
    layout: base
    name: Treemap Charts
    order: 13
    page_type: u-guide
    permalink: python/treemaps/
    thumbnail: thumbnail/treemap.png
---

[Treemap charts](https://en.wikipedia.org/wiki/Treemapping) visualize hierarchical data using nested rectangles. The input data format is the same as for [Sunburst Charts](https://plotly.com/python/sunburst-charts/) and [Icicle Charts](https://plotly.com/python/icicle-charts/): the hierarchy is defined by [labels](https://plotly.com/python/reference/treemap/#treemap-labels) (`names` for `px.treemap`) and [parents](https://plotly.com/python/reference/treemap/#treemap-parents) attributes. Click on one sector to zoom in/out, which also displays a pathbar in the upper-left corner of your treemap. To zoom out you can use the path bar as well.

### Basic Treemap with plotly.express

[Plotly Express](plotly-express.md) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](px-arguments.md) and produces [easy-to-style figures](styling-plotly-express.md).

With `px.treemap`, each row of the DataFrame is represented as a sector of the treemap.

```python
import plotly.express as px
fig = px.treemap(
    names = ["Eve","Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents = ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"]
)
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
```

### Treemap of a rectangular DataFrame with plotly.express

Hierarchical data are often stored as a rectangular dataframe, with different columns corresponding to different levels of the hierarchy. `px.treemap` can take a `path` parameter corresponding to a list of columns. Note that `id` and `parent` should not be provided if `path` is given.

```python
import plotly.express as px
df = px.data.tips()
fig = px.treemap(df, path=[px.Constant("all"), 'day', 'time', 'sex'], values='total_bill')
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
```

### Treemap of a rectangular DataFrame with continuous color argument in px.treemap

If a `color` argument is passed, the color of a node is computed as the average of the color values of its children, weighted by their values.

**Note**: for best results, ensure that the first `path` element is a single root node. In the examples below we are creating a dummy column containing identical values for each row to achieve this.

```python
import plotly.express as px
import numpy as np
df = px.data.gapminder().query("year == 2007")
fig = px.treemap(df, path=[px.Constant("world"), 'continent', 'country'], values='pop',
                  color='lifeExp', hover_data=['iso_alpha'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop']))
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
```

### Treemap of a rectangular DataFrame with discrete color argument in px.treemap

When the argument of `color` corresponds to non-numerical data, discrete colors are used. If a sector has the same value of the `color` column for all its children, then the corresponding color is used, otherwise the first color of the discrete color sequence is used.

```python
import plotly.express as px
df = px.data.tips()
fig = px.treemap(df, path=[px.Constant("all"), 'sex', 'day', 'time'],
                 values='total_bill', color='day')
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
```

In the example below the color of Saturday and Sunday sectors is the same as Dinner because there are only Dinner entries for Saturday and Sunday. However, for Female -> Friday there are both lunches and dinners, hence the "mixed" color (blue here) is used.

```python
import plotly.express as px
df = px.data.tips()
fig = px.treemap(df, path=[px.Constant("all"), 'sex', 'day', 'time'],
                 values='total_bill', color='time')
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
```

### Using an explicit mapping for discrete colors

For more information about discrete colors, see the [dedicated page](discrete-color.md).

```python
import plotly.express as px
df = px.data.tips()
fig = px.treemap(df, path=[px.Constant("all"), 'sex', 'day', 'time'],
                 values='total_bill', color='time',
                  color_discrete_map={'(?)':'lightgrey', 'Lunch':'gold', 'Dinner':'darkblue'})
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
```

### Rectangular data with missing values

If the dataset is not fully rectangular, missing values should be supplied as `None`.

```python
import plotly.express as px
import pandas as pd
vendors = ["A", "B", "C", "D", None, "E", "F", "G", "H", None]
sectors = ["Tech", "Tech", "Finance", "Finance", "Other",
           "Tech", "Tech", "Finance", "Finance", "Other"]
regions = ["North", "North", "North", "North", "North",
           "South", "South", "South", "South", "South"]
sales = [1, 3, 2, 4, 1, 2, 2, 1, 4, 1]
df = pd.DataFrame(
    dict(vendors=vendors, sectors=sectors, regions=regions, sales=sales)
)
df["all"] = "all" # in order to have a single root node
print(df)
fig = px.treemap(df, path=['all', 'regions', 'sectors', 'vendors'], values='sales')
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
```

### Treemap with Rounded Corners


*New in 5.12*

Update treemap sectors to have rounded corners by configuring the `cornerradius` in px.

```python
import plotly.express as px
fig = px.treemap(
    names = ["Eve","Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents = ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"]
)
fig.update_traces(marker=dict(cornerradius=5))
fig.show()
```

### Basic Treemap with go.Treemap

If Plotly Express does not provide a good starting point, it is also possible to use [the more generic `go.Treemap` class from `plotly.graph_objects`](graph-objects.md).

```python
import plotly.graph_objects as go

fig = go.Figure(go.Treemap(
    labels = ["Eve","Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents = ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"],
    root_color="lightgrey"
))

fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
```

### Set Different Attributes in Treemap

This example uses the following attributes:

1.  [values](https://plotly.com/python/reference/treemap/#treemap-values): sets the values associated with each of the sectors.
2.  [textinfo](https://plotly.com/python/reference/treemap/#treemap-textinfo): determines which trace information appear on the graph that can be 'text', 'value', 'current path', 'percent root', 'percent entry', and 'percent parent', or any combination of them.
3.  [pathbar](https://plotly.com/python/reference/treemap/#treemap-pathbar): a main extra feature of treemap to display the current path of the visible portion of the hierarchical map. It may also be useful for zooming out of the graph.
4.  [branchvalues](https://plotly.com/python/reference/treemap/#treemap-branchvalues): determines how the items in `values` are summed. When set to "total", items in `values` are taken to be value of all its descendants. In the example below Eve = 65, which is equal to 14 + 12 + 10 + 2 + 6 + 6 + 1 + 4.
    When set to "remainder", items in `values` corresponding to the root and the branches sectors are taken to be the extra part not part of the sum of the values at their leaves.

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots

labels = ["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"]
parents = ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"]

fig = make_subplots(
    cols = 2, rows = 1,
    column_widths = [0.4, 0.4],
    subplot_titles = ('branchvalues: <b>remainder<br />&nbsp;<br />', 'branchvalues: <b>total<br />&nbsp;<br />'),
    specs = [[{'type': 'treemap', 'rowspan': 1}, {'type': 'treemap'}]]
)

fig.add_trace(go.Treemap(
    labels = labels,
    parents = parents,
    values =  [10, 14, 12, 10, 2, 6, 6, 1, 4],
    textinfo = "label+value+percent parent+percent entry+percent root",
    root_color="lightgrey"
),row = 1, col = 1)

fig.add_trace(go.Treemap(
    branchvalues = "total",
    labels = labels,
    parents = parents,
    values = [65, 14, 12, 10, 2, 6, 6, 1, 4],
    textinfo = "label+value+percent parent+percent entry",
    root_color="lightgrey"
),row = 1, col = 2)

fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
```

### Set Color of Treemap Sectors

There are three different ways to change the color of the sectors in Treemap:

1.  [marker.colors](https://plotly.com/python/reference/treemap/#treemap-marker-colors), 2) [colorway](https://plotly.com/python/reference/treemap/#treemap-colorway), 3) [colorscale](https://plotly.com/python/reference/treemap/#treemap-colorscale). The following examples show how to use each of them.

```python
import plotly.graph_objects as go

values = [0, 11, 12, 13, 14, 15, 20, 30]
labels = ["container", "A1", "A2", "A3", "A4", "A5", "B1", "B2"]
parents = ["", "container", "A1", "A2", "A3", "A4", "container", "B1"]

fig = go.Figure(go.Treemap(
    labels = labels,
    values = values,
    parents = parents,
    marker_colors = ["pink", "royalblue", "lightgray", "purple",
                     "cyan", "lightgray", "lightblue", "lightgreen"]
))

fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
```

This example uses `treemapcolorway` attribute, which should be set in layout.

```python
import plotly.graph_objects as go

values = [0, 11, 12, 13, 14, 15, 20, 30]
labels = ["container", "A1", "A2", "A3", "A4", "A5", "B1", "B2"]
parents = ["", "container", "A1", "A2", "A3", "A4", "container", "B1"]

fig = go.Figure(go.Treemap(
    labels = labels,
    values = values,
    parents = parents,
    root_color="lightblue"
))

fig.update_layout(
    treemapcolorway = ["pink", "lightgray"],
    margin = dict(t=50, l=25, r=25, b=25)
)
fig.show()
```

```python
import plotly.graph_objects as go

values = [0, 11, 12, 13, 14, 15, 20, 30]
labels = ["container", "A1", "A2", "A3", "A4", "A5", "B1", "B2"]
parents = ["", "container", "A1", "A2", "A3", "A4", "container", "B1"]

fig = go.Figure(go.Treemap(
    labels = labels,
    values = values,
    parents = parents,
    marker_colorscale = 'Blues'
))

fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))

fig.show()
```

### Treemap chart with a continuous colorscale

The example below visualizes a breakdown of sales (corresponding to sector width) and call success rate (corresponding to sector color) by region, county and salesperson level. For example, when exploring the data you can see that although the East region is behaving poorly, the Tyler county is still above average -- however, its performance is reduced by the poor success rate of salesperson GT.

In the right subplot which has a `maxdepth` of two levels, click on a sector to see its breakdown to lower levels.

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/sales_success.csv')
print(df.head())

levels = ['salesperson', 'county', 'region'] # levels used for the hierarchical chart
color_columns = ['sales', 'calls']
value_column = 'calls'

def build_hierarchical_dataframe(df, levels, value_column, color_columns=None):
    """
    Build a hierarchy of levels for Sunburst or Treemap charts.

    Levels are given starting from the bottom to the top of the hierarchy,
    ie the last level corresponds to the root.
    """
    df_list = []
    for i, level in enumerate(levels):
        df_tree = pd.DataFrame(columns=['id', 'parent', 'value', 'color'])
        dfg = df.groupby(levels[i:]).sum()
        dfg = dfg.reset_index()
        df_tree['id'] = dfg[level].copy()
        if i < len(levels) - 1:
            df_tree['parent'] = dfg[levels[i+1]].copy()
        else:
            df_tree['parent'] = 'total'
        df_tree['value'] = dfg[value_column]
        df_tree['color'] = dfg[color_columns[0]] / dfg[color_columns[1]]
        df_list.append(df_tree)
    total = pd.Series(dict(id='total', parent='',
                              value=df[value_column].sum(),
                              color=df[color_columns[0]].sum() / df[color_columns[1]].sum()), name=0)
    df_list.append(total)
    df_all_trees = pd.concat(df_list, ignore_index=True)
    return df_all_trees


df_all_trees = build_hierarchical_dataframe(df, levels, value_column, color_columns)
average_score = df['sales'].sum() / df['calls'].sum()

fig = make_subplots(1, 2, specs=[[{"type": "domain"}, {"type": "domain"}]],)

fig.add_trace(go.Treemap(
    labels=df_all_trees['id'],
    parents=df_all_trees['parent'],
    values=df_all_trees['value'],
    branchvalues='total',
    marker=dict(
        colors=df_all_trees['color'],
        colorscale='RdBu',
        cmid=average_score),
    hovertemplate='<b>%{label} </b> <br> Sales: %{value}<br> Success rate: %{color:.2f}',
    name=''
    ), 1, 1)

fig.add_trace(go.Treemap(
    labels=df_all_trees['id'],
    parents=df_all_trees['parent'],
    values=df_all_trees['value'],
    branchvalues='total',
    marker=dict(
        colors=df_all_trees['color'],
        colorscale='RdBu',
        cmid=average_score),
    hovertemplate='<b>%{label} </b> <br> Sales: %{value}<br> Success rate: %{color:.2f}',
    maxdepth=2
    ), 1, 2)

fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
```

### Nested Layers in Treemap

The following example uses hierarchical data that includes layers and grouping. Treemap and [Sunburst](https://plotly.com/python/sunburst-charts/) charts reveal insights into the data, and the format of your hierarchical data. [maxdepth](https://plotly.com/python/reference/treemap/#treemap-maxdepth) attribute sets the number of rendered sectors from the given level.

```python
import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/96c0bd/sunburst-coffee-flavors-complete.csv')

fig = go.Figure()

fig.add_trace(go.Treemap(
    ids = df.ids,
    labels = df.labels,
    parents = df.parents,
    maxdepth=3,
    root_color="lightgrey"
))

fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))

fig.show()
```

### Controlling text fontsize with uniformtext

If you want all the text labels to have the same size, you can use the `uniformtext` layout parameter. The `minsize` attribute sets the font size, and the `mode` attribute sets what happens for labels which cannot fit with the desired fontsize: either `hide` them or `show` them with overflow.

*Note: animated transitions are currently not implemented when `uniformtext` is used.*

```python
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/96c0bd/sunburst-coffee-flavors-complete.csv')

fig = go.Figure(go.Treemap(
    ids = df.ids,
    labels = df.labels,
    parents = df.parents,
    pathbar_textfont_size=15,
    root_color="lightgrey"
))
fig.update_layout(
    uniformtext=dict(minsize=10, mode='hide'),
    margin = dict(t=50, l=25, r=25, b=25)
)
fig.show()
```

### Pattern Fills

*New in 5.15*

Treemap charts support [patterns](pattern-hatching-texture.md) (also known as hatching or texture) in addition to color. In this example, we apply a pattern to the root node.

```python
import plotly.graph_objects as go

fig = go.Figure(
    go.Treemap(
        labels = ["Eve","Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
        parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"],
        root_color="lightgrey",
        textfont_size=20,
        marker=dict(pattern=dict(shape=["|"], solidity=0.80)),
    )
)

fig.show()
```

#### Reference

See [function reference for `px.treemap()`](https://plotly.com/python-api-reference/generated/plotly.express.treemap) or https://plotly.com/python/reference/treemap/ for more information and chart attribute options!
