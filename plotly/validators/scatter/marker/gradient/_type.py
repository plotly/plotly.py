import _plotly_utils.basevalidators as _bv


class TypeValidator(_bv.EnumeratedValidator):
    def __init__(
        self, plotly_name="type", parent_name="scatter.marker.gradient", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            values=kwargs.pop("values", ["radial", "horizontal", "vertical", "none"]),
            **kwargs,
        )
