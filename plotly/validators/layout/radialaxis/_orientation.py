import _plotly_utils.basevalidators


class OrientationValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self,
        plotly_name='orientation',
        parent_name='layout.radialaxis',
        **kwargs
    ):
        super(OrientationValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            role='style',
            **kwargs
        )
