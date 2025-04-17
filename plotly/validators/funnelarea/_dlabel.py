import _plotly_utils.basevalidators as _bv


class DlabelValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="dlabel", parent_name="funnelarea", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
