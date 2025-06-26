---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.1
  kernelspec:
    display_name: Python 3
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
    version: 3.8.8
  plotly:
    description: How to create charts from csv files with Plotly and Python
    display_as: advanced_opt
    has_thumbnail: false
    language: python
    layout: base
    name: Plot CSV Data
    order: 1
    page_type: example_index
    permalink: python/plot-data-from-csv/
    thumbnail: thumbnail/csv.jpg
---

CSV or comma-delimited-values is a very popular format for storing structured data. In this tutorial, we will see how to plot beautiful graphs using csv data, and Pandas. We will learn how to import csv data from an external source (a url), and plot it using Plotly and pandas.

First we import the data and look at it.

```python
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')
df.head()
```

### Plot from CSV with Plotly Express

```python
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')

fig = px.line(df, x = 'AAPL_x', y = 'AAPL_y', title='Apple Share Prices over time (2014)')
fig.show()
```

### Plot from CSV in Dash

[Dash](https://plotly.com/dash/) is the best way to build analytical apps in Python using Plotly figures. To run the app below, run `pip install dash`, click "Download" to get the code and run `python app.py`.

Get started  with [the official Dash docs](https://dash.plotly.com/installation) and **learn how to effortlessly [style](https://plotly.com/dash/design-kit/) & [deploy](https://plotly.com/dash/app-manager/) apps like this with <a class="plotly-red" href="https://plotly.com/dash/">Dash Enterprise</a>.**


```python hide_code=true
from IPython.display import IFrame
snippet_url = 'https://python-docs-dash-snippets.herokuapp.com/python-docs-dash-snippets/'
IFrame(snippet_url + 'plot-data-from-csv', width='100%', height=1200)
```

<div style="font-size: 0.9em;"><div style="width: calc(100% - 30px); box-shadow: none; border: thin solid rgb(229, 229, 229);"><div style="padding: 5px;"><div><p><strong>Sign up for Dash Club</strong> → Free cheat sheets plus updates from Chris Parmer and Adam Schroeder delivered to your inbox every two months. Includes tips and tricks, community apps, and deep dives into the Dash architecture.
<u><a href="https://go.plotly.com/dash-club?utm_source=Dash+Club+2022&utm_medium=graphing_libraries&utm_content=inline">Join now</a></u>.</p></div></div></div></div>


### Plot from CSV with `graph_objects`

```python
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')

fig = go.Figure(go.Scatter(x = df['AAPL_x'], y = df['AAPL_y'],
                  name='Share Prices (in USD)'))

fig.update_layout(title=dict(text='Apple Share Prices over time (2014)'),
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)

fig.show()
```

#### Reference

See https://plotly.com/python/getting-started for more information about Plotly's Python API!
