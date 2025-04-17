import _plotly_utils.basevalidators as _bv


class BgcolorsrcValidator(_bv.SrcValidator):
    def __init__(
        self, plotly_name="bgcolorsrc", parent_name="surface.hoverlabel", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
