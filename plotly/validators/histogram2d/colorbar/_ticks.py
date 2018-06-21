import _plotly_utils.basevalidators


class TicksValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self,
        plotly_name='ticks',
        parent_name='histogram2d.colorbar',
        **kwargs
    ):
        super(TicksValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='colorbars',
            role='style',
            values=['outside', 'inside', ''],
            **kwargs
        )
