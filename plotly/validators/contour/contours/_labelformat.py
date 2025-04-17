import _plotly_utils.basevalidators as _bv


class LabelformatValidator(_bv.StringValidator):
    def __init__(
        self, plotly_name="labelformat", parent_name="contour.contours", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
