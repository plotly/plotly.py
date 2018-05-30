import _plotly_utils.basevalidators


class OpacityValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self,
        plotly_name='opacity',
        parent_name='scatterpolar.marker',
        **kwargs
    ):
        super(OpacityValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=True,
            edit_type='style',
            max=1,
            min=0,
            role='style',
            **kwargs
        )
