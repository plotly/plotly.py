---
jupyter:
  celltoolbar: Tags
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
    name: Volcano Plot
    order: 1
    page_type: u-guide
    permalink: python/volcano-plot/
    thumbnail: thumbnail/volcano_plot.png
---

## VolcanoPlot
Volcano Plot interactively identifies clinically meaningful markers in genomic experiments, i.e., markers that are statistically significant and have an effect size greater than some threshold. Specifically, volcano plots depict the negative log-base-10 p-values plotted against their effect size.

```python
import pandas as pd
import dash_bio


df = pd.read_csv('https://git.io/volcano_data1.csv')

dash_bio.VolcanoPlot(
    dataframe=df,
)
```

## Point Sizes And Line Widths
Change the size of the points on the scatter plot, and the widths of the effect lines and genome-wide line.


```python
import pandas as pd
import dash_bio


df = pd.read_csv('https://git.io/volcano_data1.csv')

dash_bio.VolcanoPlot(
    dataframe=df,
    point_size=10,
    effect_size_line_width=4,
    genomewideline_width=2
)
```

## VolcanoPlot with Dash

```python hide_code=true
from IPython.display import IFrame
snippet_url = 'https://dash-gallery.plotly.host/python-docs-dash-snippets/'
IFrame(snippet_url + 'bio-volcano', width='100%', height=630)
```
