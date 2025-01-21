

import _plotly_utils.basevalidators as _bv


class TextinfoValidator(_bv.FlaglistValidator):
    def __init__(self, plotly_name='textinfo',
                       parent_name='funnelarea',
                       **kwargs):
        super(TextinfoValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 extras=kwargs.pop('extras', ['none']),
                 flags=kwargs.pop('flags', ['label', 'text', 'value', 'percent']),
        **kwargs)