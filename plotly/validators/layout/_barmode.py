import _plotly_utils.basevalidators


class BarmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(self, plotly_name='barmode', parent_name='layout', **kwargs):
        super(BarmodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            role='info',
            values=['stack', 'group', 'overlay', 'relative'],
            **kwargs
        )
