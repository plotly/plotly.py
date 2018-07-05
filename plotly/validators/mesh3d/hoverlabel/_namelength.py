import _plotly_utils.basevalidators


class NamelengthValidator(_plotly_utils.basevalidators.IntegerValidator):

    def __init__(
        self,
        plotly_name='namelength',
        parent_name='mesh3d.hoverlabel',
        **kwargs
    ):
        super(NamelengthValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            array_ok=True,
            edit_type='none',
            min=-1,
            role='style',
            **kwargs
        )
