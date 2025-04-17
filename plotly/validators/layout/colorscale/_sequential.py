import _plotly_utils.basevalidators as _bv


class SequentialValidator(_bv.ColorscaleValidator):
    def __init__(
        self, plotly_name="sequential", parent_name="layout.colorscale", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
