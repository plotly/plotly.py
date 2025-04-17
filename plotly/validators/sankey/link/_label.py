import _plotly_utils.basevalidators as _bv


class LabelValidator(_bv.DataArrayValidator):
    def __init__(self, plotly_name="label", parent_name="sankey.link", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
