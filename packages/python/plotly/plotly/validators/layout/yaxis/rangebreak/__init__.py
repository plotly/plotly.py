import _plotly_utils.basevalidators


class ValuesValidator(_plotly_utils.basevalidators.InfoArrayValidator):
    def __init__(
        self, plotly_name="values", parent_name="layout.yaxis.rangebreak", **kwargs
    ):
        super(ValuesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            free_length=kwargs.pop("free_length", True),
            items=kwargs.pop("items", {"valType": "any", "editType": "calc"}),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TemplateitemnameValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self,
        plotly_name="templateitemname",
        parent_name="layout.yaxis.rangebreak",
        **kwargs
    ):
        super(TemplateitemnameValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class PatternValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="pattern", parent_name="layout.yaxis.rangebreak", **kwargs
    ):
        super(PatternValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop("values", ["day of week", "hour", ""]),
            **kwargs
        )


import _plotly_utils.basevalidators


class NameValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self, plotly_name="name", parent_name="layout.yaxis.rangebreak", **kwargs
    ):
        super(NameValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "none"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class EnabledValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="enabled", parent_name="layout.yaxis.rangebreak", **kwargs
    ):
        super(EnabledValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class DvalueValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="dvalue", parent_name="layout.yaxis.rangebreak", **kwargs
    ):
        super(DvalueValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            min=kwargs.pop("min", 0),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class BoundsValidator(_plotly_utils.basevalidators.InfoArrayValidator):
    def __init__(
        self, plotly_name="bounds", parent_name="layout.yaxis.rangebreak", **kwargs
    ):
        super(BoundsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            items=kwargs.pop(
                "items",
                [
                    {"valType": "any", "editType": "calc"},
                    {"valType": "any", "editType": "calc"},
                ],
            ),
            role=kwargs.pop("role", "info"),
            **kwargs
        )
