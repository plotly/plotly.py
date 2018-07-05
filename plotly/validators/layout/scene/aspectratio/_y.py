import _plotly_utils.basevalidators


class YValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self,
        plotly_name='y',
        parent_name='layout.scene.aspectratio',
        **kwargs
    ):
        super(YValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            implied_edits={'^aspectmode': 'manual'},
            min=0,
            role='info',
            **kwargs
        )
