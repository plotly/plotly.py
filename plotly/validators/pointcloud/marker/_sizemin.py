import _plotly_utils.basevalidators


class SizeminValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self, plotly_name='sizemin', parent_name='pointcloud.marker', **kwargs
    ):
        super(SizeminValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            max=2,
            min=0.1,
            role='style',
            **kwargs
        )
