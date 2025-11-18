---
description: How to make Clustergram Charts in Python with Plotly.
---
## Default Clustergram
A clustergram is a combination heatmap-dendrogram that is commonly used in gene expression data. The hierarchical clustering that is represented by the dendrograms can be used to identify groups of genes with related expression levels. The Dash Bio Clustergram component is a Python-based component that uses plotly.py to generate a figure. It takes as input a two-dimensional numpy array of floating-point values. Imputation of missing data and computation of hierarchical clustering both occur within the component itself. Clusters that meet or exceed a user-defined threshold of similarity comprise single traces in the corresponding dendrogram, and can be highlighted with annotations. The user can specify additional parameters to customize the metrics and methods used to compute parts of the clustering, such as the pairwise distance between observations and the linkage matrix.

```python
import pandas as pd
import dash_bio


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash_Bio/Chromosomal/clustergram_brain_cancer.csv')

fig = dash_bio.Clustergram(
    data=df,
    column_labels=list(df.columns.values),
    row_labels=list(df.index),
    height=800,
    width=700
)
fig.show()
```

## Dendrogram Cluster Colors/Line Widths
Change the colors of the dendrogram traces that are used to represent clusters, and configure their line widths.


```python
import pandas as pd
import dash_bio


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash_Bio/Chromosomal/clustergram_brain_cancer.csv')

fig = dash_bio.Clustergram(
    data=df,
    column_labels=list(df.columns.values),
    row_labels=list(df.index),
    height=800,
    width=700,
    color_list={
        'row': ['#636EFA', '#00CC96', '#19D3F3'],
        'col': ['#AB63FA', '#EF553B'],
        'bg': '#506784'
    },
    line_width=2
)
fig.show()
```

## Relative Dendrogram Size
Change the relative width and height of, respectively, the row and column dendrograms compared to the width and height of the heatmap.


```python
import pandas as pd
import dash_bio


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash_Bio/Chromosomal/clustergram_brain_cancer.csv')

fig = dash_bio.Clustergram(
    data=df,
    column_labels=list(df.columns.values),
    row_labels=list(df.index),
    height=800,
    width=700,
    display_ratio=[0.1, 0.7]
)
fig.show()
```

## Clustergram with Dash

<pre hide_code="true">
```python
from IPython.display import IFrame
snippet_url = 'https://python-docs-dash-snippets.herokuapp.com/python-docs-dash-snippets/'
IFrame(snippet_url + 'bio-clustergram', width='100%', height=1200)
```
</pre>

<iframe src="https://python-docs-dash-snippets.herokuapp.com/python-docs-dash-snippets/bio-clustergram" width="100%" height="1200" style="border:none;"></iframe>
