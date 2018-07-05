import _plotly_utils.basevalidators


class SideValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self,
        plotly_name='side',
        parent_name='layout.polar.radialaxis',
        **kwargs
    ):
        super(SideValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            role='info',
            values=['clockwise', 'counterclockwise'],
            **kwargs
        )
