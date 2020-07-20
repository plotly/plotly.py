import plotly.express as px
from pytest import approx


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
