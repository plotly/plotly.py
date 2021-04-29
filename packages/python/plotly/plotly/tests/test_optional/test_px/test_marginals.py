import plotly.express as px
import pytest


@pytest.mark.parametrize("px_fn", [px.scatter, px.density_heatmap, px.density_contour])
@pytest.mark.parametrize("marginal_x", [None, "histogram", "box", "violin"])
@pytest.mark.parametrize("marginal_y", [None, "rug"])
def test_xy_marginals(px_fn, marginal_x, marginal_y):
    df = px.data.tips()

    fig = px_fn(
        df, x="total_bill", y="tip", marginal_x=marginal_x, marginal_y=marginal_y
    )
    assert len(fig.data) == 1 + (marginal_x is not None) + (marginal_y is not None)


@pytest.mark.parametrize("px_fn", [px.histogram])
@pytest.mark.parametrize("marginal", [None, "rug", "histogram", "box", "violin"])
@pytest.mark.parametrize("orientation", ["h", "v"])
def test_single_marginals(px_fn, marginal, orientation):
    df = px.data.tips()

    fig = px_fn(
        df, x="total_bill", y="total_bill", marginal=marginal, orientation=orientation
    )
    assert len(fig.data) == 1 + (marginal is not None)
