import _plotly_utils.basevalidators


class HeightValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self, plotly_name='height', parent_name='layout.annotation', **kwargs
    ):
        super(HeightValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc+arraydraw',
            min=1,
            role='style',
            **kwargs
        )
