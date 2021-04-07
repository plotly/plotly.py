---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.0
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
    description: How to make Icicle Charts.
    display_as: basic
    language: python
    layout: base
    name: Icicle Charts
    order: 10
    page_type: u-guide
    permalink: python/icicle-charts/
    thumbnail: thumbnail/icicle.gif
---

Similar to Treemap plots and Icicle plots, Icicle plots provide yet another way to visualize hierarchical data. Children are drawn next to their parent boxes, all on one side (eg. each on the right side of their parent). Icicle plots can point in one of four directions (left, right, top, bottom); this direction is acheived with the `tiling` sub-attributes `orientation` and `flip`.

Main arguments:

1. `labels` (`names` in `px.icicle` since `labels` is reserved for overriding columns names): sets the labels of icicle sectors.
2. `parents`: sets the parent sectors of icicle sectors. An empty string `''` is used for the root node in the hierarchy. In this example, the root is "Eve".
3. `values`: sets the values associated with icicle sectors, determining their width (See the `branchvalues` section below for different modes for setting the width).

### Basic Icicle Plot with plotly.express

### Icicle of a rectangular DataFrame with plotly.express

### Icicle of a rectangular DataFrame with continuous color argument in px.icicle

### Icicle of a rectangular DataFrame with discrete color argument in px.icicle

### Using an explicit mapping for discrete colors

### Rectangular data with missing values

### Basic Icicle Plot with go.Icicle

If Plotly Express does not provide a good starting point, it is also possible to use [the more generic `go.Icicle` class from `plotly.graph_objects`](/python/graph-objects/).

```python
import plotly.graph_objects as go

fig =go.Figure(go.Icicle(
    labels=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    values=[10, 14, 12, 10, 2, 6, 6, 4, 4],
))
# Update layout for tight margin
# See https://plotly.com/python/creating-and-updating-figures/
fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))

fig.show()
```

### Icicle with Repeated Labels

```python
import plotly.graph_objects as go

fig =go.Figure(go.Icicle(
 ids=[
    "North America", "Europe", "Australia", "North America - Football", "Soccer",
    "North America - Rugby", "Europe - Football", "Rugby",
    "Europe - American Football","Australia - Football", "Association",
    "Australian Rules", "Autstralia - American Football", "Australia - Rugby",
    "Rugby League", "Rugby Union"
  ],
  labels= [
    "North<br>America", "Europe", "Australia", "Football", "Soccer", "Rugby",
    "Football", "Rugby", "American<br>Football", "Football", "Association",
    "Australian<br>Rules", "American<br>Football", "Rugby", "Rugby<br>League",
    "Rugby<br>Union"
  ],
  parents=[
    "", "", "", "North America", "North America", "North America", "Europe",
    "Europe", "Europe","Australia", "Australia - Football", "Australia - Football",
    "Australia - Football", "Australia - Football", "Australia - Rugby",
    "Australia - Rugby"
  ],
))
fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))

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
))
fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))

fig.show()
```

### Large Number of Slices

This example uses a [plotly grid attribute](https://plotly.com/python/reference/layout/#layout-grid) for the suplots. Reference the row and column destination using the [domain](https://plotly.com/python/reference/icicle/#icicle-domain) attribute.

```python
import plotly.graph_objects as go

import pandas as pd

df1 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/icicle-coffee-flavors-complete.csv')
df2 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/coffee-flavors.csv')

fig = go.Figure()

fig.add_trace(go.Icicle(
    ids=df1.ids,
    labels=df1.labels,
    parents=df1.parents,
    domain=dict(column=0)
))

fig.add_trace(go.Icicle(
    ids=df2.ids,
    labels=df2.labels,
    parents=df2.parents,
    domain=dict(column=1),
    maxdepth=2
))

fig.update_layout(
    grid= dict(columns=2, rows=1),
    margin = dict(t=0, l=0, r=0, b=0)
)

fig.show()
```

### Controlling text fontsize with uniformtext

If you want all the text labels to have the same size, you can use the `uniformtext` layout parameter. The `minsize` attribute sets the font size, and the `mode` attribute sets what happens for labels which cannot fit with the desired fontsize: either `hide` them or `show` them with overflow.

```python
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/icicle-coffee-flavors-complete.csv')

fig = go.Figure(go.Icicle(
        ids = df.ids,
        labels = df.labels,
        parents = df.parents))
fig.update_layout(uniformtext=dict(minsize=10, mode='hide'))
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
    Build a hierarchy of levels for Icicle or Treemap charts.

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

fig.update_layout(margin=dict(t=10, b=10, r=10, l=10))
fig.show()
```

### Set Color of Icicle Sectors

```python
import plotly.graph_objects as go

labels = ["A1", "A2", "A3", "A4", "A5", "B1", "B2"]
parents = ["", "A1", "A2", "A3", "A4", "", "B1"]

fig = go.Figure(go.Icicle(
    labels = labels,
    parents = parents,
    marker_colors = ["pink", "royalblue", "lightgray", "purple", "cyan", "lightgray", "lightblue"]))

fig.show()
```

This example uses treemapcolorway attribute, which should be set in layout.

```python
import plotly.graph_objects as go

labels = ["A1", "A2", "A3", "A4", "A5", "B1", "B2"]
parents = ["", "A1", "A2", "A3", "A4", "", "B1"]

fig = go.Figure(go.Treemap(
    labels = labels,
    parents = parents
))

fig.update_layout(treemapcolorway = ["pink", "lightgray"])

fig.show()
```

```python
import plotly.graph_objects as go

values = ["11", "12", "13", "14", "15", "20", "30"]
labels = ["A1", "A2", "A3", "A4", "A5", "B1", "B2"]
parents = ["", "A1", "A2", "A3", "A4", "", "B1"]

fig = go.Figure(go.Treemap(
    labels = labels,
    values = values,
    parents = parents,
    marker_colorscale = 'Blues'))

fig.show()
```

### Set the Direction of Icicle charts

As mentioned above, Icicle charts can grow in one of four directions. Icicle charts have a `tiling` attribute and this has two attributes: `orientation` and `flip`. `orientation` takes either `h` (horiztonal) or `v` (vertical) and `flip` takes either `x` or `y`. You can use these two attributes in combination to create each of the four cardinal directions: left, right, top, bottom.

NB. A "flame chart" refers to an Icicle chart that is pointing upwards.

Up

```python
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/sunburst-coffee-flavors-complete.csv')

fig = go.Figure(
    go.Icicle(
        ids = df.ids,
        labels = df.labels,
        parents = df.parents,
        tiling = dict(
            orientation='v',
            flip='y'
        )
    )
)

fig.update_layout(
    margin = {'t':0, 'l':0, 'r':0, 'b':0}
)
fig.show()
```

Down

```python
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/sunburst-coffee-flavors-complete.csv')

fig = go.Figure(
    go.Icicle(
        ids = df.ids,
        labels = df.labels,
        parents = df.parents,
        tiling = dict(
            orientation='v'
        )
    )
)

fig.update_layout(
    margin = {'t':0, 'l':0, 'r':0, 'b':0}
)
fig.show()
```

Right

```python
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/sunburst-coffee-flavors-complete.csv')

fig = go.Figure(
    go.Icicle(
        ids = df.ids,
        labels = df.labels,
        parents = df.parents,
        tiling = dict(
            orientation='h'
        )
    )
)

fig.update_layout(
    margin = {'t':0, 'l':0, 'r':0, 'b':0}
)
fig.show()
```

Left

```python
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/sunburst-coffee-flavors-complete.csv')

fig = go.Figure(
    go.Icicle(
        ids = df.ids,
        labels = df.labels,
        parents = df.parents,
        tiling = dict(
            orientation='h',
            flip='x'
        )
    )
)

fig.update_layout(
    margin = {'t':0, 'l':0, 'r':0, 'b':0}
)
fig.show()
```

### Pad

Similar to [treemaps](https://plotly.com/python/treemaps/), the space between each Icicle slice can be set with `pad`, a sub-attribute of the `tiling` attribute.


```python
import plotly.graph_objs as go
from plotly.subplots import make_subplots

import pandas as pd

df1 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/sunburst-coffee-flavors-complete.csv')

pad_vals = [0, 2, 4, 8]
num_of_cols = 4

fig = make_subplots(
    rows = 1, cols = 4,
    column_titles=[f'pad: {pad_vals[i]}' for i in range(num_of_cols)],
    specs = [
        [
            {'type': 'icicle', 'rowspan': 1} for i in range(num_of_cols)
        ]
    ]
)

fig.add_trace(
    go.Icicle(
        ids = df1.ids,
        labels = df1.labels,
        parents = df1.parents,
        root = dict( color = "DodgerBlue" ),
        tiling = dict(
            pad = pad_vals[0]
        )
    ),
    col = 1,
    row = 1
)

fig.add_trace(
    go.Icicle(
        ids = df1.ids,
        labels = df1.labels,
        parents = df1.parents,
        root = dict( color = "DodgerBlue" ),
        tiling = dict(
            pad = pad_vals[1]
        )
    ),
    col = 2,
    row = 1
)

fig.add_trace(
    go.Icicle(
        ids = df1.ids,
        labels = df1.labels,
        parents = df1.parents,
        root = dict( color = "DodgerBlue" ),
        tiling = dict(
            pad = pad_vals[2]
        )
    ),
    col = 3,
    row = 1
)

fig.add_trace(
    go.Icicle(
        ids = df1.ids,
        labels = df1.labels,
        parents = df1.parents,
        root = dict( color = "DodgerBlue" ),
        tiling = dict(
            pad = pad_vals[3]
        )
    ),
    col = 4,
    row = 1
)

fig.update_layout(
    margin = {'l':0, 'r':0, 'b':0},
)

fig.show()
```


#### Reference

See [function reference for `px.icicle()`](https://plotly.com/python-api-reference/generated/plotly.express.icicle) or https://plotly.com/python/reference/icicle/ for more information and chart attribute options!
