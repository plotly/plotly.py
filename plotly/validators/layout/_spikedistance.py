import _plotly_utils.basevalidators


class SpikedistanceValidator(_plotly_utils.basevalidators.IntegerValidator):

    def __init__(
        self, plotly_name='spikedistance', parent_name='layout', **kwargs
    ):
        super(SpikedistanceValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            min=-1,
            role='info',
            **kwargs
        )
