import _plotly_utils.basevalidators


class StartarrowsizeValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self,
        plotly_name='startarrowsize',
        parent_name='layout.annotation',
        **kwargs
    ):
        super(StartarrowsizeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc+arraydraw',
            min=0.3,
            role='style',
            **kwargs
        )
