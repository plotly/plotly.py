import pytest
import numpy as np
import re


import plotly.graph_objs as go
import plotly.io as pio
from plotly.io._utils import plotly_cdn_url
from plotly.offline.offline import get_plotlyjs
from plotly.io._html import _generate_sri_hash


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


def test_versioned_cdn_included(fig1):
    assert plotly_cdn_url() in pio.to_html(fig1, include_plotlyjs="cdn")


def test_html_deterministic(fig1):
    div_id = "plotly-root"
    assert pio.to_html(fig1, include_plotlyjs="cdn", div_id=div_id) == pio.to_html(
        fig1, include_plotlyjs="cdn", div_id=div_id
    )


def test_cdn_includes_integrity_attribute(fig1):
    """Test that the CDN script tag includes an integrity attribute with SHA256 hash"""
    html_output = pio.to_html(fig1, include_plotlyjs="cdn")

    # Check that the script tag includes integrity attribute
    assert 'integrity="sha256-' in html_output
    assert 'crossorigin="anonymous"' in html_output

    # Verify it's in the correct script tag
    cdn_pattern = re.compile(
        r'<script[^>]*src="'
        + re.escape(plotly_cdn_url())
        + r'"[^>]*integrity="sha256-[A-Za-z0-9+/=]+"[^>]*>'
    )
    match = cdn_pattern.search(html_output)
    assert match is not None, "CDN script tag with integrity attribute not found"


def test_cdn_integrity_hash_matches_bundled_content(fig1):
    """Test that the SRI hash in CDN script tag matches the bundled plotly.js content"""
    html_output = pio.to_html(fig1, include_plotlyjs="cdn")

    # Extract the integrity hash from the HTML output
    integrity_pattern = re.compile(r'integrity="(sha256-[A-Za-z0-9+/=]+)"')
    match = integrity_pattern.search(html_output)
    assert match is not None, "Integrity attribute not found"
    extracted_hash = match.group(1)

    # Generate expected hash from bundled content
    plotlyjs_content = get_plotlyjs()
    expected_hash = _generate_sri_hash(plotlyjs_content)

    # Verify they match
    assert extracted_hash == expected_hash, (
        f"Hash mismatch: expected {expected_hash}, got {extracted_hash}"
    )
