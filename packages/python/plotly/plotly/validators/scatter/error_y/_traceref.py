

import _plotly_utils.basevalidators as _bv


class TracerefValidator(_bv.IntegerValidator):
    def __init__(self, plotly_name='traceref',
                       parent_name='scatter.error_y',
                       **kwargs):
        super(TracerefValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 edit_type=kwargs.pop('edit_type', 'style'),
                 min=kwargs.pop('min', 0),
        **kwargs)