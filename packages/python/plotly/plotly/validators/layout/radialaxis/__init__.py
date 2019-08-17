import _plotly_utils.basevalidators


class VisibleValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="visible", parent_name="layout.radialaxis", **kwargs
    ):
        super(VisibleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TicksuffixValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self, plotly_name="ticksuffix", parent_name="layout.radialaxis", **kwargs
    ):
        super(TicksuffixValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TickorientationValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="tickorientation", parent_name="layout.radialaxis", **kwargs
    ):
        super(TickorientationValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            values=kwargs.pop("values", ["horizontal", "vertical"]),
            **kwargs
        )


import _plotly_utils.basevalidators


class TicklenValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="ticklen", parent_name="layout.radialaxis", **kwargs
    ):
        super(TicklenValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TickcolorValidator(_plotly_utils.basevalidators.ColorValidator):
    def __init__(
        self, plotly_name="tickcolor", parent_name="layout.radialaxis", **kwargs
    ):
        super(TickcolorValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowticklabelsValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="showticklabels", parent_name="layout.radialaxis", **kwargs
    ):
        super(ShowticklabelsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ShowlineValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="showline", parent_name="layout.radialaxis", **kwargs
    ):
        super(ShowlineValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class RangeValidator(_plotly_utils.basevalidators.InfoArrayValidator):
    def __init__(self, plotly_name="range", parent_name="layout.radialaxis", **kwargs):
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


class OrientationValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="orientation", parent_name="layout.radialaxis", **kwargs
    ):
        super(OrientationValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class EndpaddingValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="endpadding", parent_name="layout.radialaxis", **kwargs
    ):
        super(EndpaddingValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class DomainValidator(_plotly_utils.basevalidators.InfoArrayValidator):
    def __init__(self, plotly_name="domain", parent_name="layout.radialaxis", **kwargs):
        super(DomainValidator, self).__init__(
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
