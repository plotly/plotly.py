import _plotly_utils.basevalidators


class LocationmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self, plotly_name='locationmode', parent_name='choropleth', **kwargs
    ):
        super(LocationmodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='info',
            values=['ISO-3', 'USA-states', 'country names'],
            **kwargs
        )
