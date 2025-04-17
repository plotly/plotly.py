import _plotly_utils.basevalidators as _bv


class MeasureValidator(_bv.DataArrayValidator):
    def __init__(self, plotly_name="measure", parent_name="waterfall", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
