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
    description: A tutorial showing how to plot Amazon AWS Redshift data with Plotly.
    display_as: databases
    has_thumbnail: false
    language: python
    layout: base
    name: Plot Data From Amazon Redshift
    order: 3
    page_type: example_index
    permalink: python/amazon-redshift/
    redirect_from: ipython-notebooks/amazon-redshift/
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

This notebook will go over one of the easiest ways to graph data from your [Amazon Redshift data warehouse](http://aws.amazon.com/redshift/) using [Plotly's public platform](https://plot.ly/) for publishing beautiful, interactive graphs from Python to the web.

[Plotly's Enterprise platform](https://plot.ly/product/enterprise/) allows for an easy way for your company to build and share graphs without the data leaving your servers.

#### Imports
In this notebook we'll be using [Amazon's Sample Redshift Data](http://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-create-sample-db.html) for this notebook. Although we won't be connecting through a JDBC/ODBC connection we'll be using the [psycopg2 package](http://initd.org/psycopg/docs/index.html) with [SQLAlchemy](http://www.sqlalchemy.org/)  and [pandas](http://pandas.pydata.org/) to make it simple to query and analyze our data.

```python
from __future__ import print_function #python 3 support

import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
import pandas as pd
import os
import requests
requests.packages.urllib3.disable_warnings() # this squashes insecure SSL warnings - DO NOT DO THIS ON PRODUCTION!
```

#### Connect to Redshift
You'll need your [Redshift Endpoint URL](http://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-connect-to-cluster.html) in order to access your Redshift instance. I've obscured mine below but yours will be in a format similar to `datawarehouse.some_chars_here.region_name.redshift.amazonaws.com`. Connecting to Redshift is made extremely simple once you've set your cluster configuration. This configuration needs to include the username, password, port, host and database name. I've opted to store mine as environmental variables on my machine.


```python
redshift_endpoint = os.getenv("REDSHIFT_ENDPOINT")
redshift_user = os.getenv("REDSHIFT_USER")
redshift_pass = os.getenv("REDSHIFT_PASS")
port = 5439
dbname = 'dev'
```

As I mentioned there are numerous ways to connect to a Redshift databause and I've included two below. We can use either the SQLAlchemy package or we can use the psycopg2 package for a more direct access.

Both will allow us to execute SQL queries and get results however the SQLAlchemy engine makes it a bit easier to directly return our data as a dataframe using pandas. Plotly has a tight integration with pandas as well, making it extremely easy to make interactive graphs to share with your company.


#### SQLAlchemy

```python
from sqlalchemy import create_engine
engine_string = "postgresql+psycopg2://%s:%s@%s:%d/%s" \
% (redshift_user, redshift_pass, redshift_endpoint, port, dbname)
engine = create_engine(engine_string)
```

#### Psycopg2

```python
import psycopg2
conn = psycopg2.connect(
    host="datawarehouse.cm4z2iunjfsc.us-west-2.redshift.amazonaws.com",
    user=redshift_user,
    port=port,
    password=redshift_pass,
    dbname=dbname)
cur = conn.cursor() # create a cursor for executing queries
```

#### Load Data

This next section goes over loading in the sample data from Amazon's sample database. This is strictly for the purposes of the tutorial so feel free to skim this section if you're going to be working with your own data.

-----------------START DATA LOADING-----------------

```python
cur.execute("""drop table users;

drop table venue;

drop table category;

drop table date;

drop table event;

drop table listing;

drop table sales;""")
conn.commit()
```

```python
aws_key = os.getenv("AWS_ACCESS_KEY_ID") # needed to access S3 Sample Data
aws_secret = os.getenv("AWS_SECRET_ACCESS_KEY")

base_copy_string = """copy %s from 's3://awssampledbuswest2/tickit/%s.txt'
credentials 'aws_access_key_id=%s;aws_secret_access_key=%s'
delimiter '%s';""" # the base COPY string that we'll be using

#easily generate each table that we'll need to COPY data from
tables = ["users", "venue", "category", "date", "event", "listing"]
data_files = ["allusers_pipe", "venue_pipe", "category_pipe", "date2008_pipe", "allevents_pipe", "listings_pipe"]
delimiters = ["|", "|", "|", "|", "|", "|", "|"]

#the generated COPY statements we'll be using to load data;
copy_statements = []
for tab, f, delim in zip(tables, data_files, delimiters):
    copy_statements.append(base_copy_string % (tab, f, aws_key, aws_secret, delim))

# add in Sales data, delimited by '\t'
copy_statements.append("""copy sales from 's3://awssampledbuswest2/tickit/sales_tab.txt'
credentials 'aws_access_key_id=%s;aws_secret_access_key=%s'
delimiter '\t' timeformat 'MM/DD/YYYY HH:MI:SS';""" % (aws_key, aws_secret))
```

```python
# Create Table Statements
cur.execute("""
create table users(
	userid integer not null distkey sortkey,
	username char(8),
	firstname varchar(30),
	lastname varchar(30),
	city varchar(30),
	state char(2),
	email varchar(100),
	phone char(14),
	likesports boolean,
	liketheatre boolean,
	likeconcerts boolean,
	likejazz boolean,
	likeclassical boolean,
	likeopera boolean,
	likerock boolean,
	likevegas boolean,
	likebroadway boolean,
	likemusicals boolean);

create table venue(
	venueid smallint not null distkey sortkey,
	venuename varchar(100),
	venuecity varchar(30),
	venuestate char(2),
	venueseats integer);

create table category(
	catid smallint not null distkey sortkey,
	catgroup varchar(10),
	catname varchar(10),
	catdesc varchar(50));

create table date(
	dateid smallint not null distkey sortkey,
	caldate date not null,
	day character(3) not null,
	week smallint not null,
	month character(5) not null,
	qtr character(5) not null,
	year smallint not null,
	holiday boolean default('N'));

create table event(
	eventid integer not null distkey,
	venueid smallint not null,
	catid smallint not null,
	dateid smallint not null sortkey,
	eventname varchar(200),
	starttime timestamp);

create table listing(
	listid integer not null distkey,
	sellerid integer not null,
	eventid integer not null,
	dateid smallint not null  sortkey,
	numtickets smallint not null,
	priceperticket decimal(8,2),
	totalprice decimal(8,2),
	listtime timestamp);

create table sales(
	salesid integer not null,
	listid integer not null distkey,
	sellerid integer not null,
	buyerid integer not null,
	eventid integer not null,
	dateid smallint not null sortkey,
	qtysold smallint not null,
	pricepaid decimal(8,2),
	commission decimal(8,2),
	saletime timestamp);""")
```

```python
for copy_statement in copy_statements: # execute each COPY statement
    cur.execute(copy_statement)
conn.commit()
```

```python
for table in tables + ["sales"]:
    cur.execute("select count(*) from %s;" % (table,))
    print(cur.fetchone())
conn.commit() # make sure data went through and commit our statements permanently.
```

-----------------END DATA LOADING-----------------


Now that we've loaded some data into our Redshift cluster, we can start running queries against it.

We're going to start off by exploring and presenting some of our user's tastes and habits. Pandas makes it easy to query our data base and get back a dataframe in return. In this query, I'm simply getting the preferences of our users. What kinds of events do they like?

```python
df = pd.read_sql_query("""
SELECT sum(likesports::int) as sports, sum(liketheatre::int) as theatre,
sum(likeconcerts::int) as concerts, sum(likejazz::int) as jazz,
sum(likeclassical::int) as classical, sum(likeopera::int) as opera,
sum(likerock::int) as rock, sum(likevegas::int) as vegas,
sum(likebroadway::int) as broadway, sum(likemusicals::int) as musical,
state
FROM users
GROUP BY state
ORDER BY state asc;
""", engine)
```

Now that I've gotten a DataFrame back, let's make a quick heatmap using plotly.

```python
data = [
        go.Heatmap(
            z = df.drop('state', axis=1).values,
            x = df.drop('state', axis=1).columns,
            y = df.state,
            colorscale = 'Hot'
        )
    ]
layout = go.Layout(title="State and Music Tastes", yaxis=dict(autotick=False, dtick=1))
py.iplot(Figure(data=data, layout=layout), filename='redshift/state and music taste heatmap', height=1000)
```

*the above graph is interactive, click and drag to zoom, double click to return to initial layout, shift click to pan*


This graph is simple to produce and even more simple to explore. The interactivity makes it great for those that aren't completely familiar with heatmaps.

Looking at this particular one we can easily get a sense of popularity. We can see here that sports events don't seem to be particularly popular among our users and that certain states have much higher preferences (and possibly users) than others.

A common next step might be to create some box plots of these user preferences.

```python
layout = go.Layout(title="Declared User Preference Box Plots",
                yaxis=dict())

data = []
for pref in df.drop('state', axis=1).columns:
    # for every preference type, make a box plot
    data.append(go.Box(y=df[pref], name=pref))

py.iplot(go.Figure(data=data, layout=layout), filename='redshift/user preference box plots')
```

*the above graph is interactive, click and drag to zoom, double click to return to initial layout, shift click to pan*


It seems to be that sports are just a bit more compressed than the rest. This may be because there's simply fewer people interested in sports or our company doesn't have many sporting events.


Now that we've explored a little bit about some of our customers we've stumbled upon this sports anomoly. Are we listing less sports events? Do we sell approximately the same amount of all event types and our users just aren't drawn to sports events?

We've got to understand a bit more and to do so we'll be plotting a simple bar graph of our event information.

```python
df = pd.read_sql_query("""
SELECT sum(event.catid) as category_sum, catname as category_name
FROM event, category
where event.catid = category.catid
GROUP BY category.catname
""", engine)
```

```python
layout = go.Layout(title="Event Categories Sum", yaxis=dict(title="Sum"))
data = [go.Bar(x=df.category_name, y=df.category_sum)]
py.iplot(go.Figure(data=data, layout=layout))
```

It's a good thing we started exploring this data because we've got to rush to management and report the discrepancy between our users' preferences and the kinds of events that we're hosting! Luckily, sharing plotly's graphs is extremely easy using the `play with this data` link at the bottom right.

However for our report, let's dive a bit deeper into the events that we're listing and when we're listing them. Maybe we're trending upwards with certain event types?

```python
df = pd.read_sql_query("""
SELECT sum(sales.qtysold) as quantity_sold, date.caldate
FROM sales, date
WHERE sales.dateid = date.dateid
GROUP BY date.caldate
ORDER BY date.caldate asc;
""", engine)
```

```python
layout = go.Layout(title="Event Sales Per Day", yaxis=dict(title="Sales Quantity"))
data = [go.Scatter(x=df.caldate, y=df.quantity_sold)]
py.iplot(go.Figure(data=data, layout=layout))
```

```
Overall it seems inconclusive except that our events seem to be seasonal. This aggregate graph doesn't show too much so it's likely worth exploring a bit more about each category.
```

```python
df = pd.read_sql_query("""
SELECT sum(sales.qtysold) as quantity_sold, date.caldate, category.catname as category_name
FROM sales, date, event, category
WHERE sales.dateid = date.dateid
AND sales.eventid = event.eventid
AND event.catid = category.catid
GROUP BY date.caldate, category_name
ORDER BY date.caldate asc;
""", engine)
```

It's always great to try and better understand which graph type conveys your message the best. Sometimes subplots do the best and other times it's best to put them all on one graph. Plotly makes it easy to do either one!

```python
data = []
for count, (name, g) in enumerate(df.groupby("category_name")):
    data.append(go.Scatter(
            name=name,
            x=g.caldate,
            y=g.quantity_sold,
            xaxis='x' + str(count + 1),
            yaxis='y' + str(count + 1)
        ))

fig = tls.make_subplots(rows=2,cols=2)
fig['layout'].update(title="Event Sales Per Day By Category")
fig['data'] += data
py.iplot(fig)
```

The above subplots seem to tell an interesting story although it's important to note that with subplots the axes are not always aligned. So let's try plotting all of them together, with lines for each category.

```python
data = []
for name, g in df.groupby("category_name"):
    data.append(go.Scatter(
            name=name,
            x=g.caldate,
            y=g.quantity_sold
        ))

fig = go.Figure()
fig['layout'].update(title="Event Sales Per Day By Category")
fig['data'] += data
py.iplot(fig, filename='redshift/Event Sales Per Day by Category')
```

This looks much better and explains the story perfectly. It seems that all of our events are fairly regular through the year except for a spike in musicals and plays around March. This might be of interest to so I'm going to mark up this graph and share it with some of the relevant sales representatives in my company.

The rest of my team can edit the graph with me in a web app. Collaborating does not require coding, emailing, or downloading software. I can even fit a function to the data in the web app.

```python
from IPython.display import Image
```

```python
Image(url="http://i.imgur.com/nUVihzx.png")
```

```python
tls.embed("https://plot.ly/~bill_chambers/195")
```

Plotly makes it easier for data analysts and data scientists to share data in meaningful ways. By marking up drawings and embedding comments on the graph, I can make sure that I'm sharing everything within a context. Rather than having to send a static image, I can share an interactive plot a coworker can explore and understand as well. Plotly makes it easy for companies to make sure that information is conveyed in the right context.

#### References
Learn more about:
- [Amazon Redshift Data Warehouse](http://aws.amazon.com/redshift/)
- [Chart Studio Enterprise - Plotly Hosted on your servers](https://plot.ly/product/enterprise/)
- [Subplots in Plotly](https://plot.ly/python/subplots/)
- [Creating a plot of best fit](https://plot.ly/online-graphing/tutorials/create-a-line-of-best-fit-online/)

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'redshift.ipynb', 'python/amazon-redshift/', 'Plot Data From Amazon Redshift',
    'A tutorial showing how to plot Amazon AWS Redshift data with Plotly.',
    title = 'Plot Data from Amazon Redshift | plotly',
    has_thumbnail='false', redirect_from='ipython-notebooks/amazon-redshift/',
    language='python', page_type='example_index',
    display_as='databases', order=3,
    ipynb= '~notebook_demo/1')
```

```python

```
