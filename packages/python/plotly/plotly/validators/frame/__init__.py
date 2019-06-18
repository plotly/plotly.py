import _plotly_utils.basevalidators


class TracesValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="traces", parent_name="frame", **kwargs):
        super(TracesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import _plotly_utils.basevalidators


class NameValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="name", parent_name="frame", **kwargs):
        super(NameValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import plotly.validators


class LayoutValidator(plotly.validators.LayoutValidator):
    def __init__(self, plotly_name="layout", parent_name="frame", **kwargs):
        super(LayoutValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            role=kwargs.pop("role", "object"),
            **kwargs
        )


import _plotly_utils.basevalidators


class GroupValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="group", parent_name="frame", **kwargs):
        super(GroupValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            role=kwargs.pop("role", "info"),
            **kwargs
        )


import plotly.validators


class DataValidator(plotly.validators.DataValidator):
    def __init__(self, plotly_name="data", parent_name="frame", **kwargs):
        super(DataValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            role=kwargs.pop("role", "object"),
            **kwargs
        )


import _plotly_utils.basevalidators


class BaseframeValidator(_plotly_utils.basevalidators.StringValidator):
    def __init__(self, plotly_name="baseframe", parent_name="frame", **kwargs):
        super(BaseframeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            role=kwargs.pop("role", "info"),
            **kwargs
        )
