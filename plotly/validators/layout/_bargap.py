import _plotly_utils.basevalidators


class BargapValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(self, plotly_name='bargap', parent_name='layout', **kwargs):
        super(BargapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            max=1,
            min=0,
            role='style',
            **kwargs
        )
