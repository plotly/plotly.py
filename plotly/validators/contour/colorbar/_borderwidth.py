import _plotly_utils.basevalidators


class BorderwidthValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self,
        plotly_name='borderwidth',
        parent_name='contour.colorbar',
        **kwargs
    ):
        super(BorderwidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='colorbars',
            min=0,
            role='style',
            **kwargs
        )
