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
    thumbnail: thumbnail/alignment_chart.png
---

## Alignment Viewer

The Alignment Viewer (MSA) component is used to align multiple genomic or proteomic sequences from a FASTA or Clustal file. Among its extensive set of features, the multiple sequence alignment viewer can display multiple subplots showing gap and conservation info, alongside industry standard colorscale support and consensus sequence. No matter what size your alignment is, Alignment Viewer is able to display your genes or proteins snappily thanks to the underlying WebGL architecture powering the component. You can quickly scroll through your long sequence with a slider or a heatmap overview.

Note that the AlignmentChart only returns a chart of the sequence, while AlignmentViewer has integrated controls for colorscale, heatmaps, and subplots allowing you to interactively control your sequences.

## Bar Chart for conservation visualization

```python
import plotly.express as px
import pandas as pd

df = (pd.read_csv('https://git.io/gene_conservation.csv')
        .set_index('0')
        .loc[['consensus','conservation']]
        .T
        .astype({"conservation": float}))

fig = px.bar(df, labels={ 'index': 'base' }, hover_name='consensus', y='conservation')
fig.show()
```

## Alignment Chart in dash_bio

```python hide_code=true
from IPython.display import IFrame
snippet_url = 'https://dash-gallery.plotly.host/python-docs-dash-snippets/'
IFrame(snippet_url + 'bio-alignmentchart', width='100%', height=630)
```
