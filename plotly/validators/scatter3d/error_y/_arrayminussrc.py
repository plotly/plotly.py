import _plotly_utils.basevalidators as _bv


class ArrayminussrcValidator(_bv.SrcValidator):
    def __init__(
        self, plotly_name="arrayminussrc", parent_name="scatter3d.error_y", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
