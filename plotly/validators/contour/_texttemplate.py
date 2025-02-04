

import _plotly_utils.basevalidators as _bv


class TexttemplateValidator(_bv.StringValidator):
    def __init__(self, plotly_name='texttemplate',
                       parent_name='contour',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'plot'),
        **kwargs)