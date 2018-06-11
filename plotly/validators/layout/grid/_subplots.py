import _plotly_utils.basevalidators


class SubplotsValidator(_plotly_utils.basevalidators.InfoArrayValidator):

    def __init__(
        self, plotly_name='subplots', parent_name='layout.grid', **kwargs
    ):
        super(SubplotsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            dimensions=2,
            edit_type='plot',
            free_length=True,
            items={
                'valType': 'enumerated',
                'values':
                ['/^x([2-9]|[1-9][0-9]+)?y([2-9]|[1-9][0-9]+)?$/', ''],
                'editType': 'plot'
            },
            role='info',
            **kwargs
        )
