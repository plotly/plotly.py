import _plotly_utils.basevalidators as _bv


class YhoverformatValidator(_bv.StringValidator):
    def __init__(self, plotly_name="yhoverformat", parent_name="volume", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
