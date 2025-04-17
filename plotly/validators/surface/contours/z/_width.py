import _plotly_utils.basevalidators as _bv


class WidthValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="width", parent_name="surface.contours.z", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 16),
            min=kwargs.pop("min", 1),
            **kwargs,
        )
