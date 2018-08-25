import _plotly_utils.basevalidators


class AutorangeValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self, plotly_name='autorange', parent_name='layout.yaxis', **kwargs
    ):
        super(AutorangeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='axrange',
            implied_edits={},
            role='info',
            values=[True, False, 'reversed'],
            **kwargs
        )
