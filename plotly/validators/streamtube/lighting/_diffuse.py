import _plotly_utils.basevalidators


class DiffuseValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self,
        plotly_name='diffuse',
        parent_name='streamtube.lighting',
        **kwargs
    ):
        super(DiffuseValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            max=1,
            min=0,
            role='style',
            **kwargs
        )
