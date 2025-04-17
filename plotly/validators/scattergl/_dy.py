import _plotly_utils.basevalidators as _bv


class DyValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="dy", parent_name="scattergl", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
