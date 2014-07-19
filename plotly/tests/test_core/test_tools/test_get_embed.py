import plotly.tools as tls
from nose.tools import raises
from plotly.exceptions import PlotlyError


def test_get_valid_embed():
    url = 'https://plot.ly/~PlotBot/82/'
    embed = tls.get_embed(url)


@raises(PlotlyError)
def test_get_invalid_embed():
    url = 'https://plot.ly/~PlotBot/a/'
    embed = tls.get_embed(url)
