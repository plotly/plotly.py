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


def test_custom_data_scatter():
    iris = px.data.iris()
    # No hover, no custom data
    fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species")
    assert fig.data[0].customdata is None
    # Hover, no custom data
    fig = px.scatter(
        iris,
        x="sepal_width",
        y="sepal_length",
        color="species",
        hover_data=["petal_length", "petal_width"],
    )
    for data in fig.data:
        assert np.all(np.in1d(data.customdata[:, 1], iris.petal_width))
    # Hover and custom data, no repeated arguments
    fig = px.scatter(
        iris,
        x="sepal_width",
        y="sepal_length",
        hover_data=["petal_length", "petal_width"],
        custom_data=["species_id", "species"],
    )
    assert np.all(fig.data[0].customdata[:, 0] == iris.species_id)
    assert fig.data[0].customdata.shape[1] == 4
    # Hover and custom data, with repeated arguments
    fig = px.scatter(
        iris,
        x="sepal_width",
        y="sepal_length",
        hover_data=["petal_length", "petal_width", "species_id"],
        custom_data=["species_id", "species"],
    )
    assert np.all(fig.data[0].customdata[:, 0] == iris.species_id)
    assert fig.data[0].customdata.shape[1] == 4
    assert (
        fig.data[0].hovertemplate
        == "sepal_width=%{x}<br>sepal_length=%{y}<br>petal_length=%{customdata[2]}<br>petal_width=%{customdata[3]}<br>species_id=%{customdata[0]}"
    )
