"""
Tests that every function requiring Kaleido raises a RuntimeError with the
correct message when Kaleido v0 is installed.
"""

import pytest

import plotly.graph_objects as go
import plotly.io as pio
from plotly.io._kaleido import kaleido_available


# Skip every test in this module if Kaleido v1 is installed
pytestmark = pytest.mark.skipif(
    kaleido_available(),
    reason="These tests only apply when Kaleido v1 is not installed.",
)


fig = {"data": [], "layout": {"title": {"text": "figure title"}}}


def assert_error_message_contents(excinfo):
    """Check that the raised RuntimeError has the expected wording."""
    assert "Image export requires the Kaleido package, v1.0.0 or greater" in str(
        excinfo.value
    )


# plotly/io/_kaleido.py


def test_to_image_raises():
    with pytest.raises(RuntimeError) as excinfo:
        pio.to_image(fig, format="png", validate=False)
    assert_error_message_contents(excinfo)


def test_write_image_raises(tmp_path):
    with pytest.raises(RuntimeError) as excinfo:
        pio.write_image(fig, tmp_path / "test.png", validate=False)
    assert_error_message_contents(excinfo)


def test_write_images_raises(tmp_path):
    figs = [dict(fig), dict(fig)]
    paths = [tmp_path / f"test_{i}.png" for i in range(len(figs))]
    with pytest.raises(RuntimeError) as excinfo:
        pio.write_images(fig, paths, validate=False)
    assert_error_message_contents(excinfo)


def test_full_figure_for_development_raises():
    with pytest.raises(RuntimeError) as excinfo:
        pio.full_figure_for_development(fig, warn=False)
    assert_error_message_contents(excinfo)


def test_get_chrome_raises():
    with pytest.raises(RuntimeError) as excinfo:
        pio.get_chrome()
    assert_error_message_contents(excinfo)


# plotly/basedatatypes.py


def test_figure_to_image_raises():
    test_fig = go.Figure(fig)
    with pytest.raises(RuntimeError) as excinfo:
        test_fig.to_image(format="png", validate=False)
    assert_error_message_contents(excinfo)


def test_figure_write_image_raises(tmp_path):
    test_fig = go.Figure(fig)
    with pytest.raises(RuntimeError) as excinfo:
        test_fig.write_image(tmp_path / "test.png", validate=False)
    assert_error_message_contents(excinfo)


def test_figure_full_figure_for_development_raises():
    test_fig = go.Figure(fig)
    with pytest.raises(RuntimeError) as excinfo:
        test_fig.full_figure_for_development(warn=False)
    assert_error_message_contents(excinfo)
