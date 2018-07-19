import _plotly_utils.basevalidators


class ZValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self,
        plotly_name='z',
        parent_name='streamtube.lightposition',
        **kwargs
    ):
        super(ZValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            max=100000,
            min=-100000,
            role='style',
            **kwargs
        )
