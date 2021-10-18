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

## Default AlignmentChart
An example of a default AlignmentChart component without any extra properties

```python
import urllib.request as urlreq

import dash_bio as dashbio


data = urlreq.urlopen(
    'https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/' +
    'alignment_viewer_p53.fasta'
).read().decode('utf-8')

app.layout = dashbio.AlignmentChart(
    id='my-default-alignment-viewer',
    data=data
)
```

## Consensus Sequence
Toggle the display of the consensus sequence at the bottom of the heatmap.

```python
import urllib.request as urlreq

import dash_bio as dashbio


data = urlreq.urlopen('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/alignment_viewer_p53.fasta').read().decode('utf-8')

app.layout = dashbio.AlignmentChart(
    data=data,
    showconsensus=False
)
```

## Tile Size
Change the height and/or width of the tiles.


```python
import urllib.request as urlreq
import dash_bio as dashbio

data = urlreq.urlopen('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/alignment_viewer_p53.fasta').read().decode('utf-8')

app.layout = dashbio.AlignmentChart(
    data=data,
    tilewidth=50
)
```

## Alignment Chart in `dash_bio`

```python
from IPython.display import IFrame
snippet_url = 'https://dash-gallery.plotly.host/python-docs-dash-snippets/'
IFrame(snippet_url + 'bio-circos', width='100%', height=630)
```
