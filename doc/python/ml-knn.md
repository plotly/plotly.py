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
    description: Visualize scikit-learn's k-Nearest Neighbors (kNN) classification
      in Python with Plotly.
    display_as: ai_ml
    language: python
    layout: base
    name: kNN Classification
    order: 2
    page_type: u-guide
    permalink: python/knn-classification/
    thumbnail: thumbnail/knn-classification.png
---

## Basic binary classification with kNN

This section gets us started with displaying basic binary classification using 2D data. We first show how to display training versus testing data using [various marker styles](https://plot.ly/python/marker-style/), then demonstrate how to evaluate our classifier's performance on the **test split** using a continuous color gradient to indicate the model's predicted score.

We will use [Scikit-learn](https://scikit-learn.org/) for training our model and for loading and splitting data. Scikit-learn is a popular Machine Learning (ML) library that offers various tools for creating and training ML algorithms, feature engineering, data cleaning, and evaluating and testing models. It was designed to be accessible, and to work seamlessly with popular libraries like NumPy and Pandas.

We will train a [k-Nearest Neighbors (kNN)](https://scikit-learn.org/stable/modules/neighbors.html) classifier. First, the model records the label of each training sample. Then, whenever we give it a new sample, it will look at the `k` closest samples from the training set to find the most common label, and assign it to our new sample.


### Display training and test splits

Using Scikit-learn, we first generate synthetic data that form the shape of a moon. We then split it into a training and testing set. Finally, we display the ground truth labels using [a scatter plot](https://plotly.com/python/line-and-scatter/).

In the graph, we display all the negative labels as squares, and positive labels as circles. We differentiate the training and test set by adding a dot to the center of test data.

In this example, we will use [graph objects](/python/graph-objects/), Plotly's low-level API for building figures.

```python
import plotly.graph_objects as go
import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load and split data
X, y = make_moons(noise=0.3, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(
    X, y.astype(str), test_size=0.25, random_state=0)

trace_specs = [
    [X_train, y_train, '0', 'Train', 'square'],
    [X_train, y_train, '1', 'Train', 'circle'],
    [X_test, y_test, '0', 'Test', 'square-dot'],
    [X_test, y_test, '1', 'Test', 'circle-dot']
]

fig = go.Figure(data=[
    go.Scatter(
        x=X[y==label, 0], y=X[y==label, 1],
        name=f'{split} Split, Label {label}',
        mode='markers', marker_symbol=marker
    )
    for X, y, label, split, marker in trace_specs
])
fig.update_traces(
    marker_size=12, marker_line_width=1.5,
    marker_color="lightyellow"
)
fig.show()
```

### Visualize predictions on test split with [`plotly.express`](https://plotly.com/python/plotly-express/)


Now, we train the kNN model on the same training data displayed in the previous graph. Then, we predict the confidence score of the model for each of the data points in the test set. We will use shapes to denote the true labels, and the color will indicate the confidence of the model for assign that score.

In this example, we will use [Plotly Express](/python/plotly-express/), Plotly's high-level API for building figures. Notice that `px.scatter` only require 1 function call to plot both negative and positive labels, and can additionally set a continuous color scale based on the `y_score` output by our kNN model.

```python
import plotly.express as px
import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load and split data
X, y = make_moons(noise=0.3, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(
    X, y.astype(str), test_size=0.25, random_state=0)

# Fit the model on training data, predict on test data
clf = KNeighborsClassifier(15)
clf.fit(X_train, y_train)
y_score = clf.predict_proba(X_test)[:, 1]

fig = px.scatter(
    X_test, x=0, y=1,
    color=y_score, color_continuous_scale='RdBu',
    symbol=y_test, symbol_map={'0': 'square-dot', '1': 'circle-dot'},
    labels={'symbol': 'label', 'color': 'score of <br>first class'}
)
fig.update_traces(marker_size=12, marker_line_width=1.5)
fig.update_layout(legend_orientation='h')
fig.show()
```

## Probability Estimates with `go.Contour`

Just like the previous example, we will first train our kNN model on the training set.

Instead of predicting the conference for the test set, we can predict the confidence map for the entire area that wraps around the dimensions of our dataset. To do this, we use [`np.meshgrid`](https://numpy.org/doc/stable/reference/generated/numpy.meshgrid.html) to create a grid, where the distance between each point is denoted by the `mesh_size` variable.

Then, for each of those points, we will use our model to give a confidence score, and plot it with a [contour plot](https://plotly.com/python/contour-plots/).

In this example, we will use [graph objects](/python/graph-objects/), Plotly's low-level API for building figures.

```python
import plotly.graph_objects as go
import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

mesh_size = .02
margin = 0.25

# Load and split data
X, y = make_moons(noise=0.3, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(
    X, y.astype(str), test_size=0.25, random_state=0)

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


# Plot the figure
fig = go.Figure(data=[
    go.Contour(
        x=xrange,
        y=yrange,
        z=Z,
        colorscale='RdBu'
    )
])
fig.show()
```

Now, let's try to combine our `go.Contour` plot with the first scatter plot of our data points, so that we can visually compare the confidence of our model with the true labels.

```python
import plotly.graph_objects as go
import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

mesh_size = .02
margin = 0.25

# Load and split data
X, y = make_moons(noise=0.3, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(
    X, y.astype(str), test_size=0.25, random_state=0)

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

trace_specs = [
    [X_train, y_train, '0', 'Train', 'square'],
    [X_train, y_train, '1', 'Train', 'circle'],
    [X_test, y_test, '0', 'Test', 'square-dot'],
    [X_test, y_test, '1', 'Test', 'circle-dot']
]

fig = go.Figure(data=[
    go.Scatter(
        x=X[y==label, 0], y=X[y==label, 1],
        name=f'{split} Split, Label {label}',
        mode='markers', marker_symbol=marker
    )
    for X, y, label, split, marker in trace_specs
])
fig.update_traces(
    marker_size=12, marker_line_width=1.5,
    marker_color="lightyellow"
)

fig.add_trace(
    go.Contour(
        x=xrange,
        y=yrange,
        z=Z,
        showscale=False,
        colorscale='RdBu',
        opacity=0.4,
        name='Score',
        hoverinfo='skip'
    )
)
fig.show()
```

## k-NN classification in Dash

[Dash](https://plotly.com/dash/) is the best way to build analytical apps in Python using Plotly figures. To run the app below, run `pip install dash`, click "Download" to get the code and run `python app.py`.

Get started  with [the official Dash docs](https://dash.plotly.com/installation) and **learn how to effortlessly [style](https://plotly.com/dash/design-kit/) & [deploy](https://plotly.com/dash/app-manager/) apps like this with <a class="plotly-red" href="https://plotly.com/dash/">Dash Enterprise</a>.**


```python hide_code=true
from IPython.display import IFrame
snippet_url = 'https://dash-gallery.plotly.host/python-docs-dash-snippets/'
IFrame(snippet_url + 'knn-classification', width='100%', height=630)
```

## Multi-class prediction confidence with [`go.Heatmap`](https://plotly.com/python/heatmaps/)

It is also possible to visualize the prediction confidence of the model using [heatmaps](https://plotly.com/python/heatmaps/). In this example, you can see how to compute how confident the model is about its prediction at every point in the 2D grid. Here, we define the confidence as the difference between the highest score and the score of the other classes summed, at a certain point.

In this example, we will use [Plotly Express](/python/plotly-express/), Plotly's high-level API for building figures.

```python
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

mesh_size = .02
margin = 1

# We will use the iris data, which is included in px
df = px.data.iris()
df_train, df_test = train_test_split(df, test_size=0.25, random_state=0)
X_train = df_train[['sepal_length', 'sepal_width']]
y_train = df_train.species_id

# Create a mesh grid on which we will run our model
l_min, l_max = df.sepal_length.min() - margin, df.sepal_length.max() + margin
w_min, w_max = df.sepal_width.min() - margin, df.sepal_width.max() + margin
lrange = np.arange(l_min, l_max, mesh_size)
wrange = np.arange(w_min, w_max, mesh_size)
ll, ww = np.meshgrid(lrange, wrange)

# Create classifier, run predictions on grid
clf = KNeighborsClassifier(15, weights='distance')
clf.fit(X_train, y_train)
Z = clf.predict(np.c_[ll.ravel(), ww.ravel()])
Z = Z.reshape(ll.shape)
proba = clf.predict_proba(np.c_[ll.ravel(), ww.ravel()])
proba = proba.reshape(ll.shape + (3,))

# Compute the confidence, which is the difference
diff = proba.max(axis=-1) - (proba.sum(axis=-1) - proba.max(axis=-1))

fig = px.scatter(
    df_test, x='sepal_length', y='sepal_width',
    symbol='species',
    symbol_map={
        'setosa': 'square-dot',
        'versicolor': 'circle-dot',
        'virginica': 'diamond-dot'},
)
fig.update_traces(
    marker_size=12, marker_line_width=1.5,
    marker_color="lightyellow"
)
fig.add_trace(
    go.Heatmap(
        x=lrange,
        y=wrange,
        z=diff,
        opacity=0.25,
        customdata=proba,
        colorscale='RdBu',
        hovertemplate=(
            'sepal length: %{x} <br>'
            'sepal width: %{y} <br>'
            'p(setosa): %{customdata[0]:.3f}<br>'
            'p(versicolor): %{customdata[1]:.3f}<br>'
            'p(virginica): %{customdata[2]:.3f}<extra></extra>'
        )
    )
)
fig.update_layout(
    legend_orientation='h',
    title='Prediction Confidence on Test Split'
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
