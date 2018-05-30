import _plotly_utils.basevalidators


class OffsetValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(self, plotly_name='offset', parent_name='bar', **kwargs):
        super(OffsetValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=True,
            edit_type='calc',
            role='info',
            **kwargs
        )
