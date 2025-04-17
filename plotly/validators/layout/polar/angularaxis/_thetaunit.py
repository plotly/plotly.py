import _plotly_utils.basevalidators as _bv


class ThetaunitValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="thetaunit", parent_name="layout.polar.angularaxis", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", ["radians", "degrees"]),
            **kwargs,
        )
