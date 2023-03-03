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


df = pd.read_csv('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/manhattan_data.csv')

"""
Keyword arguments:
- dataframe (dataframe; required): A pandas dataframe which must contain at
    least the following three columns:
            - the chromosome number
            - genomic base-pair position
            - a numeric quantity to plot such as a p-value or zscore
- chrm (string; default 'CHR'): A string denoting the column name for
    the chromosome. This column must be float or integer. Minimum
    number of chromosomes required is 1. If you have X, Y, or MT
    chromosomes, be sure to renumber these 23, 24, 25, etc.
- bp (string; default 'BP'): A string denoting the column name for the
    chromosomal position.
- p (string; default 'P'): A string denoting the column name for the
    float quantity to be plotted on the y-axis. This column must be
    numeric. It does not have to be a p-value. It can be any numeric
    quantity such as peak heights, Bayes factors, test statistics. If
    it is not a p-value, make sure to set logp = False.
- snp (string; default 'SNP'): A string denoting the column name for
    the SNP names (e.g., rs number). More generally, this column could
    be anything that identifies each point being plotted. For example,
    in an Epigenomewide association study (EWAS), this could be the
    probe name or cg number. This column should be a character. This
    argument is optional, however it is necessary to specify it if you
    want to highlight points on the plot, using the highlight argument
    in the figure method.
- gene (string; default 'GENE'): A string denoting the column name for
    the GENE names. This column could be a string or a float. More
    generally, it could be any annotation information that you want
    to include in the plot.
- annotation (string; optional): A string denoting the column to use
    as annotations. This column could be a string or a float. It
    could be any annotation information that you want to include in
    the plot (e.g., zscore, effect size, minor allele frequency).
- logp (bool; optional): If True, the -log10 of the p-value is
    plotted. It isn't very useful to plot raw p-values; however,
    plotting the raw value could be useful for other genome-wide plots
    (e.g., peak heights, Bayes factors, test statistics, other
    "scores", etc.)
- title (string; default 'Manhattan Plot'): The title of the graph.
- showgrid (bool; default true): Boolean indicating whether gridlines
    should be shown.
- xlabel (string; optional): Label of the x axis.
- ylabel (string; default '-log10(p)'): Label of the y axis.
- point_size (number; default 5): Size of the points of the Scatter
    plot.
- showlegend (bool; default true): Boolean indicating whether legends
    should be shown.
- col (string; optional): A string representing the color of the
    points of the scatter plot. Can be in any color format accepted by
    plotly.graph_objects.
- suggestiveline_value (bool | float; default 8): A value which must
    be either False to deactivate the option, or a numerical value
    corresponding to the p-value at which the line should be drawn.
    The line has no influence on the data points.
- suggestiveline_color (string; default 'grey'): Color of the suggestive
  line.
- suggestiveline_width (number; default 2): Width of the suggestive
    line.
- genomewideline_value (bool | float; default -log10(5e-8)): A boolean
    which must be either False to deactivate the option, or a numerical value
    corresponding to the p-value above which the data points are
    considered significant.
- genomewideline_color (string; default 'red'): Color of the genome-wide
    line. Can be in any color format accepted by plotly.graph_objects.
- genomewideline_width (number; default 1): Width of the genome-wide
  line.
- highlight (bool; default True): turning on/off the highlighting of
    data points considered significant.
- highlight_color (string; default 'red'): Color of the data points
    highlighted because they are significant. Can be in any color
    format accepted by plotly.graph_objects.
""" 

dash_bio.ManhattanPlot(
    dataframe=df,
)
```

## Highlighted points color, and colors of the suggestive line and the genome-wide line
Change the color of the points that are considered significant.

```python
import pandas as pd
import dash_bio


df = pd.read_csv('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/manhattan_data.csv')

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
snippet_url = 'https://python-docs-dash-snippets.herokuapp.com/python-docs-dash-snippets/'
IFrame(snippet_url + 'bio-manhattanplot', width='100%', height=1200)
```
