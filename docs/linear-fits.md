---
jupyter:
  jupytext:
    notebook_metadata_filter: all
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.2
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
    version: 3.7.7
  plotly:
    description: Add linear Ordinary Least Squares (OLS) regression trendlines or
      non-linear Locally Weighted Scatterplot Smoothing (LOWESS) trendlines to scatterplots
      in Python. Options for moving averages (rolling means) as well as exponentially-weighted
      and expanding functions.
    display_as: statistical
    language: python
    layout: base
    name: Linear and Non-Linear Trendlines
    order: 12
    page_type: u-guide
    permalink: python/linear-fits/
    thumbnail: thumbnail/linear_fit.jpg
---

### Linear fit trendlines with Plotly Express

[Plotly Express](/python/plotly-express/) is the easy-to-use, high-level interface to Plotly, which [operates on a variety of types of data](/python/px-arguments/) and produces [easy-to-style figures](/python/styling-plotly-express/).

Plotly Express allows you to add [Ordinary Least Squares](https://en.wikipedia.org/wiki/Ordinary_least_squares) regression trendline to scatterplots with the `trendline` argument. In order to do so, you will need to [install `statsmodels` and its dependencies](https://www.statsmodels.org/stable/install.html). Hovering over the trendline will show the equation of the line and its R-squared value.

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

### Displaying a single trendline with multiple traces

_new in v5.2_

To display a single trendline using the entire dataset, set the `trendline_scope` argument to `"overall"`. The same trendline will be overlaid on all facets and animation frames. The trendline color can be overridden with `trendline_color_override`.

```python
import plotly.express as px

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", symbol="smoker", color="sex", trendline="ols", trendline_scope="overall")
fig.show()
```

```python
import plotly.express as px

df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", facet_col="smoker", color="sex", 
                 trendline="ols", trendline_scope="overall", trendline_color_override="black")
fig.show()
```

### OLS Parameters

_new in v5.2_

OLS trendlines can be fit with log transformations to both X or Y data using the `trendline_options` argument, independently of whether or not the plot has [logarithmic axes](https://plotly.com/python/log-plot/).

```python
import plotly.express as px

df = px.data.gapminder(year=2007)
fig = px.scatter(df, x="gdpPercap", y="lifeExp", 
                 trendline="ols", trendline_options=dict(log_x=True),
                 title="Log-transformed fit on linear axes")
fig.show()
```

```python
import plotly.express as px

df = px.data.gapminder(year=2007)
fig = px.scatter(df, x="gdpPercap", y="lifeExp", log_x=True, 
                 trendline="ols", trendline_options=dict(log_x=True),
                 title="Log-scaled X axis and log-transformed fit")
fig.show()
```

### Locally WEighted Scatterplot Smoothing (LOWESS)

Plotly Express also supports non-linear [LOWESS](https://en.wikipedia.org/wiki/Local_regression) trendlines. In order use this feature, you will need to [install `statsmodels` and its dependencies](https://www.statsmodels.org/stable/install.html).

```python
import plotly.express as px

df = px.data.stocks(datetimes=True)
fig = px.scatter(df, x="date", y="GOOG", trendline="lowess")
fig.show()
```

_new in v5.2_

The level of smoothing can be controlled via the `frac` trendline option, which indicates the fraction of the data that the LOWESS smoother should include. The default is a fairly smooth line with `frac=0.6666` and lowering this fraction will give a line that more closely follows the data.

```python
import plotly.express as px

df = px.data.stocks(datetimes=True)
fig = px.scatter(df, x="date", y="GOOG", trendline="lowess", trendline_options=dict(frac=0.1))
fig.show()
```

### Moving Averages

_new in v5.2_

Plotly Express can leverage Pandas' [`rolling`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html), [`ewm`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ewm.html) and [`expanding`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.expanding.html) functions in trendlines as well, for example to display moving averages. Values passed to `trendline_options` are passed directly to the underlying Pandas function (with the exception of the `function` and `function_options` keys, see below).

```python
import plotly.express as px

df = px.data.stocks(datetimes=True)
fig = px.scatter(df, x="date", y="GOOG", trendline="rolling", trendline_options=dict(window=5),
                title="5-point moving average")
fig.show()
```

```python
import plotly.express as px

df = px.data.stocks(datetimes=True)
fig = px.scatter(df, x="date", y="GOOG", trendline="ewm", trendline_options=dict(halflife=2),
                title="Exponentially-weighted moving average (halflife of 2 points)")
fig.show()
```

```python
import plotly.express as px

df = px.data.stocks(datetimes=True)
fig = px.scatter(df, x="date", y="GOOG", trendline="expanding", title="Expanding mean")
fig.show()
```

### Other Functions

The `rolling`, `expanding` and `ewm` trendlines support other functions than the default `mean`, enabling, for example, a moving-median trendline, or an expanding-max trendline.

```python
import plotly.express as px

df = px.data.stocks(datetimes=True)
fig = px.scatter(df, x="date", y="GOOG", trendline="rolling", trendline_options=dict(function="median", window=5),
                title="Rolling Median")
fig.show()
```

```python
import plotly.express as px

df = px.data.stocks(datetimes=True)
fig = px.scatter(df, x="date", y="GOOG", trendline="expanding", trendline_options=dict(function="max"),
                title="Expanding Maximum")
fig.show()
```

In some cases, it is necessary to pass options into the underying Pandas function, for example the `std` parameter must be provided if the `win_type` argument to `rolling` is `"gaussian"`. This is possible with the `function_args` trendline option.

```python
import plotly.express as px

df = px.data.stocks(datetimes=True)
fig = px.scatter(df, x="date", y="GOOG", trendline="rolling", 
                 trendline_options=dict(window=5, win_type="gaussian", function_args=dict(std=2)),
                title="Rolling Mean with Gaussian Window")
fig.show()
```

### Displaying only the trendlines

In some cases, it may be desirable to show only the trendlines, by removing the scatter points.

```python
import plotly.express as px

df = px.data.stocks(indexed=True, datetimes=True)
fig = px.scatter(df, trendline="rolling", trendline_options=dict(window=5),
                title="5-point moving average")
fig.data = [t for t in fig.data if t.mode == "lines"]
fig.update_traces(showlegend=True) #trendlines have showlegend=False by default
fig.show()
```

```python

```
