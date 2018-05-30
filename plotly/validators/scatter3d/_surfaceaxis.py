import _plotly_utils.basevalidators


class SurfaceaxisValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self, plotly_name='surfaceaxis', parent_name='scatter3d', **kwargs
    ):
        super(SurfaceaxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='info',
            values=[-1, 0, 1, 2],
            **kwargs
        )
