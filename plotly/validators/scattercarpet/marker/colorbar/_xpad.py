import _plotly_utils.basevalidators


class XpadValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self,
        plotly_name='xpad',
        parent_name='scattercarpet.marker.colorbar',
        **kwargs
    ):
        super(XpadValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='colorbars',
            min=0,
            role='style',
            **kwargs
        )
