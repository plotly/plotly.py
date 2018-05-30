import _plotly_utils.basevalidators


class TokenValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='token', parent_name='scattergl.stream', **kwargs
    ):
        super(TokenValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            no_blank=True,
            role='info',
            strict=True,
            **kwargs
        )
