import _plotly_utils.basevalidators


class HoverinfoValidator(_plotly_utils.basevalidators.FlaglistValidator):

    def __init__(
        self, plotly_name='hoverinfo', parent_name='parcoords', **kwargs
    ):
        super(HoverinfoValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=True,
            edit_type='none',
            extras=['all', 'none', 'skip'],
            flags=['x', 'y', 'z', 'text', 'name'],
            role='info',
            **kwargs
        )
