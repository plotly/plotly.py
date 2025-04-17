import _plotly_utils.basevalidators as _bv


class VhoverformatValidator(_bv.StringValidator):
    def __init__(self, plotly_name="vhoverformat", parent_name="cone", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
