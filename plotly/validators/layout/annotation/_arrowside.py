import _plotly_utils.basevalidators


class ArrowsideValidator(_plotly_utils.basevalidators.FlaglistValidator):

    def __init__(
        self,
        plotly_name='arrowside',
        parent_name='layout.annotation',
        **kwargs
    ):
        super(ArrowsideValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='arraydraw',
            extras=['none'],
            flags=['end', 'start'],
            role='style',
            **kwargs
        )
