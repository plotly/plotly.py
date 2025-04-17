import _plotly_utils.basevalidators as _bv


class ArrowlenValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="arrowlen", parent_name="sankey.link", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
