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
    description: A primer on out-of-memory analytics of large datasets with Pandas,
      SQLite, and IPython notebooks.
    display_as: databases
    has_thumbnail: false
    language: python
    layout: base
    name: Big Data Analytics with Pandas and SQLite
    order: 4
    page_type: example_index
    permalink: python/big-data-analytics-with-pandas-and-sqlite/
    redirect_from: ipython-notebooks/big-data-analytics-with-pandas-and-sqlite/
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
This notebook explores a 3.9Gb CSV file containing NYC's 311 complaints since 2003. It's the most popular data set in [NYC's open data portal](https://nycopendata.socrata.com/data). This is a primer on out-of-memory data analysis with
- [pandas](http://pandas.pydata.org/): A library with easy-to-use data structures and data analysis tools. Also, interfaces to out-of-memory databases like SQLite.
- [IPython notebook](ipython.org/notebook.html): An interface for writing and sharing python code, text, and plots.
- [SQLite](https://www.sqlite.org/): An self-contained, server-less database that's easy to set-up and query from Pandas.
- [Plotly](https://plot.ly/python/): A platform for publishing beautiful, interactive graphs from Python to the web.

The dataset is too large to load into a Pandas dataframe. So, instead we'll perform out-of-memory aggregations with SQLite and load the result directly into a dataframe with Panda's `iotools`. It's pretty easy to stream a CSV into SQLite and SQLite requires no setup. The SQL query language is pretty intuitive coming from a Pandas mindset.

```python
import plotly.tools as tls
tls.embed('https://plot.ly/~chris/7365')
```

```python
import pandas as pd
from sqlalchemy import create_engine # database connection
import datetime as dt
from IPython.display import display

import plotly.plotly as py # interactive graphing
import plotly.graph_objs as go
```

#### Import the CSV data into SQLite
1. Load the CSV, chunk-by-chunk, into a DataFrame
2. Process the data a bit, strip out uninteresting columns
3. Append it to the SQLite database

```python
pd.read_csv('311_100M.csv', nrows=2).head()
```

```python
!wc -l < 311_100M.csv # Number of lines in dataset
```

```python
disk_engine = create_engine('sqlite:///311_8M.db') # Initializes database with filename 311_8M.db in current directory
```

```python
start = dt.datetime.now()
chunksize = 20000
j = 0
index_start = 1

for df in pd.read_csv('311_100M.csv', chunksize=chunksize, iterator=True, encoding='utf-8'):

    df = df.rename(columns={c: c.replace(' ', '') for c in df.columns}) # Remove spaces from columns

    df['CreatedDate'] = pd.to_datetime(df['CreatedDate']) # Convert to datetimes
    df['ClosedDate'] = pd.to_datetime(df['ClosedDate'])

    df.index += index_start

    # Remove the un-interesting columns
    columns = ['Agency', 'CreatedDate', 'ClosedDate', 'ComplaintType', 'Descriptor',
               'CreatedDate', 'ClosedDate', 'TimeToCompletion',
               'City']

    for c in df.columns:
        if c not in columns:
            df = df.drop(c, axis=1)


    j+=1
    print '{} seconds: completed {} rows'.format((dt.datetime.now() - start).seconds, j*chunksize)

    df.to_sql('data', disk_engine, if_exists='append')
    index_start = df.index[-1] + 1
```

##### `LIMIT` the number of rows that are retrieved

```python
df = pd.read_sql_query('SELECT Agency, Descriptor FROM data LIMIT 3', disk_engine)
df = pd.read_sql_query('SELECT ComplaintType, Descriptor, Agency '
                       'FROM data '
                       'LIMIT 10', disk_engine)
```

###### Filter rows with `WHERE`

```python
df = pd.read_sql_query('SELECT ComplaintType, Descriptor, Agency '
                       'FROM data '
                       'WHERE Agency = "NYPD" '
                       'LIMIT 10', disk_engine)
```

###### Filter multiple values in a column with `WHERE` and `IN`

```python
df = pd.read_sql_query('SELECT ComplaintType, Descriptor, Agency '
                       'FROM data '
                       'WHERE Agency IN ("NYPD", "DOB")'
                       'LIMIT 10', disk_engine)
```

###### Find the unique values in a column with `DISTINCT`

```python
df = pd.read_sql_query('SELECT DISTINCT City FROM data', disk_engine)
```

###### Query value counts with `COUNT(*)` and `GROUP BY`

```python
df = pd.read_sql_query('SELECT Agency, COUNT(*) as `num_complaints`'
                       'FROM data '
                       'GROUP BY Agency ', disk_engine)
```

###### Order the results with `ORDER` and `-`
Housing and Development Dept receives the most complaints

```python
df = pd.read_sql_query('SELECT Agency, COUNT(*) as `num_complaints`'
                       'FROM data '
                       'GROUP BY Agency '
                       'ORDER BY -num_complaints', disk_engine)

py.iplot([go.Bar(x=df.Agency, y=df.num_complaints)], filename='311/most common complaints by agency')
```

###### Heat / Hot Water is the most common complaint

```python
df = pd.read_sql_query('SELECT ComplaintType, COUNT(*) as `num_complaints`, Agency '
                       'FROM data '
                       'GROUP BY `ComplaintType` '
                       'ORDER BY -num_complaints', disk_engine)


most_common_complaints = df # used later
py.iplot({
    'data': [go.Bar(x=df['ComplaintType'], y=df.num_complaints)],
    'layout': {
        'margin': {'b': 150}, # Make the bottom margin a bit bigger to handle the long text
        'xaxis': {'tickangle': 40}} # Angle the labels a bit
    }, filename='311/most common complaints by complaint type')
```

*This graph is interactive. Click-and-drag horizontally to zoom, shift-click to pan, double click to autoscale*


##### What's the most common complaint in each city?


First, let's see how many cities are recorded in the dataset

```python
len(pd.read_sql_query('SELECT DISTINCT City FROM data', disk_engine))
```

Yikes - let's just plot the 10 most complained about cities

```python
df = pd.read_sql_query('SELECT City, COUNT(*) as `num_complaints` '
                                'FROM data '
                                'GROUP BY `City` '
                       'ORDER BY -num_complaints '
                       'LIMIT 10 ', disk_engine)
```

Flushing and FLUSHING, Jamaica and JAMAICA... the complaints are case sensitive.


###### Perform case insensitive queries with `GROUP BY` with `COLLATE NOCASE`

```python
df = pd.read_sql_query('SELECT City, COUNT(*) as `num_complaints` '
                        'FROM data '
                        'GROUP BY `City` '
                       'COLLATE NOCASE '
                       'ORDER BY -num_complaints '
                       'LIMIT 11 ', disk_engine)
cities = list(df.City)
cities.remove(None)

traces = [] # the series in the graph - one trace for each city

for city in cities:
    df = pd.read_sql_query('SELECT ComplaintType, COUNT(*) as `num_complaints` '
                           'FROM data '
                           'WHERE City = "{}" COLLATE NOCASE '
                           'GROUP BY `ComplaintType` '
                           'ORDER BY -num_complaints'.format(city), disk_engine)

    traces.append(go.Bar(x=df['ComplaintType'], y=df.num_complaints, name=city.capitalize()))

py.iplot({'data': traces, 'layout': go.Layout(barmode='stack', xaxis={'tickangle': 40}, margin={'b': 150})}, filename='311/complaints by city stacked')
```

*You can also `click` on the legend entries to hide/show the traces. Click-and-drag to zoom in and shift-drag to pan.*


Now let's normalize these counts. This is super easy now that this data has been reduced into a dataframe.

```python
for trace in traces:
    trace['y'] = 100.*trace['y']/sum(trace['y'])

py.iplot({'data': traces,
          'layout': go.Layout(
                barmode='group',
                xaxis={'tickangle': 40, 'autorange': False, 'range': [-0.5, 16]},
                yaxis={'title': 'Percent of Complaints by City'},
                margin={'b': 150},
                title='Relative Number of 311 Complaints by City')
         }, filename='311/relative complaints by city', validate=False)
```

- New York is loud
- Staten Island is moldy, wet, and vacant
- Flushing's muni meters are broken
- Trash collection is great in the Bronx
- Woodside doesn't like its graffiti

Click and drag to pan across the graph and see more of the complaints.


### Part 2: SQLite time series with Pandas


######  Filter SQLite rows with timestamp strings: `YYYY-MM-DD hh:mm:ss`

```python
df = pd.read_sql_query('SELECT ComplaintType, CreatedDate, City '
                       'FROM data '
                       'WHERE CreatedDate < "2014-11-16 23:47:00" '
                       'AND CreatedDate > "2014-11-16 23:45:00"', disk_engine)
```

######  Pull out the hour unit from timestamps with `strftime`


```python
df = pd.read_sql_query('SELECT CreatedDate, '
                              'strftime(\'%H\', CreatedDate) as hour, '
                              'ComplaintType '
                       'FROM data '
                       'LIMIT 5 ', disk_engine)
```

######  Count the number of complaints (rows) per hour with `strftime`, `GROUP BY`, and `count(*)`

```python
df = pd.read_sql_query('SELECT CreatedDate, '
                               'strftime(\'%H\', CreatedDate) as hour,  '
                               'count(*) as `Complaints per Hour`'
                       'FROM data '
                       'GROUP BY hour', disk_engine)

py.iplot({
    'data': [go.Bar(x=df['hour'], y=df['Complaints per Hour'])],
    'layout': go.Layout(xaxis={'title': 'Hour in Day'},
                     yaxis={'title': 'Number of Complaints'})}, filename='311/complaints per hour')
```

######  Filter noise complaints by hour

```python
df = pd.read_sql_query('SELECT CreatedDate, '
                               'strftime(\'%H\', CreatedDate) as `hour`,  '
                               'count(*) as `Complaints per Hour`'
                       'FROM data '
                       'WHERE ComplaintType IN ("Noise", '
                                               '"Noise - Street/Sidewalk", '
                                               '"Noise - Commercial", '
                                               '"Noise - Vehicle", '
                                               '"Noise - Park", '
                                               '"Noise - House of Worship", '
                                               '"Noise - Helicopter", '
                                               '"Collection Truck Noise") '
                       'GROUP BY hour', disk_engine)

py.iplot({
    'data': [go.Bar(x=df['hour'], y=df['Complaints per Hour'])],
    'layout': go.Layout(xaxis={'title': 'Hour in Day'},
                     yaxis={'title': 'Number of Complaints'},
                     title='Number of Noise Complaints in NYC by Hour in Day'
                    )}, filename='311/noise complaints per hour')
```

######  Segregate complaints by hour

```python
complaint_traces = {} # Each series in the graph will represent a complaint
complaint_traces['Other'] = {}

for hour in range(1, 24):
    hour_str = '0'+str(hour) if hour < 10 else str(hour)
    df = pd.read_sql_query('SELECT  CreatedDate, '
                                   'ComplaintType ,'
                                   'strftime(\'%H\', CreatedDate) as `hour`,  '
                                   'COUNT(*) as num_complaints '
                           'FROM data '
                           'WHERE hour = "{}" '
                           'GROUP BY ComplaintType '
                           'ORDER BY -num_complaints'.format(hour_str), disk_engine)

    complaint_traces['Other'][hour] = sum(df.num_complaints)

    # Grab the 7 most common complaints for that hour
    for i in range(7):
        complaint = df.get_value(i, 'ComplaintType')
        count = df.get_value(i, 'num_complaints')
        complaint_traces['Other'][hour] -= count
        if complaint in complaint_traces:
            complaint_traces[complaint][hour] = count
        else:
            complaint_traces[complaint] = {hour: count}

traces = []
for complaint in complaint_traces:
    traces.append({
        'x': range(25),
        'y': [complaint_traces[complaint].get(i, None) for i in range(25)],
        'name': complaint,
        'type': 'bar'
    })

py.iplot({
    'data': traces,
    'layout': {
        'barmode': 'stack',
        'xaxis': {'title': 'Hour in Day'},
        'yaxis': {'title': 'Number of Complaints'},
        'title': 'The 7 Most Common 311 Complaints by Hour in a Day'
    }}, filename='311/most common complaints by hour')
```

##### Aggregated time series


First, create a new column with timestamps rounded to the previous 15 minute interval


Then, `GROUP BY` that interval and `COUNT(*)`

```python
minutes = 15
seconds = 15*60

df = pd.read_sql_query('SELECT CreatedDate, '
                               'datetime(('
                                   'strftime(\'%s\', CreatedDate) / {seconds}) * {seconds}, \'unixepoch\') interval '
                       'FROM data '
                       'LIMIT 10 '.format(seconds=seconds), disk_engine)

minutes = 15
seconds = minutes*60

df = pd.read_sql_query('SELECT datetime(('
                                   'strftime(\'%s\', CreatedDate) / {seconds}) * {seconds}, \'unixepoch\') interval ,'
                               'COUNT(*) as "Complaints / interval"'
                       'FROM data '
                       'GROUP BY interval '
                       'ORDER BY interval '
                       'LIMIT 500'.format(seconds=seconds), disk_engine)

py.iplot(
    {
        'data': [{
            'x': df.interval,
            'y': df['Complaints / interval'],
            'type': 'bar'
        }],
        'layout': {
            'title': 'Number of 311 Complaints per 15 Minutes'
        }
}, filename='311/complaints per 15 minutes')
```

```python
hours = 24
minutes = hours*60
seconds = minutes*60

df = pd.read_sql_query('SELECT datetime(('
                                   'strftime(\'%s\', CreatedDate) / {seconds}) * {seconds}, \'unixepoch\') interval ,'
                               'COUNT(*) as "Complaints / interval"'
                       'FROM data '
                       'GROUP BY interval '
                       'ORDER BY interval'.format(seconds=seconds), disk_engine)

py.iplot(
    {
        'data': [{
            'x': df.interval,
            'y': df['Complaints / interval'],
            'type': 'bar'
        }],
        'layout': {
            'title': 'Number of 311 Complaints per Day'
        }
}, filename='311/complaints per day')
```

#### References

- Find more open data sets on [Data.gov](https://data.gov) and [NYC Open Data](https://nycopendata.socrata.com)
- Learn how to setup [MySql with Pandas and Plotly](http://moderndata.plot.ly/graph-data-from-mysql-database-in-python/)
- Add [interactive widgets to IPython notebooks](http://moderndata.plot.ly/widgets-in-ipython-notebook-and-plotly/) for customized data exploration
- Big data workflows with [HDF5 and Pandas](http://stackoverflow.com/questions/14262433/large-data-work-flows-using-pandas)
- [Interactive graphing with Plotly](https://plot.ly/python/)

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'sqlite.ipynb', 'python/big-data-analytics-with-pandas-and-sqlite/', 'Big Data Analytics with Pandas and SQLite',
    'A primer on out-of-memory analytics of large datasets with Pandas, SQLite, and IPython notebooks.',
    title='Big Data Workflow with Pandas and SQLite | Plotly', has_thumbnail='false',
    redirect_from='ipython-notebooks/big-data-analytics-with-pandas-and-sqlite/',
    language='python', page_type='example_index', display_as='databases', order=4, ipynb= '~notebook_demo/1')
```

```python

```
