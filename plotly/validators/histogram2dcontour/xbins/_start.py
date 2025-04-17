import _plotly_utils.basevalidators as _bv


class StartValidator(_bv.AnyValidator):
    def __init__(
        self, plotly_name="start", parent_name="histogram2dcontour.xbins", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
