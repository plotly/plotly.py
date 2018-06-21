import _plotly_utils.basevalidators


class BargroupgapValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self, plotly_name='bargroupgap', parent_name='layout', **kwargs
    ):
        super(BargroupgapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            max=1,
            min=0,
            role='style',
            **kwargs
        )
