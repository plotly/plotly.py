import _plotly_utils.basevalidators as _bv


class DragmodeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name="dragmode", parent_name="layout.scene", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            values=kwargs.pop("values", ["orbit", "turntable", "zoom", "pan", False]),
            **kwargs,
        )
