import _plotly_utils.basevalidators as _bv


class SeparatethousandsValidator(_bv.BooleanValidator):
    def __init__(
        self,
        plotly_name="separatethousands",
        parent_name="scatterpolargl.marker.colorbar",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
