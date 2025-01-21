

import _plotly_utils.basevalidators as _bv


class XbinsValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='xbins',
                       parent_name='histogram',
                       **kwargs):
        super(XbinsValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'XBins'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)