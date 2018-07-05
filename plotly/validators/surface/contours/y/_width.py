import _plotly_utils.basevalidators


class WidthValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self, plotly_name='width', parent_name='surface.contours.y', **kwargs
    ):
        super(WidthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            max=16,
            min=1,
            role='style',
            **kwargs
        )
