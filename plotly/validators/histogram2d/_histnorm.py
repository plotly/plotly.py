import _plotly_utils.basevalidators as _bv


class HistnormValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="histnorm", parent_name="histogram2d", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop(
                "values",
                ["", "percent", "probability", "density", "probability density"],
            ),
            **kwargs,
        )
