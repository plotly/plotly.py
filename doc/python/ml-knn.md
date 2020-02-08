## K-Nearest Neighbors (kNN)

How to visualize the K-Nearest Neighbors (kNN) algorithm using scikit-learn.


### Binary Probability Estimates with `go.Contour`

```python
import numpy as np
from sklearn.datasets import make_moons
from sklearn.neighbors import KNeighborsClassifier
import plotly.express as px
import plotly.graph_objects as go

X, y = make_moons(noise=0.3, random_state=0)

# Create a mesh grid on which we will run our model
x_min, x_max = X[:, 0].min() - margin, X[:, 0].max() + margin
y_min, y_max = X[:, 1].min() - margin, X[:, 1].max() + margin
xrange = np.arange(x_min, x_max, mesh_size)
yrange = np.arange(y_min, y_max, mesh_size)
xx, yy = np.meshgrid(xrange, yrange)

# Create classifier, run predictions on grid
clf = neighbors.KNeighborsClassifier(15, weights='uniform')
clf.fit(X, y)
Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
Z = Z.reshape(xx.shape)

fig = px.scatter(X, x=0, y=1, color=y.astype(str))
fig.add_trace(
    go.Contour(
        x=xrange, 
        y=yrange, 
        z=Z, 
        showscale=False,
        colorscale=['Blue', 'Red'],
        opacity=0.4
    )
)
```

### Multi-class classification with `px.data` and `go.Heatmap`

```python
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import plotly.express as px
import plotly.graph_objects as go

mesh_size = .02
margin = 1

df = px.data.iris()
X = df[['sepal_length', 'sepal_width']]
y = df.species_id

# Create a mesh grid on which we will run our model
l_min, l_max = df.sepal_length.min() - margin, df.sepal_length.max() + margin
w_min, w_max = df.sepal_width.min() - margin, df.sepal_width.max() + margin
lrange = np.arange(l_min, l_max, mesh_size)
wrange = np.arange(w_min, w_max, mesh_size)
ll, ww = np.meshgrid(lrange, wrange)

# Create classifier, run predictions on grid
clf = KNeighborsClassifier(15, weights='distance')
clf.fit(X, y)
Z = clf.predict(np.c_[ll.ravel(), ww.ravel()])
Z = Z.reshape(ll.shape)

fig = px.scatter(df, x='sepal_length', y='sepal_width', color='species')
fig.update_traces(marker_size=10, marker_line_width=1)
fig.add_trace(
    go.Heatmap(
        x=lrange, 
        y=wrange, 
        z=Z, 
        showscale=False,
        colorscale=[[0.0, 'blue'], [0.5, 'red'], [1.0, 'green']],
        opacity=0.25
    )
)
```

### Visualizing kNN Regression

```python
from sklearn.neighbors import KNeighborsRegressor
import plotly.express as px
import plotly.graph_objects as go

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
```

### Reference

Learn more about `px`, `go.Contour`, and `go.Heatmap` here:
* https://plot.ly/python/plotly-express/
* https://plot.ly/python/heatmaps/
* https://plot.ly/python/contour-plots/

This tutorial was inspired by amazing examples from the official scikit-learn docs:
* https://scikit-learn.org/stable/auto_examples/neighbors/plot_regression.html
* https://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html
* https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html
