import _plotly_utils.basevalidators


class SpikesnapValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self, plotly_name='spikesnap', parent_name='layout.yaxis', **kwargs
    ):
        super(SpikesnapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'none'),
            role=kwargs.pop('role', 'style'),
            values=kwargs.pop('values', ['data', 'cursor']),
            **kwargs
        )
