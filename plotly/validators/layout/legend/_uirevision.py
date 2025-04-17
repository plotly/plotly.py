import _plotly_utils.basevalidators as _bv


class UirevisionValidator(_bv.AnyValidator):
    def __init__(self, plotly_name="uirevision", parent_name="layout.legend", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
