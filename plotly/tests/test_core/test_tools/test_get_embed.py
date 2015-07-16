from __future__ import absolute_import

from nose.tools import raises

import plotly.tools as tls
from plotly.exceptions import PlotlyError


def test_get_valid_embed():
    url = 'https://plot.ly/~PlotBot/82/'
    tls.get_embed(url)


@raises(PlotlyError)
def test_get_invalid_embed():
    url = 'https://plot.ly/~PlotBot/a/'
    tls.get_embed(url)
