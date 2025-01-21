

import _plotly_utils.basevalidators as _bv


class XperiodalignmentValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='xperiodalignment',
                       parent_name='scattergl',
                       **kwargs):
        super(XperiodalignmentValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 values=kwargs.pop('values', ['start', 'middle', 'end']),
        **kwargs)