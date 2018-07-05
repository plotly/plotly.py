import _plotly_utils.basevalidators


class ArgsValidator(_plotly_utils.basevalidators.InfoArrayValidator):

    def __init__(
        self, plotly_name='args', parent_name='layout.slider.step', **kwargs
    ):
        super(ArgsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='arraydraw',
            free_length=True,
            items=[
                {
                    'valType': 'any',
                    'editType': 'arraydraw'
                }, {
                    'valType': 'any',
                    'editType': 'arraydraw'
                }, {
                    'valType': 'any',
                    'editType': 'arraydraw'
                }
            ],
            role='info',
            **kwargs
        )
