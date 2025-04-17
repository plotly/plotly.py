import _plotly_utils.basevalidators as _bv


class UhoverformatValidator(_bv.StringValidator):
    def __init__(self, plotly_name="uhoverformat", parent_name="cone", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
