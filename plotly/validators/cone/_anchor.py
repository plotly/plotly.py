import _plotly_utils.basevalidators as _bv


class AnchorValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="anchor", parent_name="cone", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", ["tip", "tail", "cm", "center"]),
            **kwargs,
        )
