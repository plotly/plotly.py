import _plotly_utils.basevalidators


class BaseValidator(_plotly_utils.basevalidators.AnyValidator):

    def __init__(self, plotly_name='base', parent_name='bar', **kwargs):
        super(BaseValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=True,
            edit_type='calc',
            role='info',
            **kwargs
        )
