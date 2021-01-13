---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.6.0
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
    version: 3.7.6
  plotly:
    description: How to make Heatmaps in Python with Plotly.
    display_as: scientific
    language: python
    layout: base
    name: Heatmaps
    order: 2
    page_type: example_index
    permalink: python/heatmaps/
    redirect_from: python/heatmap/
    thumbnail: thumbnail/heatmap.jpg
---

### Heatmap with `plotly.express` and `px.imshow`

[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/). With `px.imshow`, each value of the input array or data frame is represented as a heatmap pixel.

For more examples using `px.imshow`, see the [tutorial on displaying image data with plotly](/python/imshow).

```python
import plotly.express as px

fig = px.imshow([[1, 20, 30],
                 [20, 1, 60],
                 [30, 60, 1]])
fig.show()
```

```python
import plotly.express as px

df = px.data.medals_wide(indexed=True)
fig = px.imshow(df)
fig.show()
```

#### Heatmaps in Dash

[Dash](https://plotly.com/dash/) is the best way to build analytical apps in Python using Plotly figures. To run the app below, run `pip install dash`, click "Download" to get the code and run `python app.py`.

Get started  with [the official Dash docs](https://dash.plotly.com/installation) and **learn how to effortlessly [style](https://plotly.com/dash/design-kit/) & [deploy](https://plotly.com/dash/app-manager/) apps like this with <a class="plotly-red" href="https://plotly.com/dash/">Dash Enterprise</a>.**


```python hide_code=true
from IPython.display import IFrame
snippet_url = 'https://dash-gallery.plotly.host/python-docs-dash-snippets/'
IFrame(snippet_url + 'heatmaps', width='100%', height=630)
```

### Customizing the axes and labels on a heatmap

You can use the `x`, `y` and `labels` arguments to customize the display of a heatmap, and use `.update_xaxes()` to move the x axis tick labels to the top:

```python
import plotly.express as px
data=[[1, 25, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, 5, 20]]
fig = px.imshow(data,
                labels=dict(x="Day of Week", y="Time of Day", color="Productivity"),
                x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                y=['Morning', 'Afternoon', 'Evening']
               )
fig.update_xaxes(side="top")
fig.show()
```

### Basic Heatmap with `plotly.graph_objects`

If Plotly Express does not provide a good starting point, it is also possible to use [the more generic `go.Heatmap` class from `plotly.graph_objects`](/python/graph-objects/).

```python
import plotly.graph_objects as go

fig = go.Figure(data=go.Heatmap(
                    z=[[1, 20, 30],
                      [20, 1, 60],
                      [30, 60, 1]]))
fig.show()
```

### Heatmap with Categorical Axis Labels

In this example we also show how to ignore [hovertext](https://plotly.com/python/hover-text-and-formatting/) when we have missing values in the data by setting the [hoverongaps](https://plotly.com/python/reference/heatmap/#heatmap-hoverongaps) to False.

```python
import plotly.graph_objects as go

fig = go.Figure(data=go.Heatmap(
                   z=[[1, None, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
                   x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                   y=['Morning', 'Afternoon', 'Evening'],
                   hoverongaps = False))
fig.show()
```

### Heatmap with Unequal Block Sizes


```python
import plotly.graph_objects as go
import numpy as np

# Build the rectangles as a heatmap
# specify the edges of the heatmap squares
phi = (1 + np.sqrt(5) )/2. # golden ratio
xe = [0, 1, 1+(1/(phi**4)), 1+(1/(phi**3)), phi]
ye = [0, 1/(phi**3), 1/phi**3+1/phi**4, 1/(phi**2), 1]

z = [ [13,3,3,5],
      [13,2,1,5],
      [13,10,11,12],
      [13,8,8,8]
    ]

fig = go.Figure(data=go.Heatmap(
          x = np.sort(xe),
          y = np.sort(ye),
          z = z,
          type = 'heatmap',
          colorscale = 'Viridis'))

# Add spiral line plot

def spiral(th):
    a = 1.120529
    b = 0.306349
    r = a*np.exp(-b*th)
    return (r*np.cos(th), r*np.sin(th))

theta = np.linspace(-np.pi/13,4*np.pi,1000); # angle
(x,y) = spiral(theta)

fig.add_trace(go.Scatter(x= -x+x[0], y= y-y[0],
     line =dict(color='white',width=3)))

axis_template = dict(range = [0,1.6], autorange = False,
             showgrid = False, zeroline = False,
             linecolor = 'black', showticklabels = False,
             ticks = '' )

fig.update_layout(margin = dict(t=200,r=200,b=200,l=200),
    xaxis = axis_template,
    yaxis = axis_template,
    showlegend = False,
    width = 700, height = 700,
    autosize = False )

fig.show()
```

### Heatmap with Datetime Axis

```python
import plotly.graph_objects as go
import datetime
import numpy as np
np.random.seed(1)

programmers = ['Alex','Nicole','Sara','Etienne','Chelsea','Jody','Marianne']

base = datetime.datetime.today()
dates = base - np.arange(180) * datetime.timedelta(days=1)
z = np.random.poisson(size=(len(programmers), len(dates)))

fig = go.Figure(data=go.Heatmap(
        z=z,
        x=dates,
        y=programmers,
        colorscale='Viridis'))

fig.update_layout(
    title='GitHub commits per day',
    xaxis_nticks=36)

fig.show()
```

### Heatmap and datashader

Arrays of rasterized values build by datashader can be visualized using
plotly's heatmaps, as shown in the [plotly and datashader tutorial](/python/datashader/).

#### Reference
See [function reference for `px.(imshow)`](https://plotly.com/python-api-reference/generated/plotly.express.imshow) or https://plotly.com/python/reference/heatmap/ for more information and chart attribute options!
