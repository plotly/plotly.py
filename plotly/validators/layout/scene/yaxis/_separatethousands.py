import _plotly_utils.basevalidators as _bv


class SeparatethousandsValidator(_bv.BooleanValidator):
    def __init__(
        self,
        plotly_name="separatethousands",
        parent_name="layout.scene.yaxis",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
