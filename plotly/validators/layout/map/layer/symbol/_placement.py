import _plotly_utils.basevalidators as _bv


class PlacementValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="placement", parent_name="layout.map.layer.symbol", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            values=kwargs.pop("values", ["point", "line", "line-center"]),
            **kwargs,
        )
