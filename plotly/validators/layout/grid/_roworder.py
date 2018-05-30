import _plotly_utils.basevalidators


class RoworderValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self, plotly_name='roworder', parent_name='layout.grid', **kwargs
    ):
        super(RoworderValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            role='info',
            values=['top to bottom', 'bottom to top'],
            **kwargs
        )
