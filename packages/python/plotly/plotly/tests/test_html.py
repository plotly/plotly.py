import sys

import pytest
import numpy as np


import plotly.graph_objs as go
import plotly.io as pio
from plotly.tests.utils import plotly_cdn_url


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
def assert_latest_cdn_connected(html):
    assert plotly_cdn_url(cdn_ver="latest") in html


def assert_locked_version_cdn_connected(html):
    assert plotly_cdn_url() in html


def test_latest_cdn_included(fig1):
    html_str = pio.to_html(fig1, include_plotlyjs="cdn-latest")
    assert_latest_cdn_connected(html_str)


def test_versioned_cdn_included(fig1):
    html_str = pio.to_html(fig1, include_plotlyjs="cdn")
    assert_locked_version_cdn_connected(html_str)
