import _plotly_utils.basevalidators


class Tick0Validator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="tick0", parent_name="layout.geo.lonaxis", **kwargs):
        super(Tick0Validator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowgridValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="showgrid", parent_name="layout.geo.lonaxis", **kwargs
    ):
        super(ShowgridValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class RangeValidator(_plotly_utils.basevalidators.InfoArrayValidator):
    def __init__(self, plotly_name="range", parent_name="layout.geo.lonaxis", **kwargs):
        super(RangeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            items=kwargs.pop(
                "items",
                [
                    {"valType": "number", "editType": "plot"},
                    {"valType": "number", "editType": "plot"},
                ],
            ),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class GridwidthValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="gridwidth", parent_name="layout.geo.lonaxis", **kwargs
    ):
        super(GridwidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class GridcolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(
        self, plotly_name="gridcolor", parent_name="layout.geo.lonaxis", **kwargs
    ):
        super(GridcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class DtickValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(self, plotly_name="dtick", parent_name="layout.geo.lonaxis", **kwargs):
        super(DtickValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )
