import pytest

from plotly import optional_imports
from ...utils import compare_dict, strip_dict_params
from ...test_optional.optional_utils import run_fig
from ...test_optional.test_matplotlylib.data.scatter import (
    D,
    DOUBLE_SCATTER,
    SIMPLE_SCATTER,
)

matplotlylib = optional_imports.get_module("plotly.matplotlylib")

if matplotlylib:
    import matplotlib.pyplot as plt


@pytest.mark.skip
def test_simple_scatter():
    fig, ax = plt.subplots()
    ax.scatter(D["x1"], D["y1"])
    renderer = run_fig(fig)
    for data_no, data_dict in enumerate(renderer.plotly_fig["data"]):
        d1, d2 = strip_dict_params(
            data_dict, SIMPLE_SCATTER["data"][data_no], ignore=["uid"]
        )
        print(d1)
        print("\n")
        print(d2)
        assert d1 == d2

    equivalent, msg = compare_dict(
        renderer.plotly_fig["layout"], SIMPLE_SCATTER["layout"]
    )
    assert equivalent, msg


@pytest.mark.skip
def test_double_scatter():
    fig, ax = plt.subplots()
    ax.scatter(D["x1"], D["y1"], color="red", s=121, marker="^", alpha=0.5)
    ax.scatter(D["x2"], D["y2"], color="purple", s=64, marker="s", alpha=0.5)
    renderer = run_fig(fig)
    for data_no, data_dict in enumerate(renderer.plotly_fig["data"]):
        d1, d2 = strip_dict_params(
            data_dict, DOUBLE_SCATTER["data"][data_no], ignore=["uid"]
        )
        print(d1)
        print("\n")
        print(d2)
        assert d1 == d2

    equivalent, msg = compare_dict(
        renderer.plotly_fig["layout"], DOUBLE_SCATTER["layout"]
    )
    assert equivalent, msg
