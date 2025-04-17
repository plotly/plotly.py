import _plotly_utils.basevalidators as _bv


class ArrowwidthValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="arrowwidth", parent_name="layout.annotation", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc+arraydraw"),
            min=kwargs.pop("min", 0.1),
            **kwargs,
        )
