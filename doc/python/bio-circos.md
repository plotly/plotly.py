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
    version: 3.9.7
  plotly:
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
import pandas as pd
import dash_bio


df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/Dash_Bio/Chromosomal/' +
    'clustergram_brain_cancer.csv', 
)

dash_bio.Clustergram(
    data=df,
    column_labels=list(df.columns.values),
    row_labels=list(df.index),
    height=800,
    width=700
)
```

## Dendrogram Cluster Colors/Line Widths
Change the colors of the dendrogram traces that are used to represent clusters, and configure their line widths.


```python
import pandas as pd
import dash_bio

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/Dash_Bio/Chromosomal/' +
    'clustergram_brain_cancer.csv', 
)

dash_bio.Clustergram(
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
```

## Relative Dendrogram Size
Change the relative width and height of, respectively, the row and column dendrograms compared to the width and height of the heatmap.


```python
import pandas as pd
import dash_bio

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/Dash_Bio/Chromosomal/' +
    'clustergram_brain_cancer.csv', 
)

dash_bio.Clustergram(
    data=df,
    column_labels=list(df.columns.values),
    row_labels=list(df.index),
    height=800,
    width=700,
    display_ratio=[0.1, 0.7]
)
```

## Circos with Dash

```python
from IPython.display import IFrame
snippet_url = 'https://dash-gallery.plotly.host/python-docs-dash-snippets/'
IFrame(snippet_url + 'bio-circos', width='100%', height=630)
```
