import _plotly_utils.basevalidators as _bv


class DividerwidthValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="dividerwidth", parent_name="layout.xaxis", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "ticks"),
            **kwargs,
        )
