# Default settings for image generation

# This header is necessary to comply with Open Street Map tile policy:
# https://openstreetmap.github.io/owg-website/policies/tiles/#31-identification
DEFAULT_HEADERS = {"X-Requested-With": "plotly.py"}


class _Defaults(object):
    """
    Class to store default settings for image generation.
    """

    def __init__(self):
        self.default_format = "png"
        self.default_width = 700
        self.default_height = 500
        self.default_scale = 1
        self.mathjax = None
        self.topojson = None
        self.plotlyjs = None
        self.headers = dict(DEFAULT_HEADERS)


defaults = _Defaults()
