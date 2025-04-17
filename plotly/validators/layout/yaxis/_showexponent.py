import _plotly_utils.basevalidators as _bv


class ShowexponentValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="showexponent", parent_name="layout.yaxis", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "ticks"),
            values=kwargs.pop("values", ["all", "first", "last", "none"]),
            **kwargs,
        )
