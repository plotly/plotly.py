import _plotly_utils.basevalidators as _bv


class SubunitcolorValidator(_bv.ColorValidator):
    def __init__(self, plotly_name="subunitcolor", parent_name="layout.geo", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
