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
    description: How to make interactive linear-guage charts in Python with Plotly.
    display_as: basic
    language: python
    layout: base
    name: Linear-Gauge Chart
    order: 12
    page_type: u-guide
    permalink: python/linear-gauge-chart/
    thumbnail: thumbnail/linear-gauge.jpg
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Linear Gauge Chart Shell
Note the following tutorial shows how to create a linear-gauge chart with 4 gauges. It's recommended to use a `width` between 600-1000px and `ticklen` should be `width/20`. These variables are definied in the code below.

```python
from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go

# Define Titles and Labels for Each Scale
scales = ['<b>Tension</b>', '<b>Energy</b>',
          '<b>Valence</b>', '<b>Prefer</b>']
scale1 = ['Very <br> Calm ', 'Moderately <br> Calm ',
          'Slightly <br> Calm ', 'Neutral ',
          'Slightly <br> Tense ', 'Moderately <br> Tense ',
          'Very <br> Tense ']
scale2 = ['Very <br> Tired ', 'Moderately <br> Tired ',
          'Slightly <br> Tired ', 'Neutral ',
          'Slightly <br> Awake ', 'Moderately <br> Awake ',
          'Very <br> Awake ']
scale3 = ['Very <br> Displeased ', 'Moderately <br> Displeased ',
          'Slightly <br> Displeased ', 'Neutral ',
          'Slightly <br> Pleased ', 'Moderately <br> Pleased ',
          'Very <br> Pleased ']
scale4 = ['Strongly <br> Dislike ', 'Moderately <br> Dislike ',
          'Slightly <br> Dislike ', 'Neutral ',
          'Slightly <br> Like ', 'Moderately <br> Like ',
          'Strongly <br> Like ']
scale_labels = [scale1, scale2, scale3, scale4]

# Add Scale Titles to the Plot
traces = []
for i in range(len(scales)):
    traces.append(go.Scatter(
        x=[0.6], # Pad the title - a longer scale title would need a higher value
        y=[6.25],
        text=scales[i],
        mode='text',
        hoverinfo='none',
        showlegend=False,
        xaxis='x'+str(i+1),
        yaxis='y'+str(i+1)
    ))

# Create Scales
## Since we have 7 lables, the scale will range from 0-6
shapes = []
for i in range(len(scales)):
    shapes.append({'type': 'rect',
                   'x0': .02, 'x1': 1.02,
                   'y0': 0, 'y1': 6,
                   'xref':'x'+str(i+1), 'yref':'y'+str(i+1)})

x_domains = [[0, .25], [.25, .5], [.5, .75], [.75, 1]] # Split for 4 scales
chart_width = 800

# Define X-Axes
xaxes = []
for i in range(len(scales)):
    xaxes.append({'domain': x_domains[i], 'range':[0, 4],
                  'showgrid': False, 'showline': False,
                  'zeroline': False, 'showticklabels': False})

# Define Y-Axes (and set scale labels)
## ticklen is used to create the segments of the scale,
## for more information see: https://plot.ly/python/reference/#layout-yaxis-ticklen
yaxes = []
for i in range(len(scales)):
    yaxes.append({'anchor':'x'+str(i+1), 'range':[-.5,6.5],
                  'showgrid': False, 'showline': False, 'zeroline': False,
                  'ticks':'inside', 'ticklen': chart_width/20,
                  'ticktext':scale_labels[i], 'tickvals':[0., 1., 2., 3., 4., 5., 6.]
                 })

# Put all elements of the layout together
layout = {'shapes': shapes,
          'xaxis1': xaxes[0],
          'xaxis2': xaxes[1],
          'xaxis3': xaxes[2],
          'xaxis4': xaxes[3],
          'yaxis1': yaxes[0],
          'yaxis2': yaxes[1],
          'yaxis3': yaxes[2],
          'yaxis4': yaxes[3],
          'autosize': False,
          'width': chart_width,
          'height': 600
}

### ADD RATING DATA HERE ###

fig = dict(data=traces, layout=layout)
py.iplot(fig, filename='linear-gauge-layout')
```

#### Add Rating Data
Ratings should be scaled between 0 - 6 to fit the y-values of the scales created above.

```python
ratings = [4.5, 5, 1, 2.75]

for i in range(len(ratings)):
    traces.append(go.Scatter(
            x=[0.5], y=[ratings[i]],
            xaxis='x'+str(i+1), yaxis='y'+str(i+1),
            mode='markers', marker={'size': 16, 'color': '#29ABD6'},
            text=ratings[i], hoverinfo='text', showlegend=False
    ))

fig = dict(data=traces, layout=layout)
py.iplot(fig, filename='linear-gauge')
```

#### Reference
See https://plot.ly/python/reference/ for more information and chart attribute options!

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'linear-gauge.ipynb', 'python/linear-gauge-chart/', 'Python Linear-Gauge Chart | plotly',
    'How to make interactive linear-guage charts in Python with Plotly. ',
    title = 'Python Linear-Gauge Chart | plotly',
    name = 'Linear-Gauge Chart',
    thumbnail='thumbnail/linear-gauge.jpg', language='python',
    has_thumbnail='true', display_as='basic', order=12,
    ipynb='~notebook_demo/12')
```

```python

```
