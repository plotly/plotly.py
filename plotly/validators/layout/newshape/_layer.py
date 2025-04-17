import _plotly_utils.basevalidators as _bv


class LayerValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="layer", parent_name="layout.newshape", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            values=kwargs.pop("values", ["below", "above", "between"]),
            **kwargs,
        )
