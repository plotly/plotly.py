import _plotly_utils.basevalidators


class ArraydtickValidator(_plotly_utils.basevalidators.IntegerValidator):

    def __init__(
        self, plotly_name='arraydtick', parent_name='carpet.aaxis', **kwargs
    ):
        super(ArraydtickValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            min=1,
            role='info',
            **kwargs
        )
