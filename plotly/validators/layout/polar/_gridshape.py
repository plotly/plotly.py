import _plotly_utils.basevalidators as _bv


class GridshapeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="gridshape", parent_name="layout.polar", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            values=kwargs.pop("values", ["circular", "linear"]),
            **kwargs,
        )
