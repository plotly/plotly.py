from __future__ import absolute_import

from nose.plugins.attrib import attr

from plotly import optional_imports
from plotly.tests.utils import compare_dict
from plotly.tests.test_optional.optional_utils import run_fig
from plotly.tests.test_optional.test_matplotlylib.data.subplots import *

matplotlylib = optional_imports.get_module('plotly.matplotlylib')

if matplotlylib:
    import matplotlib

    # Force matplotlib to not use any Xwindows backend.
    matplotlib.use('Agg')
    from matplotlib.gridspec import GridSpec
    import matplotlib.pyplot as plt


@attr('matplotlib')
def test_blank_subplots():
    fig = plt.figure()
    gs = GridSpec(4, 6)
    ax1 = fig.add_subplot(gs[0, 1])
    ax1.plot(D['x1'], D['y1'])
    fig.add_subplot(gs[1, 1])
    fig.add_subplot(gs[2:, 1])
    fig.add_subplot(gs[0, 2:])
    fig.add_subplot(gs[1:3, 2:4])
    fig.add_subplot(gs[3, 2:5])
    fig.add_subplot(gs[1:3, 4:])
    fig.add_subplot(gs[3, 5])
    gs.update(hspace=.6, wspace=.6)
    renderer = run_fig(fig)
    equivalent, msg = compare_dict(renderer.plotly_fig['layout'],
                                   BLANK_SUBPLOTS['layout'])
    assert equivalent, msg
