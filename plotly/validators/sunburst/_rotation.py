import _plotly_utils.basevalidators as _bv


class RotationValidator(_bv.AngleValidator):
    def __init__(self, plotly_name="rotation", parent_name="sunburst", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
