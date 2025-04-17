import _plotly_utils.basevalidators as _bv


class MatchesValidator(_bv.BooleanValidator):
    def __init__(
        self, plotly_name="matches", parent_name="splom.dimension.axis", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
