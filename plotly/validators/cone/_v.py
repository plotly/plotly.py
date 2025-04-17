import _plotly_utils.basevalidators as _bv


class VValidator(_bv.DataArrayValidator):
    def __init__(self, plotly_name="v", parent_name="cone", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
