import _plotly_utils.basevalidators


class RowsValidator(_plotly_utils.basevalidators.IntegerValidator):

    def __init__(
        self, plotly_name='rows', parent_name='layout.grid', **kwargs
    ):
        super(RowsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            min=1,
            role='info',
            **kwargs
        )
