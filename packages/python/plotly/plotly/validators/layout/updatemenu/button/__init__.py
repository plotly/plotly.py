import _plotly_utils.basevalidators


class VisibleValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="visible", parent_name="layout.updatemenu.button", **kwargs
    ):
        super(VisibleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class TemplateitemnameValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self,
        plotly_name="templateitemname",
        parent_name="layout.updatemenu.button",
        **kwargs
    ):
        super(TemplateitemnameValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class NameValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self, plotly_name="name", parent_name="layout.updatemenu.button", **kwargs
    ):
        super(NameValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class MethodValidator(_plotly_utils.basevalidators.EnumeratedValidator):
    def __init__(
        self, plotly_name="method", parent_name="layout.updatemenu.button", **kwargs
    ):
        super(MethodValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "info"),
            values=kwargs.pop(
                "values", ["restyle", "relayout", "animate", "update", "skip"]
            ),
            **kwargs
        )


import _plotly_utils.basevalidators


class LabelValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(
        self, plotly_name="label", parent_name="layout.updatemenu.button", **kwargs
    ):
        super(LabelValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ExecuteValidator(_plotly_utils.basevalidators.BooleanValidator):
    def __init__(
        self, plotly_name="execute", parent_name="layout.updatemenu.button", **kwargs
    ):
        super(ExecuteValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class ArgsValidator(_plotly_utils.basevalidators.InfoArrayValidator):
    def __init__(
        self, plotly_name="args", parent_name="layout.updatemenu.button", **kwargs
    ):
        super(ArgsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "arraydraw"),
            free_length=kwargs.pop("free_length", True),
            items=kwargs.pop(
                "items",
                [
                    {"valType": "any", "editType": "arraydraw"},
                    {"valType": "any", "editType": "arraydraw"},
                    {"valType": "any", "editType": "arraydraw"},
                ],
            ),
            role=kwargs.pop("role", "info"),
            **kwargs
        )
