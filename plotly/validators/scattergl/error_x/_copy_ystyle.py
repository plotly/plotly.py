import _plotly_utils.basevalidators


class CopyYstyleValidator(_plotly_utils.basevalidators.BooleanValidator):

    def __init__(
        self,
        plotly_name='copy_ystyle',
        parent_name='scattergl.error_x',
        **kwargs
    ):
        super(CopyYstyleValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='style',
            **kwargs
        )
