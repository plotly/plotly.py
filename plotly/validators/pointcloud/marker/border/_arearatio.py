import _plotly_utils.basevalidators


class ArearatioValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self,
        plotly_name='arearatio',
        parent_name='pointcloud.marker.border',
        **kwargs
    ):
        super(ArearatioValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            max=1,
            min=0,
            role='style',
            **kwargs
        )
