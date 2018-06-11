import _plotly_utils.basevalidators


class RangeValidator(_plotly_utils.basevalidators.InfoArrayValidator):

    def __init__(
        self,
        plotly_name='range',
        parent_name='layout.xaxis.rangeslider',
        **kwargs
    ):
        super(RangeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            implied_edits={'autorange': False},
            items=[
                {
                    'valType': 'any',
                    'editType': 'calc',
                    'impliedEdits': {
                        '^autorange': False
                    }
                }, {
                    'valType': 'any',
                    'editType': 'calc',
                    'impliedEdits': {
                        '^autorange': False
                    }
                }
            ],
            role='info',
            **kwargs
        )
