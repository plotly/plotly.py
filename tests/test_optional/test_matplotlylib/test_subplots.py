import pytest

from plotly import optional_imports
from ...utils import compare_dict, strip_dict_params
from ...test_optional.optional_utils import run_fig
from ...test_optional.test_matplotlylib.data.subplots import D, BLANK_SUBPLOTS

matplotlylib = optional_imports.get_module("plotly.matplotlylib")

if matplotlylib:
    from matplotlib.gridspec import GridSpec
    import matplotlib.pyplot as plt


@pytest.mark.skip
def test_blank_subplots():
    fig = plt.figure()
    gs = GridSpec(4, 6)
    ax1 = fig.add_subplot(gs[0, 1])
    ax1.plot(D["x1"], D["y1"])
    fig.add_subplot(gs[1, 1])
    fig.add_subplot(gs[2:, 1])
    fig.add_subplot(gs[0, 2:])
    fig.add_subplot(gs[1:3, 2:4])
    fig.add_subplot(gs[3, 2:5])
    fig.add_subplot(gs[1:3, 4:])
    fig.add_subplot(gs[3, 5])
    gs.update(hspace=0.6, wspace=0.6)
    renderer = run_fig(fig)

    for data_no, data_dict in enumerate(renderer.plotly_fig["data"]):
        d1, d2 = strip_dict_params(
            data_dict, BLANK_SUBPLOTS["data"][data_no], ignore=["uid"]
        )
        equivalent, msg = compare_dict(d1, d2)

    equivalent, msg = compare_dict(
        renderer.plotly_fig["layout"], BLANK_SUBPLOTS["layout"]
    )
    assert equivalent, msg
