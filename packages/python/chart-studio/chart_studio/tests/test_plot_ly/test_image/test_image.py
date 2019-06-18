from __future__ import absolute_import

import imghdr
import tempfile
import os
import itertools
import warnings

from nose.plugins.attrib import attr

import _plotly_utils.exceptions
from chart_studio.plotly import plotly as py
from chart_studio.tests.utils import PlotlyTestCase


@attr("slow")
class TestImage(PlotlyTestCase):
    def setUp(self):
        super(TestImage, self).setUp()
        py.sign_in("PlotlyImageTest", "786r5mecv0")
        self.data = [{"x": [1, 2, 3], "y": [3, 1, 6]}]


def _generate_image_get_returns_valid_image_test(image_format, width, height, scale):
    def test(self):
        # TODO: better understand why this intermittently fails. See #649
        num_attempts = 5
        for i in range(num_attempts):
            if i > 0:
                warnings.warn("image test intermittently failed, retrying...")
            try:
                image = py.image.get(self.data, image_format, width, height, scale)
                if image_format in ["png", "jpeg"]:
                    assert imghdr.what("", image) == image_format
                return
            except (KeyError, _plotly_utils.exceptions.PlotlyError):
                if i == num_attempts - 1:
                    raise

    return test


def _generate_image_save_as_saves_valid_image(image_format, width, height, scale):
    def _test(self):
        f, filename = tempfile.mkstemp(".{}".format(image_format))
        py.image.save_as(
            self.data,
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

    return _test


kwargs = {
    "format": ["png", "jpeg", "pdf", "svg", "emf"],
    "width": [None, 300],
    "height": [None, 300],
    "scale": [None, 5],
}

for args in itertools.product(
    kwargs["format"], kwargs["width"], kwargs["height"], kwargs["scale"]
):
    for test_generator in [
        _generate_image_get_returns_valid_image_test,
        _generate_image_save_as_saves_valid_image,
    ]:

        _test = test_generator(*args)
        arg_string = ", ".join([str(a) for a in args])
        test_name = test_generator.__name__.replace("_generate", "test")
        test_name += "({})".format(arg_string)
        setattr(TestImage, test_name, _test)
