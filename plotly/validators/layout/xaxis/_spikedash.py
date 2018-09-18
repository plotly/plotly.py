import _plotly_utils.basevalidators


class SpikedashValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='spikedash', parent_name='layout.xaxis', **kwargs
    ):
        super(SpikedashValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='style',
            values=[
                'solid', 'dot', 'dash', 'longdash', 'dashdot', 'longdashdot'
            ],
            **kwargs
        )
