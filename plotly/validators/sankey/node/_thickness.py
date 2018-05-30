import _plotly_utils.basevalidators


class ThicknessValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self, plotly_name='thickness', parent_name='sankey.node', **kwargs
    ):
        super(ThicknessValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=False,
            edit_type='calc',
            min=1,
            role='style',
            **kwargs
        )
