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
    description: Learn how to perform a one and two way ANOVA test using Python.
    display_as: statistics
    has_thumbnail: false
    language: python
    layout: base
    name: Anova
    order: 8
    page_type: example_index
    permalink: python/anova/
    thumbnail: /images/static-image
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by dowloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


#### Imports
The tutorial below imports [NumPy](http://www.numpy.org/), [Pandas](https://plot.ly/pandas/intro-to-pandas-tutorial/), [SciPy](https://www.scipy.org/), and [Statsmodels](http://statsmodels.sourceforge.net/stable/).

```python
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.tools import FigureFactory as FF

import numpy as np
import pandas as pd
import scipy

import statsmodels
import statsmodels.api as sm
from statsmodels.formula.api import ols
```

#### One-Way ANOVA


An `Analysis of Variance Test` or an `ANOVA` is a generalization of the t-tests to more than 2 groups. Our null hypothesis states that there are equal means in the populations from which the groups of data were sampled. More succinctly:

$$
\begin{align*}
\mu_1 = \mu_2 = ... = \mu_n
\end{align*}
$$

for $n$ groups of data. Our alternative hypothesis would be that any one of the equivalences in the above equation fail to be met.

```python
moore = sm.datasets.get_rdataset("Moore", "car", cache=True)

data = moore.data
data = data.rename(columns={"partner.status" :"partner_status"})  # make name pythonic

moore_lm = ols('conformity ~ C(fcategory, Sum)*C(partner_status, Sum)', data=data).fit()
table = sm.stats.anova_lm(moore_lm, typ=2) # Type 2 ANOVA DataFrame

print(table)
```

In this ANOVA test, we are dealing with an `F-Statistic` and not a `p-value`. Their connection is integral as they are two ways of expressing the same thing. When we set a `significance level` at the start of our statistical tests (usually 0.05), we are saying that if our variable in question takes on the 5% ends of our distribution, then we can start to make the case that there is evidence against the null, which states that the data belongs to _this particular distribution_.

The F value is the point such that the area of the curve past that point to the tail is just the p-value. Therefore:

$$
\begin{align*}
Pr(>F) = p
\end{align*}
$$

For more information on the choice of 0.05 for a significance level, check out [this page](http://www.investopedia.com/exam-guide/cfa-level-1/quantitative-methods/hypothesis-testing.asp).


Let us import some data for our next analysis. This time some data on tooth growth:

```python
data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/tooth_growth_csv')
df = data[0:10]

table = FF.create_table(df)
py.iplot(table, filename='tooth-data-sample')
```

#### Two-Way ANOVA


In a `Two-Way ANOVA`, there are two variables to consider. The question is whether our variable in question (tooth length `len`) is related to the two other variables `supp` and `dose` by the equation:

$$
\begin{align*}
len = supp + dose + supp \times dose
\end{align*}
$$

```python
formula = 'len ~ C(supp) + C(dose) + C(supp):C(dose)'
model = ols(formula, data).fit()
aov_table = statsmodels.stats.anova.anova_lm(model, typ=2)
print(aov_table)
```

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'python-Anova.ipynb', 'python/anova/', 'Anova | plotly',
    'Learn how to perform a one and two way ANOVA test using Python.',
    title='Anova in Python | plotly',
    name='Anova',
    language='python',
    page_type='example_index', has_thumbnail='false', display_as='statistics', order=8,
    ipynb= '~notebook_demo/108')
```

```python

```
