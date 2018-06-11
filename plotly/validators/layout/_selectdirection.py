import _plotly_utils.basevalidators


class SelectdirectionValidator(
    _plotly_utils.basevalidators.EnumeratedValidator
):

    def __init__(
        self, plotly_name='selectdirection', parent_name='layout', **kwargs
    ):
        super(SelectdirectionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            values=['h', 'v', 'd', 'any'],
            **kwargs
        )
