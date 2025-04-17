import _plotly_utils.basevalidators as _bv


class WidthValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="width", parent_name="layout.newselection.line", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            min=kwargs.pop("min", 1),
            **kwargs,
        )
