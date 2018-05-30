import _plotly_utils.basevalidators


class ColumnwidthsrcValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='columnwidthsrc', parent_name='table', **kwargs
    ):
        super(ColumnwidthsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
