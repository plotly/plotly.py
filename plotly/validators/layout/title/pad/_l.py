import _plotly_utils.basevalidators as _bv


class LValidator(_bv.NumberValidator):
    def __init__(self, plotly_name="l", parent_name="layout.title.pad", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "layoutstyle"),
            **kwargs,
        )
