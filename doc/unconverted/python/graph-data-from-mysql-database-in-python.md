---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.1.1
  kernelspec:
    display_name: Python 2
    language: python
    name: python2
  plotly:
    description: How to graph data from a MySQL database with Python.
    display_as: databases
    has_thumbnail: false
    language: python
    layout: base
    name: Plot Data from MySQL
    order: 1
    page_type: example_index
    permalink: python/graph-data-from-mysql-database-in-python/
    thumbnail: /images/static-image
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!
#### Version Check
Plotly's python package is updated frequently. Run `pip install plotly --upgrade` to use the latest version.

```python
import plotly
plotly.__version__
```

#### Imports
This notebook uses the MySQL world database:http://dev.mysql.com/doc/index-other.html. Instructions for setting up the world database in MySQL are [here](https://dev.mysql.com/doc/world-setup/en/). This notebook was created for [this article in <em>Modern Data</em>](http://mod.plot.ly/graph-data-from-mysql-database-in-python/)

```python
import plotly.plotly as py
import plotly.graph_objs as go

import MySQLdb
import pandas as pd
```

#### Connect to MySQL Database

```python
conn = MySQLdb.connect(host="localhost", user="root", passwd="xxxx", db="world")
cursor = conn.cursor()
cursor.execute('select Name, Continent, Population, LifeExpectancy, GNP from Country');

rows = cursor.fetchall()
str(rows)[0:300]
```

```python
df = pd.DataFrame( [[ij for ij in i] for i in rows] )
df.rename(columns={0: 'Name', 1: 'Continent', 2: 'Population', 3: 'LifeExpectancy', 4:'GNP'}, inplace=True);
df = df.sort_values(['LifeExpectancy'], ascending=[1]);
```

Some country names cause serialization errors in early versions of Plotly's Python client. The code block below takes care of this.

```python
country_names = df['Name']
for i in range(len(country_names)):
    try:
        country_names[i] = str(country_names[i]).decode('utf-8')
    except:
        country_names[i] = 'Country name decode error'
```

```python
trace1 = go.Scatter(
    x=df['GNP'],
    y=df['LifeExpectancy'],
    text=country_names,
    mode='markers'
)
layout = go.Layout(
    title='Life expectancy vs GNP from MySQL world database',
    xaxis=dict( type='log', title='GNP' ),
    yaxis=dict( title='Life expectancy' )
)
data = [trace1]
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='world GNP vs life expectancy')
```

```python
# (!) Set 'size' values to be proportional to rendered area,
#     instead of diameter. This makes the range of bubble sizes smaller
sizemode='area'

# (!) Set a reference for 'size' values (i.e. a population-to-pixel scaling).
#     Here the max bubble area will be on the order of 100 pixels
sizeref=df['Population'].max()/1e2**2

colors = {
    'Asia':"rgb(255,65,54)",
    'Europe':"rgb(133,20,75)",
    'Africa':"rgb(0,116,217)",
    'North America':"rgb(255,133,27)",
    'South America':"rgb(23,190,207)",
    'Antarctica':"rgb(61,153,112)",
    'Oceania':"rgb(255,220,0)",
}

# Define a hover-text generating function (returns a list of strings)
def make_text(X):
    return 'Country: %s\
    <br>Life Expectancy: %s years\
    <br>Population: %s million'\
    % (X['Name'], X['LifeExpectancy'], X['Population']/1e6)

# Define a trace-generating function (returns a Scatter object)
def make_trace(X, continent, sizes, color):
    return go.Scatter(
        x=X['GNP'],  # GDP on the x-xaxis
        y=X['LifeExpectancy'],    # life Exp on th y-axis
        name=continent,    # label continent names on hover
        mode='markers',    # (!) point markers only on this plot
        text=X.apply(make_text, axis=1).tolist(),
        marker= dict(
            color=color,           # marker color
            size=sizes,            # (!) marker sizes (sizes is a list)
            sizeref=sizeref,       # link sizeref
            sizemode=sizemode,     # link sizemode
            opacity=0.6,           # (!) partly transparent markers
            line= dict(width=3,color="white")  # marker borders
        )
    )

# Initialize data object
data = []

# Group data frame by continent sub-dataframe (named X),
#   make one trace object per continent and append to data object
for continent, X in df.groupby('Continent'):

    sizes = X['Population']                 # get population array
    color = colors[continent]               # get bubble color

    data.append(
        make_trace(X, continent, sizes, color)  # append trace to data object
    )

    # Set plot and axis titles
title = "Life expectancy vs GNP from MySQL world database (bubble chart)"
x_title = "Gross National Product"
y_title = "Life Expectancy [in years]"

# Define a dictionary of axis style options
axis_style = dict(
    type='log',
    zeroline=False,       # remove thick zero line
    gridcolor='#FFFFFF',  # white grid lines
    ticks='outside',      # draw ticks outside axes
    ticklen=8,            # tick length
    tickwidth=1.5         #   and width
)

# Make layout object
layout = go.Layout(
    title=title,             # set plot title
    plot_bgcolor='#EFECEA',  # set plot color to grey
    hovermode="closest",
    xaxis=dict(
        axis_style,      # add axis style dictionary
        title=x_title,   # x-axis title
        range=[2.0,7.2], # log of min and max x limits
    ),
    yaxis=dict(
        axis_style,      # add axis style dictionary
        title=y_title,   # y-axis title
    )
)

# Make Figure object
fig = go.Figure(data=data, layout=layout)

# (@) Send to Plotly and show in notebook
py.iplot(fig, filename='s3_life-gdp')
```

#### References
See https://plot.ly/python/getting-started/ for more information about Plotly's Python API!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish('mysql-ipython-notebook.ipynb', 'python/graph-data-from-mysql-database-in-python/',
                  'Plot Data from MySQL', 'How to graph data from a MySQL database with Python.',
                  title='Plot Data from a MySQL Database | Plotly', has_thumbnail='false',
                  page_type='example_index', display_as='databases', order=1, language='python',
                  uses_plotly_offline=True)
```

```python

```
