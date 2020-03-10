---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: "1.1"
      jupytext_version: 1.1.1
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
    version: 3.6.8
  plotly:
    description:
      Add linear Ordinary Least Squares (OLS) regression trendlines or non-linear
      Locally Weighted Scatterplot Smoothing (LOEWSS) trendlines to scatterplots in Python.
    display_as: statistical
    language: python
    layout: base
    name: Linear and Non-Linear Trendlines
    order: 13
    page_type: u-guide
    permalink: python/linear-fits/
    thumbnail: thumbnail/linear_fit.jpg
---

### Linear fit trendlines with Plotly Express

[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on "tidy" data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/).

Plotly Express allows you to add [Ordinary Least](https://en.wikipedia.org/wiki/Ordinary_least_squares) Squares regression trendline to scatterplots with the `trendline` argument. In order to do so, you will need to install `statsmodels` and its dependencies. Hovering over the trendline will show the equation of the line and its R-squared value.

```python
import plotly.express as px

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", trendline="ols")
fig.show()
```

### Fitting multiple lines and retrieving the model parameters

Plotly Express will fit a trendline per trace, and allows you to access the underlying model parameters for all the models.

```python
import plotly.express as px

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", facet_col="smoker", color="sex", trendline="ols")
fig.show()

results = px.get_trendline_results(fig)
print(results)

results.query("sex == 'Male' and smoker == 'Yes'").px_fit_results.iloc[0].summary()
```

### Non-Linear Trendlines

Plotly Express also supports non-linear [LOWESS](https://en.wikipedia.org/wiki/Local_regression) trendlines.

```python
import plotly.express as px

df = px.data.gapminder().query("year == 2007")
fig = px.scatter(df, x="gdpPercap", y="lifeExp", color="continent", trendline="lowess")
fig.show()
```
