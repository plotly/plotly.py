import _plotly_utils.basevalidators


class CminValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self, plotly_name='cmin', parent_name='histogram.marker', **kwargs
    ):
        super(CminValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            implied_edits={'cauto': False},
            role='info',
            **kwargs
        )
