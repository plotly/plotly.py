import _plotly_utils.basevalidators


class SmoothingValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self,
        plotly_name='smoothing',
        parent_name='scatterternary.line',
        **kwargs
    ):
        super(SmoothingValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            max=1.3,
            min=0,
            role='style',
            **kwargs
        )
