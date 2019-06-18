import _plotly_utils.basevalidators


class YValidator(_plotly_utils.basevalidators.InfoArrayValidator):
    def __init__(self, plotly_name="y", parent_name="table.domain", **kwargs):
        super(YValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            items=kwargs.pop(
                "items",
                [
                    {"valType": "number", "min": 0, "max": 1, "editType": "calc"},
                    {"valType": "number", "min": 0, "max": 1, "editType": "calc"},
                ],
            ),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class XValidator(_plotly_utils.basevalidators.InfoArrayValidator):
    def __init__(self, plotly_name="x", parent_name="table.domain", **kwargs):
        super(XValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            items=kwargs.pop(
                "items",
                [
                    {"valType": "number", "min": 0, "max": 1, "editType": "calc"},
                    {"valType": "number", "min": 0, "max": 1, "editType": "calc"},
                ],
            ),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class RowValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(self, plotly_name="row", parent_name="table.domain", **kwargs):
        super(RowValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ColumnValidator(_plotly_utils.basevalidators.IntegerValidator):
    def __init__(self, plotly_name="column", parent_name="table.domain", **kwargs):
        super(ColumnValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "info"),
            **kwargs
        )
