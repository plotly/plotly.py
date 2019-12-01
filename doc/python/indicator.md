---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.2.1
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
    version: 3.7.3
  plotly:
    description: How to make guage charts in Python with Plotly.
    display_as: financial
    language: python
    layout: base
    name: Indicators
    order: 7
    page_type: u-guide
    permalink: python/indicator/
    thumbnail: thumbnail/indicator.jpg
---

#### Overview
In this tutorial we introduce a new trace named "Indicator". The purpose of "indicator" is to visualize a single value specified by the "value" attribute.
  Three distinct visual elements are available to represent that value: number, delta and gauge. Any combination of them can be specified via the "mode" attribute.
  Top-level attributes are:
    <ol>
      <li>value: the value to visualize</li>
      <li> mode: which visual elements to draw</li>
      <li> align: how to align number and delta (left, center, right)</li>
      <li> domain: the extent of the figure</li>
    </ol>

  Then we can configure the 3 different visual elements via their respective container:
    <ol>
      <li> number is simply a representation of the number in text. It has attributes:
      <li> valueformat: to format the number</li>
      <li> prefix: a string before the number</li>
      <li> suffix: a string after the number </li>
      <li> font.(family|size): to control the font</li>
    </ol>
   "delta" simply displays the difference between the value with respect to a reference. It has attributes:
    <ol>
      <li> reference: the number to compare the value with</li>
      <li> relative: whether that difference is absolute or relative</li>
      <li> valueformat: to format the delta</li>
      <li> (increasing|decreasing).color: color to be used for positive or decreasing delta</li>
      <li> (increasing|decreasing).symbol: symbol displayed on the left of the delta</li>
      <li> font.(family|size): to control the font</li>
      <li> position: position relative to `number` (either top, left, bottom, right)</li>
    </ol>
    Finally, we can have a simple title for the indicator via `title` with 'text' attribute which is a string, and 'align' which can be set to left, center, and right.
    There are two gauge types: [angular](https://plot.ly/python/gauge-charts/) and [bullet](https://plot.ly/python/bullet-charts/). Here is a combination of both shapes (angular, bullet), and different modes (guage, delta, and value):

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Indicator(
    value = 200,
    delta = {'reference': 160},
    gauge = {
        'axis': {'visible': False}},
    domain = {'row': 0, 'column': 0}))

fig.add_trace(go.Indicator(
    value = 120,
    gauge = {
        'shape': "bullet",
        'axis' : {'visible': False}},
    domain = {'x': [0.05, 0.5], 'y': [0.15, 0.35]}))

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = 300,
    domain = {'row': 0, 'column': 1}))

fig.add_trace(go.Indicator(
    mode = "delta",
    value = 40,
    domain = {'row': 1, 'column': 1}))

fig.update_layout(
    grid = {'rows': 2, 'columns': 2, 'pattern': "independent"},
    template = {'data' : {'indicator': [{
        'title': {'text': "Speed"},
        'mode' : "number+delta+gauge",
        'delta' : {'reference': 90}}]
                         }})
```

#### A Single Angular Gauge Chart

```python
import plotly.graph_objects as go

fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = 450,
    title = {'text': "Speed"},
    domain = {'x': [0, 1], 'y': [0, 1]}
))

fig.show()
```

##### Bullet Gauge
The equivalent of above "angular gauge":

```python
import plotly.graph_objects as go

fig = go.Figure(go.Indicator(
    mode = "number+gauge+delta",
    gauge = {'shape': "bullet"},
    delta = {'reference': 300},
    value = 220,
    domain = {'x': [0.1, 1], 'y': [0.2, 0.9]},
    title = {'text': "Avg order size"}))

fig.show()
```

#### Showing Information above Your Chart
Another interesting feature is that indicator trace sits above the other traces (even the 3d ones). This way, it can be easily used as an overlay as demonstrated below

```python
import plotly.graph_objects as go

fig = go.Figure(go.Indicator(
    mode = "number+delta",
    value = 492,
    delta = {"reference": 512, "valueformat": ".0f"},
    title = {"text": "Users online"},
    domain = {'y': [0, 1], 'x': [0.25, 0.75]}))

fig.add_trace(go.Scatter(
    y = [325, 324, 405, 400, 424, 404, 417, 432, 419, 394, 410, 426, 413, 419, 404, 408, 401, 377, 368, 361, 356, 359, 375, 397, 394, 418, 437, 450, 430, 442, 424, 443, 420, 418, 423, 423, 426, 440, 437, 436, 447, 460, 478, 472, 450, 456, 436, 418, 429, 412, 429, 442, 464, 447, 434, 457, 474, 480, 499, 497, 480, 502, 512, 492]))

fig.update_layout(xaxis = {'range': [0, 62]})
fig.show()
```
#### Data Cards / Big Numbers
Data card helps to display more contextual information about the data. Sometimes one number is all you want to see in a report, such as total sales, annual revenue, etc. This example shows how to visualize these big numbers:

```python
import plotly.graph_objects as go

fig = go.Figure(go.Indicator(
    mode = "number+delta",
    value = 400,
    number = {'prefix': "$"},
    delta = {'position': "top", 'reference': 320},
    domain = {'x': [0, 1], 'y': [0, 1]}))

fig.update_layout(paper_bgcolor = "lightgray")

fig.show()
```

#### It's possible to display several numbers

```python
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = 200,
    domain = {'x': [0, 0.5], 'y': [0, 0.5]},
    delta = {'reference': 400, 'relative': True, 'position' : "top"}))

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = 350,
    delta = {'reference': 400, 'relative': True},
    domain = {'x': [0, 0.5], 'y': [0.5, 1]}))

fig.add_trace(go.Indicator(
    mode = "number+delta",
    value = 450,
    title = {"text": "Accounts<br><span style='font-size:0.8em;color:gray'>Subtitle</span><br><span style='font-size:0.8em;color:gray'>Subsubtitle</span>"},
    delta = {'reference': 400, 'relative': True},
    domain = {'x': [0.6, 1], 'y': [0, 1]}))

fig.show()
```

#### Reference
See https://plot.ly/python/reference/#indicator for more information and chart attribute options!

```python

```
