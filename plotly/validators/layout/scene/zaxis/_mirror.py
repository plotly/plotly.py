

import _plotly_utils.basevalidators as _bv


class MirrorValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='mirror',
                       parent_name='layout.scene.zaxis',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
                 values=kwargs.pop('values', [True, 'ticks', False, 'all', 'allticks']),
        **kwargs)