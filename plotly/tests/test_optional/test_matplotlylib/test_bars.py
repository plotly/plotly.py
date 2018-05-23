from __future__ import absolute_import

from nose.plugins.attrib import attr

from plotly import optional_imports
from plotly.tests.utils import compare_dict, strip_dict_params
from plotly.tests.test_optional.optional_utils import run_fig
from plotly.tests.test_optional.test_matplotlylib.data.bars import *

matplotlylib = optional_imports.get_module('plotly.matplotlylib')

if matplotlylib:
    import matplotlib
    # Force matplotlib to not use any Xwindows backend.
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt


@attr('matplotlib')
def test_vertical_bar():
    fig, ax = plt.subplots()
    ax.bar(left=D['left'], height=D['height'])
    renderer = run_fig(fig)

    for data_no, data_dict in enumerate(renderer.plotly_fig['data']):
        d1, d2 = strip_dict_params(data_dict, VERTICAL_BAR['data'][data_no], ignore=['uid'])

        equivalent, msg = compare_dict(d1, d2)
        assert equivalent, msg

    equivalent, msg = compare_dict(renderer.plotly_fig['layout'],
                                   VERTICAL_BAR['layout'])
    assert equivalent, msg


@attr('matplotlib')
def test_horizontal_bar():
    fig, ax = plt.subplots()
    ax.barh(bottom=D['bottom'], width=D['width'])
    renderer = run_fig(fig)

    for data_no, data_dict in enumerate(renderer.plotly_fig['data']):
        d1, d2 = strip_dict_params(data_dict, HORIZONTAL_BAR['data'][data_no], ignore=['uid'])

        equivalent, msg = compare_dict(d1, d2)
        assert equivalent, msg

    equivalent, msg = compare_dict(renderer.plotly_fig['layout'],
                                   HORIZONTAL_BAR['layout'])
    assert equivalent, msg


@attr('matplotlib')
def test_h_and_v_bars():
    fig, ax = plt.subplots()
    ax.bar(left=D['multi_left'], height=D['multi_height'],
           width=10, color='green', alpha=.5)
    # changing height 10 -> 14 because ValueError if bargap not in [0, 1]
    ax.barh(bottom=D['multi_bottom'], width=D['multi_width'],
            height=14, color='red', alpha=.5)
    renderer = run_fig(fig)
    for data_no, data_dict in enumerate(renderer.plotly_fig['data']):
        d1, d2 = strip_dict_params(data_dict, H_AND_V_BARS['data'][data_no], ignore=['uid'])

        equivalent, msg = compare_dict(d1, d2)
        assert equivalent, msg

    equivalent, msg = compare_dict(renderer.plotly_fig['layout'],
                                   H_AND_V_BARS['layout'])
    assert equivalent, msg
