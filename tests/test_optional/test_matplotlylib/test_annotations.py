import pytest

from plotly import optional_imports

matplotlylib = optional_imports.get_module("plotly.matplotlylib")

if matplotlylib:
    import matplotlib.pyplot as plt

    from ...utils import compare_dict, strip_dict_params
    from ..optional_utils import run_fig
    from ..test_matplotlylib.data.annotations import ANNOTATIONS


@pytest.mark.skip
def test_annotations():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], "b-")
    ax.plot([3, 2, 1], "b-")
    ax.text(0.001, 0.999, "top-left", transform=ax.transAxes, va="top", ha="left")
    ax.text(
        0.001, 0.001, "bottom-left", transform=ax.transAxes, va="baseline", ha="left"
    )
    ax.text(0.999, 0.999, "top-right", transform=ax.transAxes, va="top", ha="right")
    ax.text(
        0.999, 0.001, "bottom-right", transform=ax.transAxes, va="baseline", ha="right"
    )
    renderer = run_fig(fig)
    for data_no, data_dict in enumerate(renderer.plotly_fig["data"]):
        d1, d2 = strip_dict_params(
            data_dict, ANNOTATIONS["data"][data_no], ignore=["uid"]
        )
        equivalent, msg = compare_dict(d1, d2)
        assert equivalent, msg
    for no, note in enumerate(renderer.plotly_fig["layout"]["annotations"]):
        equivalent, msg = compare_dict(note, ANNOTATIONS["layout"]["annotations"][no])
        assert equivalent, msg
