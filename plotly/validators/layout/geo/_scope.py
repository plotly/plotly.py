import _plotly_utils.basevalidators


class ScopeValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self, plotly_name='scope', parent_name='layout.geo', **kwargs
    ):
        super(ScopeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            role='info',
            values=[
                'world', 'usa', 'europe', 'asia', 'africa', 'north america',
                'south america'
            ],
            **kwargs
        )
