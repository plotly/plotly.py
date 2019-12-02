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
    description: Create interactive graphs with salesforce, IPython Notebooks and
      Plotly
    display_as: databases
    has_thumbnail: false
    language: python
    layout: base
    name: Plot Data from Salesforce
    order: 4
    page_type: example_index
    permalink: python/salesforce/
    redirect_from: ipython-notebooks/salesforce/
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
Salesforce reports are great for getting a handle on the numbers but [Plotly](https://plot.ly/) allows for interactivity not built into the Reports Module in Salesforce. Luckily Salesforce has amazing tools around exporting data, from excel and csv files to a robust and reliable API. With [Simple Salesforce](https://github.com/neworganizing/simple-salesforce), it's simple to make REST calls to the Salesforce API and get your hands on data to make real time, interactive charts.

This notebook walks you through that basic process of getting something like that set up.
First you'll need [Plotly](https://plot.ly/). Plotly is a free web-based platform for making graphs. You can keep graphs private, make them public, and run Plotly on your own servers (https://plot.ly/product/enterprise/). To get started visit https://plot.ly/python/getting-started/ . It's simple interface makes it easy to get interactive graphics done quickly.

You'll also need a Salesforce Developer (or regular Salesforce Account). [You can get a salesforce developer account for free](https://developer.salesforce.com/signup) at their developer portal.

```python
import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
import numpy as np
from collections import Counter
import requests

from simple_salesforce import Salesforce
requests.packages.urllib3.disable_warnings() # this squashes insecure SSL warnings - DO NOT DO THIS ON PRODUCTION!
```

#### Log In to Salesforce
I've stored my Salesforce login in a text file however you're free to store them as environmental variables. As a reminder, login details should NEVER be included in version control. Logging into Salesforce is as easy as entering in your username, password, and security token given to you by Salesforce. [Here's how to get your security token from Salesforce.](https://help.salesforce.com/apex/HTViewHelpDoc?id=user_security_token.htm)

```python
with open('salesforce_login.txt') as f:
    username, password, token = [x.strip("\n") for x in f.readlines()]
sf = Salesforce(username=username, password=password, security_token=token)
```

#### SOQL Queries
At this time we're going to write a simple SOQL query to get some basic information from some leads. We'll query the status and Owner from our leads. Further reference for the Salesforce API and writing SOQL queries: http://www.salesforce.com/us/developer/docs/soql_sosl/ SOQL is just Salesforce's version of SQL.

```python
leads_for_status = sf.query("SELECT Id, Status, Owner.Name FROM Lead")
```

Now we'll use a quick list comprehension to get just our statuses from those records (which are in an ordered dictionary format).

```python
statuses = [x['Status'] for x in leads_for_status["records"]]
status_counts = Counter(statuses)
```

Now we can take advantage of Plotly's simple IPython Notebook interface to plot the graph in our notebook.

```python
data = [go.Bar(x=status_counts.keys(), y=status_counts.values())]
py.iplot(data, filename='salesforce/lead-distributions')
```

While this graph gives us a great overview what status our leads are in, we'll likely want to know how each of the sales representatives are doing with their own leads. For that we'll need to get the owners using a similar list comprehension as we did above for the status.

```python
owners = [x['Owner']['Name'] for x in leads_for_status["records"]]
```

For simplicity in grouping the values, I'm going to plug them into a pandas DataFrame.

```python
df = pd.DataFrame({'Owners':owners, 'Status':statuses})
```

Now that we've got that we can do a simple lead comparison to compare how our Sales Reps are doing with their leads. We just create the bars for each lead owner.

```python
lead_comparison = []
for name, vals in df.groupby('Owners'):
    counts = vals.Status.value_counts()
    lead_comparison.append(Bar(x=counts.index, y=counts.values, name=name))
```

```python
py.iplot(lead_comparison, filename='salesforce/lead-owner-status-groupings')
```

What's great is that plotly makes it simple to compare across groups. However now that we've seen leads, it's worth it to look into Opportunities.

```python
opportunity_amounts = sf.query("SELECT Id, Probability, StageName, Amount, Owner.Name FROM Opportunity WHERE AMOUNT < 10000")
```

```python
amounts = [x['Amount'] for x in opportunity_amounts['records']]
owners = [x['Owner']['Name'] for x in opportunity_amounts['records']]
```

```python
hist1 = go.Histogram(x=amounts)
```

```python
py.iplot([hist1], filename='salesforce/opportunity-probability-histogram')
```

```python
df2 = pd.DataFrame({'Amounts':amounts,'Owners':owners})
```

```python
opportunity_comparisons = []
for name, vals in df2.groupby('Owners'):
    temp = Histogram(x=vals['Amounts'], opacity=0.75, name=name)
    opportunity_comparisons.append(temp)
```

```python
layout = go.Layout(
    barmode='stack'
)
fig = go.Figure(data=opportunity_comparisons, layout=layout)
```

```python
py.iplot(fig, filename='salesforce/opportunities-histogram')
```

By clicking on the "play with this data!" you can export, share, collaborate, and embed these plots. I've used it to share annotations about data and try out more colors. The GUI makes it easy for less technically oriented people to play with the data as well. Check out how the above was changed below or you can follow the link to make your own edits.

```python
from IPython.display import HTML
HTML("""<div>
    <a href="https://plot.ly/~bill_chambers/21/" target="_blank" title="Chuck vs Bill Sales Amounts" style="display: block; text-align: center;"><img src="https://plot.ly/~bill_chambers/21.png" alt="Chuck vs Bill Sales Amounts" style="max-width: 100%;width: 1368px;"  width="1368" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="bill_chambers:21" src="https://plot.ly/embed.js" async></script>
</div>""")
```

After comparing those two representatives. It's always helpful to have that high level view of the sales pipeline. Below I'm querying all of our open opportunities with their Probabilities and close dates. This will help us make a forecasting graph of what's to come soon.

```python
large_opps = sf.query("SELECT Id, Name, Probability, ExpectedRevenue, StageName, Amount, CloseDate, Owner.Name FROM Opportunity WHERE StageName NOT IN ('Closed Lost', 'Closed Won') AND Amount > 5000")
```

```python
large_opps_df = pd.DataFrame(large_opps['records'])
large_opps_df['Owner'] = large_opps_df.Owner.apply(lambda x: x['Name']) # just extract owner name
large_opps_df.drop('attributes', inplace=True, axis=1) # get rid of extra return data from Salesforce
large_opps_df.head()
```

```python
scatters = []
for name, temp_df in large_opps_df.groupby('Owner'):
    hover_text = temp_df.Name + "<br>Close Probability: " + temp_df.Probability.map(str) + "<br>Stage:" + temp_df.StageName
    scatters.append(
        go.Scatter(
            x=temp_df.CloseDate,
            y=temp_df.Amount,
            mode='markers',
            name=name,
            text=hover_text,
            marker=dict(
                size=(temp_df.Probability / 2) # helps keep the bubbles of managable size
            )
        )
    )
```

```python
data = scatters
layout = go.Layout(
    title='Open Large Deals',
    xaxis=dict(
        title='Close Date'
    ),
    yaxis=dict(
        title='Deal Amount',
        showgrid=False
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='salesforce/open-large-deals-scatter')
```

Plotly makes it easy to create many different kinds of charts. The above graph shows the deals in the pipeline over the coming months. The larger the bubble, the more likely it is to close. Hover over the bubbles to see that data. This graph is ideal for a sales manager to see how each of his sales reps are doing over the coming months.

One of the benefits of Plotly is the availability of features.

#### References

- [Live update Plotly graphs in Python with cron jobs](http://moderndata.plot.ly/update-plotly-charts-with-cron-jobs-and-python/)
- [Graph mysql data with Plotly and Python](http://moderndata.plot.ly/graph-data-from-mysql-database-in-python/)
- [More on creating web-based visualizations in Python with Plotly](https://plot.ly/python/)

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'salesforce.ipynb', 'python/salesforce/', 'Plot Data from Salesforce',
    'Create interactive graphs with salesforce, IPython Notebooks and Plotly',
    title='Interactive Salesforce Graphing | Plotly',
    redirect_from='ipython-notebooks/salesforce/', has_thumbnail='false', language='python', page_type='example_index',
    display_as='databases', order=4, ipynb= '~notebook_demo/1')
```

```python

```
