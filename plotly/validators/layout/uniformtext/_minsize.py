import _plotly_utils.basevalidators as _bv


class MinsizeValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="minsize", parent_name="layout.uniformtext", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
