import _plotly_utils.basevalidators


class SizeValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self, plotly_name='size', parent_name='violin.marker', **kwargs
    ):
        super(SizeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=False,
            edit_type='calc',
            min=0,
            role='style',
            **kwargs
        )
