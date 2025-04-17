import _plotly_utils.basevalidators as _bv


class SectorValidator(_bv.InfoArrayValidator):
    def __init__(self, plotly_name="sector", parent_name="layout.polar", **kwargs):
        super().__init__(
            plotly_name,
            parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            items=kwargs.pop(
                "items",
                [
                    {"editType": "plot", "valType": "number"},
                    {"editType": "plot", "valType": "number"},
                ],
            ),
            **kwargs,
        )
