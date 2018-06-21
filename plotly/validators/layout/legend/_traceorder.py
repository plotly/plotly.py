import _plotly_utils.basevalidators


class TraceorderValidator(_plotly_utils.basevalidators.FlaglistValidator):

    def __init__(
        self, plotly_name='traceorder', parent_name='layout.legend', **kwargs
    ):
        super(TraceorderValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='legend',
            extras=['normal'],
            flags=['reversed', 'grouped'],
            role='style',
            **kwargs
        )
