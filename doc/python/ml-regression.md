# Regression


### Visualizing kNN Regression

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

### Reference

Learn more about `px` here:
* https://plot.ly/python/plotly-express/

This tutorial was inspired by amazing examples from the official scikit-learn docs:
* https://scikit-learn.org/stable/auto_examples/neighbors/plot_regression.html
