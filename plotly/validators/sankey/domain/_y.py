import _plotly_utils.basevalidators


class YValidator(_plotly_utils.basevalidators.InfoArrayValidator):

    def __init__(self, plotly_name='y', parent_name='sankey.domain', **kwargs):
        super(YValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            items=[
                {
                    'valType': 'number',
                    'min': 0,
                    'max': 1,
                    'editType': 'calc'
                }, {
                    'valType': 'number',
                    'min': 0,
                    'max': 1,
                    'editType': 'calc'
                }
            ],
            role='info',
            **kwargs
        )
