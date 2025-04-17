import _plotly_utils.basevalidators as _bv


class EndlinecolorValidator(_bv.ColorValidator):
    def __init__(
        self, plotly_name="endlinecolor", parent_name="carpet.baxis", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
