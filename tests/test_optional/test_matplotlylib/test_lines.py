import pytest

from plotly import optional_imports
from ...utils import compare_dict, strip_dict_params
from ...test_optional.optional_utils import run_fig
from ...test_optional.test_matplotlylib.data.lines import (
    COMPLICATED_LINE,
    D,
    SIMPLE_LINE,
)

matplotlylib = optional_imports.get_module("plotly.matplotlylib")

if matplotlylib:
    import matplotlib.pyplot as plt


@pytest.mark.skip
def test_simple_line():
    fig, ax = plt.subplots()
    ax.plot(D["x1"], D["y1"], label="simple")
    renderer = run_fig(fig)
    for data_no, data_dict in enumerate(renderer.plotly_fig["data"]):
        d1, d2 = strip_dict_params(
            data_dict, SIMPLE_LINE["data"][data_no], ignore=["uid"]
        )

        equivalent, msg = compare_dict(d1, d2)
        assert equivalent, msg
    equivalent, msg = compare_dict(renderer.plotly_fig["layout"], SIMPLE_LINE["layout"])
    assert equivalent, msg


@pytest.mark.skip
def test_complicated_line():
    fig, ax = plt.subplots()
    ax.plot(D["x1"], D["y1"], "ro", markersize=10, alpha=0.5, label="one")
    ax.plot(D["x1"], D["y1"], "-b", linewidth=2, alpha=0.7, label="two")
    ax.plot(
        D["x2"],
        D["y2"],
        "b+",
        markeredgewidth=2,
        markersize=10,
        alpha=0.6,
        label="three",
    )
    ax.plot(D["x2"], D["y2"], "--r", linewidth=2, alpha=0.8, label="four")
    renderer = run_fig(fig)
    for data_no, data_dict in enumerate(renderer.plotly_fig["data"]):
        d1, d2 = strip_dict_params(
            data_dict, COMPLICATED_LINE["data"][data_no], ignore=["uid"]
        )

        equivalent, msg = compare_dict(d1, d2)
        assert equivalent, msg

    equivalent, msg = compare_dict(
        renderer.plotly_fig["layout"], COMPLICATED_LINE["layout"]
    )
    assert equivalent, msg
