import _plotly_utils.basevalidators as _bv


class FunnelmodeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="funnelmode", parent_name="layout", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", ["stack", "group", "overlay"]),
            **kwargs,
        )
