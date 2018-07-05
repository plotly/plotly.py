import _plotly_utils.basevalidators


class RangeValidator(_plotly_utils.basevalidators.InfoArrayValidator):

    def __init__(
        self, plotly_name='range', parent_name='parcoords.dimension', **kwargs
    ):
        super(RangeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            items=[
                {
                    'valType': 'number',
                    'editType': 'calc'
                }, {
                    'valType': 'number',
                    'editType': 'calc'
                }
            ],
            role='info',
            **kwargs
        )
