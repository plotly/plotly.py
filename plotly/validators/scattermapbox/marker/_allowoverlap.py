import _plotly_utils.basevalidators as _bv


class AllowoverlapValidator(_bv.BooleanValidator):
    def __init__(
        self, plotly_name="allowoverlap", parent_name="scattermapbox.marker", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
