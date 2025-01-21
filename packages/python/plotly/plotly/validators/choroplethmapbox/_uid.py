

import _plotly_utils.basevalidators as _bv


class UidValidator(_bv.StringValidator):
    def __init__(self, plotly_name='uid',
                       parent_name='choroplethmapbox',
                       **kwargs):
        super(UidValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
        **kwargs)