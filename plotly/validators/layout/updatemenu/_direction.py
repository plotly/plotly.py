import _plotly_utils.basevalidators


class DirectionValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self,
        plotly_name='direction',
        parent_name='layout.updatemenu',
        **kwargs
    ):
        super(DirectionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='arraydraw',
            role='info',
            values=['left', 'right', 'up', 'down'],
            **kwargs
        )
