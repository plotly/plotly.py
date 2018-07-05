import _plotly_utils.basevalidators


class AccesstokenValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='accesstoken', parent_name='layout.mapbox', **kwargs
    ):
        super(AccesstokenValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            no_blank=True,
            role='info',
            strict=True,
            **kwargs
        )
