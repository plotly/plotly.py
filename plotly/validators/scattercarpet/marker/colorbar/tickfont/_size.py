import _plotly_utils.basevalidators


class SizeValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self,
        plotly_name='size',
        parent_name='scattercarpet.marker.colorbar.tickfont',
        **kwargs
    ):
        super(SizeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='colorbars',
            min=1,
            role='style',
            **kwargs
        )
