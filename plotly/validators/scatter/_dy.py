import _plotly_utils.basevalidators


class DyValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(self, plotly_name='dy', parent_name='scatter', **kwargs):
        super(DyValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='info',
            **kwargs
        )
