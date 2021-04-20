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
    description: Visualize regression in scikit-learn with Plotly.
    display_as: ai_ml
    language: python
    layout: base
    name: ML Regression
    order: 1
    page_type: u-guide
    permalink: python/ml-regression/
    thumbnail: thumbnail/ml-regression.png
---

<!-- #region -->
This page shows how to use Plotly charts for displaying various types of regression models, starting from simple models like [Linear Regression](https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html), and progressively move towards models like [Decision Tree][tree] and [Polynomial Features][poly]. We highlight various capabilities of plotly, such as comparative analysis of the same model with different parameters, displaying Latex, [surface plots](https://plotly.com/python/3d-surface-plots/) for 3D data, and enhanced prediction error analysis with [Plotly Express](https://plotly.com/python/plotly-express/).

We will use [Scikit-learn](https://scikit-learn.org/) to split and preprocess our data and train various regression models. Scikit-learn is a popular Machine Learning (ML) library that offers various tools for creating and training ML algorithms, feature engineering, data cleaning, and evaluating and testing models. It was designed to be accessible, and to work seamlessly with popular libraries like NumPy and Pandas.


[lasso]: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html
[tree]: https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html
[poly]: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html
<!-- #endregion -->

## Basic linear regression plots

In this section, we show you how to apply a simple regression model for predicting tips a server will receive based on various client attributes (such as sex, time of the week, and whether they are a smoker).

We will be using the [Linear Regression][lr], which is a simple model that fit an intercept (the mean tip received by a server), and add a slope for each feature we use, such as the value of the total bill. We show you how to do that with both Plotly Express and Scikit-learn.

### Ordinary Least Square (OLS) with `plotly.express`

This example shows [how to use `plotly.express`'s `trendline` parameter to train a simply Ordinary Least Square (OLS)](/python/linear-fits/) for predicting the tips waiters will receive based on the value of the total bill.

[lr]: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html

```python
import plotly.express as px

df = px.data.tips()
fig = px.scatter(
    df, x='total_bill', y='tip', opacity=0.65,
    trendline='ols', trendline_color_override='darkblue'
)
fig.show()
```

### Linear Regression with scikit-learn

You can also perform the same prediction using scikit-learn's `LinearRegression`.

```python
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

df = px.data.tips()
X = df.total_bill.values.reshape(-1, 1)

model = LinearRegression()
model.fit(X, df.tip)

x_range = np.linspace(X.min(), X.max(), 100)
y_range = model.predict(x_range.reshape(-1, 1))

fig = px.scatter(df, x='total_bill', y='tip', opacity=0.65)
fig.add_traces(go.Scatter(x=x_range, y=y_range, name='Regression Fit'))
fig.show()
```

### ML Regression in Dash

[Dash](https://plotly.com/dash/) is the best way to build analytical apps in Python using Plotly figures. To run the app below, run `pip install dash`, click "Download" to get the code and run `python app.py`.

Get started  with [the official Dash docs](https://dash.plotly.com/installation) and **learn how to effortlessly [style](https://plotly.com/dash/design-kit/) & [deploy](https://plotly.com/dash/app-manager/) apps like this with <a class="plotly-red" href="https://plotly.com/dash/">Dash Enterprise</a>.**


```python hide_code=true
from IPython.display import IFrame
snippet_url = 'https://dash-gallery.plotly.host/python-docs-dash-snippets/'
IFrame(snippet_url + 'ml-regression', width='100%', height=630)
```

## Model generalization on unseen data

With `go.Scatter`, you can easily color your plot based on a predefined data split. By coloring the training and the testing data points with different colors, you can easily see if whether the model generalizes well to the test data or not.

```python
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = px.data.tips()
X = df.total_bill[:, None]
X_train, X_test, y_train, y_test = train_test_split(X, df.tip, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)

x_range = np.linspace(X.min(), X.max(), 100)
y_range = model.predict(x_range.reshape(-1, 1))


fig = go.Figure([
    go.Scatter(x=X_train.squeeze(), y=y_train, name='train', mode='markers'),
    go.Scatter(x=X_test.squeeze(), y=y_test, name='test', mode='markers'),
    go.Scatter(x=x_range, y=y_range, name='prediction')
])
fig.show()
```

## Comparing different kNN models parameters

In addition to linear regression, it's possible to fit the same data using [k-Nearest Neighbors][knn]. When you perform a prediction on a new sample, this model either takes the weighted or un-weighted average of the neighbors. In order to see the difference between those two averaging options, we train a kNN model with both of those parameters, and we plot them in the same way as the previous graph.

Notice how we can combine scatter points with lines using Plotly.py. You can learn more about [multiple chart types](https://plotly.com/python/graphing-multiple-chart-types/).

[knn]: https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html

```python
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.neighbors import KNeighborsRegressor

df = px.data.tips()
X = df.total_bill.values.reshape(-1, 1)
x_range = np.linspace(X.min(), X.max(), 100)

# Model #1
knn_dist = KNeighborsRegressor(10, weights='distance')
knn_dist.fit(X, df.tip)
y_dist = knn_dist.predict(x_range.reshape(-1, 1))

# Model #2
knn_uni = KNeighborsRegressor(10, weights='uniform')
knn_uni.fit(X, df.tip)
y_uni = knn_uni.predict(x_range.reshape(-1, 1))

fig = px.scatter(df, x='total_bill', y='tip', color='sex', opacity=0.65)
fig.add_traces(go.Scatter(x=x_range, y=y_uni, name='Weights: Uniform'))
fig.add_traces(go.Scatter(x=x_range, y=y_dist, name='Weights: Distance'))
fig.show()
```

<!-- #region -->
## Displaying `PolynomialFeatures` using $\LaTeX$

Notice how linear regression fits a straight line, but kNN can take non-linear shapes. Moreover, it is possible to extend linear regression to polynomial regression by using scikit-learn's `PolynomialFeatures`, which lets you fit a slope for your features raised to the power of `n`, where `n=1,2,3,4` in our example.


With Plotly, it's easy to display latex equations in legend and titles by simply adding `$` before and after your equation. This way, you can see the coefficients that our polynomial regression fitted.
<!-- #endregion -->

```python
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def format_coefs(coefs):
    equation_list = [f"{coef}x^{i}" for i, coef in enumerate(coefs)]
    equation = "$" +  " + ".join(equation_list) + "$"

    replace_map = {"x^0": "", "x^1": "x", '+ -': '- '}
    for old, new in replace_map.items():
        equation = equation.replace(old, new)

    return equation

df = px.data.tips()
X = df.total_bill.values.reshape(-1, 1)
x_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)

fig = px.scatter(df, x='total_bill', y='tip', opacity=0.65)
for degree in [1, 2, 3, 4]:
    poly = PolynomialFeatures(degree)
    poly.fit(X)
    X_poly = poly.transform(X)
    x_range_poly = poly.transform(x_range)

    model = LinearRegression(fit_intercept=False)
    model.fit(X_poly, df.tip)
    y_poly = model.predict(x_range_poly)

    equation = format_coefs(model.coef_.round(2))
    fig.add_traces(go.Scatter(x=x_range.squeeze(), y=y_poly, name=equation))

fig.show()
```

## 3D regression surface with `px.scatter_3d` and `go.Surface`

Visualize the decision plane of your model whenever you have more than one variable in your input data. Here, we will use [`sklearn.svm.SVR`](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html), which is a Support Vector Machine (SVM) model specifically designed for regression.

```python
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.svm import SVR

mesh_size = .02
margin = 0

df = px.data.iris()

X = df[['sepal_width', 'sepal_length']]
y = df['petal_width']

# Condition the model on sepal width and length, predict the petal width
model = SVR(C=1.)
model.fit(X, y)

# Create a mesh grid on which we will run our model
x_min, x_max = X.sepal_width.min() - margin, X.sepal_width.max() + margin
y_min, y_max = X.sepal_length.min() - margin, X.sepal_length.max() + margin
xrange = np.arange(x_min, x_max, mesh_size)
yrange = np.arange(y_min, y_max, mesh_size)
xx, yy = np.meshgrid(xrange, yrange)

# Run model
pred = model.predict(np.c_[xx.ravel(), yy.ravel()])
pred = pred.reshape(xx.shape)

# Generate the plot
fig = px.scatter_3d(df, x='sepal_width', y='sepal_length', z='petal_width')
fig.update_traces(marker=dict(size=5))
fig.add_traces(go.Surface(x=xrange, y=yrange, z=pred, name='pred_surface'))
fig.show()
```

## Visualizing coefficients for multiple linear regression (MLR)

Visualizing regression with one or two variables is straightforward, since we can respectively plot them with scatter plots and 3D scatter plots. Moreover, if you have more than 2 features, you will need to find alternative ways to visualize your data.

One way is to use [bar charts](https://plotly.com/python/bar-charts/). In our example, each bar indicates the coefficients of our linear regression model for each input feature. Our model was trained on the [Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris).

```python
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

df = px.data.iris()

X = df.drop(columns=['petal_width', 'species_id'])
X = pd.get_dummies(X, columns=['species'], prefix_sep='=')
y = df['petal_width']

model = LinearRegression()
model.fit(X, y)

colors = ['Positive' if c > 0 else 'Negative' for c in model.coef_]

fig = px.bar(
    x=X.columns, y=model.coef_, color=colors,
    color_discrete_sequence=['red', 'blue'],
    labels=dict(x='Feature', y='Linear coefficient'),
    title='Weight of each feature for predicting petal width'
)
fig.show()
```

## Prediction Error Plots

When you are working with very high-dimensional data, it is inconvenient to plot every dimension with your output `y`. Instead, you can use methods such as prediction error plots, which let you visualize how well your model does compared to the ground truth.


### Simple actual vs predicted plot

This example shows you the simplest way to compare the predicted output vs. the actual output. A good model will have most of the scatter dots near the diagonal black line.

```python
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

df = px.data.iris()
X = df[['sepal_width', 'sepal_length']]
y = df['petal_width']

# Condition the model on sepal width and length, predict the petal width
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

fig = px.scatter(x=y, y=y_pred, labels={'x': 'ground truth', 'y': 'prediction'})
fig.add_shape(
    type="line", line=dict(dash='dash'),
    x0=y.min(), y0=y.min(),
    x1=y.max(), y1=y.max()
)
fig.show()
```

### Enhanced prediction error analysis using `plotly.express`

Add marginal histograms to quickly diagnoses any prediction bias your model might have. The built-in `OLS` functionality let you visualize how well your model generalizes by comparing it with the theoretical optimal fit (black dotted line).

```python
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = px.data.iris()

# Split data into training and test splits
train_idx, test_idx = train_test_split(df.index, test_size=.25, random_state=0)
df['split'] = 'train'
df.loc[test_idx, 'split'] = 'test'

X = df[['sepal_width', 'sepal_length']]
y = df['petal_width']
X_train = df.loc[train_idx, ['sepal_width', 'sepal_length']]
y_train = df.loc[train_idx, 'petal_width']

# Condition the model on sepal width and length, predict the petal width
model = LinearRegression()
model.fit(X_train, y_train)
df['prediction'] = model.predict(X)

fig = px.scatter(
    df, x='petal_width', y='prediction',
    marginal_x='histogram', marginal_y='histogram',
    color='split', trendline='ols'
)
fig.update_traces(histnorm='probability', selector={'type':'histogram'})
fig.add_shape(
    type="line", line=dict(dash='dash'),
    x0=y.min(), y0=y.min(),
    x1=y.max(), y1=y.max()
)

fig.show()
```

## Residual plots

Just like prediction error plots, it's easy to visualize your prediction residuals in just a few lines of codes using `plotly.express` built-in capabilities.

```python
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = px.data.iris()

# Split data into training and test splits
train_idx, test_idx = train_test_split(df.index, test_size=.25, random_state=0)
df['split'] = 'train'
df.loc[test_idx, 'split'] = 'test'

X = df[['sepal_width', 'sepal_length']]
X_train = df.loc[train_idx, ['sepal_width', 'sepal_length']]
y_train = df.loc[train_idx, 'petal_width']

# Condition the model on sepal width and length, predict the petal width
model = LinearRegression()
model.fit(X_train, y_train)
df['prediction'] = model.predict(X)
df['residual'] = df['prediction'] - df['petal_width']

fig = px.scatter(
    df, x='prediction', y='residual',
    marginal_y='violin',
    color='split', trendline='ols'
)
fig.show()
```

## Visualize regularization across cross-validation folds


In this example, we show how to plot the results of various $\alpha$ penalization values from the results of cross-validation using scikit-learn's `LassoCV`. This is useful to see how much the error of the optimal alpha actually varies across CV folds.

```python
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LassoCV

N_FOLD = 6

# Load and preprocess the data
df = px.data.gapminder()
X = df.drop(columns=['lifeExp', 'iso_num'])
X = pd.get_dummies(X, columns=['country', 'continent', 'iso_alpha'])
y = df['lifeExp']

# Train model to predict life expectancy
model = LassoCV(cv=N_FOLD, normalize=True)
model.fit(X, y)
mean_alphas = model.mse_path_.mean(axis=-1)

fig = go.Figure([
    go.Scatter(
        x=model.alphas_, y=model.mse_path_[:, i],
        name=f"Fold: {i+1}", opacity=.5, line=dict(dash='dash'),
        hovertemplate="alpha: %{x} <br>MSE: %{y}"
    )
    for i in range(N_FOLD)
])
fig.add_traces(go.Scatter(
    x=model.alphas_, y=mean_alphas,
    name='Mean', line=dict(color='black', width=3),
    hovertemplate="alpha: %{x} <br>MSE: %{y}",
))

fig.add_shape(
    type="line", line=dict(dash='dash'),
    x0=model.alpha_, y0=0,
    x1=model.alpha_, y1=1,
    yref='paper'
)

fig.update_layout(
    xaxis_title='alpha',
    xaxis_type="log",
    yaxis_title="Mean Square Error (MSE)"
)
fig.show()
```

## Grid search visualization using `px.density_heatmap` and `px.box`

In this example, we show how to visualize the results of a grid search on a `DecisionTreeRegressor`. The first plot shows how to visualize the score of each model parameter on individual splits (grouped using facets). The second plot aggregates the results of all splits such that each box represents a single model.

```python
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor

N_FOLD = 6

# Load and shuffle dataframe
df = px.data.iris()
df = df.sample(frac=1, random_state=0)

X = df[['sepal_width', 'sepal_length']]
y = df['petal_width']

# Define and fit the grid
model = DecisionTreeRegressor()
param_grid = {
    'criterion': ['mse', 'friedman_mse', 'mae'],
    'max_depth': range(2, 5)
}
grid = GridSearchCV(model, param_grid, cv=N_FOLD)
grid.fit(X, y)
grid_df = pd.DataFrame(grid.cv_results_)

# Convert the wide format of the grid into the long format
# accepted by plotly.express
melted = (
    grid_df
    .rename(columns=lambda col: col.replace('param_', ''))
    .melt(
        value_vars=[f'split{i}_test_score' for i in range(N_FOLD)],
        id_vars=['mean_test_score', 'mean_fit_time', 'criterion', 'max_depth'],
        var_name="cv_split",
        value_name="r_squared"
    )
)

# Format the variable names for simplicity
melted['cv_split'] = (
    melted['cv_split']
    .str.replace('_test_score', '')
    .str.replace('split', '')
)

# Single function call to plot each figure
fig_hmap = px.density_heatmap(
    melted, x="max_depth", y='criterion',
    histfunc="sum", z="r_squared",
    title='Grid search results on individual fold',
    hover_data=['mean_fit_time'],
    facet_col="cv_split", facet_col_wrap=3,
    labels={'mean_test_score': "mean_r_squared"}
)

fig_box = px.box(
    melted, x='max_depth', y='r_squared',
    title='Grid search results ',
    hover_data=['mean_fit_time'],
    points='all',
    color="criterion",
    hover_name='cv_split',
    labels={'mean_test_score': "mean_r_squared"}
)

# Display
fig_hmap.show()
fig_box.show()
```

### Reference

Learn more about the `px` figures used in this tutorial:
* Plotly Express: https://plot.ly/python/plotly-express/
* Vertical Lines: https://plot.ly/python/shapes/
* Heatmaps: https://plot.ly/python/heatmaps/
* Box Plots: https://plot.ly/python/box-plots/
* 3D Scatter: https://plot.ly/python/3d-scatter-plots/
* Surface Plots: https://plot.ly/python/3d-surface-plots/

Learn more about the Machine Learning models used in this tutorial:
* https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
* https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html
* https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsRegressor.html
* https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html
* https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html

Other tutorials that inspired this notebook:
* https://seaborn.pydata.org/examples/residplot.html
* https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html
* http://www.scikit-yb.org/zh/latest/api/regressor/peplot.html
