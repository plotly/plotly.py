import _plotly_utils.basevalidators as _bv


class LayerValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="layer", parent_name="layout.xaxis", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            values=kwargs.pop("values", ["above traces", "below traces"]),
            **kwargs,
        )
