import _plotly_utils.basevalidators


class XAxisValidator(_plotly_utils.basevalidators.SubplotidValidator):

    def __init__(self, plotly_name='xaxis', parent_name='heatmapgl', **kwargs):
        super(XAxisValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            dflt=kwargs.pop('dflt', 'x'),
            edit_type=kwargs.pop('edit_type', 'calc+clearAxisTypes'),
            role=kwargs.pop('role', 'info'),
            **kwargs
        )
