from __future__ import absolute_import

from nose.tools import raises

from plotly.exceptions import PlotlyError
import plotly.tools as tls


def test_validate_valid_fig():
    fig = {
        'layout': {
            'title': 'something'
        },
        'data': [
            {
                'x': [1, 2, 3],
                'y': [2, 1, 2]
            }
        ]
    }
    tls.validate(fig, 'Figure')


@raises(ValueError)
def test_validate_invalid_fig():
    fig = {
        'layout': {
            'title': 'something'
        },
        'data': {
            'x': [1, 2, 3],
            'y': [2, 1, 2]
        }
    }
    tls.validate(fig, 'Figure')
