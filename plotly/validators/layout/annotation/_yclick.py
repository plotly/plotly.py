import _plotly_utils.basevalidators as _bv


class YclickValidator(_bv.AnyValidator):
    def __init__(self, plotly_name="yclick", parent_name="layout.annotation", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            **kwargs,
        )
