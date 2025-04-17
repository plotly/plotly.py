import _plotly_utils.basevalidators as _bv


class IntensitymodeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="intensitymode", parent_name="mesh3d", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", ["vertex", "cell"]),
            **kwargs,
        )
