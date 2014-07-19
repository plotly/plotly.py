from __future__ import absolute_import

import plotly.tools as tls
from nose.tools import raises
from plotly.exceptions import PlotlyError


def test_validate_valid_fig():
    fig = {
        'layout':{
            'title':'something'
        },
        'data':[
            {
                'x':[1,2,3],
                'y':[2,1,2]
            }
        ]
    }
    tls.validate(fig, 'Figure')


@raises(PlotlyError)
def test_validate_invalid_fig():
    fig = {
        'layout':{
            'title':'something'
        },
        'data':{
            'x':[1,2,3],
            'y':[2,1,2]
        }
    }
    tls.validate(fig, 'Figure')
