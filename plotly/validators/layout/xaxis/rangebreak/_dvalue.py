import _plotly_utils.basevalidators as _bv


class DvalueValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="dvalue", parent_name="layout.xaxis.rangebreak", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
