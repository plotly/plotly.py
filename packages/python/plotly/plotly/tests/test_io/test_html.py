import sys

import pytest
import numpy as np


import plotly.graph_objs as go
import plotly.io as pio
from plotly.io._utils import plotly_cdn_url


if sys.version_info >= (3, 3):
    import unittest.mock as mock
    from unittest.mock import MagicMock
else:
    import mock
    from mock import MagicMock

# fixtures
# --------
@pytest.fixture
def fig1(request):
    return go.Figure(
        data=[
            {
                "type": "scatter",
                "y": np.array([2, 1, 3, 2, 4, 2]),
                "marker": {"color": "green"},
            }
        ],
        layout={"title": {"text": "Figure title"}},
    )


# HTML
# ----


def test_versioned_cdn_included(fig1):
    assert plotly_cdn_url() in pio.to_html(fig1, include_plotlyjs="cdn")
