import _plotly_utils.basevalidators as _bv


class AngleValidator(_bv.AngleValidator):
    def __init__(
        self, plotly_name="angle", parent_name="layout.polar.radialaxis", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
