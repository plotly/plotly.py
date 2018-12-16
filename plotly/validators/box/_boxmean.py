import _plotly_utils.basevalidators


class BoxmeanValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(self, plotly_name='boxmean', parent_name='box', **kwargs):
        super(BoxmeanValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='style',
            values=[True, 'sd', False],
            **kwargs
        )
