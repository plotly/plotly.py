from __future__ import absolute_import

import imghdr
import tempfile
import os
import itertools
import warnings
import pytest

import _plotly_utils.exceptions
from chart_studio.plotly import plotly as py

py.sign_in("PlotlyImageTest", "786r5mecv0")
data = [{"x": [1, 2, 3], "y": [3, 1, 6]}]


@pytest.mark.parametrize('image_format', ("png", "jpeg", "pdf", "svg", "emf"))
@pytest.mark.parametrize('width', (None, 300))
@pytest.mark.parametrize('height', (None, 300))
@pytest.mark.parametrize('scale', (None, 5))
def test_image_get_returns_valid_image_test(image_format, width, height, scale):
    # TODO: better understand why this intermittently fails. See #649
    num_attempts = 5
    for i in range(num_attempts):
        if i > 0:
            warnings.warn("image test intermittently failed, retrying...")
        try:
            image = py.image.get(data, image_format, width, height, scale)
            if image_format in ["png", "jpeg"]:
                assert imghdr.what("", image) == image_format
            return
        except (KeyError, _plotly_utils.exceptions.PlotlyError):
            if i == num_attempts - 1:
                raise


@pytest.mark.parametrize('image_format', ("png", "jpeg", "pdf", "svg", "emf"))
@pytest.mark.parametrize('width', (None, 300))
@pytest.mark.parametrize('height', (None, 300))
@pytest.mark.parametrize('scale', (None, 5))
def test_image_save_as_saves_valid_image(image_format, width, height, scale):
    f, filename = tempfile.mkstemp(".{}".format(image_format))
    py.image.save_as(
        data,
        filename,
        format=image_format,
        width=width,
        height=height,
        scale=scale,
    )
    if image_format in ["png", "jpeg"]:
        assert imghdr.what(filename) == image_format
    else:
        assert os.path.getsize(filename) > 0

    os.remove(filename)

