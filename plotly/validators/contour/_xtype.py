import _plotly_utils.basevalidators


class XtypeValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(self, plotly_name='xtype', parent_name='contour', **kwargs):
        super(XtypeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc+clearAxisTypes',
            role='info',
            values=['array', 'scaled'],
            **kwargs
        )
