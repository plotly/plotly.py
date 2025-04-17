import _plotly_utils.basevalidators as _bv


class XbingroupValidator(_bv.StringValidator):
    def __init__(
        self, plotly_name="xbingroup", parent_name="histogram2dcontour", **kwargs
    ):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            **kwargs,
        )
