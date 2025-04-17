import _plotly_utils.basevalidators as _bv


class FramewidthValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="framewidth", parent_name="layout.geo", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
