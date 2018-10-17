import _plotly_utils.basevalidators


class CategoryorderValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self,
        plotly_name='categoryorder',
        parent_name='layout.polar.radialaxis',
        **kwargs
    ):
        super(CategoryorderValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'calc'),
            role=kwargs.pop('role', 'info'),
            values=kwargs.pop(
                'values', [
                    'trace', 'category ascending', 'category descending',
                    'array'
                ]
            ),
            **kwargs
        )
