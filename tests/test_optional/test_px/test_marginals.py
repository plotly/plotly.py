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


@pytest.mark.parametrize("px_fn", [px.density_heatmap, px.density_contour])
def test_marginal_histogram_uses_z_and_histfunc(backend, px_fn):  # issue 3521
    df = px.data.tips(return_type=backend)

    fig = px_fn(
        df,
        x="total_bill",
        y="tip",
        z="size",
        histfunc="sum",
        marginal_x="histogram",
        marginal_y="histogram",
    )
    marginal_x_trace, marginal_y_trace = fig.data[1], fig.data[2]

    assert marginal_x_trace.histfunc == "sum"
    assert marginal_x_trace.orientation == "v"
    assert marginal_x_trace.y is not None
    assert len(marginal_x_trace.y) == len(df)
    assert "sum of size=%{y}" in marginal_x_trace.hovertemplate

    assert marginal_y_trace.histfunc == "sum"
    assert marginal_y_trace.orientation == "h"
    assert marginal_y_trace.x is not None
    assert len(marginal_y_trace.x) == len(df)
    assert "sum of size=%{x}" in marginal_y_trace.hovertemplate


@pytest.mark.parametrize("px_fn", [px.density_heatmap, px.density_contour])
def test_marginal_histogram_without_z_is_unchanged(backend, px_fn):  # issue 3521
    df = px.data.tips(return_type=backend)

    fig = px_fn(
        df, x="total_bill", y="tip", marginal_x="histogram", marginal_y="histogram"
    )
    marginal_x_trace, marginal_y_trace = fig.data[1], fig.data[2]

    assert marginal_x_trace.histfunc is None
    assert marginal_x_trace.orientation is None
    assert marginal_x_trace.y is None
    assert "count=%{y}" in marginal_x_trace.hovertemplate

    assert marginal_y_trace.histfunc is None
    assert marginal_y_trace.orientation is None
    assert marginal_y_trace.x is None
    assert "count=%{x}" in marginal_y_trace.hovertemplate


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
