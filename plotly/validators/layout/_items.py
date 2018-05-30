import _plotly_utils.basevalidators


class ItemsValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(self, plotly_name='items', parent_name='layout', **kwargs):
        super(ItemsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            values=['/^x([2-9]|[1-9][0-9]+)?y([2-9]|[1-9][0-9]+)?$/', ''],
            **kwargs
        )
