import _plotly_utils.basevalidators as _bv


class IciclecolorwayValidator(_bv.ColorlistValidator):
    def __init__(self, plotly_name="iciclecolorway", parent_name="layout", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
