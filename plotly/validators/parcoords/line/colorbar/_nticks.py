import _plotly_utils.basevalidators


class NticksValidator(_plotly_utils.basevalidators.IntegerValidator):

    def __init__(
        self,
        plotly_name='nticks',
        parent_name='parcoords.line.colorbar',
        **kwargs
    ):
        super(NticksValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='colorbars',
            min=0,
            role='style',
            **kwargs
        )
