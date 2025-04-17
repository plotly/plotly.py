import _plotly_utils.basevalidators as _bv


class NticksValidator(_bv.IntegerValidator):
    def __init__(
        self, plotly_name="nticks", parent_name="layout.ternary.caxis", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 1),
            **kwargs,
        )
