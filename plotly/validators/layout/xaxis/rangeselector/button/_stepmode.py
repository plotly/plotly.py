import _plotly_utils.basevalidators as _bv


class StepmodeValidator(_bv.EnumeratedValidator):
    def __init__(
        self,
        plotly_name="stepmode",
        parent_name="layout.xaxis.rangeselector.button",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            values=kwargs.pop("values", ["backward", "todate"]),
            **kwargs,
        )
