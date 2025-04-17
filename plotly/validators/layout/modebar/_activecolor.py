import _plotly_utils.basevalidators as _bv


class ActivecolorValidator(_bv.ColorValidator):
    def __init__(
        self, plotly_name="activecolor", parent_name="layout.modebar", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "modebar"),
            **kwargs,
        )
