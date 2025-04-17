import _plotly_utils.basevalidators as _bv


class ModeValidator(_bv.FlaglistValidator):
    def __init__(self, plotly_name="mode", parent_name="indicator", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            flags=kwargs.pop("flags", ["number", "delta", "gauge"]),
            **kwargs,
        )
