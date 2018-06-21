import _plotly_utils.basevalidators


class YpadValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self,
        plotly_name='ypad',
        parent_name='scatter.marker.colorbar',
        **kwargs
    ):
        super(YpadValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='colorbars',
            min=0,
            role='style',
            **kwargs
        )
