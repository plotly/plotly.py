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
    description: How to make tables in Python with Plotly.
    display_as: basic
    language: python
    layout: base
    name: Tables
    order: 11
    page_type: u-guide
    permalink: python/table/
    thumbnail: thumbnail/table.gif
---

`go.Table` provides a Table object for detailed data viewing. The data are arranged in
a grid of rows and columns. Most styling can be specified for header, columns, rows or individual cells. Table is using a column-major order, ie. the grid is represented as a vector of column vectors.

Note that [Dash](https://dash.plotly.com/) provides a different type of [DataTable](https://dash.plotly.com/datatable).

#### Basic Table

```python
import plotly.graph_objects as go

fig = go.Figure(data=[go.Table(header=dict(values=['A Scores', 'B Scores']),
                 cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]]))
                     ])
fig.show()
```

#### Styled Table

```python
import plotly.graph_objects as go

fig = go.Figure(data=[go.Table(
    header=dict(values=['A Scores', 'B Scores'],
                line_color='darkslategray',
                fill_color='lightskyblue',
                align='left'),
    cells=dict(values=[[100, 90, 80, 90], # 1st column
                       [95, 85, 75, 95]], # 2nd column
               line_color='darkslategray',
               fill_color='lightcyan',
               align='left'))
])

fig.update_layout(width=500, height=300)
fig.show()
```

#### Use a Pandas Dataframe

```python
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')

fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df.Rank, df.State, df.Postal, df.Population],
               fill_color='lavender',
               align='left'))
])

fig.show()
```

#### Tables in Dash

[Dash](https://plotly.com/dash/) is the best way to build analytical apps in Python using Plotly figures. To run the app below, run `pip install dash`, click "Download" to get the code and run `python app.py`.

Get started  with [the official Dash docs](https://dash.plotly.com/installation) and **learn how to effortlessly [style](https://plotly.com/dash/design-kit/) & publish apps like this with <a class="plotly-red" href="https://plotly.com/dash/">Dash Enterprise</a> or <a class="plotly-red" href="https://plotly.com/cloud/">Plotly Cloud</a>.**

```python hide_code=true
from IPython.display import IFrame
snippet_url = 'https://python-docs-dash-snippets.herokuapp.com/python-docs-dash-snippets/'
IFrame(snippet_url + 'table', width='100%', height=1200)
```

<div style="font-size: 0.9em;"><div style="width: calc(100% - 30px); box-shadow: none; border: thin solid rgb(229, 229, 229);"><div style="padding: 5px;"><div><p><strong>Sign up for Dash Club</strong> → Free cheat sheets plus updates from Chris Parmer and Adam Schroeder delivered to your inbox every two months. Includes tips and tricks, community apps, and deep dives into the Dash architecture.
<u><a href="https://go.plotly.com/dash-club?utm_source=Dash+Club+2022&utm_medium=graphing_libraries&utm_content=inline">Join now</a></u>.</p></div></div></div></div>


#### Changing Row and Column Size

```python
import plotly.graph_objects as go

values = [['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL<br>EXPENSES</b>'], #1st col
  ["Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
  "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
  "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
  "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad",
  "Lorem ipsum dolor sit amet, tollit discere inermis pri ut. Eos ea iusto timeam, an prima laboramus vim. Id usu aeterno adversarium, summo mollis timeam vel ad"]]


fig = go.Figure(data=[go.Table(
  columnorder = [1,2],
  columnwidth = [80,400],
  header = dict(
    values = [['<b>EXPENSES</b><br>as of July 2017'],
                  ['<b>DESCRIPTION</b>']],
    line_color='darkslategray',
    fill_color='royalblue',
    align=['left','center'],
    font=dict(color='white', size=12),
    height=40
  ),
  cells=dict(
    values=values,
    line_color='darkslategray',
    fill=dict(color=['paleturquoise', 'white']),
    align=['left', 'center'],
    font_size=12,
    height=30)
    )
])
fig.show()
```

#### Alternating Row Colors

```python
import plotly.graph_objects as go

headerColor = 'grey'
rowEvenColor = 'lightgrey'
rowOddColor = 'white'

fig = go.Figure(data=[go.Table(
  header=dict(
    values=['<b>EXPENSES</b>','<b>Q1</b>','<b>Q2</b>','<b>Q3</b>','<b>Q4</b>'],
    line_color='darkslategray',
    fill_color=headerColor,
    align=['left','center'],
    font=dict(color='white', size=12)
  ),
  cells=dict(
    values=[
      ['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL</b>'],
      [1200000, 20000, 80000, 2000, 12120000],
      [1300000, 20000, 70000, 2000, 130902000],
      [1300000, 20000, 120000, 2000, 131222000],
      [1400000, 20000, 90000, 2000, 14102000]],
    line_color='darkslategray',
    # 2-D list of colors for alternating rows
    fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],
    align = ['left', 'center'],
    font = dict(color = 'darkslategray', size = 11)
    ))
])

fig.show()
```

#### Row Color Based on Variable

```python
import plotly.graph_objects as go

import pandas as pd

colors = ['rgb(239, 243, 255)', 'rgb(189, 215, 231)', 'rgb(107, 174, 214)',
          'rgb(49, 130, 189)', 'rgb(8, 81, 156)']
data = {'Year' : [2010, 2011, 2012, 2013, 2014], 'Color' : colors}
df = pd.DataFrame(data)

fig = go.Figure(data=[go.Table(
  header=dict(
    values=["Color", "<b>YEAR</b>"],
    line_color='white', fill_color='white',
    align='center', font=dict(color='black', size=12)
  ),
  cells=dict(
    values=[df.Color, df.Year],
    line_color=[df.Color], fill_color=[df.Color],
    align='center', font=dict(color='black', size=11)
  ))
])

fig.show()
```

#### Cell Color Based on Variable

```python
import plotly.graph_objects as go
from plotly.colors import n_colors
import numpy as np
np.random.seed(1)

colors = n_colors('rgb(255, 200, 200)', 'rgb(200, 0, 0)', 9, colortype='rgb')
a = np.random.randint(low=0, high=9, size=10)
b = np.random.randint(low=0, high=9, size=10)
c = np.random.randint(low=0, high=9, size=10)

fig = go.Figure(data=[go.Table(
  header=dict(
    values=['<b>Column A</b>', '<b>Column B</b>', '<b>Column C</b>'],
    line_color='white', fill_color='white',
    align='center',font=dict(color='black', size=12)
  ),
  cells=dict(
    values=[a, b, c],
    line_color=[np.array(colors)[a],np.array(colors)[b], np.array(colors)[c]],
    fill_color=[np.array(colors)[a],np.array(colors)[b], np.array(colors)[c]],
    align='center', font=dict(color='white', size=11)
    ))
])

fig.show()
```

#### Reference
For more information on tables and table attributes see: https://plotly.com/python/reference/table/.
