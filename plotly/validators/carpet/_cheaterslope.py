import _plotly_utils.basevalidators as _bv


class CheaterslopeValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="cheaterslope", parent_name="carpet", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
