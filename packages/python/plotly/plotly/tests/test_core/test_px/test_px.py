import plotly.express as px
import numpy as np


def test_scatter():
    iris = px.data.iris()
    fig = px.scatter(iris, x="sepal_width", y="sepal_length")
    assert fig.data[0].type == "scatter"
    assert np.all(fig.data[0].x == iris.sepal_width)
    assert np.all(fig.data[0].y == iris.sepal_length)
    # test defaults
    assert fig.data[0].mode == "markers"
