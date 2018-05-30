import _plotly_utils.basevalidators


class ValignValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self, plotly_name='valign', parent_name='layout.annotation', **kwargs
    ):
        super(ValignValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='arraydraw',
            role='style',
            values=['top', 'middle', 'bottom'],
            **kwargs
        )
