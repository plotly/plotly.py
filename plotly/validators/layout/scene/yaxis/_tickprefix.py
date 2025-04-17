import _plotly_utils.basevalidators as _bv


class TickprefixValidator(_bv.StringValidator):
    def __init__(
        self, plotly_name="tickprefix", parent_name="layout.scene.yaxis", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            **kwargs,
        )
