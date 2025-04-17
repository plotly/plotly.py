import _plotly_utils.basevalidators as _bv


class PullValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="pull", parent_name="pie", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 1),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
