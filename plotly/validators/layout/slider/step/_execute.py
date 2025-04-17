import _plotly_utils.basevalidators as _bv


class ExecuteValidator(_bv.BooleanValidator):
    def __init__(
        self, plotly_name="execute", parent_name="layout.slider.step", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            **kwargs,
        )
