import _plotly_utils.basevalidators as _bv


class ValueValidator(_bv.AnyValidator):
    def __init__(self, plotly_name="value", parent_name="contour.contours", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
