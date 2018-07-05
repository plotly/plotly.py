import _plotly_utils.basevalidators


class CopyZstyleValidator(_plotly_utils.basevalidators.BooleanValidator):

    def __init__(
        self,
        plotly_name='copy_zstyle',
        parent_name='scatter3d.error_x',
        **kwargs
    ):
        super(CopyZstyleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='style',
            **kwargs
        )
