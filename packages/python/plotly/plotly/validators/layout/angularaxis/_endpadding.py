import _plotly_utils.basevalidators


class EndpaddingValidator(_plotly_utils.basevalidators.NumberValidator):
    def __init__(
        self, plotly_name="endpadding", parent_name="layout.angularaxis", **kwargs
    ):
        super(EndpaddingValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop("edit_type", "plot"),
            role=kwargs.pop("role", "style"),
            **kwargs
        )
