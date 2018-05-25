from __future__ import absolute_import

from nose.plugins.attrib import attr

from plotly import optional_imports
from plotly.tests.utils import compare_dict, strip_dict_params
from plotly.tests.test_optional.optional_utils import run_fig
from plotly.tests.test_optional.test_matplotlylib.data.scatter import *

matplotlylib = optional_imports.get_module('plotly.matplotlylib')

if matplotlylib:
    import matplotlib

    # Force matplotlib to not use any Xwindows backend.
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt


@attr('matplotlib')
def test_simple_scatter():
    fig, ax = plt.subplots()
    ax.scatter(D['x1'], D['y1'])
    renderer = run_fig(fig)
    for data_no, data_dict in enumerate(renderer.plotly_fig['data']):
        d1, d2 = strip_dict_params(data_dict, SIMPLE_SCATTER['data'][data_no], ignore=['uid'])
        print(d1)
        print('\n')
        print(d2)
        assert d1 == d2

    equivalent, msg = compare_dict(renderer.plotly_fig['layout'],
                                   SIMPLE_SCATTER['layout'])
    assert equivalent, msg


@attr('matplotlib')
def test_double_scatter():
    fig, ax = plt.subplots()
    ax.scatter(D['x1'], D['y1'], color='red', s=121, marker='^', alpha=0.5)
    ax.scatter(D['x2'], D['y2'], color='purple', s=64, marker='s', alpha=0.5)
    renderer = run_fig(fig)
    for data_no, data_dict in enumerate(renderer.plotly_fig['data']):
        d1, d2 = strip_dict_params(data_dict, DOUBLE_SCATTER['data'][data_no], ignore=['uid'])
        print(d1)
        print('\n')
        print(d2)
        assert d1 == d2

    equivalent, msg = compare_dict(renderer.plotly_fig['layout'],
                                   DOUBLE_SCATTER['layout'])
    assert equivalent, msg
