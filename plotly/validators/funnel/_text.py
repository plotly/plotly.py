import _plotly_utils.basevalidators as _bv


class TextValidator(_bv.StringValidator):
    def __init__(self, plotly_name="text", parent_name="funnel", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
