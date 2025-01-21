

import _plotly_utils.basevalidators as _bv


class DirectionValidator(_bv.EnumeratedValidator):
    def __init__(self, plotly_name='direction',
                       parent_name='layout.polar.angularaxis',
                       **kwargs):
        super(DirectionValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 values=kwargs.pop('values', ['counterclockwise', 'clockwise']),
        **kwargs)