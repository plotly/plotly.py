import _plotly_utils.basevalidators as _bv


class Q3Validator(_bv.DataArrayValidator):
    def __init__(self, plotly_name="q3", parent_name="box", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            **kwargs,
        )
