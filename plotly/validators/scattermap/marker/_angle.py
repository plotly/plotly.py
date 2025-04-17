import _plotly_utils.basevalidators as _bv


class AngleValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="angle", parent_name="scattermap.marker", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
