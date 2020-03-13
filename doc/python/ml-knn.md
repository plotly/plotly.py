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
    description: Visualize scikit-learn's k-Nearest Neighbors (kNN) classification
      with Plotly
    display_as: ai_ml
    language: python
    layout: base
    name: kNN Classification
    order: 1
    page_type: example_index
    permalink: python/knn-classification/
    thumbnail: thumbnail/knn-classification.png
---

## Basic binary classification with kNN


### Display training and test splits

```python

```

### Visualize predictions on test split

```python

```

```python
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.datasets import make_moons
from sklearn.neighbors import KNeighborsClassifier

X, y = make_moons(noise=0.3, random_state=0)
X_test, _ = make_moons(noise=0.3, random_state=1)

clf = KNeighborsClassifier(15)
clf.fit(X, y.astype(str))  # Fit on training set
y_pred = clf.predict(X_test)  # Predict on new data

fig = px.scatter(x=X_test[:, 0], y=X_test[:, 1], color=y_pred, labels={'color': 'predicted'})
fig.update_traces(marker_size=10)
fig.show()
```

## Visualize Binary Prediction Scores

```python
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsClassifier

X, y = make_classification(n_features=2, n_redundant=0, random_state=0)
X_test, _ = make_classification(n_features=2, n_redundant=0, random_state=1)

clf = KNeighborsClassifier(15)
clf.fit(X, y)  # Fit on training set
y_score = clf.predict_proba(X_test)[:, 1]  # Predict on new data

fig = px.scatter(x=X_test[:, 0], y=X_test[:, 1], color=y_score, labels={'color': 'score'})
fig.update_traces(marker_size=10)
fig.show()
```

## Probability Estimates with `go.Contour`

```python
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.datasets import make_moons
from sklearn.neighbors import KNeighborsClassifier

mesh_size = .02
margin = 1

X, y = make_moons(noise=0.3, random_state=0)

# Create a mesh grid on which we will run our model
x_min, x_max = X[:, 0].min() - margin, X[:, 0].max() + margin
y_min, y_max = X[:, 1].min() - margin, X[:, 1].max() + margin
xrange = np.arange(x_min, x_max, mesh_size)
yrange = np.arange(y_min, y_max, mesh_size)
xx, yy = np.meshgrid(xrange, yrange)

# Create classifier, run predictions on grid
clf = KNeighborsClassifier(15, weights='uniform')
clf.fit(X, y)
Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
Z = Z.reshape(xx.shape)

fig = px.scatter(X, x=0, y=1, color=y.astype(str), labels={'0':'', '1':''})
fig.update_traces(marker_size=10, marker_line_width=1)
fig.add_trace(
    go.Contour(
        x=xrange, 
        y=yrange, 
        z=Z, 
        showscale=False,
        colorscale=['Blue', 'Red'],
        opacity=0.4,
        name='Score'
    )
)
fig.show()
```

## Multi-class prediction confidence with `go.Heatmap`

```python
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.neighbors import KNeighborsClassifier

mesh_size = .02
margin = 1

# We will use the iris data, which is included in px
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
proba = clf.predict_proba(np.c_[ll.ravel(), ww.ravel()])
proba = proba.reshape(ll.shape + (3,))

fig = px.scatter(df, x='sepal_length', y='sepal_width', color='species')
fig.update_traces(marker_size=10, marker_line_width=1)
fig.add_trace(
    go.Heatmap(
        x=lrange, 
        y=wrange, 
        z=Z, 
        showscale=False,
        colorscale=[[0.0, 'blue'], [0.5, 'red'], [1.0, 'green']],
        opacity=0.25,
        customdata=proba,
        hovertemplate=(
            'sepal length: %{x} <br>'
            'sepal width: %{y} <br>'
            'p(setosa): %{customdata[0]:.3f}<br>'
            'p(versicolor): %{customdata[1]:.3f}<br>'
            'p(virginica): %{customdata[2]:.3f}<extra></extra>'
        )
    )
)
fig.show()
```

### Reference

Learn more about `px`, `go.Contour`, and `go.Heatmap` here:
* https://plot.ly/python/plotly-express/
* https://plot.ly/python/heatmaps/
* https://plot.ly/python/contour-plots/

This tutorial was inspired by amazing examples from the official scikit-learn docs:
* https://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html
* https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html
* https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
