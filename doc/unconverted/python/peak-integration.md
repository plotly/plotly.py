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
    description: Learn how to integrate the area between peaks and bassline in Python.
    display_as: peak-analysis
    has_thumbnail: false
    language: python
    layout: base
    name: Peak Integration
    order: 4
    page_type: example_index
    permalink: python/peak-integration/
    thumbnail: /images/static-image
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by downloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Imports
The tutorial below imports [NumPy](http://www.numpy.org/), [Pandas](https://plot.ly/pandas/intro-to-pandas-tutorial/), [SciPy](https://www.scipy.org/) and [PeakUtils](http://pythonhosted.org/PeakUtils/).

```python
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff

import numpy as np
import pandas as pd
import scipy
import peakutils
```

#### Tips
Our method for finding the area under any peak is to find the area from the `data values` to the x-axis, the area from the `baseline` to the x-axis, and then take the difference between them. In particular, we want to find the areas of these functions defined on the x-axis interval $I$ under the peak.

Let $T(x)$ be the function of the data, $B(x)$ the function of the baseline, and $Area$ the peak integration area between the baseline and the first peak. Since $T(x) \geq B(x)$ for all $x$, then we know that

$$
\begin{align}
A = \int_{I} T(x)dx - \int_{I} B(x)dx
\end{align}
$$


#### Import Data
For our example below we will import some data on milk production by month:

```python
milk_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/monthly-milk-production-pounds.csv')
time_series = milk_data['Monthly milk production (pounds per cow)']
time_series = np.asarray(time_series)

df = milk_data[0:15]

table = ff.create_table(df)
py.iplot(table, filename='milk-production-dataframe')
```

#### Area Under One Peak

```python
baseline_values = peakutils.baseline(time_series)

x = [j for j in range(len(time_series))]
time_series = time_series.tolist()
baseline_values = baseline_values.tolist()

rev_baseline_values = baseline_values[:11]
rev_baseline_values.reverse()
area_x = [0,1,2,3,4,5,6,7,8,9,10,11,10,9,8,7,6,5,4,3,2,1]
area_y = time_series[:11] + rev_baseline_values

trace = go.Scatter(
    x=x,
    y=time_series,
    mode='lines',
    marker=dict(
        color='#B292EA',
    ),
    name='Original Plot'
)

trace2 = go.Scatter(
    x=x,
    y=baseline_values,
    mode='markers',
    marker=dict(
        size=3,
        color='#EB55BF',
    ),
    name='Bassline'
)

trace3 = go.Scatter(
    x=area_x,
    y=area_y,
    mode='lines+markers',
    marker=dict(
        size=4,
        color='rgb(255,0,0)',
    ),
    name='1st Peak Outline'
)

first_peak_x = [j for j in range(11)]
area_under_first_peak = np.trapz(time_series[:11], first_peak_x) - np.trapz(baseline_values[:11], first_peak_x)
area_under_first_peak

annotation = go.Annotation(
    x=80,
    y=1000,
    text='The peak integration for the first peak is approximately %s' % (area_under_first_peak),
    showarrow=False
)

layout = go.Layout(
    annotations=[annotation]
)

trace_data = [trace, trace2, trace3]
fig = go.Figure(data=trace_data, layout=layout)
py.iplot(fig, filename='milk-production-peak-integration')
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'python-Peak-Integration.ipynb', 'python/peak-integration/', 'Peak Integration | plotly',
    'Learn how to integrate the area between peaks and bassline in Python.',
    title='Peak Integration in Python | plotly',
    name='Peak Integration',
    language='python',
    page_type='example_index', has_thumbnail='false', display_as='peak-analysis', order=4,
    ipynb= '~notebook_demo/121')
```

```python

```
