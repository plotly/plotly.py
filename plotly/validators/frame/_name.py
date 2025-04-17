import _plotly_utils.basevalidators as _bv


class NameValidator(_bv.StringValidator):
    def __init__(self, plotly_name="name", parent_name="frame", **kwargs):
        super().__init__(plotly_name, parent_name, **kwargs)
