import pytest

from plotly import optional_imports
from ...utils import compare_dict, strip_dict_params
from ...test_optional.optional_utils import run_fig
from ...test_optional.test_matplotlylib.data.axis_scales import EVEN_LINEAR_SCALE

matplotlylib = optional_imports.get_module("plotly.matplotlylib")

if matplotlylib:
    import matplotlib.pyplot as plt


@pytest.mark.skip
def test_even_linear_scale():
    fig, ax = plt.subplots()
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [10, 3, 100, 6, 45, 4, 80, 45, 3, 59]
    ax.plot(x, y)
    _ = ax.set_xticks(list(range(0, 20, 3)), True)
    _ = ax.set_yticks(list(range(0, 200, 13)), True)
    renderer = run_fig(fig)
    for data_no, data_dict in enumerate(renderer.plotly_fig["data"]):
        # equivalent, msg = compare_dict(data_dict.to_plotly_json(),
        #                                EVEN_LINEAR_SCALE['data'][data_no].to_plotly_json())
        # assert equivalent, msg
        d1, d2 = strip_dict_params(
            data_dict, EVEN_LINEAR_SCALE["data"][data_no], ignore=["uid"]
        )

        equivalent, msg = compare_dict(d1, d2)
        assert equivalent, msg

    equivalent, msg = compare_dict(
        renderer.plotly_fig["layout"], EVEN_LINEAR_SCALE["layout"]
    )
    assert equivalent, msg
