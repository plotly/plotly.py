import _plotly_utils.basevalidators as _bv


class XValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="x", parent_name="cone.lightposition", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 100000),
            min=kwargs.pop("min", -100000),
            **kwargs,
        )
