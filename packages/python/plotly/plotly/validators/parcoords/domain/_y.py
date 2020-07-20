import _plotly_utils.basevalidators


class YValidator(_plotly_utils.basevalidators.InfoArrayValidator):
    def __init__(self, plotly_name="y", parent_name="parcoords.domain", **kwargs):
        super(YValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            items=kwargs.pop(
                "items",
                [
                    {"valType": "number", "min": 0, "max": 1, "editType": "plot"},
                    {"valType": "number", "min": 0, "max": 1, "editType": "plot"},
                ],
            ),
            role=kwargs.pop("role", "info"),
            **kwargs
        )
