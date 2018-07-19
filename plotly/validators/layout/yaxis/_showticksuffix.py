import _plotly_utils.basevalidators


class ShowticksuffixValidator(
    _plotly_utils.basevalidators.EnumeratedValidator
):

    def __init__(
        self,
        plotly_name='showticksuffix',
        parent_name='layout.yaxis',
        **kwargs
    ):
        super(ShowticksuffixValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='ticks',
            role='style',
            values=['all', 'first', 'last', 'none'],
            **kwargs
        )
