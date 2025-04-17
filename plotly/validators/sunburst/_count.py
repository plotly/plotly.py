import _plotly_utils.basevalidators as _bv


class CountValidator(_bv.FlaglistValidator):
    def __init__(self, plotly_name="count", parent_name="sunburst", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            flags=kwargs.pop("flags", ["branches", "leaves"]),
            **kwargs,
        )
