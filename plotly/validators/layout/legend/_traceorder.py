import _plotly_utils.basevalidators as _bv


class TraceorderValidator(_bv.FlaglistValidator):
    def __init__(self, plotly_name="traceorder", parent_name="layout.legend", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "legend"),
            extras=kwargs.pop("extras", ["normal"]),
            flags=kwargs.pop("flags", ["reversed", "grouped"]),
            **kwargs,
        )
