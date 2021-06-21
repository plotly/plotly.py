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
    description: How to make Icicle Charts.
    display_as: basic
    language: python
    layout: base
    name: Icicle Charts
    order: 17
    page_type: u-guide
    permalink: python/icicle-charts/
    thumbnail: thumbnail/icicle.png
---

*New in v5.0*

Icicle charts visualize hierarchical data using rectangular sectors that cascade from root to leaves in one of four directions: up, down, left, or right. Similar to [Sunburst charts](https://plotly.com/python/sunburst-charts/) and [Treemaps](https://plotly.com/python/treemaps/) charts, the hierarchy is defined by `labels` (`names` for `px.icicle`) and `parents` attributes. Click on one sector to zoom in/out, which also displays a pathbar on the top of your icicle. To zoom out, you can click the parent sector or click the pathbar as well.

### Basic Icicle Plot with plotly.express

[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/).

With `px.icicle`, each item in the `character` list is represented as a rectangular sector of the icicle.

```python
import plotly.express as px
data = dict(
    character=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    value=[10, 14, 12, 10, 2, 6, 6, 4, 4])

fig =px.icicle(
    data,
    names='character',
    parents='parent',
    values='value',
)
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
```

### Icicle of a rectangular DataFrame with plotly.express

Hierarchical data are often stored as a rectangular dataframe, with different columns corresponding to different levels of the hierarchy. `px.icicle` can take a path parameter corresponding to a list of columns. Note that `id` and `parent` should not be provided if path is given.


```python
import plotly.express as px
df = px.data.tips()
fig = px.icicle(df, path=[px.Constant("all"), 'day', 'time', 'sex'], values='total_bill')
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
```

### Icicle of a rectangular DataFrame with continuous color argument in px.icicle

If a color argument is passed, the color of a node is computed as the average of the color values of its children, weighted by their values.

```python
import plotly.express as px
import numpy as np
df = px.data.gapminder().query("year == 2007")
fig = px.icicle(df, path=[px.Constant("world"), 'continent', 'country'], values='pop',
                  color='lifeExp', hover_data=['iso_alpha'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df['lifeExp'], weights=df['pop']))
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
```

### Icicle of a rectangular DataFrame with discrete color argument in px.icicle

When the argument of color corresponds to non-numerical data, discrete colors are used. If a sector has the same value of the color column for all its children, then the corresponding color is used, otherwise the first color of the discrete color sequence is used.

```python
import plotly.express as px
df = px.data.tips()
fig = px.icicle(df, path=[px.Constant("all"), 'sex', 'day', 'time'],
                values='total_bill', color='day')
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
```

In the example below the color of **Saturday** and **Sunday** sectors is the same as **Dinner** because there are only Dinner entries for Saturday and Sunday. However, for Female -> Friday there are both lunches and dinners, hence the "mixed" color (blue here) is used.

```python
import plotly.express as px
df = px.data.tips()
fig = px.icicle(df, path=[px.Constant("all"), 'sex', 'day', 'time'],
                values='total_bill', color='time')
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
```

### Using an explicit mapping for discrete colors

For more information about discrete colors, see the [dedicated page](https://plotly.com/python/discrete-color/).

```python
import plotly.express as px
df = px.data.tips()
fig = px.icicle(df, path=[px.Constant("all"), 'sex', 'day', 'time'],
                values='total_bill', color='time',
                color_discrete_map={'(?)':'lightgrey', 'Lunch':'gold', 'Dinner':'darkblue'})
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
```

### Rectangular data with missing values

If the dataset is not fully rectangular, missing values should be supplied as **None**. Note that the parents of **None** entries must be a leaf, i.e. it cannot have other children than **None** (otherwise a **ValueError** is raised).

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
fig = px.icicle(df, path=['all', 'regions', 'sectors', 'vendors'], values='sales')
fig.update_traces(root_color='lightgrey')
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
```

### Basic Icicle Plot with go.Icicle

If Plotly Express does not provide a good starting point, it is also possible to use [the more generic `go.Icicle` class from `plotly.graph_objects`](/python/graph-objects/).

Main arguments:

1. `labels` (`names` in `px.icicle` since `labels` is reserved for overriding columns names): sets the labels of icicle sectors.
2. `parents`: sets the parent sectors of icicle sectors. An empty string `''` is used for the root node in the hierarchy. In this example, the root is "Eve".
3. `values`: sets the values associated with icicle sectors, determining their width (See the `branchvalues` section below for different modes for setting the width).

```python
import plotly.graph_objects as go

fig =go.Figure(go.Icicle(
    labels=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    values=[10, 14, 12, 10, 2, 6, 6, 4, 4],
    root_color="lightgrey"
))

fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
```

### Icicle with Repeated Labels

```python
import plotly.graph_objects as go

fig =go.Figure(go.Icicle(
 ids=["Sports",
    "North America", "Europe", "Australia", "North America - Football", "Soccer",
    "North America - Rugby", "Europe - Football", "Rugby",
    "Europe - American Football","Australia - Football", "Association",
    "Australian Rules", "Autstralia - American Football", "Australia - Rugby",
    "Rugby League", "Rugby Union"
  ],
  labels= ["Sports",
    "North<br>America", "Europe", "Australia", "Football", "Soccer", "Rugby",
    "Football", "Rugby", "American<br>Football", "Football", "Association",
    "Australian<br>Rules", "American<br>Football", "Rugby", "Rugby<br>League",
    "Rugby<br>Union"
  ],
  parents=["",
    "Sports", "Sports", "Sports", "North America", "North America", "North America", "Europe",
    "Europe", "Europe","Australia", "Australia - Football", "Australia - Football",
    "Australia - Football", "Australia - Football", "Australia - Rugby",
    "Australia - Rugby"
  ],
    root_color="lightgrey"
))
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))

fig.show()
```

### Branchvalues

With branchvalues "total", the value of the parent represents the height/width of its slice. In the example below, "Enoch" is 4 and "Awan" is 6 and so Enoch's height is 4/6ths of Awans. With branchvalues "remainder", the parent's width is determined by its own value plus those of its children. So, Enoch's height is 4/10ths of Awan's (4 / (6 + 4)).

Note that this means that the sum of the values of the children cannot exceed the value of their parent when branchvalues is set to "total". When branchvalues is set to "remainder" (the default), children will not take up all of the space below their parent (unless the parent is the root and it has a value of 0).

```python
import plotly.graph_objects as go

fig =go.Figure(go.Icicle(
    labels=[ "Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents=["",    "Eve",  "Eve",  "Seth", "Seth", "Eve",  "Eve",  "Awan",  "Eve" ],
    values=[  65,    14,     12,     10,     2,      6,      6,      4,       4],
    branchvalues="total",
    root_color="lightgrey"
))
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))

fig.show()
```

### Large Number of Slices

This example uses a [plotly grid attribute](https://plotly.com/python/reference/layout/#layout-grid) for the suplots. Reference the row and column destination using the [domain](https://plotly.com/python/reference/icicle/#icicle-domain) attribute.

```python
import plotly.graph_objects as go

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/96c0bd/sunburst-coffee-flavors-complete.csv')

fig = go.Figure()

fig.add_trace(go.Icicle(
    ids=df.ids,
    labels=df.labels,
    parents=df.parents,
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

fig = go.Figure(go.Icicle(
    ids = df.ids,
    labels = df.labels,
    parents = df.parents,
    root_color="lightgrey"
))
fig.update_layout(
    uniformtext=dict(minsize=10, mode='hide'),
    margin = dict(t=50, l=25, r=25, b=25)
)
fig.show()
```

### Icicle chart with a continuous colorscale

The example below visualizes a breakdown of sales (corresponding to sector width) and call success rate (corresponding to sector color) by region, county and salesperson level. For example, when exploring the data you can see that although the East region is behaving poorly, the Tyler county is still above average -- however, its performance is reduced by the poor success rate of salesperson GT.

In the right subplot which has a `maxdepth` of two levels, click on a slice to see its breakdown to lower levels.

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
    Build a hierarchy of levels for Icicle charts.

    Levels are given starting from the bottom to the top of the hierarchy,
    ie the last level corresponds to the root.
    """
    df_all_trees = pd.DataFrame(columns=['id', 'parent', 'value', 'color'])
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
        df_all_trees = df_all_trees.append(df_tree, ignore_index=True)
    total = pd.Series(dict(id='total', parent='',
                              value=df[value_column].sum(),
                              color=df[color_columns[0]].sum() / df[color_columns[1]].sum()))
    df_all_trees = df_all_trees.append(total, ignore_index=True)
    return df_all_trees


df_all_trees = build_hierarchical_dataframe(df, levels, value_column, color_columns)
average_score = df['sales'].sum() / df['calls'].sum()

fig = make_subplots(1, 2, specs=[[{"type": "domain"}, {"type": "domain"}]],)

fig.add_trace(go.Icicle(
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

fig.add_trace(go.Icicle(
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

### Set Color of Icicle Sectors

```python
import plotly.graph_objects as go

labels = ["container", "A1", "A2", "A3", "A4", "A5", "B1", "B2"]
parents = ["", "container", "A1", "A2", "A3", "A4", "container", "B1"]

fig = go.Figure(go.Icicle(
    labels = labels,
    parents = parents,
    marker_colors = ["pink", "royalblue", "lightgray", "purple",
                     "cyan", "lightgray", "lightblue", "lightgreen"]))

fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
```

This example uses iciclecolorway attribute, which should be set in layout.

```python
import plotly.graph_objects as go

values = [0, 11, 12, 13, 14, 15, 20, 30]
labels = ["container", "A1", "A2", "A3", "A4", "A5", "B1", "B2"]
parents = ["", "container", "A1", "A2", "A3", "A4", "container", "B1"]

fig = go.Figure(go.Icicle(
    labels = labels,
    parents = parents,
    values=values,
    root_color="lightblue"
))

fig.update_layout(
    iciclecolorway = ["pink", "lightgray"],
    margin = dict(t=50, l=25, r=25, b=25)
)
fig.show()
```

```python
import plotly.graph_objects as go

values = [0, 11, 12, 13, 14, 15, 20, 30]
labels = ["container", "A1", "A2", "A3", "A4", "A5", "B1", "B2"]
parents = ["", "container", "A1", "A2", "A3", "A4", "container", "B1"]

fig = go.Figure(go.Icicle(
    labels = labels,
    values = values,
    parents = parents,
    marker_colorscale = 'Blues'))
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))

fig.show()
```

### Set the Direction of Icicle charts

As mentioned above, Icicle charts can grow in one of four directions. Icicle charts have a `tiling` attribute and this has two attributes: `orientation` and `flip`. `orientation` takes either `h` (horiztonal) or `v` (vertical) and `flip` takes either `x` or `y`. You can use these two attributes in combination to create each of the four cardinal directions: left, right, top, bottom.

**Up Direction (Flame Chart)**

```python
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/96c0bd/sunburst-coffee-flavors-complete.csv')

fig = go.Figure(
    go.Icicle(
        ids = df.ids,
        labels = df.labels,
        parents = df.parents,
        root_color="lightgrey",
        tiling = dict(
            orientation='v',
            flip='y'
        )
    )
)
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
```

**Down Direction (Icicle)**

```python
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/96c0bd/sunburst-coffee-flavors-complete.csv')

fig = go.Figure(
    go.Icicle(
        ids = df.ids,
        labels = df.labels,
        parents = df.parents,
        root_color="lightgrey",
        tiling = dict(
            orientation='v'
        )
    )
)
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
```

**Right Direction**

```python
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/96c0bd/sunburst-coffee-flavors-complete.csv')

fig = go.Figure(
    go.Icicle(
        ids = df.ids,
        labels = df.labels,
        parents = df.parents,
        root_color="lightgrey",
        tiling = dict(
            orientation='h'
        )
    )
)
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
```

**Left Direction**

```python
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/96c0bd/sunburst-coffee-flavors-complete.csv')

fig = go.Figure(
    go.Icicle(
        ids = df.ids,
        labels = df.labels,
        parents = df.parents,
        root_color="lightgrey",
        tiling = dict(
            orientation='h',
            flip='x'
        )
    )
)
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
```

#### Reference

See [function reference for `px.icicle()`](https://plotly.com/python-api-reference/generated/plotly.express.icicle) or https://plotly.com/python/reference/icicle/ for more information and chart attribute options!
