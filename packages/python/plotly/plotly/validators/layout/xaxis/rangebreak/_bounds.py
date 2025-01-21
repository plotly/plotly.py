

import _plotly_utils.basevalidators as _bv


class BoundsValidator(_bv.InfoArrayValidator):
    def __init__(self, plotly_name='bounds',
                       parent_name='layout.xaxis.rangebreak',
                       **kwargs):
        super(BoundsValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'calc'),
                 items=kwargs.pop('items', [{'editType': 'calc', 'valType': 'any'}, {'editType': 'calc', 'valType': 'any'}]),
        **kwargs)