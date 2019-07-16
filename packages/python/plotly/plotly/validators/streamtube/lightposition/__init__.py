import _plotly_utils.basevalidators


class ZValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="z", parent_name="streamtube.lightposition", **kwargs
    ):
        super(ZValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 100000),
            min=kwargs.pop("min", -100000),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class YValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="y", parent_name="streamtube.lightposition", **kwargs
    ):
        super(YValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 100000),
            min=kwargs.pop("min", -100000),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class XValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="x", parent_name="streamtube.lightposition", **kwargs
    ):
        super(XValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            max=kwargs.pop("max", 100000),
            min=kwargs.pop("min", -100000),
            role=kwargs.pop("role", "style"),
            **kwargs
        )
