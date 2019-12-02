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
    description: Learn how to perform a one sample and two sample t-test using Python.
    display_as: statistics
    has_thumbnail: false
    language: python
    layout: base
    name: T-Test
    order: 7
    page_type: example_index
    permalink: python/t-test/
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

#### Generate Data


Let us generate some random data from the `Normal Distriubtion`. We will sample 50 points from a normal distribution with mean $\mu = 0$ and variance $\sigma^2 = 1$ and from another with mean $\mu = 2$ and variance $\sigma^2 = 1$.

```python
data1 = np.random.normal(0, 1, size=50)
data2 = np.random.normal(2, 1, size=50)
```

The two normal probability distribution functions (p.d.f) stacked on top of each other look like this:

```python
x = np.linspace(-4, 4, 160)
y1 = scipy.stats.norm.pdf(x)
y2 = scipy.stats.norm.pdf(x, loc=2)

trace1 = go.Scatter(
    x = x,
    y = y1,
    mode = 'lines+markers',
    name='Mean of 0'
)

trace2 = go.Scatter(
    x = x,
    y = y2,
    mode = 'lines+markers',
    name='Mean of 2'
)

data = [trace1, trace2]

py.iplot(data, filename='normal-dists-plot')
```

#### One Sample T Test


A `One Sample T-Test` is a statistical test used to evaluate the null hypothesis that the mean $m$ of a 1D sample dataset of independant observations is equal to the true mean $\mu$ of the population from which the data is sampled. In other words, our null hypothesis is that

$$
\begin{align*}
m = \mu
\end{align*}
$$

For our T-test, we will be using a significance level of `0.05`. On the matter of doing ethical science, it is good practice to always state the chosen significance level for a given test _before_ actually conducting the test. This is meant to ensure that the analyst does not modify the significance level for the purpose of achieving a desired outcome.

For more information on the choice of 0.05 for a significance level, check out [this page](http://www.investopedia.com/exam-guide/cfa-level-1/quantitative-methods/hypothesis-testing.asp).

```python
true_mu = 0

onesample_results = scipy.stats.ttest_1samp(data1, true_mu)

matrix_onesample = [
    ['', 'Test Statistic', 'p-value'],
    ['Sample Data', onesample_results[0], onesample_results[1]]
]

onesample_table = FF.create_table(matrix_onesample, index=True)
py.iplot(onesample_table, filename='onesample-table')
```

Since our p-value is greater than our Test-Statistic, we have good evidence to not reject the null-hypothesis at the $0.05$ significance level. This is our expected result because the data was collected from a normal distribution.


#### Two Sample T Test


If we have two independently sampled datasets (with equal variance) and are interested in exploring the question of whether the true means $\mu_1$ and $\mu_2$ are identical, that is, if the data were sampled from the same population, we would use a `Two Sample T-Test`.

Typically when a researcher in a field is interested in the affect of a given test variable between two populations, they will take one sample from each population and will note them as the experimental group and the control group. The experimental group is the sample which will receive the variable being tested, while the control group will not.

This test variable is observed (eg. blood pressure) for all the subjects and a two sided t-test can be used to investigate if the two groups of subjects were sampled from populations with the same true mean, i.e. "Does the drug have an effect?"

```python
twosample_results = scipy.stats.ttest_ind(data1, data2)

matrix_twosample = [
    ['', 'Test Statistic', 'p-value'],
    ['Sample Data', twosample_results[0], twosample_results[1]]
]

twosample_table = FF.create_table(matrix_twosample, index=True)
py.iplot(twosample_table, filename='twosample-table')
```

Since our p-value is much less than our Test Statistic, then with great evidence we can reject our null hypothesis of identical means. This is in alignment with our setup, since we sampled from two different normal pdfs with different means.

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'python-T-Test.ipynb', 'python/t-test/', 'T-Test | plotly',
    'Learn how to perform a one sample and two sample t-test using Python.',
    title='T-Test in Python. | plotly',
    name='T-Test',
    language='python',
    page_type='example_index', has_thumbnail='false', display_as='statistics', order=7,
    ipynb= '~notebook_demo/115')
```

```python

```
