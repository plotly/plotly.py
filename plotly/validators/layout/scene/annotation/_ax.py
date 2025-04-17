import _plotly_utils.basevalidators as _bv


class AxValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="ax", parent_name="layout.scene.annotation", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
