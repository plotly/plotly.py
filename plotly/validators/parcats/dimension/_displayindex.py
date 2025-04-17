import _plotly_utils.basevalidators as _bv


class DisplayindexValidator(_bv.IntegerValidator):
    def __init__(
        self, plotly_name="displayindex", parent_name="parcats.dimension", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
