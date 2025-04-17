import _plotly_utils.basevalidators as _bv


class ThicknessValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="thickness", parent_name="sankey.node", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            array_ok=kwargs.pop("array_ok", False),
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 1),
            **kwargs,
        )
