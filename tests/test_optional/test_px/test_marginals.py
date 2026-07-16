import plotly.express as px
import pytest


@pytest.mark.parametrize("px_fn", [px.scatter, px.density_heatmap, px.density_contour])
@pytest.mark.parametrize("marginal_x", [None, "histogram", "box", "violin"])
@pytest.mark.parametrize("marginal_y", [None, "rug"])
def test_xy_marginals(backend, px_fn, marginal_x, marginal_y):
    df = px.data.tips(return_type=backend)

    fig = px_fn(
        df, x="total_bill", y="tip", marginal_x=marginal_x, marginal_y=marginal_y
    )
    assert len(fig.data) == 1 + (marginal_x is not None) + (marginal_y is not None)


@pytest.mark.parametrize("px_fn", [px.histogram, px.ecdf])
@pytest.mark.parametrize("marginal", [None, "rug", "histogram", "box", "violin"])
@pytest.mark.parametrize("orientation", ["h", "v"])
def test_single_marginals(backend, px_fn, marginal, orientation):
    df = px.data.tips(return_type=backend)

    fig = px_fn(
        df, x="total_bill", y="total_bill", marginal=marginal, orientation=orientation
    )
    assert len(fig.data) == 1 + (marginal is not None)


def test_unsupported_marginal_raises_clear_error():  # issue 4654
    # An unsupported marginal type used to fail deep inside make_figure with a
    # cryptic "'NoneType' object has no attribute 'constructor'". It should
    # instead raise a clear error naming the supported values.
    with pytest.raises(ValueError, match="Supported marginal plot types"):
        px.scatter(x=[1, 2, 3], y=[2, 3, 4], marginal_x="density")
    with pytest.raises(ValueError, match="Supported marginal plot types"):
        px.scatter(x=[1, 2, 3], y=[2, 3, 4], marginal_y="density")
    with pytest.raises(ValueError, match="Supported marginal plot types"):
        px.histogram(x=[1, 2, 3], marginal="density")
