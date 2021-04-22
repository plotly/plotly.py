import plotly
import pandas as pd
import plotly.express as px
from pytest import approx
import pytest
import random


def test_facets():
    df = px.data.tips()
    fig = px.scatter(df, x="total_bill", y="tip")
    assert "xaxis2" not in fig.layout
    assert "yaxis2" not in fig.layout
    assert fig.layout.xaxis.domain == (0.0, 1.0)
    assert fig.layout.yaxis.domain == (0.0, 1.0)

    fig = px.scatter(df, x="total_bill", y="tip", facet_row="sex", facet_col="smoker")
    assert fig.layout.xaxis4.domain[0] - fig.layout.xaxis.domain[1] == approx(0.02)
    assert fig.layout.yaxis4.domain[0] - fig.layout.yaxis.domain[1] == approx(0.03)

    fig = px.scatter(df, x="total_bill", y="tip", facet_col="day", facet_col_wrap=2)
    assert fig.layout.xaxis4.domain[0] - fig.layout.xaxis.domain[1] == approx(0.02)
    assert fig.layout.yaxis4.domain[0] - fig.layout.yaxis.domain[1] == approx(0.07)

    fig = px.scatter(
        df,
        x="total_bill",
        y="tip",
        facet_row="sex",
        facet_col="smoker",
        facet_col_spacing=0.09,
        facet_row_spacing=0.08,
    )
    assert fig.layout.xaxis4.domain[0] - fig.layout.xaxis.domain[1] == approx(0.09)
    assert fig.layout.yaxis4.domain[0] - fig.layout.yaxis.domain[1] == approx(0.08)

    fig = px.scatter(
        df,
        x="total_bill",
        y="tip",
        facet_col="day",
        facet_col_wrap=2,
        facet_col_spacing=0.09,
        facet_row_spacing=0.08,
    )
    assert fig.layout.xaxis4.domain[0] - fig.layout.xaxis.domain[1] == approx(0.09)
    assert fig.layout.yaxis4.domain[0] - fig.layout.yaxis.domain[1] == approx(0.08)


def test_facets_with_marginals():
    df = px.data.tips()

    fig = px.histogram(df, x="total_bill", facet_col="sex", marginal="rug")
    assert len(fig.data) == 4
    fig = px.histogram(df, x="total_bill", facet_row="sex", marginal="rug")
    assert len(fig.data) == 2

    fig = px.histogram(df, y="total_bill", facet_col="sex", marginal="rug")
    assert len(fig.data) == 2
    fig = px.histogram(df, y="total_bill", facet_row="sex", marginal="rug")
    assert len(fig.data) == 4

    fig = px.scatter(df, x="total_bill", y="tip", facet_col="sex", marginal_x="rug")
    assert len(fig.data) == 4
    fig = px.scatter(
        df, x="total_bill", y="tip", facet_col="day", facet_col_wrap=2, marginal_x="rug"
    )
    assert len(fig.data) == 8  # ignore the wrap when marginal is used
    fig = px.scatter(df, x="total_bill", y="tip", facet_col="sex", marginal_y="rug")
    assert len(fig.data) == 2  # ignore the marginal in the facet direction

    fig = px.scatter(df, x="total_bill", y="tip", facet_row="sex", marginal_x="rug")
    assert len(fig.data) == 2  # ignore the marginal in the facet direction
    fig = px.scatter(df, x="total_bill", y="tip", facet_row="sex", marginal_y="rug")
    assert len(fig.data) == 4

    fig = px.scatter(
        df, x="total_bill", y="tip", facet_row="sex", marginal_y="rug", marginal_x="rug"
    )
    assert len(fig.data) == 4  # ignore the marginal in the facet direction
    fig = px.scatter(
        df, x="total_bill", y="tip", facet_col="sex", marginal_y="rug", marginal_x="rug"
    )
    assert len(fig.data) == 4  # ignore the marginal in the facet direction
    fig = px.scatter(
        df,
        x="total_bill",
        y="tip",
        facet_row="sex",
        facet_col="sex",
        marginal_y="rug",
        marginal_x="rug",
    )
    assert len(fig.data) == 2  # ignore all marginals


@pytest.fixture
def bad_facet_spacing_df():
    NROWS = 101
    NDATA = 1000
    categories = [n % NROWS for n in range(NDATA)]
    df = pd.DataFrame(
        {
            "x": [random.random() for _ in range(NDATA)],
            "y": [random.random() for _ in range(NDATA)],
            "category": categories,
        }
    )
    return df


def test_bad_facet_spacing_eror(bad_facet_spacing_df):
    df = bad_facet_spacing_df
    with pytest.raises(
        ValueError, match="Use the facet_row_spacing argument to adjust this spacing\."
    ):
        fig = px.scatter(
            df, x="x", y="y", facet_row="category", facet_row_spacing=0.01001
        )
    with pytest.raises(
        ValueError, match="Use the facet_col_spacing argument to adjust this spacing\."
    ):
        fig = px.scatter(
            df, x="x", y="y", facet_col="category", facet_col_spacing=0.01001
        )
    # Check error is not raised when the spacing is OK
    try:
        fig = px.scatter(df, x="x", y="y", facet_row="category", facet_row_spacing=0.01)
    except ValueError:
        # Error shouldn't be raised, so fail if it is
        assert False
    try:
        fig = px.scatter(df, x="x", y="y", facet_col="category", facet_col_spacing=0.01)
    except ValueError:
        # Error shouldn't be raised, so fail if it is
        assert False
