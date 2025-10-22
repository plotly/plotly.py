---
description: Visualize Principle Component Analysis (PCA) of your high-dimensional
  data in Python with Plotly.
---
This page first shows how to visualize higher dimension data using various Plotly figures combined with dimensionality reduction (aka projection). Then, we dive into the specific details of our projection algorithm.

We will use [Scikit-learn](https://scikit-learn.org/) to load one of the datasets, and apply dimensionality reduction. Scikit-learn is a popular Machine Learning (ML) library that offers various tools for creating and training ML algorithms, feature engineering, data cleaning, and evaluating and testing models. It was designed to be accessible, and to work seamlessly with popular libraries like NumPy and Pandas.


## High-dimensional PCA Analysis with  `px.scatter_matrix`

The dimensionality reduction technique we will be using is called the [Principal Component Analysis (PCA)](https://scikit-learn.org/stable/modules/decomposition.html#pca). It is a powerful technique that arises from linear algebra and probability theory. In essence, it computes a matrix that represents the variation of your data ([covariance matrix/eigenvectors][covmatrix]), and rank them by their relevance (explained variance/eigenvalues). For a video tutorial, see [this segment on PCA](https://youtu.be/rng04VJxUt4?t=98) from the Coursera ML course.

[covmatrix]: https://stats.stackexchange.com/questions/2691/making-sense-of-principal-component-analysis-eigenvectors-eigenvalues#:~:text=As%20it%20is%20a%20square%20symmetric%20matrix%2C%20it%20can%20be%20diagonalized%20by%20choosing%20a%20new%20orthogonal%20coordinate%20system%2C%20given%20by%20its%20eigenvectors%20(incidentally%2C%20this%20is%20called%20spectral%20theorem)%3B%20corresponding%20eigenvalues%20will%20then%20be%20located%20on%20the%20diagonal.%20In%20this%20new%20coordinate%20system%2C%20the%20covariance%20matrix%20is%20diagonal%20and%20looks%20like%20that%3A


### Visualize all the original dimensions

First, let's plot all the features and see how the `species` in the Iris dataset are grouped. In a [Scatter Plot Matrix (splom)](splom.md), each subplot displays a feature against another, so if we have $N$ features we have a $N \times N$ matrix.

In our example, we are plotting all 4 features from the Iris dataset, thus we can see how `sepal_width` is compared against `sepal_length`, then against `petal_width`, and so forth. Keep in mind how some pairs of features can more easily separate different species.

In this example, we will use [Plotly Express](plotly-express.md), Plotly's high-level API for building figures.

```python
import plotly.express as px

df = px.data.iris()
features = ["sepal_width", "sepal_length", "petal_width", "petal_length"]

fig = px.scatter_matrix(
    df,
    dimensions=features,
    color="species"
)
fig.update_traces(diagonal_visible=False)
fig.show()
```

###  Visualize all the principal components

Now, we apply `PCA` the same dataset, and retrieve **all** the components. We use the same `px.scatter_matrix` trace to display our results, but this time our features are the resulting *principal components*, ordered by how much variance they are able to explain.

The importance of explained variance is demonstrated in the example below. The subplot between PC3 and PC4 is clearly unable to separate each class, whereas the subplot between PC1 and PC2 shows a clear separation between each species.

In this example, we will use [Plotly Express](plotly-express.md), Plotly's high-level API for building figures.

```python
import plotly.express as px
from sklearn.decomposition import PCA

df = px.data.iris()
features = ["sepal_width", "sepal_length", "petal_width", "petal_length"]

pca = PCA()
components = pca.fit_transform(df[features])
labels = {
    str(i): f"PC {i+1} ({var:.1f}%)"
    for i, var in enumerate(pca.explained_variance_ratio_ * 100)
}

fig = px.scatter_matrix(
    components,
    labels=labels,
    dimensions=range(4),
    color=df["species"]
)
fig.update_traces(diagonal_visible=False)
fig.show()
```

### Visualize a subset of the principal components

When you will have too many features to visualize, you might be interested in only visualizing the most relevant components. Those components often capture a majority of the [explained variance](https://en.wikipedia.org/wiki/Explained_variation), which is a good way to tell if those components are sufficient for modelling this dataset.

In the example below, our dataset contains 8 features, but we only select the first 2 components.

```python
import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing(as_frame=True)
df = housing.data
n_components = 2

pca = PCA(n_components=n_components)
components = pca.fit_transform(df)

total_var = pca.explained_variance_ratio_.sum() * 100

labels = {str(i): f"PC {i+1}" for i in range(n_components)}
labels['color'] = 'Median Price'

fig = px.scatter_matrix(
    components,
    color=housing.target,
    dimensions=range(n_components),
    labels=labels,
    title=f'Total Explained Variance: {total_var:.2f}%',
)
fig.update_traces(diagonal_visible=False)
fig.show()
```


<div style="font-size: 0.9em;"><div style="width: calc(100% - 30px); box-shadow: none; border: thin solid rgb(229, 229, 229);"><div style="padding: 5px;"><div><p><strong>Sign up for Dash Club</strong> → Free cheat sheets plus updates from Chris Parmer and Adam Schroeder delivered to your inbox every two months. Includes tips and tricks, community apps, and deep dives into the Dash architecture.
<u><a href="https://go.plotly.com/dash-club?utm_source=Dash+Club+2022&utm_medium=graphing_libraries&utm_content=inline">Join now</a></u>.</p></div></div></div></div>


## 2D PCA Scatter Plot

In the previous examples, you saw how to visualize high-dimensional PCs. In this example, we show you how to simply visualize the first two principal components of a PCA, by reducing a dataset of 4 dimensions to 2D.

```python
import plotly.express as px
from sklearn.decomposition import PCA

df = px.data.iris()
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]

pca = PCA(n_components=2)
components = pca.fit_transform(X)

fig = px.scatter(components, x=0, y=1, color=df['species'])
fig.show()
```

## Visualize PCA with `px.scatter_3d`

With `px.scatter_3d`, you can visualize an additional dimension, which let you capture even more variance.

```python
import plotly.express as px
from sklearn.decomposition import PCA

df = px.data.iris()
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]

pca = PCA(n_components=3)
components = pca.fit_transform(X)

total_var = pca.explained_variance_ratio_.sum() * 100

fig = px.scatter_3d(
    components, x=0, y=1, z=2, color=df['species'],
    title=f'Total Explained Variance: {total_var:.2f}%',
    labels={'0': 'PC 1', '1': 'PC 2', '2': 'PC 3'}
)
fig.show()
```

## Plotting explained variance

Often, you might be interested in seeing how much variance PCA is able to explain as you increase the number of components, in order to decide how many dimensions to ultimately keep or analyze. This example shows you how to quickly plot the cumulative sum of explained variance for a high-dimensional dataset like [Diabetes](https://scikit-learn.org/stable/datasets/index.html#diabetes-dataset).

With a higher explained variance, you are able to capture more variability in your dataset, which could potentially lead to better performance when training your model. For a more mathematical explanation, see this [Q&A thread](https://stats.stackexchange.com/questions/22569/pca-and-proportion-of-variance-explained).

```python
import plotly.express as px
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.datasets import load_diabetes

boston = load_diabetes()
df = pd.DataFrame(boston.data, columns=boston.feature_names)

pca = PCA()
pca.fit(df)
exp_var_cumul = np.cumsum(pca.explained_variance_ratio_)

px.area(
    x=range(1, exp_var_cumul.shape[0] + 1),
    y=exp_var_cumul,
    labels={"x": "# Components", "y": "Explained Variance"}
)
```

## Visualize Loadings

It is also possible to visualize loadings using `shapes`, and use `annotations` to indicate which feature a certain loading originally belonged to. Here, we define loadings as:

$$
loadings = eigenvectors \cdot \sqrt{eigenvalues}
$$

For more details about the linear algebra behind eigenvectors and loadings, see this [Q&A thread](https://stats.stackexchange.com/questions/143905/loadings-vs-eigenvectors-in-pca-when-to-use-one-or-another).

```python
import plotly.express as px
import numpy as np
from sklearn.decomposition import PCA
from sklearn import datasets
from sklearn.preprocessing import StandardScaler

df = px.data.iris()
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
X = df[features]

pca = PCA(n_components=2)
components = pca.fit_transform(X)

loadings = pca.components_.T * np.sqrt(pca.explained_variance_)

fig = px.scatter(components, x=0, y=1, color=df['species'])

for i, feature in enumerate(features):
    fig.add_annotation(
        ax=0, ay=0,
        axref="x", ayref="y",
        x=loadings[i, 0],
        y=loadings[i, 1],
        showarrow=True,
        arrowsize=2,
        arrowhead=2,
        xanchor="right",
        yanchor="top"
    )
    fig.add_annotation(
        x=loadings[i, 0],
        y=loadings[i, 1],
        ax=0, ay=0,
        xanchor="center",
        yanchor="bottom",
        text=feature,
        yshift=5,
    )
fig.show()
```

## References

Learn more about `px`, `px.scatter_3d`, and `px.scatter_matrix` here:

* [Plotly express](plotly-express.md)
* [3D Scatter Plots](3d-scatter-plots.md)
* [Splom](splom.md)

The following resources offer an in-depth overview of PCA and explained variance:

* <https://en.wikipedia.org/wiki/Explained_variation>
* <https://scikit-learn.org/stable/modules/decomposition.html#pca>
* <https://stats.stackexchange.com/questions/2691/making-sense-of-principal-component-analysis-eigenvectors-eigenvalues/140579#140579>
* <https://stats.stackexchange.com/questions/143905/loadings-vs-eigenvectors-in-pca-when-to-use-one-or-another>
* <https://stats.stackexchange.com/questions/22569/pca-and-proportion-of-variance-explained>
