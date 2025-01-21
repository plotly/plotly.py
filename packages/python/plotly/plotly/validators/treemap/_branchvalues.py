

import _plotly_utils.basevalidators as _bv


class BranchvaluesValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='branchvalues',
                       parent_name='treemap',
                       **kwargs):
        super(BranchvaluesValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 values=kwargs.pop('values', ['remainder', 'total']),
        **kwargs)