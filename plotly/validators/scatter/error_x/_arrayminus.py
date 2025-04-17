import _plotly_utils.basevalidators as _bv


class ArrayminusValidator(_bv.DataArrayValidator):
    def __init__(
        self, plotly_name="arrayminus", parent_name="scatter.error_x", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
