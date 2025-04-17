import _plotly_utils.basevalidators as _bv


class OffsetValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="offset", parent_name="carpet.baxis.title", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
