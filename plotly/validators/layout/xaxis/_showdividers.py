import _plotly_utils.basevalidators as _bv


class ShowdividersValidator(_bv.BooleanValidator):
    def __init__(
        self, plotly_name="showdividers", parent_name="layout.xaxis", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "ticks"),
            **kwargs,
        )
