import _plotly_utils.basevalidators as _bv


class ScaleValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="scale", parent_name="scatter3d.projection.y", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 10),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
