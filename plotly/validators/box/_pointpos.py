import _plotly_utils.basevalidators


class PointposValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(self, plotly_name='pointpos', parent_name='box', **kwargs):
        super(PointposValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            max=2,
            min=-2,
            role='style',
            **kwargs
        )
