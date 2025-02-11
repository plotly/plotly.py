import plotly.validators as _bv


class LayoutValidator(_bv.LayoutValidator):
    def __init__(self, plotly_name="layout", parent_name="frame", **kwargs):
        super().__init__(plotly_name, parent_name, **kwargs)
