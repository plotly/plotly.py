import plotly
from plotly.graph_objs import *
import plotly.tools as tls
from nose.tools import raises
import numpy as np


@raises(Exception)
def test_wrong_kwarg():
    fig = tls.make_subplots(stuff='not gonna work')
