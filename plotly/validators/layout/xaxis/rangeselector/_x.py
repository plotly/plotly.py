import _plotly_utils.basevalidators


class XValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self,
        plotly_name='x',
        parent_name='layout.xaxis.rangeselector',
        **kwargs
    ):
        super(XValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            max=3,
            min=-2,
            role='style',
            **kwargs
        )
