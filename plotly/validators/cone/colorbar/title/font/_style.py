import _plotly_utils.basevalidators as _bv


class StyleValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="style", parent_name="cone.colorbar.title.font", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "colorbars"),
            values=kwargs.pop("values", ["normal", "italic"]),
            **kwargs,
        )
