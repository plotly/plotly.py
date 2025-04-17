import _plotly_utils.basevalidators as _bv


class DirectionValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="direction", parent_name="layout.updatemenu", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            values=kwargs.pop("values", ["left", "right", "up", "down"]),
            **kwargs,
        )
