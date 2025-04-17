import _plotly_utils.basevalidators as _bv


class FamilysrcValidator(_bv.SrcValidator):
    def __init__(
        self, plotly_name="familysrc", parent_name="funnel.hoverlabel.font", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
