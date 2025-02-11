import _plotly_utils.basevalidators as _bv


class StackgroupValidator(_bv.StringValidator):
    def __init__(self, plotly_name="stackgroup", parent_name="scatter", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
