

import _plotly_utils.basevalidators as _bv


class TextpositionsrcValidator(_bv.SrcValidator):
    def __init__(self, plotly_name='textpositionsrc',
                       parent_name='funnel',
                       **kwargs):
        super(TextpositionsrcValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'none'),
        **kwargs)