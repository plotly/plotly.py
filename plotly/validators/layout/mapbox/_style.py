import _plotly_utils.basevalidators


class StyleValidator(_plotly_utils.basevalidators.AnyValidator):

    def __init__(
        self, plotly_name='style', parent_name='layout.mapbox', **kwargs
    ):
        super(StyleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            role='style',
            values=[
                'basic', 'streets', 'outdoors', 'light', 'dark', 'satellite',
                'satellite-streets'
            ],
            **kwargs
        )
