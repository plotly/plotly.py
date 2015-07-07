from __future__ import absolute_import

import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from plotly.tests.utils import compare_dict
from plotly.tests.test_optional.optional_utils import run_fig
from plotly.tests.test_optional.test_matplotlylib.data.lines import *


def test_simple_line():
    fig, ax = plt.subplots()
    ax.plot(D['x1'], D['y1'], label='simple')
    renderer = run_fig(fig)
    for data_no, data_dict in enumerate(renderer.plotly_fig['data']):
        equivalent, msg = compare_dict(data_dict, SIMPLE_LINE['data'][data_no])
        assert equivalent, msg
    equivalent, msg = compare_dict(renderer.plotly_fig['layout'],
                                   SIMPLE_LINE['layout'])
    assert equivalent, msg


def test_complicated_line():
    fig, ax = plt.subplots()
    ax.plot(D['x1'], D['y1'], 'ro', markersize=10, alpha=.5, label='one')
    ax.plot(D['x1'], D['y1'], '-b', linewidth=2, alpha=.7, label='two')
    ax.plot(D['x2'], D['y2'], 'b+', markeredgewidth=2,
            markersize=10, alpha=.6, label='three')
    ax.plot(D['x2'], D['y2'], '--r', linewidth=2, alpha=.8, label='four')
    renderer = run_fig(fig)
    for data_no, data_dict in enumerate(renderer.plotly_fig['data']):
        equivalent, msg = compare_dict(data_dict,
                                       COMPLICATED_LINE['data'][data_no])
        assert equivalent, msg
    equivalent, msg = compare_dict(renderer.plotly_fig['layout'],
                                   COMPLICATED_LINE['layout'])
    assert equivalent, msg
