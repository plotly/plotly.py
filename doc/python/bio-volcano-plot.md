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
    name: Volcano plot
    order: 1
    page_type: u-guide
    permalink: python/volcano-plot/
    thumbnail: thumbnail/volcano-plot.png
---

## VolcanoPlot
An example of a default VolcanoPlot component without any extra properties.


```python
import pandas as pd
import dash_bio 


df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/' +
    'volcano_data1.csv'
)

dash_bio.VolcanoPlot(
    dataframe=df,
)
```

## Point Sizes And Line Widths
Change the size of the points on the scatter plot, and the widths of the effect lines and genome-wide line.


```python
import pandas as pd
import dash_bio as dashbio

df = pd.read_csv('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/volcano_data1.csv')

dashbio.VolcanoPlot(
    dataframe=df,
    point_size=10,
    effect_size_line_width=4,
    genomewideline_width=2
)
```

## VolcanoPlot with Dash

```python
from IPython.display import IFrame
snippet_url = 'https://dash-gallery.plotly.host/python-docs-dash-snippets/'
IFrame(snippet_url + 'bio-volcano', width='100%', height=630)
```

## VolcanoPlot Properties
> Access this documentation in your Python terminal with:
> 
> ```>>> help(dash_bio.VolcanoPlot)```
> 
> Our recommended IDE for writing Dash apps is Dash Enterprise's Data Science Workspaces, which has typeahead support for Dash Component Properties. Find out if your company is using Dash Enterprise.

**dataframe** (_dataframe_; required): A pandas dataframe which must contain at least the following two columns: - a numeric quantity to plot such as a p-value or zscore - a numeric quantity measuring the strength of association, typically an odds ratio, regression coefficient, or log fold change. Here, it is referred to as `effect_size`.

**Additional keys** (misc.): Arbitrary arguments can be passed to modify the Layout and styling of the graph. A full reference of acceptable args is available [here](https://plotly.com/python-api-reference/generated/plotly.graph_objects.Layout.html). Some commonly used layout keys are: - title (dict: optional): Dict with compatible properties for the title of the figure layout. - xaxis (dict: optional): Dict with compatible properties for the x-axis of the figure layout. - yaxis (dict: optional): Dict with compatible properties for the y-axis of the figure layout. - height (number; optional): Sets the plot's height (in px). - width (number; optional): Sets the plot's width (in px). - margin (dict | plotly.graph_objects.layout.Margin instance): A dict or Margin instance that sets the separation between the main plotting space and the outside of the figure. - legend (dict | plotly.graph_objects.layout.Legend instance): A dict or Legend instance with compatible properties.

**annotation** (_string_; optional): A string denoting the column to use as annotations. This could be any annotation information that you want to include in the plot (e.g., zscore, effect size, minor allele frequency).

**col** (_string_; optional): Color of the points of the Scatter plot. Can be in any color format accepted by plotly.graph_objects.

**effect_size** (_string_; default `'EFFECTSIZE'`): A string denoting the column name for the effect size. This column must be numeric and must not contain missing nor NaN values.

**effect_size_line** (_bool_ | list; default `[-1, 1]`): A boolean which must be either False to deactivate the option, or a list/array containing the upper and lower bounds of the effect size values. Significant data points will have lower values than the lower bound, or higher values than the higher bound. Keeping the default value will result in assigning the list [-1, 1] to the argument.

**effect_size_line_color** (_string_; default `'grey'`): Color of the effect size lines.

**effect_size_line_width** (_number_; default `2`): Width of the effect size lines.

**gene** (_string_; default `GENE`): A string denoting the column name for the GENE names. More generally, this could be any annotation information that should be included in the plot.

**genomewideline_value** (_bool_ | number; default `-log10(5e-8)`): A boolean which must be either False to deactivate the option, or a numerical value corresponding to the p-value above which the data points are considered significant.

**genomewideline_color** (_string_; default `'red'`): Color of the genome-wide line. Can be in any color format accepted by plotly.graph_objects.

**genomewideline_width** (_number_; default `1`): Width of the genome-wide line.

**highlight** (_bool_; default `True`): Whether the data points considered significant should be highlighted or not.

**highlight_color** (_string_; default `'red'`): Color of the data points highlighted because considered significant. Can be in any color format accepted by plotly.graph_objects. # ... Example 1: Random Volcano Plot ''' dataframe = pd.DataFrame( np.random.randint(0,100,size=(100, 2)), columns=['P', 'EFFECTSIZE']) fig = create_volcano(dataframe, title=dict(text='XYZ Volcano plot')) plotly.offline.plot(fig, image='png') '''

**logp** (_bool_; default `True`): If True, the -log10 of the p-value is plotted. It isn't very useful to plot raw p-values; however, plotting the raw value could be useful for other genome-wide plots (e.g., peak heights, Bayes factors, test statistics, and other "scores").

**p (_string_;** default `'P'`): A string denoting the column name for the float quantity to be plotted on the y-axis. This column must be numeric. It does not have to be a p-value. It can be any numeric quantity such as peak heights, Bayes factors, test statistics. If it is not a p-value, make sure to set logp = False.

**point_size** (_number_; default `5`): Size of the points of the Scatter plot.

**snp** (_string_; default `'SNP'`): A string denoting the column name for the SNP names (e.g., rs number). More generally, this column could be anything that identifies each point being plotted. For example, in an Epigenomewide association study (EWAS), this could be the probe name or cg number. This column should be a character. This argument is optional, however it is necessary to specify it if you want to highlight points on the plot using the highlight argument in the figure method.

**xlabel** (_string_; optional): Label of the x axis.

**ylabel** (_string_; default `'-log10(p)'`): Label of the y axis.

```python

```
