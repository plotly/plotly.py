import _plotly_utils.basevalidators as _bv


class OffsetValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="offset", parent_name="funnel", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            array_ok=kwargs.pop("array_ok", False),
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
