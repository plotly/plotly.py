import _plotly_utils.basevalidators as _bv


class YaxisValidator(_bv.SubplotidValidator):
    def __init__(self, plotly_name="yaxis", parent_name="carpet", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            dflt=kwargs.pop("dflt", "y"),
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            **kwargs,
        )
