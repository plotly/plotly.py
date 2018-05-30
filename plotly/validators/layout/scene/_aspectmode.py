import _plotly_utils.basevalidators


class AspectmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self, plotly_name='aspectmode', parent_name='layout.scene', **kwargs
    ):
        super(AspectmodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            implied_edits={},
            role='info',
            values=['auto', 'cube', 'data', 'manual'],
            **kwargs
        )
