import _plotly_utils.basevalidators as _bv


class LegendgroupValidator(_bv.StringValidator):
    def __init__(self, plotly_name="legendgroup", parent_name="layout.shape", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc+arraydraw"),
            **kwargs,
        )
