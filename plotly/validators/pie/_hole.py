import _plotly_utils.basevalidators


class HoleValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(self, plotly_name='hole', parent_name='pie', **kwargs):
        super(HoleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            max=1,
            min=0,
            role='style',
            **kwargs
        )
