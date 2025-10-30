---
How to make Manhattan Plots in Python with Plotly.
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

**Error:**
```
Error executing code: cannot import name 'make_docstring' from 'plotly.express._doc' (/Users/daelenia/Desktop/plotly/plotly.py/plotly/express/_doc.py)
Traceback (most recent call last):
  File "/Users/daelenia/Desktop/plotly/plotly.py/bin/run_markdown.py", line 273, in _run_code
    exec(code, exec_globals)
  File "<string>", line 2, in <module>
  File "/Users/daelenia/Desktop/plotly/plotly.py/.venv/lib/python3.12/site-packages/dash_bio/__init__.py", line 11, in <module>
    from .component_factory._clustergram import Clustergram
  File "/Users/daelenia/Desktop/plotly/plotly.py/.venv/lib/python3.12/site-packages/dash_bio/component_factory/_clustergram.py", line 12, in <module>
    import plotly.figure_factory as ff
  File "/Users/daelenia/Desktop/plotly/plotly.py/plotly/figure_factory/__init__.py", line 32, in <module>
    from plotly.figure_factory._hexbin_map import (
  File "/Users/daelenia/Desktop/plotly/plotly.py/plotly/figure_factory/_hexbin_map.py", line 2, in <module>
    from plotly.express._doc import make_docstring
ImportError: cannot import name 'make_docstring' from 'plotly.express._doc' (/Users/daelenia/Desktop/plotly/plotly.py/plotly/express/_doc.py)
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

**Error:**
```
Error executing code: cannot import name 'make_docstring' from 'plotly.express._doc' (/Users/daelenia/Desktop/plotly/plotly.py/plotly/express/_doc.py)
Traceback (most recent call last):
  File "/Users/daelenia/Desktop/plotly/plotly.py/bin/run_markdown.py", line 273, in _run_code
    exec(code, exec_globals)
  File "<string>", line 2, in <module>
  File "/Users/daelenia/Desktop/plotly/plotly.py/.venv/lib/python3.12/site-packages/dash_bio/__init__.py", line 11, in <module>
    from .component_factory._clustergram import Clustergram
  File "/Users/daelenia/Desktop/plotly/plotly.py/.venv/lib/python3.12/site-packages/dash_bio/component_factory/_clustergram.py", line 12, in <module>
    import plotly.figure_factory as ff
  File "/Users/daelenia/Desktop/plotly/plotly.py/plotly/figure_factory/__init__.py", line 32, in <module>
    from plotly.figure_factory._hexbin_map import (
  File "/Users/daelenia/Desktop/plotly/plotly.py/plotly/figure_factory/_hexbin_map.py", line 2, in <module>
    from plotly.express._doc import make_docstring
ImportError: cannot import name 'make_docstring' from 'plotly.express._doc' (/Users/daelenia/Desktop/plotly/plotly.py/plotly/express/_doc.py)
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
