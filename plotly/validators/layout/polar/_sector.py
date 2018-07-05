import _plotly_utils.basevalidators


class SectorValidator(_plotly_utils.basevalidators.InfoArrayValidator):

    def __init__(
        self, plotly_name='sector', parent_name='layout.polar', **kwargs
    ):
        super(SectorValidator, self).__init__(
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
