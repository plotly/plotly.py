import _plotly_utils.basevalidators


class ViolingapValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self, plotly_name='violingap', parent_name='layout', **kwargs
    ):
        super(ViolingapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            max=1,
            min=0,
            role='style',
            **kwargs
        )
