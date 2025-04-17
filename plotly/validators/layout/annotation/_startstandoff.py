import _plotly_utils.basevalidators as _bv


class StartstandoffValidator(_bv.NumberValidator):
    def __init__(
        self, plotly_name="startstandoff", parent_name="layout.annotation", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc+arraydraw"),
            min=kwargs.pop("min", 0),
            **kwargs,
        )
