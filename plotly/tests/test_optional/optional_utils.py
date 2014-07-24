from __future__ import absolute_import

import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
from plotly.matplotlylib import Exporter, PlotlyRenderer
from plotly.tests.utils import *


def run_fig(fig):
    renderer = PlotlyRenderer()
    exporter = Exporter(renderer)
    exporter.run(fig)
    return renderer
