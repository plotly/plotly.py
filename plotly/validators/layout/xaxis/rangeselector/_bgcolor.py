import _plotly_utils.basevalidators as _bv


class BgcolorValidator(_bv.ColorValidator):
    def __init__(
        self, plotly_name="bgcolor", parent_name="layout.xaxis.rangeselector", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
