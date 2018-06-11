import _plotly_utils.basevalidators


class RoughnessValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self, plotly_name='roughness', parent_name='cone.lighting', **kwargs
    ):
        super(RoughnessValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            max=1,
            min=0,
            role='style',
            **kwargs
        )
