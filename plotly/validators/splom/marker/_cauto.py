import _plotly_utils.basevalidators


class CautoValidator(_plotly_utils.basevalidators.BooleanValidator):

    def __init__(
        self, plotly_name='cauto', parent_name='splom.marker', **kwargs
    ):
        super(CautoValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            implied_edits={},
            role='info',
            **kwargs
        )
