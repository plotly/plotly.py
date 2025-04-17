import _plotly_utils.basevalidators as _bv


class TextcaseValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="textcase", parent_name="table.header.font", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", ["normal", "word caps", "upper", "lower"]),
            **kwargs,
        )
