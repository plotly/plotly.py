import _plotly_utils.basevalidators


class TsrcValidator(_plotly_utils.basevalidators.SrcValidator):

    def __init__(self, plotly_name='tsrc', parent_name='scatter', **kwargs):
        super(TsrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'none'),
            role=kwargs.pop('role', 'info'),
            **kwargs
        )
