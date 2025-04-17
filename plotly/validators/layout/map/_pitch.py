import _plotly_utils.basevalidators as _bv


class PitchValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="pitch", parent_name="layout.map", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
