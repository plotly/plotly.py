import _plotly_utils.basevalidators


class CheatertypeValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self, plotly_name='cheatertype', parent_name='carpet.aaxis', **kwargs
    ):
        super(CheatertypeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='info',
            values=['index', 'value'],
            **kwargs
        )
