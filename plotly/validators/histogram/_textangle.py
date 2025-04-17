import _plotly_utils.basevalidators as _bv


class TextangleValidator(_bv.AngleValidator):
    def __init__(self, plotly_name="textangle", parent_name="histogram", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
