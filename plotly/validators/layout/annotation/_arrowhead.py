import _plotly_utils.basevalidators


class ArrowheadValidator(_plotly_utils.basevalidators.IntegerValidator):

    def __init__(
        self,
        plotly_name='arrowhead',
        parent_name='layout.annotation',
        **kwargs
    ):
        super(ArrowheadValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='arraydraw',
            max=8,
            min=0,
            role='style',
            **kwargs
        )
