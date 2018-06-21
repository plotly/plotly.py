import _plotly_utils.basevalidators


class SizemodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self,
        plotly_name='sizemode',
        parent_name='scattermapbox.marker',
        **kwargs
    ):
        super(SizemodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='info',
            values=['diameter', 'area'],
            **kwargs
        )
