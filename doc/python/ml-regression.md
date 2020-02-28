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
    description: Visualize regression in scikit-learn with Plotly
    display_as: ai_ml
    language: python
    layout: base
    name: ML Regression
    order: 2
    page_type: example_index
    permalink: python/ml-regression/
    thumbnail: thumbnail/knn-classification.png
---

## Basic linear regression

This example shows how to train a simple linear regression from `sklearn` to predicts the tips servers will receive based on the value of the total bill (dataset is included in `px.data`).

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

## Model generalization on unseen data

```python
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = px.data.tips()
X = df.total_bill.values.reshape(-1, 1)
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

```python
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.neighbors import KNeighborsRegressor

df = px.data.tips()
X = df.total_bill.values.reshape(-1, 1)

knn_dist = KNeighborsRegressor(10, weights='distance')
knn_uni = KNeighborsRegressor(10, weights='uniform')
knn_dist.fit(X, df.tip)
knn_uni.fit(X, df.tip)

x_range = np.linspace(X.min(), X.max(), 100)
y_dist = knn_dist.predict(x_range.reshape(-1, 1))
y_uni = knn_uni.predict(x_range.reshape(-1, 1))

fig = px.scatter(df, x='total_bill', y='tip', color='sex', opacity=0.65)
fig.add_traces(go.Scatter(x=x_range, y=y_uni, name='Weights: Uniform'))
fig.add_traces(go.Scatter(x=x_range, y=y_dist, name='Weights: Distance'))
fig.show()
```

## 3D regression surface with `px.scatter_3d` and `go.Surface`

```python
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.neighbors import KNeighborsRegressor

mesh_size = .02
margin = 0

df = px.data.iris()
features = ["sepal_width", "sepal_length", "petal_width"]

X = df[['sepal_width', 'sepal_length']]
y = df['petal_width']

# Condition the model on sepal width and length, predict the petal width
knn = KNeighborsRegressor(10, weights='distance')
knn.fit(X, y)

# Create a mesh grid on which we will run our model
x_min, x_max = X.sepal_width.min() - margin, X.sepal_width.max() + margin
y_min, y_max = X.sepal_length.min() - margin, X.sepal_length.max() + margin
xrange = np.arange(x_min, x_max, mesh_size)
yrange = np.arange(y_min, y_max, mesh_size)
xx, yy = np.meshgrid(xrange, yrange)

# Run kNN
pred = knn.predict(np.c_[xx.ravel(), yy.ravel()])
pred = pred.reshape(xx.shape)

# Generate the plot
fig = px.scatter_3d(df, x='sepal_width', y='sepal_length', z='petal_width')
fig.update_traces(marker=dict(size=5))
fig.add_traces(go.Surface(x=xrange, y=yrange, z=pred, name='pred_surface'))
fig.show()
```

## Label polynomial fits with latex

```python

```

## Prediction Error Plots


### Simple Prediction Error

```python

```

### Augmented Prediction Error plot using `px`

```python

```

### Grid Search Visualization using `px.scatter_matrix`


## Residual Plots

```python

```

### Reference

Learn more about `px` here:
* https://plot.ly/python/plotly-express/

This tutorial was inspired by amazing examples from the official scikit-learn docs:
* https://scikit-learn.org/stable/auto_examples/neighbors/plot_regression.html
