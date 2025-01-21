

import _plotly_utils.basevalidators as _bv


class LinepositionValidator(_bv.FlaglistValidator):
    def __init__(self, plotly_name='lineposition',
                       parent_name='funnel.textfont',
                       **kwargs):
        super(LinepositionValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 array_ok=kwargs.pop('array_ok', True),
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 extras=kwargs.pop('extras', ['none']),
                 flags=kwargs.pop('flags', ['under', 'over', 'through']),
        **kwargs)