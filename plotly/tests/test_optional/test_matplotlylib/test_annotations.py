from __future__ import absolute_import

import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from plotly.tests.utils import compare_dict
from plotly.tests.test_optional.optional_utils import run_fig
from plotly.tests.test_optional.test_matplotlylib.data.annotations import *


def test_annotations():
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], 'b-')
    ax.plot([3, 2, 1], 'b-')
    ax.text(0.001, 0.999,
            'top-left', transform=ax.transAxes, va='top', ha='left')
    ax.text(0.001, 0.001,
            'bottom-left', transform=ax.transAxes, va='baseline', ha='left')
    ax.text(0.999, 0.999,
            'top-right', transform=ax.transAxes, va='top', ha='right')
    ax.text(0.999, 0.001,
            'bottom-right', transform=ax.transAxes, va='baseline', ha='right')
    renderer = run_fig(fig)
    for data_no, data_dict in enumerate(renderer.plotly_fig['data']):
        equivalent, msg = compare_dict(data_dict,
                                       ANNOTATIONS['data'][data_no])
        assert equivalent, msg
    for no, note in enumerate(renderer.plotly_fig['layout']['annotations']):
        equivalent, msg = compare_dict(note,
                                       ANNOTATIONS['layout']['annotations'][no])
        assert equivalent, msg
