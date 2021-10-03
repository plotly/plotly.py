---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.0
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
    version: 3.9.6
  plotly:
    # description:
    display_as: bio
    language: python
    layout: base
    name: Clustergram
    order: 1
    page_type: u-guide
    permalink: python/clustergram/
    thumbnail: thumbnail/clustergram.png
---

## Default Clustergram
An example of a default Clustergram component without any extra properties.


```python
from jupyter_dash import JupyterDash

import pandas as pd
from dash.dependencies import Input, Output
import dash_bio as dashbio
from dash import html
from dash import dcc

app = JupyterDash(__name__)

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/' +
    'clustergram_mtcars.tsv',
    sep='	', skiprows=4
).set_index('model')

columns = list(df.columns.values)
rows = list(df.index)

app.layout = html.Div([
    "Rows to display",
    dcc.Dropdown(
        id='my-default-clustergram-input',
        options=[
            {'label': row, 'value': row} for row in list(df.index)
        ],
        value=rows[:10],
        multi=True
    ),

    html.Div(id='my-default-clustergram')
])

@app.callback(
    Output('my-default-clustergram', 'children'),
    Input('my-default-clustergram-input', 'value')
)
def update_clustergram(rows):
    if len(rows) < 2:
        return "Please select at least two rows to display."

    return dcc.Graph(figure=dashbio.Clustergram(
        data=df.loc[rows].values,
        column_labels=columns,
        row_labels=rows,
        color_threshold={
            'row': 250,
            'col': 700
        },
        hidden_labels='row',
        height=800,
        width=700
    ))

app.run_server()
```

## Dendrogram Cluster Colors/Line Widths
Change the colors of the dendrogram traces that are used to represent clusters, and configure their line widths.


```python
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_bio as dashbio
import pandas as pd

app = JupyterDash(__name__)


df = pd.read_csv('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/clustergram_mtcars.tsv',
                 sep='	', skiprows=4).set_index('model')

columns = list(df.columns.values)
rows = list(df.index)

app.layout = dcc.Graph(
    figure=dashbio.Clustergram(
        data=df.loc[rows].values,
        row_labels=rows,
        column_labels=columns,
        color_threshold={
            'row': 250,
            'col': 700
        },
        height=800,
        width=700,
        color_list={
            'row': ['#636EFA', '#00CC96', '#19D3F3'],
            'col': ['#AB63FA', '#EF553B'],
            'bg': '#506784'
        },
        line_width=2
))

app.run_server(mode="inline")
```

## Relative Dendrogram Size
Change the relative width and height of, respectively, the row and column dendrograms compared to the width and height of the heatmap.


```python
from jupyter_dash import JupyterDash
import pandas as pd
from dash import dcc
import dash_bio as dashbio


app = JupyterDash(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/clustergram_mtcars.tsv',
                 sep='	', skiprows=4).set_index('model')

columns = list(df.columns.values)
rows = list(df.index)

clustergram = 

app.layout = dcc.Graph(
    figure=dashbio.Clustergram(
        data=df.loc[rows].values,
        row_labels=rows,
        column_labels=columns,
        color_threshold={
            'row': 250,
            'col': 700
        },
        height=800,
        width=700,
        display_ratio=[0.1, 0.7]
))

app.run_server(mode="inline")
```

## Clustergram Properties
> Access this documentation in your Python terminal with:
>
> ```>>> help(dash_bio.Clustergram)```
> 
> Our recommended IDE for writing Dash apps is Dash Enterprise's Data Science Workspaces, which has typeahead support for Dash Component Properties. Find out if your company is using Dash Enterprise.

**data** (_2D array-like_; required): Matrix or table of observations (dropping columns of non-numeric dtype).

**annotation_font** (_dict_; optional): The font options for annotations, as specified in the Plotly graph_objects documentation (see: https://plotly.cp,/python/reference/#layout-scene-annotations-items-annotation-font).

**computed_traces** (_dict_; optional): The dendrogram traces from another (precomputed) Clustergram component.

**column_labels** (_list_; optional): List of column category labels (observation labels).

**cluster** (_string_; default `'all'`): The dimension along which the data will be clustered: 'row', 'column', or 'all'; 'all' means data will be clustered along columns, then clustered along rows of column-clustered data.

**col_dist** (_string_; default `'euclidean'`): Distance metric for columns. Passed as argument `metric` to the function specified in `dist_fun` when called for clustering along columns.

**color_threshold** (_dict_; default `{'row': 0, 'col': 0}`): Maximum linkage value for which unique colors are assigned to clusters; 'row' for rows, and 'col' for columns.

**color_map** (_list_; default `[[0.0, 'rgb(255,0,0)'], [0.5, 'rgb(0,0,0)'], [1.0, 'rgb(0,255,0)']]`): Colorscale for the heatmap. Top-level elements contain two elements, the first of which refers to the percentile rank, and the second to the applied color. For instance, [[0.0, 'white'], [0.5, 'gray'], [1.0, 'black']] means that cells in the 49th percentile would be white; cells at the 50th or higher percentiles, excluding the 100th percentile, would be gray; and the cell(s) at the 100th percentile would be black.

**color_list** (_dict_; optional): The list of colors to use for different clusters in the dendrogram that have a root under the threshold for each dimension. If there are fewer colors than there are clusters along a specific dimension, the colors of the clusters will cycle through the colors specified in the list. The keys are: 'row' (for row clusters), 'col' (for column clusters), and 'bg' (for all traces above the clustering threshold for both row and column).

**center_values** (_bool_; default `True`): Whether or not to center the values of the heatmap about zero.

**col_group_marker** (_list_; optional): A list containing the annotations for column clusters in the dendrogram. Each annotation is a dictionary with the keys 'group_number' (the cluster number to highlight), 'annotation' (a string containing the text of the annotation), and 'color' (a string representation of the color of the annotation).

**dist_fun** (_function_; default `scipy.spatial.distance.pdist`): Function to compute the pairwise distance from the observations (see docs for scipy.spatial.distance.pdist).

**display_range** (_double_; default `3.0`): In the heatmap, standardized values from the dataset that are below the negative of this value will be colored with one shade, and the values that are above this value will be colored with another.

**display_ratio** (_list_ | number; default `0.2`): The dendrograms' heights with respect to the size of the heatmap; with one element, both the row and column dendrograms have the same ratio; with two, the row dendrogram ratio corresponds to the first element of the list and the column dendrogram ratio corresponds to the second element of the list.

**generate_curves_dict** (_bool_; default `False`): Whether or not to return a dictionary containing information about the cluster number associated with each curve number in the graph. (May be useful for capturing the cluster number that is clicked.)

**hidden_labels** (_list_; optional): List containing strings 'row' and/or 'col' if row and/or column labels should be hidden on the final plot.

**height** (_number_; default `500`): The height of the graph, in px.

**imputer_parameters** (_dict_; optional): Specifies the parameters 'missing_values' and 'strategy' of the SimpleImputer class from scikit-learn 0.20.1 (both of these parameters must be keys in the dictionary). An additional parameter, 'axis', is used to specify the direction along which to impute (a parameter of Imputer, which was deprecated in scikit-learn 0.20.0): 'axis=0' indicates that imputing should happen along columns, while 'axis=1' indicates that it should happen along rows (see: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Imputer.html).

**link_fun** (_function_; default `scipy.cluster.hierarchy.linkage`): Function to compute the linkage matrix from the pairwise distances (see docs for scipy.cluster.hierarchy.linkage).

**log_transform** (_bool_; default `False`): Whether or not to transform the data by taking the base-two logarithm of all values in the dataset.

**line_width** (_list_ | number; default `0.5`): The line width for the dendrograms. If in list format, the first element corresponds to the width of the row dendrogram traces, and the second corresponds to the width of the column dendrogram traces.

**optimal_leaf_order** (_bool_; default `False`): Whether to enable (True) or disable (False) the option to determine leaf order that maximizes similarity between neighboring leaves.

**paper_bg_color** (_string_; default `rgba(0,0,0,0)`): The background color of the paper on the graph.

**plot_bg_color** (_string_; default `rgba(0,0,0,0)`): The background color of the subplots on the graph.

**return_computed_traces** (_bool_; default `False`): Whether or not to return the precomputed dendrogram traces. (May be useful if one wishes to add, e.g., group markers to the figure without recalculating the clustering in the entire figure.)

**row_labels** (_list_; optional): Listm of row category labels (observation labels).

**row_dist** (_string_; default `'euclidean'`): Distance metric for rows. Passed as argument `metric` to the function specified in `dist_fun` when called for clustering along rows.

**row_group_marker** (_list_; optional): A list containing the annotations for row clusters in the dendrogram. Each annotation is a dictionary with the keys 'group_number' (the cluster number to highlight), 'annotation' (a string containing the text of the annotation), and 'color' (a string representation of the color of the annotation).

**standardize** (_string_; default `'none'`): The dimension for standardizing values, so that the mean is 0 and the standard deviation is 1, along the specified dimension: 'row', 'column', or 'none'.

**tick_font** (_dict_; optional): The font options for ticks, as specified in the Plotly graph_objects documentation (see: https://plotly.com/python/reference/#bar-marker-colorbar-tickfont).

**width** (_number_; default `500`): The width of the graph, in px.

```python

```
