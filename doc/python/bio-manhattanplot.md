---
description: Manhattan plot
---
## Manhattan Plot
ManhattanPlot allows you to visualize genome-wide association studies (GWAS) efficiently. Using WebGL under the hood, you can interactively explore overviews of massive datasets comprising hundreds of thousands of points at once, or take a closer look at a small subset of your data. Hover data and click data are accessible from within the Dash app.

```python
import pandas as pd
import dash_bio


df = pd.read_csv('https://raw.githubusercontent.com/plotly/dash-bio-docs-files/master/manhattan_data.csv')


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

<pre hide_code="true">
```python
from IPython.display import IFrame
snippet_url = 'https://python-docs-dash-snippets.herokuapp.com/python-docs-dash-snippets/'
IFrame(snippet_url + 'bio-manhattanplot', width='100%', height=1200)
```
</pre>

<iframe src="https://python-docs-dash-snippets.herokuapp.com/python-docs-dash-snippets/bio-manhattanplot" width="100%" height="1200" style="border:none;"></iframe>
