import _plotly_utils.basevalidators


class OrientationValidator(_plotly_utils.basevalidators.AngleValidator):

    def __init__(
        self, plotly_name='orientation', parent_name='layout', **kwargs
    ):
        super(OrientationValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'plot'),
            role=kwargs.pop('role', 'info'),
            **kwargs
        )
