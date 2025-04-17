import _plotly_utils.basevalidators as _bv


class ShadowValidator(_bv.StringValidator):
    def __init__(
        self, plotly_name="shadow", parent_name="table.legendgrouptitle.font", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "style"),
            **kwargs,
        )
