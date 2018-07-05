import _plotly_utils.basevalidators


class RangeValidator(_plotly_utils.basevalidators.InfoArrayValidator):

    def __init__(
        self, plotly_name='range', parent_name='layout.radialaxis', **kwargs
    ):
        super(RangeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            items=[
                {
                    'valType': 'number',
                    'editType': 'plot'
                }, {
                    'valType': 'number',
                    'editType': 'plot'
                }
            ],
            role='info',
            **kwargs
        )
