import _plotly_utils.basevalidators as _bv


class MaxpointsValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="maxpoints", parent_name="splom.stream", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 10000),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
