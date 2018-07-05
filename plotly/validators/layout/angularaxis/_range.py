import _plotly_utils.basevalidators


class RangeValidator(_plotly_utils.basevalidators.InfoArrayValidator):

    def __init__(
        self, plotly_name='range', parent_name='layout.angularaxis', **kwargs
    ):
        super(RangeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            items=[
                {
                    'valType': 'number',
                    'dflt': 0,
                    'editType': 'plot'
                }, {
                    'valType': 'number',
                    'dflt': 360,
                    'editType': 'plot'
                }
            ],
            role='info',
            **kwargs
        )
