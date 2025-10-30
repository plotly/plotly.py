---
description: How to make Alignment Charts in Python with Plotly.
---
## Alignment Viewer

The Alignment Viewer (MSA) component is used to align multiple genomic or proteomic sequences from a FASTA or Clustal file. Among its extensive set of features, the multiple sequence alignment viewer can display multiple subplots showing gap and conservation info, alongside industry standard colorscale support and consensus sequence. No matter what size your alignment is, Alignment Viewer is able to display your genes or proteins snappily thanks to the underlying WebGL architecture powering the component. You can quickly scroll through your long sequence with a slider or a heatmap overview.

Note that the AlignmentChart only returns a chart of the sequence, while AlignmentViewer has integrated controls for colorscale, heatmaps, and subplots allowing you to interactively control your sequences.

## Bar Chart for conservation visualization

```python
import plotly.express as px
import pandas as pd

df = (pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash_Bio/Genetic/gene_conservation.csv')
        .set_index('0')
        .loc[['consensus','conservation']]
        .T
        .astype({"conservation": float}))

fig = px.bar(df, labels={ 'index': 'base' }, hover_name='consensus', y='conservation')
fig.show()
```

## Alignment Chart in dash_bio

<pre hide_code="true">
```python
from IPython.display import IFrame
snippet_url = 'https://python-docs-dash-snippets.herokuapp.com/python-docs-dash-snippets/'
IFrame(snippet_url + 'bio-alignmentchart', width='100%', height=1200)
```
</pre>

<iframe src="https://python-docs-dash-snippets.herokuapp.com/python-docs-dash-snippets/bio-alignmentchart" width="100%" height="1200" style="border:none;"></iframe>
