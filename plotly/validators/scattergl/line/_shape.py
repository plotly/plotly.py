

import _plotly_utils.basevalidators as _bv


class ShapeValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='shape',
                       parent_name='scattergl.line',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 values=kwargs.pop('values', ['linear', 'hv', 'vh', 'hvh', 'vhv']),
        **kwargs)