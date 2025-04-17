import _plotly_utils.basevalidators as _bv


class InsidetextorientationValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="insidetextorientation", parent_name="pie", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            values=kwargs.pop("values", ["horizontal", "radial", "tangential", "auto"]),
            **kwargs,
        )
