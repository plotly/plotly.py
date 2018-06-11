import _plotly_utils.basevalidators


class XaxesValidator(_plotly_utils.basevalidators.InfoArrayValidator):

    def __init__(
        self, plotly_name='xaxes', parent_name='layout.grid', **kwargs
    ):
        super(XaxesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            free_length=True,
            items={
                'valType': 'enumerated',
                'values': ['/^x([2-9]|[1-9][0-9]+)?$/', ''],
                'editType': 'plot'
            },
            role='info',
            **kwargs
        )
