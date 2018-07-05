import _plotly_utils.basevalidators


class BoxgroupgapValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self, plotly_name='boxgroupgap', parent_name='layout', **kwargs
    ):
        super(BoxgroupgapValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            max=1,
            min=0,
            role='style',
            **kwargs
        )
