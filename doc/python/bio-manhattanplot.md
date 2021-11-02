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
    name: Manhattan Plot
    order: 1
    page_type: u-guide
    permalink: python/manhattan-plot/
    thumbnail: thumbnail/manhattan_plot.png
---

## Manhattan Plot
ManhattanPlot allows you to visualize genome-wide association studies (GWAS) efficiently. Using WebGL under the hood, you can interactively explore overviews of massive datasets comprising hundreds of thousands of points at once, or take a closer look at a small subset of your data. Hover data and click data are accessible from within the Dash app.

```python
import pandas as pd
import dash_bio


df = pd.read_csv('https://git.io/manhattan_data.csv')


dash_bio.ManhattanPlot(
    dataframe=df,
)
```

## Highlighted points color, and colors of the suggestive line and the genome-wide line
Change the color of the points that are considered significant.

```python
import pandas as pd
import dash_bio


df = pd.read_csv('https://git.io/manhattan_data.csv')

dash_bio.ManhattanPlot(
    dataframe=df,
    highlight_color='#00FFAA',
    suggestiveline_color='#AA00AA',
    genomewideline_color='#AA5500'
)
```

## ManhattanPlot with Dash

```python hide_code=true
from IPython.display import IFrame
snippet_url = 'https://dash-gallery.plotly.host/python-docs-dash-snippets/'
IFrame(snippet_url + 'bio-manhattanplot', width='100%', height=630)
```
