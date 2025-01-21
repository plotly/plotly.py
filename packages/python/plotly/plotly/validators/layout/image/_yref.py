

import _plotly_utils.basevalidators as _bv


class YrefValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='yref',
                       parent_name='layout.image',
                       **kwargs):
        super(YrefValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'arraydraw'),
                 values=kwargs.pop('values', ['paper', '/^y([2-9]|[1-9][0-9]+)?( domain)?$/']),
        **kwargs)