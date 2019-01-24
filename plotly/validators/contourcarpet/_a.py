import _plotly_utils.basevalidators


class AValidator(_plotly_utils.basevalidators.DataArrayValidator):

    def __init__(self, plotly_name='a', parent_name='contourcarpet', **kwargs):
        super(AValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            anim=kwargs.pop('anim', True),
            edit_type=kwargs.pop('edit_type', 'calc+clearAxisTypes'),
            implied_edits=kwargs.pop('implied_edits', {'xtype': 'array'}),
            role=kwargs.pop('role', 'data'),
            **kwargs
        )
