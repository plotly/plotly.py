import _plotly_utils.basevalidators as _bv


class FgcolorsrcValidator(_bv.SrcValidator):
    def __init__(
        self, plotly_name="fgcolorsrc", parent_name="histogram.marker.pattern", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
