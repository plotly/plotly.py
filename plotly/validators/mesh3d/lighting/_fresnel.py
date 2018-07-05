import _plotly_utils.basevalidators


class FresnelValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self, plotly_name='fresnel', parent_name='mesh3d.lighting', **kwargs
    ):
        super(FresnelValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            max=5,
            min=0,
            role='style',
            **kwargs
        )
