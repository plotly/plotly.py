import _plotly_utils.basevalidators as _bv


class ArraysrcValidator(_bv.SrcValidator):
    def __init__(
        self, plotly_name="arraysrc", parent_name="histogram.error_x", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
