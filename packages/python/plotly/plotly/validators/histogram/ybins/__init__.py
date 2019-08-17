import _plotly_utils.basevalidators


class StartValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="start", parent_name="histogram.ybins", **kwargs):
        super(StartValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class SizeValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="size", parent_name="histogram.ybins", **kwargs):
        super(SizeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )


import _plotly_utils.basevalidators


class EndValidator(_plotly_utils.basevalidators.AnyValidator):
    def __init__(self, plotly_name="end", parent_name="histogram.ybins", **kwargs):
        super(EndValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "calc"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )
