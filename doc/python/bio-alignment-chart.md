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
    name: Alignment Chart
    order: 1
    page_type: u-guide
    permalink: python/alignment-chart/
    thumbnail: thumbnail/alignment-chart.png
---

## Bar Chart for conservation visualization

```python
import plotly.express as px
import pandas as pd

df = (pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash_Bio/Genetic/gene_conservation.csv')
        .set_index('0')
        .loc[['consensus','conservation']]
        .T)

fig = px.bar(df, labels={ 'index': 'base' }, hover_name='consensus', y='conservation')
fig.show()
```

## Alignment Chart in dash_bio

```python no_display=true
from IPython.display import IFrame
snippet_url = 'https://dash-gallery.plotly.host/python-docs-dash-snippets/'
IFrame(snippet_url + 'bio-alignmentchart', width='100%', height=630)
```
