import _plotly_utils.basevalidators as _bv


class ShowticksuffixValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="showticksuffix", parent_name="carpet.baxis", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", ["all", "first", "last", "none"]),
            **kwargs,
        )
