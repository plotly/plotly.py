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
    description: Visualize scikit-learn's t-SNE and UMAP in Python with Plotly.
    display_as: ai_ml
    language: python
    layout: base
    name: t-SNE and UMAP projections
    order: 6
    page_type: u-guide
    permalink: python/t-sne-and-umap-projections/
    thumbnail: thumbnail/tsne-umap-projections.png
---

This page presents various ways to visualize two popular dimensionality reduction techniques, namely the [t-distributed stochastic neighbor embedding](https://lvdmaaten.github.io/tsne/) (t-SNE) and [Uniform Manifold Approximation and Projection](https://umap-learn.readthedocs.io/en/latest/index.html) (UMAP). They are needed whenever you want to visualize data with more than two or three features (i.e. dimensions).

We first show how to visualize data with more than three features using the [scatter plot matrix](https://medium.com/plotly/what-is-a-splom-chart-make-scatterplot-matrices-in-python-8dc4998921c3), then we apply dimensionality reduction techniques to get 2D/3D representation of our data, and visualize the results with [scatter plots](https://plotly.com/python/line-and-scatter/) and [3D scatter plots](https://plotly.com/python/3d-scatter-plots/).


## Basic t-SNE projections

t-SNE is a popular dimensionality reduction algorithm that arises from probability theory. Simply put, it projects the high-dimensional data points (sometimes with hundreds of features) into 2D/3D by inducing the projected data to have a similar distribution as the original data points by minimizing something called the [KL divergence](https://towardsdatascience.com/light-on-math-machine-learning-intuitive-guide-to-understanding-kl-divergence-2b382ca2b2a8).

Compared to a method like Principal Component Analysis (PCA), it takes significantly more time to converge, but present significantly better insights when visualized. For example, by projecting features of a flowers, it will be able to distinctly group


### Visualizing high-dimensional data with `px.scatter_matrix`

First, let's try to visualize every feature of the [Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris), and color everything by the species. We will use the Scatter Plot Matrix ([splom](https://plotly.com/python/splom/)), which lets us plot each feature against everything else, which is convenient when your dataset has more than 3 dimensions.

```python
import plotly.express as px

df = px.data.iris()
features = ["sepal_width", "sepal_length", "petal_width", "petal_length"]
fig = px.scatter_matrix(df, dimensions=features, color="species")
fig.show()
```

### Project data into 2D with t-SNE and `px.scatter`

Now, let's use the t-SNE algorithm to project the data shown above into two dimensions. Notice how each of the species is physically separate from each other.

```python
from sklearn.manifold import TSNE
import plotly.express as px

df = px.data.iris()

features = df.loc[:, :'petal_width']

tsne = TSNE(n_components=2, random_state=0)
projections = tsne.fit_transform(features)

fig = px.scatter(
    projections, x=0, y=1,
    color=df.species, labels={'color': 'species'}
)
fig.show()
```

### Project data into 3D with t-SNE and `px.scatter_3d`

t-SNE can reduce your data to any number of dimensions you want! Here, we show you how to project it to 3D and visualize with a 3D scatter plot.

```python
from sklearn.manifold import TSNE
import plotly.express as px

df = px.data.iris()

features = df.loc[:, :'petal_width']

tsne = TSNE(n_components=3, random_state=0)
projections = tsne.fit_transform(features, )

fig = px.scatter_3d(
    projections, x=0, y=1, z=2,
    color=df.species, labels={'color': 'species'}
)
fig.update_traces(marker_size=8)
fig.show()
```

## Projections with UMAP

Just like t-SNE, [UMAP](https://umap-learn.readthedocs.io/en/latest/index.html) is a dimensionality reduction specifically designed for visualizing complex data in low dimensions (2D or 3D). As the number of data points increase, [UMAP becomes more time efficient](https://umap-learn.readthedocs.io/en/latest/benchmarking.html) compared to TSNE.

In the example below, we see how easy it is to use UMAP as a drop-in replacement for scikit-learn's `manifold.TSNE`.

```python
from umap import UMAP
import plotly.express as px

df = px.data.iris()

features = df.loc[:, :'petal_width']

umap_2d = UMAP(n_components=2, init='random', random_state=0)
umap_3d = UMAP(n_components=3, init='random', random_state=0)

proj_2d = umap_2d.fit_transform(features)
proj_3d = umap_3d.fit_transform(features)

fig_2d = px.scatter(
    proj_2d, x=0, y=1,
    color=df.species, labels={'color': 'species'}
)
fig_3d = px.scatter_3d(
    proj_3d, x=0, y=1, z=2,
    color=df.species, labels={'color': 'species'}
)
fig_3d.update_traces(marker_size=5)

fig_2d.show()
fig_3d.show()
```

## Visualizing image datasets

In the following example, we show how to visualize large image datasets using UMAP. Here, we use [`load_digits`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html), a subset of the famous [MNIST dataset](http://yann.lecun.com/exdb/mnist/) that was downsized to 8x8 and flattened to 64 dimensions.

Although there's over 1000 data points, and many more dimensions than the previous example, it is still extremely fast. This is because UMAP is optimized for speed, both from a theoretical perspective, and in the way it is implemented. Learn more in [this comparison post](https://umap-learn.readthedocs.io/en/latest/benchmarking.html).

```python
import plotly.express as px
from sklearn.datasets import load_digits
from umap import UMAP

digits = load_digits()

umap_2d = UMAP(random_state=0)
umap_2d.fit(digits.data)

projections = umap_2d.transform(digits.data)

fig = px.scatter(
    projections, x=0, y=1,
    color=digits.target.astype(str), labels={'color': 'digit'}
)
fig.show()
```

<!-- #region -->
## Reference

Plotly figures:
* https://plotly.com/python/line-and-scatter/
* https://plotly.com/python/3d-scatter-plots/
* https://plotly.com/python/splom/


Details about algorithms:
* UMAP library: https://umap-learn.readthedocs.io/en/latest/
* t-SNE User guide: https://scikit-learn.org/stable/modules/manifold.html#t-sne
* t-SNE paper: https://www.jmlr.org/papers/volume9/vandermaaten08a/vandermaaten08a.pdf
* MNIST: http://yann.lecun.com/exdb/mnist/
<!-- #endregion -->
