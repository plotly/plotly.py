"""
Tests for _plotly_utils.data_utils.image_array_to_data_uri.

Uses the pypng backend so the tests do not require Pillow.
"""

import numpy as np
import pytest

from _plotly_utils.data_utils import image_array_to_data_uri

PNG_PREFIX = "data:image/png;base64,"


def test_greyscale_array_returns_png_data_uri():
    img = np.zeros((2, 2), dtype=np.uint8)
    uri = image_array_to_data_uri(img, backend="pypng")
    assert uri.startswith(PNG_PREFIX)


def test_rgb_array_returns_png_data_uri():
    img = np.zeros((2, 2, 3), dtype=np.uint8)
    uri = image_array_to_data_uri(img, backend="pypng")
    assert uri.startswith(PNG_PREFIX)


def test_rgba_array_returns_png_data_uri():
    img = np.zeros((2, 2, 4), dtype=np.uint8)
    uri = image_array_to_data_uri(img, backend="pypng")
    assert uri.startswith(PNG_PREFIX)


@pytest.mark.parametrize("compression", [-1, 10])
def test_invalid_compression_raises(compression):
    img = np.zeros((2, 2), dtype=np.uint8)
    with pytest.raises(ValueError, match="compression level"):
        image_array_to_data_uri(img, backend="pypng", compression=compression)


def test_invalid_shape_raises():
    img = np.zeros(5, dtype=np.uint8)
    with pytest.raises(ValueError, match="Invalid image shape"):
        image_array_to_data_uri(img, backend="pypng")


def test_jpg_without_pil_backend_raises():
    img = np.zeros((2, 2), dtype=np.uint8)
    with pytest.raises(ValueError, match="jpg binary strings"):
        image_array_to_data_uri(img, backend="pypng", ext="jpg")
