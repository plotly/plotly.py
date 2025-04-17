import _plotly_utils.basevalidators as _bv


class HiddenlabelsValidator(_bv.DataArrayValidator):
    def __init__(self, plotly_name="hiddenlabels", parent_name="layout", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
