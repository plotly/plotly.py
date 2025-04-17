import _plotly_utils.basevalidators as _bv


class AutobinyValidator(_bv.BooleanValidator):
    def __init__(
        self, plotly_name="autobiny", parent_name="histogram2dcontour", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
