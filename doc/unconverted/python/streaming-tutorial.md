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
    description: Plotly Streaming
    has_thumbnail: false
    language: python
    layout: base
    name: Plotly Streaming
    page_type: u-guide
    permalink: python/streaming-tutorial/
    redirect_from: python/streaming-line-tutorial/
    thumbnail: /images/static-image
---

### Streaming Support
**Streaming is no longer supported in Chart Studio Cloud.<br>Streaming is still available as part of [Chart Studio Enterprise](https://plot.ly/products/on-premise/). Additionally, [Dash](https://plot.ly/products/dash/) supports streaming, as demonstrated by the [Dash Wind Streaming example](https://github.com/plotly/dash-wind-streaming).**


### Getting Started with Streaming

```python
import numpy as np
import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go
```

Before you start streaming, you're going to need some [stream tokens](https://plot.ly/settings/api). You will need **one unique stream token for every `trace object` ** you wish to stream to. Thus if you have two traces that you want to plot and stream, you're going to require two unique stream tokens. Notice that more tokens can be added via the settings section of your Plotly profile: https://plot.ly/settings/api


![](https://cloud.githubusercontent.com/assets/12302455/15023505/bb729d8c-11fe-11e6-87a6-332ff9dfad2d.png)


Now in the same way that you set your credentials, as shown in [Getting Started](https://plot.ly/python/getting-started/), you can add stream tokens to your credentials file.

```python
stream_ids = tls.get_credentials_file()['stream_ids']
print stream_ids
```

You'll see that `stream_ids` will contain a list of the stream tokens we added to the credentials file.


#### An Example to Get You Started


Now that you have some stream tokens to play with, we're going to go over how we're going to put these into action.
There are two main objects that will be created and used for streaming:
- Stream Id Object
- Stream link Object

We're going to look at these objects sequentially as we work through our first streaming example. For our first example, we're going to be streaming random data to a single scatter trace, and get something that behaves like the following:

![](https://cloud.githubusercontent.com/assets/12302455/14826664/e7d59c56-0bac-11e6-953e-e215410f3f03.png)


##### Stream Id Object


The `Stream Id Object` comes bundled in the `graph_objs` package. We can then call help to see the description of this object:

```python
help(go.Stream)
```

As we can see, the `Stream Id Object` is a dictionary-like object that takes two parameters, and has all the methods that are assoicated with dictionaries.
We will need one of these objects for each of trace that we wish to stream data to.
We'll now create a single stream token for our streaming example, which will include one scatter trace.

```python
# Get stream id from stream id list
stream_id = stream_ids[0]

# Make instance of stream id object
stream_1 = go.Stream(
    token=stream_id,  # link stream id to 'token' key
    maxpoints=80      # keep a max of 80 pts on screen
)
```

The `'maxpoints'` key sets the maxiumum number of points to keep on the plotting surface at any given time.
More over, if you want to avoid the use of these `Stream Id Objects`, you can just create a dictionary with at least the token parameter defined, for example:

```python
stream_1 = dict(token=stream_id, maxpoints=60)
```

Now that we have our `Stream Id Object` ready to go, we can set up our plot. We do this in the same way that we would any other plot, the only thing is that we now have to set the stream parameter in our trace object.

```python
# Initialize trace of streaming plot by embedding the unique stream_id
trace1 = go.Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=stream_1         # (!) embed stream id, 1 per trace
)

data = go.Data([trace1])

# Add title to layout object
layout = go.Layout(title='Time Series')

# Make a figure object
fig = go.Figure(data=data, layout=layout)
```

#### Stream Link Object


The Stream Link Object is what will be used to communicate with the Plotly server in order to update the data contained in your trace objects. This object is in the `plotly.plotly` object, an can be reference with `py.Stream`

```python
help(py.Stream)  # run help() of the Stream link object
```

You're going to need to set up one of these stream link objects for each trace you wish to stream data to.
<br>Below we'll set one up for the scatter trace we have in our plot.

```python
# We will provide the stream link object the same token that's associated with the trace we wish to stream to
s = py.Stream(stream_id)

# We then open a connection
s.open()
```

We can now use the Stream Link object `s` in order to `stream` data to our plot.
<br>As an example, we will send a time stream and some random numbers:

```python
# (*) Import module keep track and format current time
import datetime
import time

i = 0    # a counter
k = 5    # some shape parameter

# Delay start of stream by 5 sec (time to switch tabs)
time.sleep(5)

while True:

    # Current time on x-axis, random numbers on y-axis
    x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    y = (np.cos(k*i/50.)*np.cos(i/50.)+np.random.randn(1))[0]

    # Send data to your plot
    s.write(dict(x=x, y=y))

    #     Write numbers to stream to append current data on plot,
    #     write lists to overwrite existing data on plot

    time.sleep(1)  # plot a point every second
# Close the stream when done plotting
s.close()
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade

import publisher
publisher.publish(
    'python_streaming', 'python/streaming-tutorial/', 'Plotly Streaming',
    'Plotly Streaming', name='Plotly Streaming',
    title = 'Plotly Streaming',
    redirect_from = 'python/streaming-line-tutorial/',
    language='python',
    layout='user-guide',
    ipynb= '~notebook_demo/80')
```

```python

```
