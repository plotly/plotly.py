

import _plotly_utils.basevalidators as _bv


class CaptureeventsValidator(_bv.BooleanValidator):
    def __init__(self, plotly_name='captureevents',
                       parent_name='layout.annotation',
                       **kwargs):
        super().__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'arraydraw'),
        **kwargs)