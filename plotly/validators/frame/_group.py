import _plotly_utils.basevalidators as _bv


class GroupValidator(_bv.StringValidator):
    def __init__(self, plotly_name="group", parent_name="frame", **kwargs):
        super().__init__(plotly_name, parent_name, **kwargs)
