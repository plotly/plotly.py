import _plotly_utils.basevalidators


class XValidator(_plotly_utils.basevalidators.DataArrayValidator):

    def __init__(self, plotly_name='x', parent_name='scatter', **kwargs):
        super(XValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc+clearAxisTypes',
            role='data',
            **kwargs
        )
