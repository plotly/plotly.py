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
    display_name: Python 3
    language: python
    name: python3
  plotly:
    description: Learn how to generate various normality tests using Python.
    display_as: statistics
    has_thumbnail: false
    language: python
    layout: base
    name: Normality Tests
    order: 2
    page_type: u-guide
    permalink: python/normality-test/
    thumbnail: /images/static-image
---

#### New to Plotly?
Plotly's Python library is free and open source! [Get started](https://plot.ly/python/getting-started/) by dowloading the client and [reading the primer](https://plot.ly/python/getting-started/).
<br>You can set up Plotly to work in [online](https://plot.ly/python/getting-started/#initialization-for-online-plotting) or [offline](https://plot.ly/python/getting-started/#initialization-for-offline-plotting) mode, or in [jupyter notebooks](https://plot.ly/python/getting-started/#start-plotting-online).
<br>We also have a quick-reference [cheatsheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf) (new!) to help you get started!


### Normality Tests


In statistics, normality tests are used to determine whether a data set is modeled for Normal (Gaussian) Distribution. Many statistical functions require that a distribution be normal or nearly normal.

There are several methods of assessing whether data are normally distributed or not. They fall into two broad categories: _graphical_ and _statistical_.
The common techniques are:

**_Graphical_**
   - Histogram Plot
   - Quantile-Quantile Plot

**_Statistical_**
   - Shapiro-Wilk Test
   - Kolmogorov-Smirnov
   - D'Agostino's $K^{2}$ Test
   - Anderson-Darling Test


### Test Dataset


Let's first develop a test dataset that we can use throughout this tutorial.

_The tutorial below imports [NumPy](http://www.numpy.org/), [Pandas](https://plot.ly/pandas/intro-to-pandas-tutorial/), and [SciPy](https://www.scipy.org/)._

```python
# Imports
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff

import numpy as np
import pandas as pd
import scipy
```

_Generate Gaussian Data_

```python
# Seed the random number generator
np.random.seed(10)

# Generate Univariate Observations
gauss_data = 5 * np.random.randn(100) + 50
print('mean=%.3f stdv=%.3f' % (np.mean(gauss_data), np.std(gauss_data)))
```

We can see that the mean and standard deviation are reasonable but rough estimations of the true underlying population mean and standard deviation, given the small-ish sample size.


### Histogram Plot
A simple and commonly used plot to quickly check the distribution of a sample of data is the histogram.

In the histogram, the data is divided into a pre-specified number of groups called bins. The data is then sorted into each bin and the count of the number of observations in each bin is retained.

The plot shows the bins across the x-axis maintaining their ordinal relationship, and the count in each bin on the y-axis.

A sample of data has a Gaussian distribution of the histogram plot, showing the familiar bell shape. By default, the number of bins is automatically estimated from the data provided.

```python
trace = go.Histogram(
    x=gauss_data
)

py.iplot([trace], filename='normality-histogram')
```

We can see a Gaussian-like shape to the data, that although is not strongly the familiar bell-shape, is a rough approximation.


### Quantile-Quantile Plot


Another popular plot for checking the distribution of a data sample is the quantile-quantile plot, Q-Q plot, or QQ plot for short.

This plot generates its own sample of the idealized distribution that we are comparing with, in this case the Gaussian distribution. The idealized samples are divided into groups (e.g. 5), called quantiles. Each data point in the sample is paired with a similar member from the idealized distribution at the same cumulative distribution.

The resulting points are plotted as a scatter plot with the idealized value on the x-axis and the data sample on the y-axis.

A perfect match for the distribution will be shown by a line of dots on a 45-degree angle from the bottom left of the plot to the top right. Often a line is drawn on the plot to help make this expectation clear. Deviations by the dots from the line shows a deviation from the expected distribution.

We can develop a QQ plot in Python using the [qqplot() statsmodels function](http://www.statsmodels.org/dev/generated/statsmodels.graphics.gofplots.qqplot.html). The function takes the data sample and by default assumes we are comparing it to a Gaussian distribution. We can draw the standardized line by setting the `'line'` argument to `'s'`

A complete example of plotting the test dataset as a QQ plot is provided below.

```python
from statsmodels.graphics.gofplots import qqplot

qqplot_data = qqplot(gauss_data, line='s').gca().lines
```

```python
fig = go.Figure()

fig.add_trace({
    'type': 'scatter',
    'x': qqplot_data[0].get_xdata(),
    'y': qqplot_data[0].get_ydata(),
    'mode': 'markers',
    'marker': {
        'color': '#19d3f3'
    }
})

fig.add_trace({
    'type': 'scatter',
    'x': qqplot_data[1].get_xdata(),
    'y': qqplot_data[1].get_ydata(),
    'mode': 'lines',
    'line': {
        'color': '#636efa'
    }

})


fig['layout'].update({
    'title': 'Quantile-Quantile Plot',
    'xaxis': {
        'title': 'Theoritical Quantities',
        'zeroline': False
    },
    'yaxis': {
        'title': 'Sample Quantities'
    },
    'showlegend': False,
    'width': 800,
    'height': 700,
})


py.iplot(fig, filename='normality-QQ')
```

Running the example creates the QQ plot showing the scatter plot of points in a diagonal line, closely fitting the expected diagonal pattern for a sample from a Gaussian distribution.

There are a few small deviations, especially at the bottom of the plot, which is to be expected given the small data sample.


### Statistical Normality Tests


There are many statistical tests that we can use to quantify whether a sample of data looks as though it was drawn from a Gaussian distribution.

Each test makes different assumptions and considers different aspects of the data.

We will look at 3 commonly used tests in this section that you can apply to your own data samples

#### Interpretation of a Test
Before you can apply the statistical tests, you must know how to interpret the results.

Each test will return at least two things:

- **_Statistic_**: A quantity calculated by the test that can be interpreted in the context of the test via comparing it to critical values from the distribution of the test statistic.
- **_p-value_**: Used to interpret the test, in this case whether the sample was drawn from a Gaussian distribution.

Each test calculates a test-specific statistic. This statistic can aid in the interpretation of the result, although it may require a deeper proficiency with statistics and a deeper knowledge of the specific statistical test. Instead, the p-value can be used to quickly and accurately interpret the statistic in practical applications.

The tests assume that that the sample was drawn from a Gaussian distribution. Technically this is called the null hypothesis, or H0. A threshold level is chosen called alpha, typically 5% (or 0.05), that is used to interpret the p-value.

In the SciPy implementation of these tests, you can interpret the p value as follows.
 - **_p <= alpha_**: reject H0, not normal.
 - **_p > alpha_**: fail to reject H0, normal.

This means that, in general, we are seeking results with a larger p-value to confirm that our sample was likely drawn from a Gaussian distribution.

A result above 5% does not mean that the null hypothesis is true. It means that it is very likely true given available evidence. The p-value is not the probability of the data fitting a Gaussian distribution; it can be thought of as a value that helps us interpret the statistical test.


### Shapiro-Wilk Test


The [Shapiro-Wilk test](https://en.wikipedia.org/wiki/Shapiro%E2%80%93Wilk_test) evaluates a data sample and quantifies how likely it is that the data was drawn from a Gaussian distribution, named for Samuel Shapiro and Martin Wilk.

In practice, the Shapiro-Wilk test is believed to be a reliable test of normality, although there is some suggestion that the test may be suitable for smaller samples of data, e.g. thousands of observations or fewer.

The [shapiro() SciPy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html) function will calculate the Shapiro-Wilk on a given dataset. The function returns both the W-statistic calculated by the test and the p-value.

The complete example of performing the Shapiro-Wilk test on the dataset is listed below.

```python
from scipy.stats import shapiro
stat, p = shapiro(gauss_data)

# interpret
alpha = 0.05
if p > alpha:
    msg = 'Sample looks Gaussian (fail to reject H0)'
else:
    msg = 'Sample does not look Gaussian (reject H0)'

result_mat = [
    ['Length of the sample data', 'Test Statistic', 'p-value', 'Comments'],
    [len(gauss_data), stat, p, msg]
]

swt_table = ff.create_table(result_mat)
swt_table['data'][0].colorscale=[[0, '#2a3f5f'],[1, '#ffffff']]
swt_table['layout']['height']=200
swt_table['layout']['margin']['t']=50
swt_table['layout']['margin']['b']=50

py.iplot(swt_table, filename='shapiro-wilk-table')
```

Running the above example calculates the statistic and p-value.

The p-value is interested and finds that the data is likely drawn from a Gaussian distribution.


### Anderson-Darling Test


[Anderson-Darling Test](https://en.wikipedia.org/wiki/Anderson%E2%80%93Darling_test) is a statistical test that can be used to evaluate whether a data sample comes from one of among many known data samples, named for Theodore Anderson and Donald Darling.

It can be used to check whether a data sample is normal. The test is a modified version of a more sophisticated nonparametric goodness-of-fit statistical test called the [Kolmogorov-Smirnov test](https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test).

A feature of the Anderson-Darling test is that it returns a list of critical values rather than a single p-value. This can provide the basis for a more thorough interpretation of the result.

The [anderson() SciPy function](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.anderson.html) implements the Anderson-Darling test. It takes as parameters the data sample and the name of the distribution to test it against. By default, the test will check against the Gaussian distribution (`dist='norm'`).

The complete example of calculating the Anderson-Darling test on the sample problem is listed below.

```python
from scipy.stats import anderson

result = anderson(gauss_data)
stat = round(result.statistic, 4)

p = 0
result_mat = []
for i in range(len(result.critical_values)):
    sl, cv = result.significance_level[i], result.critical_values[i]
    if result.statistic < result.critical_values[i]:
        msg = 'Sample looks Gaussian (fail to reject H0)'
    else:
        msg = 'Sample does not look Gaussian (reject H0)'
    result_mat.append([len(gauss_data), stat, sl, cv, msg])

trace = go.Table(
    header=dict(values=['<b>Sample Size</b>', '<b>Statistic</b>', '<b>Significance Level</b>', '<b>Critical Value</b>', '<b>Comment</b>'],
                line = dict(width=0),
                fill = dict(color='rgba(42,63,95,0.8)'),
                align = 'center',
                font = dict(
                    color = '#ffffff',
                    size = 12
                )),
    cells=dict(values=np.array(result_mat).T,
               line = dict(width=0),
               fill = dict(color=[['#EBF0F8', '#ffffff', '#EBF0F8', '#ffffff', '#EBF0F8']]),
               align = 'center',
               height = 40),
    columnwidth=[0.3, 0.25, 0.3, 0.25, 0.5])
layout = dict(
    height=300,
    margin=dict(
        l=5,
        r=5,
        t=30,
        b=0
    )
)
data = [trace]
andar_table = dict(data=data, layout=layout)

py.iplot(andar_table, filename='anderson-darling-table')
```

Running the example calculates the statistic on the test data set and the critical values are tabulated.

Critical values in a statistical test are a range of pre-defined significance boundaries at which the H0 can be failed to be rejected if the calculated statistic is less than the critical value. Rather than just a single p-value, the test returns a critical value for a range of different commonly used significance levels.

We can interpret the results by failing to reject the null hypothesis that the data is normal if the calculated test statistic is less than the critical value at a chosen significance level.

We can see that at each significance level, the test has found that the data follows a normal distribution


### D'Agostino's $K^{2}$Test


The [D'Agostino's $K^{2}$ test](https://en.wikipedia.org/wiki/D%27Agostino%27s_K-squared_test) calculates summary statistics from the data, namely kurtosis and skewness, to determine if the data distribution departs from the normal distribution, named for Ralph D’Agostino.

 - Skew is a quantification of how much a distribution is pushed left or right, a measure of asymmetry in the distribution.
 - Kurtosis quantifies how much of the distribution is in the tail. It is a simple and commonly used statistical test for normality.

The D'Agostino's $K^{2}$ test is available via the [normaltest() SciPy function](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.normaltest.html) and returns the test statistic and the p-value.

The complete example of the D'Agostino's $K^{2}$ test on the dataset is listed below.

```python
from scipy.stats import normaltest

stat, p = normaltest(gauss_data)

# interpret
alpha = 0.05
if p > alpha:
    msg = 'Sample looks Gaussian (fail to reject H0)'
else:
    msg = 'Sample does not look Gaussian (reject H0)'

result_mat = [
    ['Length of the sample data', 'Test Statistic', 'p-value', 'Comments'],
    [len(gauss_data), stat, p, msg]
]

normt_table = ff.create_table(result_mat)
normt_table['data'][0].colorscale=[[0, '#2a3f5f'],[1, '#ffffff']]
normt_table['layout']['height']=200
normt_table['layout']['margin']['t']=50
normt_table['layout']['margin']['b']=50

py.iplot(normt_table, filename="D'Agostino-test-table")
```

Running the above example calculates the statistic and p-value.
The p-value is interpreted against an alpha of 5% and finds that the test dataset does not significantly deviate from normal.

<!-- #region -->
#### Conclusion
We have covered a few normality tests, but this is not all of the tests that exist. It is recommended to use all possible tests on your data, where appropriate.


**_How to interpret the results?_**
   - Your data may not be normal for many different reasons. Each test looks at the question of whether a sample was drawn from a Gaussian distribution from a slightly different perspective.
   - Investigate why your data is not normal and perhaps use data preparation techniques to normalize the data.
   - Start looking into the use of nonparametric statistical methods instead of the parametric methods.
   - If some of the methods suggest that the sample is Gaussian and some not, then perhaps take this as an indication that your data is Gaussian-like.

_This tuorial is inspired from ["A Gentle Introduction to Normality Tests"](https://machinelearningmastery.com/a-gentle-introduction-to-normality-tests-in-python/)_
<!-- #endregion -->

```python
from IPython.display import display, HTML

display(HTML('<link href="//fonts.googleapis.com/css?family=Open+Sans:600,400,300,200|Inconsolata|Ubuntu+Mono:400,700" rel="stylesheet" type="text/css" />'))
display(HTML('<link rel="stylesheet" type="text/css" href="http://help.plot.ly/documentation/all_static/css/ipython-notebook-custom.css">'))

! pip install git+https://github.com/plotly/publisher.git --upgrade
import publisher
publisher.publish(
    'python-Normality-Test.ipynb', 'python/normality-test/', 'Normality Tests',
    'Learn how to generate various normality tests using Python. ',
    title = 'Normality Tests | Plotly',
    has_thumbnail='false',
    language='python',
    # page_type='example_index', // note this is only if you want the tutorial to appear on the main page: plot.ly/python
    display_as='statistics', order=2, ipynb='~notebook_demo/266')
```

```python

```
