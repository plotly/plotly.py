import _plotly_utils.basevalidators


class TickorientationValidator(
    _plotly_utils.basevalidators.EnumeratedValidator
):

    def __init__(
        self,
        plotly_name='tickorientation',
        parent_name='layout.angularaxis',
        **kwargs
    ):
        super(TickorientationValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'plot'),
            role=kwargs.pop('role', 'style'),
            values=kwargs.pop('values', ['horizontal', 'vertical']),
            **kwargs
        )
