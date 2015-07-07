from __future__ import absolute_import

import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from plotly.tests.utils import compare_dict
from plotly.tests.test_optional.optional_utils import run_fig
from plotly.tests.test_optional.test_matplotlylib.data.axis_scales import *


def test_even_linear_scale():
    fig, ax = plt.subplots()
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [10, 3, 100, 6, 45, 4, 80, 45, 3, 59]
    ax.plot(x, y)
    _ = ax.set_xticks(list(range(0, 20, 3)))
    _ = ax.set_yticks(list(range(0, 200, 13)))
    renderer = run_fig(fig)
    for data_no, data_dict in enumerate(renderer.plotly_fig['data']):
        equivalent, msg = compare_dict(data_dict,
                                       EVEN_LINEAR_SCALE['data'][data_no])
        assert equivalent, msg
    equivalent, msg = compare_dict(renderer.plotly_fig['layout'],
                                   EVEN_LINEAR_SCALE['layout'])
    assert equivalent, msg
