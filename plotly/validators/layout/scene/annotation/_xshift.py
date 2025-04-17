import _plotly_utils.basevalidators as _bv


class XshiftValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="xshift", parent_name="layout.scene.annotation", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
