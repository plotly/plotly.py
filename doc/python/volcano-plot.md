---
description: How to make Volcano Plots in Python with Plotly.
---

## Volcano Plot
Volcano Plot interactively identifies clinically meaningful markers in genomic experiments, i.e., markers that are statistically significant and have an effect size greater than some threshold. Specifically, volcano plots depict the negative log-base-10 p-values plotted against their effect size.

```python
import pandas as pd
import dash_bio


df = pd.read_csv('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/volcano_data1.csv')

dash_bio.VolcanoPlot(
    dataframe=df,
)
```

## Point Sizes And Line Widths
Change the size of the points on the scatter plot, and the widths of the effect lines and genome-wide line.


```python
import pandas as pd
import dash_bio


df = pd.read_csv('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/volcano_data1.csv')

dash_bio.VolcanoPlot(
    dataframe=df,
    point_size=10,
    effect_size_line_width=4,
    genomewideline_width=2
)
```

## VolcanoPlot with Dash

<pre hide_code="true">
```python
from IPython.display import IFrame
snippet_url = 'https://python-docs-dash-snippets.herokuapp.com/python-docs-dash-snippets/'
IFrame(snippet_url + 'bio-volcano', width='100%', height=1200)
```
</pre>

<iframe src="https://python-docs-dash-snippets.herokuapp.com/python-docs-dash-snippets/bio-volcano" width="100%" height="1200" style="border:none;"></iframe>