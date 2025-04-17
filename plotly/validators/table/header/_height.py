import _plotly_utils.basevalidators as _bv


class HeightValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="height", parent_name="table.header", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
