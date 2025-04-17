import _plotly_utils.basevalidators as _bv


class TickvalssrcValidator(_bv.SrcValidator):
    def __init__(
        self,
        plotly_name="tickvalssrc",
        parent_name="histogram2dcontour.colorbar",
        **kwargs,
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            **kwargs,
        )
