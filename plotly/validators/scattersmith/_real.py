import _plotly_utils.basevalidators as _bv


class RealValidator(_bv.DataArrayValidator):
    def __init__(self, plotly_name="real", parent_name="scattersmith", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc+clearAxisTypes"),
            **kwargs,
        )
