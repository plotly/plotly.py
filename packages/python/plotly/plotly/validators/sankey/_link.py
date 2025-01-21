

import _plotly_utils.basevalidators as _bv


class LinkValidator(_bv.CompoundValidator):
    def __init__(self, plotly_name='link',
                       parent_name='sankey',
                       **kwargs):
        super(LinkValidator, self).__init__(plotly_name=plotly_name,
                         parent_name=parent_name,
                 data_class_str=kwargs.pop('data_class_str', 'Link'),
                 data_docs=kwargs.pop('data_docs', """
"""),
        **kwargs)