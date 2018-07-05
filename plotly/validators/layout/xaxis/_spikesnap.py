import _plotly_utils.basevalidators


class SpikesnapValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self, plotly_name='spikesnap', parent_name='layout.xaxis', **kwargs
    ):
        super(SpikesnapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='style',
            values=['data', 'cursor'],
            **kwargs
        )
