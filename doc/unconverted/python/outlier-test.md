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
    description: Learn how to test for outliers in datasets using Python.
    display_as: statistics
    has_thumbnail: false
    language: python
    layout: base
    name: Outlier Test
    order: 6
    page_type: example_index
    permalink: python/outlier-test/
    thumbnail: /images/static-image
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by dowloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Imports
The tutorial below imports [NumPy](http://www.numpy.org/), [Pandas](https://plot.ly/pandas/intro-to-pandas-tutorial/), and [SciPy](https://www.scipy.org/).

```python
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

import numpy as np
import pandas as pd
import scipy
```

#### Import Data


In order to start performing outlier tests, we will import some data of average wind speed sampled every 10 minutes, also used in the [Normality Test Tutorial](https://plot.ly/python/normality-test/).

```python
data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/wind_speed_laurel_nebraska.csv')
df = data[0:10]

table = FF.create_table(df)
py.iplot(table, filename='wind-data-sample')
```

In any set of data, an `outlier` is a a datum point that is not consistent with the other data points. If the data sampled from a particular distribution then with high probability, an outlier would not belong to that distribution. There are various tests used for testing if a particular point is an outlier, and this is done with the same null-hypothesis testing used in Normality Tests.


#### Q Test


Dixon's Q-Test is used to help determine whether there is evidence for a given point to be an outlier of a 1D dataset. It is assumed that the dataset is normally distributed. Since we have very strong evidence that our dataset above is normal from all our [normality tests](https://plot.ly/python/normality-test/), we can use the Q-Test here. As with the normality tests, we are assuming a significance level of $0.05$ and for simplicity, we are only considering the smallest datum point in the set.

For more information on the choice of 0.05 for a significance level, check out [this page](http://www.investopedia.com/exam-guide/cfa-level-1/quantitative-methods/hypothesis-testing.asp).

```python
def q_test_for_smallest_point(dataset):
    q_ref = 0.29  # the reference Q value for a significance level of 95% and 30 data points
    q_stat = (dataset[1] - dataset[0])/(dataset[-1] - dataset[0])

    if q_stat > q_ref:
        print("Since our Q-statistic is %f and %f > %f, we have evidence that our "
              "minimum point IS an outlier to the data.") %(q_stat, q_stat, q_ref)
    else:
        print("Since our Q-statistic is %f and %f < %f, we have evidence that our "
              "minimum point is NOT an outlier to the data.") %(q_stat, q_stat, q_ref)
```

For our example, the Q-statistic is the ratio of the absolute distance between the smallest and closest number in the set, to the range of our dataset. This means:

$$
\begin{align*}
Q = \frac{gap}{range}
\end{align*}
$$

For our example, we will take 30 values from our dataset that contains the minimum value in full dataset, and apply the test on that sample. Then we'll convert our array to a list and sort it by increasing value.

```python
dataset = data[100:130]['10 Min Sampled Avg'].values.tolist()
dataset.sort()
q_test_for_smallest_point(dataset)
```

#### Visualize the Q Test


To properly visualize our `critical height`, we can make a scatter plot with the dataset points in increasing order and draw a line for our critical height. This critical height is the threshold such that if our lowest point in the dataset was lower than it, than it would be considered an `outlier`. To derive this value, we just take

$$
\begin{align*}
Q_{reference} = 0.29
\end{align*}
$$

from a [look-up table](http://sebastianraschka.com/Articles/2014_dixon_test.html) and then plug it into our formula for $Q$ above, replacing our smallest value with an unknown $x$

$$
\begin{align*}
0.29 = \frac{5.5 - x}{26.0}
\end{align*}
$$

and therefore we get

$$
\begin{align*}
x = -2.04
\end{align*}
$$

```python
x = [j for j in range(len(dataset))]
y1 = dataset
y2 = [-2.04 for j in range(len(dataset))]

trace1 = go.Scatter(
    x = x,
    y = y1,
    mode = 'lines+markers',
    name='Dataset',
    marker=dict(symbol=[100, 0])
)

trace2 = go.Scatter(
    x = x,
    y = y2,
    mode = 'lines',
    name='Critical Line'
)

data = [trace1, trace2]
py.iplot(data, filename='q-test-scatter')
```

Since our smallest value (the holoed out circle) is higher than the critical line, this validates the result of the test that the point is `NOT` an outlier.

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'python-Outlier-Test.ipynb', 'python/outlier-test/', 'Outlier Test | plotly',
    'Learn how to test for outliers in datasets using Python.',
    title='Outlier Test in Python. | plotly',
    name='Outlier Test',
    language='python',
    page_type='example_index', has_thumbnail='false', display_as='statistics', order=6,
    ipynb= '~notebook_demo/113')
```

```python

```
