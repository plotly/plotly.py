import _plotly_utils.basevalidators as _bv


class ClickmodeValidator(_bv.FlaglistValidator):
    def __init__(self, plotly_name="clickmode", parent_name="layout", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            extras=kwargs.pop("extras", ["none"]),
            flags=kwargs.pop("flags", ["event", "select"]),
            **kwargs,
        )
