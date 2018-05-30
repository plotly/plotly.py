import _plotly_utils.basevalidators


class LValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self, plotly_name='l', parent_name='layout.updatemenu.pad', **kwargs
    ):
        super(LValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='arraydraw',
            role='style',
            **kwargs
        )
