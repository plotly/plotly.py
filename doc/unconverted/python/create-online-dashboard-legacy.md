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
    description: How to create and publish a dashboard with the Python API.
    display_as: legacy_charts
    language: python
    layout: base
    name: Dashboard API
    order: 0
    page_type: u-guide
    permalink: python/create-online-dashboard-legacy/
    thumbnail: thumbnail/dashboard.jpg
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!
#### Version Check
Note: The dashboard API is available in version <b>2.0.5.+</b><br>
Run  `pip install plotly --upgrade` to update your Plotly version.

```python
import plotly
plotly.__version__
```

#### Plotly Dashboards
A dashboard is a collection of plots and images organized with a certain layout. There are two ways to create a Plotly dashboard: using the [online creator](https://plot.ly/dashboard/create/) or programmatically with Plotly's python API.

In Plotly, dashboards can contain plots, text and webpage images. To use the online creator, see https://plot.ly/dashboard/create/. Dashboards are stored in your Plotly account: https://plot.ly/organize
#### Dashboard Privacy
In the same way that a `plot` can be `public`, `private` or `secret`, dashboards can also be `public`, `private` or `secret` independent of the plots inside them. So if you're sharing a `dashboard` with someone and one or more of your plots are set to `private`, they will not show for the other user. For more information about this refer to the [Dashboard Privacy Doc](http://help.plot.ly/dashboard-privacy/).
#### Initialize a Dashboard
Now you can programmatically create and modify dashboards in Python. These dashboards can be uploaded to the Plotly server to join your other dashboards. You can also retrieve dashboards from Plotly.

Let's start by creating a new dashboard. To get a preview of the HTML representation of the dashboard organization - i.e. where the items in the dashboard are located with respect to one another - run the `.get_preview()` method in a notebook cell. Everytime you modify your dashboard you should run this to check what it looks like.

`IMPORTANT NOTE`: because of the way `.get_preview()` works _only_ one cell of the Jupyter notebook can display the preview of the dashboard after running this method. A good setup is to designate one cell to look like `my_dboard.get_preview()` and then run that every time you make a change to update the HTML representation of the dashboard. For the purposes of clarity, each modification of the dashboard in this tutorial is clearly shown.

```python
import plotly.dashboard_objs as dashboard

import IPython.display
from IPython.display import Image

my_dboard = dashboard.Dashboard()
my_dboard.get_preview()
```

#### Choose Plots
In order to use the dashboard, we need to put some plots into it. You can either make these on-the-fly in Jupyter or use a plot you've already created by using its url.

```python
import plotly.graph_objs as go
import plotly.plotly as py

import numpy as np

colorscale = [[0, '#FAEE1C'], [0.33, '#F3558E'], [0.66, '#9C1DE7'], [1, '#581B98']]
trace1 = go.Scatter(
    y = np.random.randn(500),
    mode='markers',
    marker=dict(
        size=16,
        color = np.random.randn(500),
        colorscale=colorscale,
        showscale=True
    )
)
data = [trace1]
url_1 = py.plot(data, filename='scatter-for-dashboard', auto_open=False)
py.iplot(data, filename='scatter-for-dashboard')
```

Create a plot with a secret key:

```python
import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

x0 = np.random.randn(50)
x1 = np.random.randn(50) + 2
x2 = np.random.randn(50) + 4
x3 = np.random.randn(50) + 6

colors = ['#FAEE1C', '#F3558E', '#9C1DE7', '#581B98']

trace0 = go.Box(x=x0, marker={'color': colors[0]})
trace1 = go.Box(x=x1, marker={'color': colors[1]})
trace2 = go.Box(x=x2, marker={'color': colors[2]})
trace3 = go.Box(x=x3, marker={'color': colors[3]})
data = [trace0, trace1, trace2, trace3]

url_2 = py.plot(data, filename='box-plots-for-dashboard', sharing='secret', auto_open=False)
py.iplot(data, filename='box-plots-for-dashboard')
```

```python
url_2
```

<!-- #region -->
#### Add a Box
If you want to place a plot, text box or a webpage into the dashboard, you need to place it in a `box` (which is just a dictionary) and `insert` it into your dashboard. We will be inserting a plot, a text box, and a secret plot.

A box with a plot in it takes the form:
```
{
    'type': 'box',
    'boxType': 'plot',
    'fileId': '',
    'shareKey': None,
    'title': ''
}
```
- `fileId` is of the form `username:number` (eg. 'PlotBot:1300') which can be found in the url of your plot once it's up on the Plotly server.
- `shareKey`: optional - the sharekey if your plot is secret.
- `title`: optional - sets the title of your box.

A box with text in it takes the form:
```
{
    'type': 'box',
    'boxType': 'text',
    'text': '',
    'title': ''
}
```
- `text`: the text you want displayed in your box.
- `title`: optional - sets the title of your box.

A box with a webpage in it takes the form:
```
{
    'type': 'box',
    'boxType': 'webpage',
    'url': '',
    'title': ''
}
```
- `url`: the url of your webpage (eg. 'https://en.wikipedia.org/wiki/Main_Page').
- `title`: optional - sets the title of your box.

Note: As above, you can run `py.plot()` to return the url of your plot and then assign it to a variable to use in a dashboard later.
<!-- #endregion -->

To extract the fileId from a url, use the `fileId_from_url` below. If your url is `secret`, use `sharekey_from_url` to return the sharekey from the url, then place in your box that contains a secret plot.

```python
import re

def fileId_from_url(url):
    """Return fileId from a url."""
    raw_fileId = re.findall("~[A-z]+/[0-9]+", url)[0][1: ]
    return raw_fileId.replace('/', ':')

def sharekey_from_url(url):
    """Return the sharekey from a url."""
    if 'share_key=' not in url:
        return "This url is not 'sercret'. It does not have a secret key."
    return url[url.find('share_key=') + len('share_key='):]

fileId_1 = fileId_from_url(url_1)
fileId_2 = fileId_from_url(url_2)

box_a = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': fileId_1,
    'title': 'scatter-for-dashboard'
}

text_for_box = """
## Distributions:


#### Scatter Plot
1. Ranging 0 - 500
2. Even distribution

#### Box Plot
1. Similar Range
2. Outliers present in trace 1 and trace 3

You can view more markdown tips [here](https://daringfireball.net/projects/markdown/syntax).
"""

box_b = {
    'type': 'box',
    'boxType': 'text',
    'text': text_for_box,
    'title': 'Markdown Options for Text Box'
}

box_c = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': fileId_2,
    'title': 'box-for-dashboard',
    'shareKey': sharekey_from_url(url_2)
}

my_dboard.insert(box_c)
```

![IPython terminal](https://images.plot.ly/plotly-documentation/images/dashboard_1.png)

```python
my_dboard.get_preview()
```

```python
my_dboard.insert(box_a, 'above', 1)
```

![IPython terminal](https://images.plot.ly/plotly-documentation/images/dashboard_2.png)


#### Add Box with Custom Sizing
By default when a box is inserted into the dashboard layout it splits the box it is referencing equally into two parts. You can now manually control the percentage that the new box takes. Use `fill_percent` to specify the percentage of the container box from the given side that the new box occupies. Run `help(dashboard.Dashboard.insert)` for more help.

```python
my_dboard.insert(box_b, 'left', 1, fill_percent=30)
```

![IPython terminal](https://images.plot.ly/plotly-documentation/images/dashboard_3.png)


#### Get Box
Each time `my_dboard.get_preview()` is run a layout of the dashboard is returned where each rectangular area is denoted by a number in the center. These numbers or `box ids` are essentially lookup keys that are assigned on-the-fly each time `.get_preview()` is run and are liable to change.

Remember that a box is just a dictionary that specifies the plot, webpage or text that it contains. For example, let's say you want to see what plot will show up in the region `1` of the dashboard. Run `my_dboard.get_box(1)` and the dict of the box will be returned:

```python
my_dboard.get_box(1)
```

You can now reassign the values in the dictionary to update that box. For example, you can change the title of that plot:

```python
my_dboard.get_box(1)['title'] = 'a new title'
my_dboard.get_box(1)
```

#### Swap Boxes
If you want to swap the locations of two boxes you've already placed in the dashboard, run `my_dboard.get_preview()` to look at the layout of the dashboard, then simply pick two _unique_ box ids and you will swap the contents stored at those locations.

```python
my_dboard.get_box(3)['title']
```

```python
my_dboard.swap(2, 3)
my_dboard.get_box(3)['title']
```

#### Remove Box
You can remove a box from the dashboard by identifying its box id from the `my_dboard.get_preview()`.

```python
my_dboard.insert(box_a, 'below', 2)
```

![IPython terminal](https://images.plot.ly/plotly-documentation/images/dashboard_4.png)

```python
my_dboard.remove(3)
```

![IPython terminal](https://images.plot.ly/plotly-documentation/images/dashboard_3.png)


#### Add Title
Set the title of your dashboard.

```python
my_dboard['settings']['title'] = 'My First Dashboard with Python'
```

#### Add a Logo
Add a logo to the top-left corner of the dashboard.

```python
my_dboard['settings']['logoUrl'] = 'https://images.plot.ly/language-icons/api-home/python-logo.png'
```

#### Add Links
Add some links to the header of the dashboard.

```python
my_dboard['settings']['links'] = []
my_dboard['settings']['links'].append({'title': 'Link to Plotly', 'url': 'https://plot.ly/'})
my_dboard['settings']['links'].append({'title': 'Link to Python Website', 'url': 'https://www.python.org/'})
```

#### Change Color Settings

```python
my_dboard['settings']['foregroundColor'] = '#000000'
my_dboard['settings']['backgroundColor'] = '#adcaea'
my_dboard['settings']['headerForegroundColor'] = '#ffffff'
my_dboard['settings']['headerBackgroundColor'] = '#D232C8'
my_dboard['settings']['boxBackgroundColor'] = '#ffffff'
my_dboard['settings']['boxBorderColor'] = '#000000'
my_dboard['settings']['boxHeaderBackgroundColor'] = '#ffffff'
```

#### Change Font Settings

Note that all other settings available in the [dashboard online creator](https://plot.ly/dashboard/create/#/) are also available to with the dashboard API.

```python
my_dboard['settings']['fontFamily'] = 'Raleway'
my_dboard['settings']['headerFontSize'] = '1.6em'
my_dboard['settings']['headerFontWeight'] = '200'
```

#### Update Dashboard Size

```python
stacked_dboard = dashboard.Dashboard()
text_box = {
    'type': 'box',
    'boxType': 'text',
    'text': 'empty space'
}
for _ in range(5):
    stacked_dboard.insert(text_box, 'below', 1)
# stacked_dboard.get_preview()
```

If a dashboard looks like the one above with small boxes, it may be difficult to resize in the [online creator](https://plot.ly/dashboard/create/). To avoid this issue, resize the dashboard:

```python
stacked_dboard['layout']['size'] = 3000
```

#### Upload Dashboard
To upload your dashboard to your [Plotly cloud account](https://plot.ly/organize/home/) use `py.dashboard_ops.upload()`.

```python
import plotly.plotly as py
py.dashboard_ops.upload(my_dboard, 'My First Dashboard with Python')
```

[![](https://images.plot.ly/plotly-documentation/images/my_dboard_from_API_with_logo_and_links.png)](https://plot.ly/~PythonPlotBot/540/my-first-dashboard-with-python/)


#### Retrieve Dashboard
You can also retrieve any of your dashboards from Plotly. To see what dashboards you have in the Plotly cloud, run `py.dashboard_ops.get_dashboard_names()` to get a list of the dashboards you have in your files. To grab a specific dashboard, simply input its name into `py.dashboard_ops.get_dashboard()` to create a `Dashboard()`.

```python
py.dashboard_ops.get_dashboard_names()
```

```python
recent_dboard = py.dashboard_ops.get_dashboard('My First Dashboard with Python')
```

#### Examples
- [Twitter Marketing Campaign](https://plot.ly/dashboard/jackp:16823/present)
- [Shell: Integrated Gas](https://plot.ly/dashboard/jackp:16820/present)
- [US Wind Turbine Example](https://plot.ly/dashboard/jackluo:430/present)
- [Motorcars Example](https://plot.ly/dashboard/jackp%3A16818/present).

You can learn more about making dashboards by going to https://plot.ly/python/dashboard/


#### Reference

```python
help(py.dashboard_ops)
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

!pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'dashboard-api.ipynb', 'python/create-online-dashboard/', 'Dashboard API | plotly',
    'How to create and publish a dashboard with the Python API.',
    title = 'Dashboard API | plotly',
    name = 'Dashboard API',
    thumbnail='thumbnail/dashboard.jpg', language='python',
    page_type='u-guide', has_thumbnail='true', display_as='legacy_charts',
    ipynb= '~notebook_demo/148', order=0)
```

```python

```
