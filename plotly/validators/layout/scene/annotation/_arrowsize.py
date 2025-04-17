import _plotly_utils.basevalidators as _bv


class ArrowsizeValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="arrowsize", parent_name="layout.scene.annotation", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0.3),
            **kwargs,
        )
