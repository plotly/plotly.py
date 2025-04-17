import _plotly_utils.basevalidators as _bv


class SuffixValidator(_bv.StringValidator):
    def __init__(self, plotly_name="suffix", parent_name="table.cells", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            array_ok=kwargs.pop("array_ok", True),
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
