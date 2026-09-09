"""
Tests for _plotly_utils.data_utils.image_array_to_data_uri.

Uses the pypng backend so the tests do not require Pillow. The generated
data URIs are decoded with the vendored pypng Reader so the tests assert on
the encoded pixels rather than only on the data URI prefix.
"""

import base64

import numpy as np
import pytest

from _plotly_utils.data_utils import image_array_to_data_uri
from _plotly_utils.png import Reader

PNG_PREFIX = "data:image/png;base64,"


def decode_data_uri(uri):
    """Decode a PNG data URI back into an array plus the PNG header info."""
    assert uri.startswith(PNG_PREFIX)
    png_bytes = base64.b64decode(uri[len(PNG_PREFIX) :])
    width, height, rows, info = Reader(bytes=png_bytes).read_flat()
    if info["greyscale"]:
        channels = 1
    elif info["alpha"]:
        channels = 4
    else:
        channels = 3
    decoded = np.array(list(rows), dtype=np.uint8).reshape(height, width, channels)
    if channels == 1:
        decoded = decoded[:, :, 0]
    return decoded, info


def test_greyscale_array_round_trips():
    img = np.array([[0, 255], [128, 64]], dtype=np.uint8)

    decoded, info = decode_data_uri(image_array_to_data_uri(img, backend="pypng"))

    assert info["greyscale"] is True
    assert info["alpha"] is False
    np.testing.assert_array_equal(decoded, img)


def test_rgb_array_round_trips():
    img = np.array(
        [[[255, 0, 0], [0, 255, 0]], [[0, 0, 255], [10, 20, 30]]], dtype=np.uint8
    )

    decoded, info = decode_data_uri(image_array_to_data_uri(img, backend="pypng"))

    assert info["greyscale"] is False
    assert info["alpha"] is False
    np.testing.assert_array_equal(decoded, img)


def test_rgba_array_round_trips():
    img = np.array(
        [[[255, 0, 0, 255], [0, 255, 0, 128]], [[0, 0, 255, 0], [10, 20, 30, 40]]],
        dtype=np.uint8,
    )

    decoded, info = decode_data_uri(image_array_to_data_uri(img, backend="pypng"))

    assert info["greyscale"] is False
    assert info["alpha"] is True
    np.testing.assert_array_equal(decoded, img)


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
