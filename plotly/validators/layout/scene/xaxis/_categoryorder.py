import _plotly_utils.basevalidators


class CategoryorderValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self,
        plotly_name='categoryorder',
        parent_name='layout.scene.xaxis',
        **kwargs
    ):
        super(CategoryorderValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            role='info',
            values=[
                'trace', 'category ascending', 'category descending', 'array'
            ],
            **kwargs
        )
