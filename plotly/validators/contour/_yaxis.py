import _plotly_utils.basevalidators


class YAxisValidator(_plotly_utils.basevalidators.SubplotidValidator):

    def __init__(self, plotly_name='yaxis', parent_name='contour', **kwargs):
        super(YAxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            dflt='y',
            edit_type='calc+clearAxisTypes',
            role='info',
            **kwargs
        )
