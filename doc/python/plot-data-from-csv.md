---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: "1.1"
      jupytext_version: 1.2.0
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
    version: 3.6.8
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

### Plot from CSV with `graph_objects`

```python
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')

fig = go.Figure(go.Scatter(x = df['AAPL_x'], y = df['AAPL_y'],
                  name='Share Prices (in USD)'))

fig.update_layout(title='Apple Share Prices over time (2014)',
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)

fig.show()
```

#### Reference

See https://plot.ly/python/getting-started for more information about Plotly's Python API!
