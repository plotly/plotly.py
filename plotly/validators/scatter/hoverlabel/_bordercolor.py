import _plotly_utils.basevalidators as _bv


class BordercolorValidator(_bv.ColorValidator):
    def __init__(
        self, plotly_name="bordercolor", parent_name="scatter.hoverlabel", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
