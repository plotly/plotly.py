

import _plotly_utils.basevalidators as _bv


class SubplotValidator(_bv.SubplotidValidator):
    def __init__(self, plotly_name='subplot',
                       parent_name='barpolar',
                       **kwargs):
        super(SubplotValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 dflt=kwargs.pop('dflt', 'polar'),
                 edit_type=kwargs.pop('edit_type', 'calc'),
        **kwargs)