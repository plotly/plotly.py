import _plotly_utils.basevalidators as _bv


class WidthValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="width", parent_name="table.cells.line", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
