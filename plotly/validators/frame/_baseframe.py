import _plotly_utils.basevalidators as _bv


class BaseframeValidator(_bv.StringValidator):
    def __init__(self, plotly_name="baseframe", parent_name="frame", **kwargs):
        super().__init__(plotly_name, parent_name, **kwargs)
